#!/usr/bin/env python3

import cv2
import numpy as np
import os
cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0
img_counter = 0
image = cv2.imread('/Users/abc/Downloads/ImageToText/49.jpg') # đường dẫn ảnh
path = '/Users/abc/Documents/Code_doAn/Text-to-Handwriting-master/data'				# đường dẫn folder lưu ảnh
oriImage = image.copy()

def mouse_crop(event, x, y, flags, param):
	global x_start, y_start, x_end, y_end, cropping, img_counter
	if event == cv2.EVENT_LBUTTONDOWN: # nếu nút chuột trái là xuống, hãy bắt đầu ghi giá toạ độ
		x_start, y_start, x_end, y_end = x, y, x, y
		cropping = True
	elif event == cv2.EVENT_MOUSEMOVE: # Chuột đang di chuyển
		if cropping == True:
			x_end, y_end = x, y
	elif event == cv2.EVENT_LBUTTONUP: # nếu nút chuột trái được thả
		x_end, y_end = x, y # ghi lại tọa độ kết thúc (x, y)
		cropping = False
		refPoint = [(x_start, y_start), (x_end, y_end)]
		if len(refPoint) == 2:
			img_cut = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]] # cắt ảnh copy theo toạ độ được ghi
			cv2.imshow("Cropped", img_cut)
			img_name = "{}B18DCDT100BS.png".format(img_counter) # sửa thành msv của mọi người
			cv2.imwrite(os.path.join(path, img_name), img_cut)
			img_counter += 1
			
def main():
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", mouse_crop)
	while True:
		i = image.copy()
		if not cropping:
			cv2.imshow("image", image)
		elif cropping:
			cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
			cv2.imshow("image", i)
		key = cv2.waitKey(1)
		if key == ord('q'): # nhấn q để thoát
			print("thoát")
			break
	cv2.destroyAllWindows()
	
if __name__ == '__main__':
	main()