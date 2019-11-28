sudo docker stop mock
sudo docker rm mock
sudo docker run -p 8004:8000 --name mock --restart always --link mysql:localhost --link redis:localhost  -d django-mock