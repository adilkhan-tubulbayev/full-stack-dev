#!/bin/bash
echo "PART 2. NGINX INSTALLATION"
sudo apt update
sudo apt install -y nginx
echo ""
echo "PART 2 HAS BEEN COMPLETED >>> SUCCESS"
nginx -version
echo ""
