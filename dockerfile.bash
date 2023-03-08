FROM ubuntu/apache2:latest
ENV TZ=IT
COPY index.html /var/www/html/
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
