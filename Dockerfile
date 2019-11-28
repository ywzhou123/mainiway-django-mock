FROM python:2.7
MAINTAINER ywzhou <www.ywzhou.shop>
ENV PY_ENV env_demo
RUN apt-get update
RUN apt-get install -y nodejs
RUN mkdir /data
WORKDIR /data
ADD . /data/
RUN pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]