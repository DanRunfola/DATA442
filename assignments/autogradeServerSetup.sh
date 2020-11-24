mkdir docker
cd docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo apt-get purge docker-ce docker-ce-cli containerd.io
sudo rm -rf /var/lib/docker


sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
sudo curl -L https://raw.githubusercontent.com/docker/compose/1.27.4/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose

git clone --recursive https://github.com/eecs-autograder/autograder-full-stack.git
cd autograder-full-stack

git pull
git submodule update --remote

echo "*                soft    nofile          1000000" >> /etc/security/limits.conf
echo "*                hard    nofile          1000000" >> /etc/security/limits.conf

ex +'%s/^ALLOWED_HOSTS=\(.*\)/ALLOWED_HOSTS=45.79.185.240/' -scwq ./autograder-server/_prod.env
ex +'%s/^SITE_DOMAIN=\(.*\)/SITE_DOMAIN=45.79.185.240/' -scwq ./autograder-server/_prod.env
ex +'%s/autograder.io/45.79.185.240/' -scwq ./nginx/production/conf.d/default.conf

mkdir /root/certs && cd /root/certs
openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out MyCertificate.crt -keyout MyKey.key


cp MyCertificate.crt /etc/ssl/certs/45.79.185.240.crt
cp MyKey.key /etc/ssl/private/45.79.185.240.key

cd /root/docker/autograder-full-stack
ex +'%s/^OAUTH2_PROVIDER=\(.*\)/OAUTH2_PROVIDER=google/' -scwq ./autograder-server/_prod.env


