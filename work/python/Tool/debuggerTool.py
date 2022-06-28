#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 14:37
# @Author  : 5in

import shelve
import pickle
filename=r'D:\wy\code\work-code\common-gis\common-gis\test\shelve.pkl'
my_shelf = shelve.open(filename)

# print(my_shelf.items())
for key in my_shelf:
    try:
        globals()[key]=my_shelf[key]
        print(key)

    except:
        pass



my_shelf.close()
print(outputDir)
import logging
import multiprocessing
from datetime import datetime
from functools import reduce, partial

def parse_road_surface(o_road, link_dict, prjCrs):
    partitioned_list = func_partition(o_road)

    logging.info("道路面: 开始map")
    cpu_count = gl.get_value('cpu_count')
    pool = multiprocessing.Pool(processes=cpu_count)

    config = gl.get_value('config')
    list_tuple = pool.map(partial(func_map, config=config, link_dict=link_dict, prjCrs=prjCrs), partitioned_list)
    pool.close()
    pool.join()
    logging.info("道路面: 结束map")

    logging.info("道路面: 开始reduce")
    roadSurfaceTable = reduce(func_reduce, list_tuple)
    logging.info("道路面: 结束reduce")

    return roadSurfaceTable


def func_partition(o_road):
    cpu_count = gl.get_value('cpu_count')
    chunksize_num = int(len(o_road) / cpu_count * 0.7) + 1
    # 每组个数
    partitioned_list = [o_road[i:i + chunksize_num] for i in range(0, len(o_road), chunksize_num)]
    return partitioned_list
roadSurfaceTable = parse_road_surface(o_road, link_dict, prjCrs)

# print(my_shelf['outputDir'])

# print(outputDir)




# with open('./your_bk.pkl', 'rb') as f:
#     bk_restore = pickle.load(f)


# print(T)
# Hiya
# print(val)
# [1, 2, 3]