FROM redhat/ubi8
RUN yum install python3 -y && pip3 insatll flask 
COPY test_app.py .
COPY app.py .
CMD ["python3","app.py"]
