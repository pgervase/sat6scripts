#!/bin/bash
mkdir -p /var/www/html/pub/export
hammer settings set --name pulp_export_destination --value /var/www/html/pub/export/
chcon --verbose --recursive --reference /var/lib/pulp/katello-export/ /var/www/html/pub/export/
chmod --verbose --recursive --reference /var/lib/pulp/katello-export/ /var/www/html/pub/export/
chown --verbose --recursive --reference /var/lib/pulp/katello-export/ /var/www/html/pub/export/
hammer content-view version export --organization dev --content-view "Default Organization View" --version "1.0"
