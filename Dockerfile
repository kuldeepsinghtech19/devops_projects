FROM redhat/ubi8
RUN yum install python3 -y && pip insatll flask -y
COPY test_app.py .
COPY app.py .
CMD ["python3","app.py"]
