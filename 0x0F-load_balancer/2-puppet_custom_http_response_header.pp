#  custom HTTP header with Puppet
new_string="\\\\n\tadd_header X-Served-By $HOSTNAME;\n"
exec { '/usr/bin/env sed -i "19i $new_string" /etc/nginx/sites-enabled/default && service nginx restart': }
