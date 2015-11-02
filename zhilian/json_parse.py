#!/usr/bin/env python
# -*- coding: utf-8 -*- \#

import json
import codecs

with open('text.json') as fp:
    json_dict = json.load(fp)
with codecs.open('text.json','w','utf-8') as fp:
    json.dump(json_dict,fp,ensure_ascii=False,indent=4)
