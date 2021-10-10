#!/bin/bash
echo " installing ssl"
#file = "/etc/letsencrypt/live/test.anuppoudel.codes/fullchain.pem"

#if [[ -f "$file" ]];
if cat /etc/letsencrypt/live/test.anuppoudel.codes/fullchain.pem 
then

echo "certs exist"
else
echo "certs not installed, installing"
certbot --nginx -m anuppoudel45@gmail.com --agree-tos -d serve.anuppoudel.codes --redirect --non-interactive

echo "DONE"
fi
exec "$@"
