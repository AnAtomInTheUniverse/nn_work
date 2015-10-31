#!/usr/bin/python

# Imports

#import numpy as np
#import matplotlib
from google.protobuf import text_format
import caffe 
from caffe.proto import caffe_pb2
import argparse
import sys

#Iterate through all of the layers in the 
#caffe model prototxt file and extract
#relevant layer information
def getLayerInfo(caffe_net):
		for layer in caffe_net.layer:
				if(layer.name == "Convolution"):
					print "Name: ", layer.name
					print "Kernel Size: ", layer.convolution_param.kernel_size
					print "Num Output: ", layer.convolution_param.num_output
#enddef

# Main procedure to read caffe model 
if len(sys.argv) != 2:
		print "Usage:", sys.argv[0], "Caffe Model File"
		sys.exit(-1)
#endif
print "About to read file " + sys.argv[1] + "\n" 
#Using argparse module to parse command line argument
#User must supply a valid '.prototxt' caffe model file 
#parser 	=	argparse.ArgumentParser()
#parser.add_argument('net_proto_file', help='Input Network prototxt file', type=argparse.FileType('r'))
#args 	=	parser.parse_args()
print "Got net param\n"
model_file	=	sys.argv[1]
net 		=	caffe_pb2.NetParameter()
f			=	open(model_file, 'r')
text_format.Merge(str(f.read()), net)
getLayerInfo(net)


