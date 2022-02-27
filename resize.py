#!/usr/bin/env python3

import os
from PIL import Image

def Resize_hsize(hsize, path_img): # hàm đổi size ảnh theo chiều cao
	img = Image.open(path_img)
	wpercent = (hsize/float(img.size[1]))
	basewidth = int((float(img.size[0])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save(path_img) 
	
def Resize_basewidth(basewidth, path_img): # hàm đổi size ảnh theo chiều rộng
	img = Image.open(path_img)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save(path_img) 


def Resizefolder(path):  # hàm đổi size nhiều ảnh trong 1 folder
	os.chdir(path)
	for file in os.listdir():
		if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
			print(os.path.join(path, file))
			path_img = os.path.join(path, file)
			Resize_hsize(120, path_img)  # tuỳ chọn hàm đổi size theo chiều cao hay chiều rộng
			

def main():
	path = "/Users/abc/Documents/Code_doAn/Text-to-Handwriting-master/data/32-3.png"
	Resize_basewidth(50, path)  # nếu đổi size 1 ảnh thì gọi hàm Resize_hsize hoặc Resize_basewidth
	
if __name__ == '__main__':
	main()