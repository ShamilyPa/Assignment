FROM python:2.7
MAINTAINER parameshwaran.shamily@gmail.com
RUN  easy_install pip && pip install requests
COPY . /home/ubuntu/assignment/code.py
EXPOSE 90
CMD ["python","/home/ubuntu/assignment/code.py"]


