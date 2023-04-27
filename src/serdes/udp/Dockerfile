FROM python:3.11
ARG DEBIAN_FRONTEND=noninteractive
COPY udp/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY udp ./udp
COPY data ./data
COPY serdesers ./serdesers
COPY tester.py .
ENV PYTHONPATH=.
CMD ["python", "-u", "udp/serdes.py"]