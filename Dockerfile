FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apt-get update && apt-get install -y libaio1 unzip curl && \
    mkdir -p /opt/oracle && \
    curl -o /opt/oracle/instantclient-basiclite.zip https://download.oracle.com/otn_software/linux/instantclient/211000/instantclient-basiclite-linux.x64-21.1.0.0.0.zip && \
    unzip /opt/oracle/instantclient-basiclite.zip -d /opt/oracle && \
    rm /opt/oracle/instantclient-basiclite.zip

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_1
ENV PATH=$PATH:/opt/oracle/instantclient_21_1

COPY . .

CMD ["python", "main.py"]