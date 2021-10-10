FROM nginx:1.21.3

RUN apt update  && apt install -y  python-certbot-nginx

EXPOSE 443 80
COPY nginx-entrypoint.sh ./
CMD ["/bin/bash"]
ENTRYPOINT ["/bin/bash","nginx-entrypoint.sh"]

