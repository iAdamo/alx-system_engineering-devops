# modifying nginx request limits

exec { 'ULIMIT':
  provider => shell,
  command  => "sed -i 's/^ULIMIT.*/ULIMIT=\"-n 10000\"/' /etc/default/nginx && service nginx restart",
}
