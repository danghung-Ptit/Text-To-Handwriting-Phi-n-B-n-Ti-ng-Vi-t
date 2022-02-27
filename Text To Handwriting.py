#Importing Library
from PIL import Image
from sys import argv
import os
from docx import Document
import random


def PNG_PDF(PNG_FILE):
    rgba = Image.open(PNG_FILE)
    print(rgba)
    rgb = Image.new('RGB', (2632, 3176), (255, 255, 255))
    rgb.paste(rgba, mask=rgba.split()[3])
    PDF_FILE = PNG_FILE.replace(".png", ".pdf")
    rgb.save(PDF_FILE,'PDF', resoultion=100.0)


def Text_To_Handwriting(path_txt, path_data, chieucao, path_out):
    img_counter = 1
    A4_List = []
    if path_txt.endswith(".txt"):
        with open(path_txt, "r") as file:
            txt = file.read()
    elif path_txt.endswith(".docx"):
        document = Document(path_txt)
        txt = ''
        for p in document.paragraphs:
            txt += p.text + "\n"
    A4_name = "A4T{}".format(img_counter)
    print(A4_name)
    A4_name = Image.new('RGB', (2632, 3176), (255, 255, 255))
    A4_List.append(A4_name)
    sheet_width = A4_name.width
    Horizontal, vertical = 0, 0
    for i in txt:
        #print(i, ord(i))
        if vertical > (3176 // chieucao - 2) * chieucao:
            img_counter += 1
            A4_name = "A4T{}".format(img_counter)
            print(A4_name)
            A4_name = Image.new('RGB', (2632, 3176), (255, 255, 255))
            A4_List.append(A4_name)
            Horizontal = 0
            vertical = 0
        if ord(i) == 10:
            Horizontal = 0
            vertical += chieucao
            continue
        try:
            cases = Image.open(path_data + "{}-{}.png".format(str(ord(i)), random.randint(1, 3)))
            A4_name.paste(cases, (Horizontal, vertical))
            size = cases.width
            height = cases.height
            Horizontal += size
            if ord(i) == 32 and (sheet_width - Horizontal) < size *5:
                Horizontal = 0
                vertical += chieucao
        except Exception as e:
            print(e, "không có kí tự {} {} trong data".format(i, ord(i)))
    A4_counter = 1
    for A4 in A4_List:
        A4.show()
        path_A4 = os.path.join(path_out,"A4T{}".format(A4_counter) + ".png")
        A4_counter += 1
        A4.save(path_A4)
    
def main():
    path_txt = "/Users/abc/Documents/Code_doAn/Text-to-Handwriting-master/testword.docx" # đường dẫn file word hoặc txt
    path_data = "/Users/abc/Documents/Code_doAn/Text-to-Handwriting-master/data/" # đường dẫn data
    path_out = "/Users/abc/Documents/Code_doAn/Text-to-Handwriting-master/A4"    # đường dẫn lưu
    chieucao = 100
    Text_To_Handwriting(path_txt, path_data, chieucao, path_out)
    
if __name__ == '__main__':
    main()