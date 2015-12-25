#!/usr/bin/python
import os
import lxml import etree


def setuser():
    mycat_user = os.getenv('MYCAT_USER')
    mycat_pwd = os.getenv('MYCAT_PWD')

    if mycat_user is None:
        return

    config = '/opt/mycat/conf/server.xml'
    tree = etree.parse(config)
    user = tree.find('user[@name="user"]')
    user.attrib['name'] = mycat_user
    user.find('property[@name="password"]').text = mycat_pwd
    with open(config, 'w') as f:
        f.write(etree.tostring(
            tree,
            xml_declaration=True,
            encoding='UTF-8',
            doctype='<!DOCTYPE mycat:server SYSTEM "server.dtd">'))


if __name__ == '__main__':
    setuser()
