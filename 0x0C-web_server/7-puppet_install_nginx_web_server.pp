# Nginx should be listening on port 80 
# When querying Nginx at its root / with a GET request (requesting a page) using curl,
# it must return a page that contains the string Hello World!
# The redirection must be a "301 Moved Permanently"

# update the server and install nginx
exec {'update & nginx':
  command => 'sudo apt -y update; sudo apt install -y nginx',
  path    => ['/usr/bin', '/usr/sbin/'],
  onlyif  => 'test ! -f /etc/nginx/',
}

# create index.html
file {'/var/www/html/index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  owner   => 'ubuntu',
  content => "Hello World!\n",
}

# create 404.html
file {'/var/www/html/404.html':
  ensure  => 'file',
  path    => '/var/www/html/404.html',
  owner   => 'ubuntu',
  content => "Ceci n'est pas une page\n",
}

# create or modify default config
file {'/etc/nginx/sites-available/default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  owner   => 'ubuntu',
  content =>
"server {
listen 80 default_server;
listen [::]:80 default_server;
root /var/www/html;
index index.html;
location / {
        rewrite ^/redirect_me https://github.com/iAdamo permanent;
        error_page 404 /404.html;
        try_files \$uri \$uri/ =404;
	}
}
",
}

# create symbolic link to availablle config
exec {'symbolic link':
  command => 'sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/',
  require => File['/etc/nginx/sites-available/default'],
  path    => '/usr/bin',
  onlyif  => 'test ! -f /etc/nginx/sites-enabled/default',
}

# restart nginx service
exec {'ngnix restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin', 'bin'],
}
