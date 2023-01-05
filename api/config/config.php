<?php

# set the environment to DEV if you want debug output
#define('ENV', 'DEV');
define('ENV', 'PROD');

# add your api base path, starting and ending with a / character
# use `/` if you want the api to operate on the root directory
# make sure to insert the same value into the .htaccess file
define('BASE_PATH', '/api/');

# if you need to connect to a database, uncomment the following lines and
# add your database config
#define('DB_NAME', 'my_database');
#define('DB_USER', 'my_user');
#define('DB_PASSWORD', 'my_password');
#define('DB_HOST', 'localhost');

# if you want e-mail, uncomment these lines and add your e-mail config
#define('MAIL_ADDRESS', 'root@localhost');
#define('MAIL_PASSWORD', 'my_password');
#define('MAIL_SMTP', 'smtp.myhost.tld');
#define('MAIL_PORT', 587);
