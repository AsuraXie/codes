echo "start nginx"
cd /
cd /home/asura/Downloads/nginx-1.6.2/objs
sudo ./nginx
echo "start php-cgi"
cd /usr/local/sbin
sudo ./php-fpm
