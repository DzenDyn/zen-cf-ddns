FROM ubuntu:20.04
COPY requirements.txt zen-cf-ddns.py ./zen-cf-ddns/
RUN apt update && \
apt install python3 python3-pip -y && \
pip install --upgrade pip && \
pip install -r ./zen-cf-ddns/requirements.txt

COPY zen-cf-ddns.conf /etc/zen-cf-ddns.conf

CMD python3 ./zen-cf-ddns/zen-cf-ddns.py