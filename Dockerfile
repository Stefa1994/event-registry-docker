FROM python:3.7
RUN mkdir /code
WORKDIR /code
COPY src /code
COPY config /code
COPY init.sh /code
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt
ADD . /code/
EXPOSE 8000
ENTRYPOINT ["./init.sh"]
#CMD ["python", "./entry_point.py"]
