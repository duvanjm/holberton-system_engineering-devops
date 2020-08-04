#connect to a server without typing a password.

file_line {'IdentityFile':
    replace => true,
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/holberton',
}

file_line {'PassworAuthentication':
    replace => true,
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthetication no',
}
