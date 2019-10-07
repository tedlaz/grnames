FROM python:alpine

RUN pip install hug && \
    mkdir fakenames

COPY . /fakenames

RUN chmod +x /fakenames/start.sh

WORKDIR /fakenames

EXPOSE 8000

CMD ["/fakenames/start.sh"]