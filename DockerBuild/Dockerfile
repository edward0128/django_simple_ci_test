FROM django

COPY django django
COPY requirements.txt requirements.txt
COPY start_up.sh start_up.sh
RUN pip install -r requirements.txt
EXPOSE 8888

CMD ./start_up.sh
