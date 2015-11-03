#!/usr/bin/env python
# -*- coding: utf-8 -*- \#

import re
import scrapy
from urllib import urlencode
from scrapy.http import Request
from zhilian.items import ZhilianItem

class ZhilianSpider(scrapy.spiders.Spider):
    name = 'zhilian'
    start_urls = []
    var = {
            'jl':'杭州',
            'kw':'数据挖掘',
            'sm':'0',
    }
    for page in range(1):
        var['p'] = page + 1
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'+urlencode(var)
        start_urls.append(url)

    @staticmethod
    def encode(unicode_list):
        for unicode in unicode_list:
            s = unicode.encode('utf-8').strip()
            if not s:
                continue
            return s
        return ''

    def parse(self, response):
        for sel in response.xpath("//table[@class='newlist']/tr"):
            link = self.encode( sel.xpath("td[@class='gsmc']/a/@href").extract() )
            if not link:
                continue
            yield Request(link,callback=self.company_parse)

    def company_parse(self, response):
        key_word = re.compile(u'数据')
        for job in response.xpath("//div[@class='part4 positionList']/div[@class='positionListContent']/div[@class='positionListContent1']"):
            jobname = self.encode( job.xpath("span[@class='jobName']/a/text()").extract() )
            if not key_word.search(jobname.decode('utf-8')):
                continue
            job_link = self.encode( job.xpath("span[@class='jobName']/a/@href").extract() )
            if not job_link:
                continue
            company = self.encode( job.xpath("span[@class='comName']/text()").extract() )
            yield Request(job_link,meta={'link':job_link,'company':company},callback=self.job_parse)

    def job_parse(self,response):
        item = ZhilianItem()
        item['link'] = response.meta['link']
        item['company'] = response.meta['company']
        description = {}
        description[ "payment" ] = re.compile(u'职位月薪：')
        description[ "place" ] = re.compile(u'工作地点：')
        description[ "date" ] = re.compile(u'发布日期：')
        description[ "prop" ] = re.compile(u'工作性质：')
        description[ "exp" ] = re.compile(u'工作经验：')
        description[ "academic" ] = re.compile(u'最低学历：')
        description[ "num" ] = re.compile(u'招聘人数：')
        description[ "job_type" ] = re.compile(u'职位类别：')
        prefix = "//div[@class='terminalpage clearfix']/div[@class='terminalpage-left']/"
        for li in response.xpath(prefix+"ul[@class='terminal-ul clearfix']/li"):
            text = self.encode( li.xpath('span/text()').extract() )
            for desc in description:
                if description[desc].search(text.decode('utf-8')):
                    text = ''
                    for childnode in li.xpath('strong/descendant-or-self::node()'):
                        t = self.encode( childnode.xpath('text()').extract() )
                        text += t
                    item[desc] = text
                    break
        text = ''
        xpath = prefix
        xpath += "div[@class='terminalpage-main clearfix']/div[@class='tab-cont-box']/div[@class='tab-inner-cont']"
        xpath += "/p/descendant-or-self::node()"
        for t in response.xpath(xpath):
            t = self.encode(t.xpath("text()").extract())
            if len(t.strip()) > 9:
                text += t + '\n  '.encode('utf-8')
        item['description'] = text
        return item
