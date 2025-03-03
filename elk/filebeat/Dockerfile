FROM elastic/filebeat:8.17.2

USER root

RUN apt-get update && \
    apt-get install -y gettext-base && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY config/filebeat.tpl.yml /usr/share/filebeat/
COPY ./entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

RUN chown filebeat:filebeat /entrypoint.sh && \
    chmod 755 /entrypoint.sh && \
    chown -R filebeat:filebeat /usr/share/filebeat

USER filebeat

ENTRYPOINT ["/entrypoint.sh"]