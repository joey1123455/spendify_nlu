FROM rasa/rasa-sdk
WORKDIR /app

USER root

COPY ./actions /app/actions
RUN pip install requests
# COPY ./start-action_server /start
# RUN sed -i 's/\r$//g' /start
# RUN chmod +x /start
# ENTRYPOINT [ "/start" ]
USER 1001
