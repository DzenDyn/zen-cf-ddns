#!/usr/bin/python -u
import CloudFlare
import json
import requests
import time
import logging
import datetime


with open('/etc/zen-cf-ddns.conf', 'r') as f:
    settings = json.load(f)
logging.basicConfig(filename=settings['log_file'], level=logging.DEBUG, format='%(levelname)s:%(message)s')


def my_ip_address():
    """Cloudflare API code - example"""

    # This list is adjustable - plus some v6 enabled services are needed
    # url = 'http://myip.dnsomatic.com'
    # url = 'http://www.trackip.net/ip'
    # url = 'http://myexternalip.com/raw'
    url = 'https://api.ipify.org'
    try:
        ip_address = requests.get(url).text
    except:
        logging.error('%s: %s: failed' % (datetime.datetime.now(), url))
        return
    if ip_address == '':
        logging.error('%s: %s: failed' % (datetime.datetime.now(), url))
        return

    if ':' in ip_address:
        ip_address_type = 'AAAA'
    else:
        ip_address_type = 'A'

    return ip_address, ip_address_type


def do_dns_update(cf, zone_name, zone_id, dns_name, ip_address, ip_address_type):
    """Cloudflare API code - example"""

    try:
        params = {'name':dns_name, 'match':'all', 'type':ip_address_type}
        dns_records = cf.zones.dns_records.get(zone_id, params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        logging.error('%s: /zones/dns_records %s - %d %s - api call failed' % (datetime.datetime.now(), dns_name, e, e))
        return

    updated = False

    # update the record - unless it's already correct
    for dns_record in dns_records:
        old_ip_address = dns_record['content']
        old_ip_address_type = dns_record['type']

        if ip_address_type not in ['A', 'AAAA']:
            # we only deal with A / AAAA records
            continue

        if ip_address_type != old_ip_address_type:
            # only update the correct address type (A or AAAA)
            # we don't see this becuase of the search params above
            logging.info('%s: IGNORED: %s %s ; wrong address family' % (datetime.datetime.now(), dns_name, old_ip_address))
            continue

        if ip_address == old_ip_address:
            logging.info(('%s: UNCHANGED: %s %s' % (datetime.datetime.now(), dns_name, ip_address)))
            continue

        # Yes, we need to update this record - we know it's the same address type

        dns_record_id = dns_record['id']
        dns_record = {
            'name': dns_name,
            'type': ip_address_type,
            'content': ip_address
        }
        try:
            dns_record = cf.zones.dns_records.put(zone_id, dns_record_id, data=dns_record)
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            logging.error('%s: /zones.dns_records.put %s - %d %s - api call failed' % (datetime.datetime.now(), dns_name, e, e))
            return
        logging.info(('%s: UPDATED: %s %s -> %s' % (datetime.datetime.now(), dns_name, old_ip_address, ip_address)))
        return


def main():
    while True:
        time.sleep(settings['update_frequency'])
        logging.info('%s: Verification begins' % datetime.datetime.now())
        ip_address, ip_address_type = my_ip_address()
        logging.info('%s: My IP address:' + ip_address % datetime.datetime.now())
        for zone in settings['zones']:
            cf = CloudFlare.CloudFlare(email=zone['email'], token=zone['api_key'])
            try:
                params = {'name': zone['name']}
                cfzones = cf.zones.get(params=params)
            except CloudFlare.exceptions.CloudFlareAPIError as e:
                logging.error('%s: /zones %d %s - api call failed' % (datetime.datetime.now(), e, e))
                continue
            except Exception as e:
                logging.error('%s: /zones.get - %s - api call failed' % (datetime.datetime.now(), e))
                continue
            if len(cfzones) == 0:
                logging.error('%s: /zones.get - %s - zone not found' % (datetime.datetime.now(), zone['name']))
                continue
            if len(cfzones) != 1:
                logging.error('%s: /zones.get - %s - api call returned %d items' % (datetime.datetime.now(), zone['name'], len(cfzones)))
                continue
            cfzone = cfzones[0]
            zone_name = cfzone['name']
            zone_id = cfzone['id']
            for a_record in zone['A_records']:
                do_dns_update(cf, zone_name, zone_id, a_record['name'], ip_address, ip_address_type)


if __name__ == '__main__':
    main()
