# rpmbuild-osticket

Create a osTicket RPM for RHEL/CentOS.

## Requirements

To download package sources and install build dependencies

    yum -y install rpmdevtools yum-utils

## Build process

To build the package follow the steps outlined below

    git clone https://github.com/linuxhq/rpmbuild-osticket.git rpmbuild
    spectool -g -R rpmbuild/rpm/osticket.spec
    yum-builddep rpmbuild/rpm/osticket.spec
    rpmbuild -ba rpmbuild/rpm/osticket.spec

## Partners

[![packagecloud](http://dka575ofm4ao0.cloudfront.net/pages-transactional_logos/retina/10543/gKme3F4XRaC5EyKJzKsA)](https://packagecloud.io)

Do you need trustworthy hosted package repositories?  Then packagecloud is for you.

A big thank you to packagecloud for supporting the open source community!

## License

BSD

## Author Information

This package was created by [Taylor Kimball](http://www.linuxhq.org).
