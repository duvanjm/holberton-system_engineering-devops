#connect to a server without typing a password.

file_line { 'IdentityFile':
  replace => true,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'PasswordAuthentication':
  replace => true,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}
