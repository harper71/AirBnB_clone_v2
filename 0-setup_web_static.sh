#!/usr/bin/env bash
# installs and configure nginx server

sudo apt update

if which nginx &> /dev/null
then
    echo "Nginx is already installed."
else
    sudo apt -y install nginx
fi

DIR1="/data/web_static/releases/test/"

if [ -d "$DIR1" ];
then
    echo "$DIR1 already exist"
else
    sudo mkdir -p "$DIR1"
fi

sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, recreating it if it already exists
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data
sudo chown -R ubuntu:ubuntu /etc/nginx/sites-available/
sudo chown -R ubuntu:ubuntu /etc/nginx/sites-enabled/

echo "
server {
	listen 80 default_server;
	listen [::]:80 default_server;


	root /var/www/html;
	#project task
	#error page redirection
	error_page 404 /custom_404.html;
	location = /custom_404.html {
		root /var/www/html;
		internal;
		}

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files \$uri \$uri/ =404;
	}
	#rewrite ^/redirect_me https://www.youtube.com permanent;

	#redirect_me
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=3lFkDc6dFoY;
		}

	# custom headers

}" > /etc/nginx/sites-available/default

# Setting up custom error page if not exists
file_path="/var/www/html/custom_404.html"
if [ -f "$file_path" ]; then
	echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom_404.html > /dev/null
else
	sudo touch /var/www/html/custom_404.html
	echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom_404.html > /dev/null
fi


config="/etc/nginx/sites-available/default"

sudo sed -i "/# custom headers/a \ \tadd_header X-Served-By $HOSTNAME;" "$config"
sudo sed -i '/server_name _;/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $config
sudo service nginx restart
