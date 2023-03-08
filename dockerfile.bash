version: '3.3'
services:
    apache2:
        container_name: ApacheSRV
        volumes:
            - '/var/www/html:/var/www/html'
        restart: always
        environment:
            - TZ=IT
            - S3_PRESIGNED_URL: <inserire qui il presigned URL>
        ports:
            - '80:80'
        image: 'ubuntu/apache2:latest'
