#!/usr/bin/python


# Imports
import csv
#import numpy as np
#import matplotlib
from google.protobuf import text_format
import caffe 
import caffe.draw
from caffe.proto import caffe_pb2
import argparse

#Iterate through all of the layers in the 
#caffe model prototxt file and extract
#relevant layer information
def getLayerInfo(caffe_net):
		for layer in caffe_net.layer:
				if(layer.name == "Convolution"):
					print "Name: ", layer.name
					print "Kernel Size: ", layer.convolution_param.kernel_size
					print "Num Output: ", layer.convolution_param.num_output

# Main procedure to read caffe model 
if len(sys.argv) != 2:
		print "Usage:", sys.argv[0], "Caffe Model File"
		sys.exit(-1)

		#Using argparse module to parse command line argument
		#User must supply a valid '.prototxt' caffe model file 
		parser 	=	argparse.ArgumentParser()
		parser.add_argument('net_proto_file', help='Input Network prototxt file', type=argparse.FileType('r'))
		args 	=	parser.parse_args()
		net 	=	caffe_pb2.NetParameter()
		text_format.Merge(open(args.net_proto_file).read(), net)
		getLayerInfo(net)


