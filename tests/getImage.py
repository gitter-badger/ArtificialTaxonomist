#!/usr/bin/python

#Script para baixar as imagens do arquivo "image.txt"

import urllib

urllib.urlretrieve("http://imagens1.jbrj.gov.br/fsi/server?type=image&width=375&height=600&rect=0,0,1,1&profile=fsi&source=hvpr%2Fmnhn%2Ftipos4%2DParis%2FP00128420%2Ejpg&", "lauraceae1.jpg")

print "Done"
