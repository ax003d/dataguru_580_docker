#!/usr/bin/python
import os
import xml.etree.ElementTree as ET


def setuser():
    mycat_user = os.getenv('MYCAT_USER')
    mycat_pwd = os.getenv('MYCAT_PWD')

    if mycat_user is None:
        return

    config = '/opt/mycat/conf/server.xml'
    tree = ET.parse(config)
    root = tree.getroot()
    user = root.find('user[@name="user"]')
    user.attrib['name'] = mycat_user
    user.find('property[@name="password"]').text = mycat_pwd
    tree.write(config)


if __name__ == '__main__':
    setuser()
