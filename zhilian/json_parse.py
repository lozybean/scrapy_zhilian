#!/usr/bin/env python
# -*- coding: utf-8 -*- \#

import json
import codecs
from collections import OrderedDict

name_table = {
    'company':u'公司名称',
    'payment':u'职位月薪',
    'place':u'工作地点',
    'date':u'发布日期',
    'prop':u'工作性质',
    'exp':u'工作经验',
    'academic':u'最低学历',
    'num':u'招聘人数',
    'job_type':u'职位类别',
    'link':u'详细链接',
    'description':u'职位描述'
}
sorted_keys = ['company','payment','place','date',
               'prop','exp','academic','num',
               'job_type','link','description']
with open('text.json') as fp:
    json_dicts = json.load(fp)
out_dicts = []
for json_dict in json_dicts:
    out_dict = OrderedDict()
    for key in sorted_keys:
        out_dict[name_table[key]] = json_dict[key]
    out_dicts.append(out_dict)
with codecs.open('text.json','w','utf-8') as fp:
    json.dump(out_dicts,fp,ensure_ascii=False,indent=4)
