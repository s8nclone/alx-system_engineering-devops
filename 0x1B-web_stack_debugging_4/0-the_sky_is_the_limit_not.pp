# Increases the amount of traffic an Nginx server can handle.

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

#restart nginx
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
