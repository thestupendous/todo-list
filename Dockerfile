
FROM python
RUN pip3 install flask pymongo
ENV MONGOHOST localhost
CMD ["python","/todolist/app.py"]


EXPOSE 9000

COPY app.py /todolist/app.py
COPY  templates/* /todolist/templates/
