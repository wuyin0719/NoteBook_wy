#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 10:53
# @Author  : 5in

from lxml import etree
import xmltodict
inputFile=r'D:\wy\code\work-code\common-gis\common-gis\input\osm-pingshan.xodr'

data = xmltodict.parse(open(inputFile,encoding='utf-8').read())
opendrive = data["OpenDRIVE"]
# print(data)

# print(opendrive["header"])

o_read = opendrive["road"]

o_read1 = o_read[0]
print(o_read1['@id'])

for geo in o_read1['planView']['geometry']:
    print(geo)
print(o_read1['planView'])
print(o_read1.keys())
# print(len(o_read))
# with open(inputFile, 'r', encoding='utf-8') as fh:
#     # logging.info("start etree.parse")
#     root_node = etree.parse(fh).getroot()
#
#     # logging.info("load OpenDrive - Start")
#
#
# print(root_node)