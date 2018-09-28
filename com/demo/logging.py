#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test logging
"""
__author__ = 'Test logging'
import logging
import os.path
import time

# logging.basicConfig(level=logging.NOTSET,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
logger.path = os.path.dirname(os.getcwd()) + '/logs/'
log_name = logger.path + rq + '.log'
log_file = log_name
fh = logging.FileHandler(log_file, mode='w')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)



def print_log():
    logger.debug(u"debug")
    logger.info(u"info")
    logger.warning(u"warning")
    logger.error(u"error")
    logger.critical(u"critical")



print_log()