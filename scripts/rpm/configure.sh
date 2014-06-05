#!/bin/bash
set -eu

DISTRIBUTION=`lsb_release -si`

echo "Configuring RPM-based build for $DISTRIBUTION"

rpm -q mock rpm-build >/dev/null 2>&1 || sudo yum install -y mock rpm-build

echo -n "Writing mock configuration..."
mkdir -p mock

MOCK_CONFIG="scripts/rpm/xenserver_el6.cfg.in"
if [[ "x$DISTRIBUTION" == "xFedora" ]] ; then
    MOCK_CONFIG="scripts/rpm/xenserver_fedora.cfg.in"
fi

sed -e "s|@PWD@|$PWD|g" $MOCK_CONFIG > mock/xenserver.cfg
ln -fs /etc/mock/default.cfg mock/
ln -fs /etc/mock/site-defaults.cfg mock/
ln -fs /etc/mock/logging.ini mock/
mkdir -p mock/cache
mkdir -p mock/root
chgrp mock mock/cache
chgrp mock mock/root
echo " done"

echo -n "Initializing repository..."
mkdir -p RPMS
createrepo --quiet RPMS
mkdir -p SRPMS
createrepo --quiet SRPMS
echo " done"

