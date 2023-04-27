FROM python:3.11
ARG DEBIAN_FRONTEND=noninteractive
COPY http/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY http ./http
COPY data ./data
COPY serdesers ./serdesers
COPY tester.py .
ENV PYTHONPATH=.
CMD ["python", "-u", "http/serdes.py"]