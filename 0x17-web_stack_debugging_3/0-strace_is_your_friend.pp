exec { 'extra_p':
  command => "sed -ie 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/bin'],
}
