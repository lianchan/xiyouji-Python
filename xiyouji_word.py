#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import jieba
import jieba.analyse
import codecs
from optparse import OptionParser


content = open('./xiyouji.txt', 'rb').read()
#打开文本，告诉解码器是unicode编码

tags = jieba.analyse.extract_tags(content,300000)
file_object = codecs.open('xiyouji_dict.txt', 'w+', 'utf-8')
file_object.write(u",".join(tags))
file_object.close( )
print ",".join(tags)  