#!/usr/bin/python

#script para baixar arquivo DwC-A do REFLORA

import urllib2

url = "http://ipt.jbrj.gov.br/reflora/archive.do?r=alcb_herbarium&v=1.117"

import urllib
urllib.urlretrieve (url, "DwC.zip")
print "Done"
