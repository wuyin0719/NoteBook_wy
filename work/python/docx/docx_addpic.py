#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/17 16:25
# @Author  : 5in


from docx import Document
from docx.shared import Cm
from docx.shared import Pt
# from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn  # 中文格式
import os

rows_n =2  # 偶数
clos_n = 1  # 输入需要的表格大小
# picture_path = 'D:/1project/ABAQUS/'
# os.chdir('D:/1project/ABAQUS')  # 工作目录
# pic_name = 'GJL_bogie_pure_M'
file_name = 'GJL_bogie.docx'
doc = Document()  # 创建一个新的word
doc.styles['Normal'].font.name = u'Times New Roman'  # 设置文档基础字体(all)
doc.styles['Normal'].element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体')
sec = doc.sections[0]


fo1=r'D:\wy\data\路面修改\20220616pm\0615\dwg'
fo2=r'D:\wy\data\路面修改\20220616pm\0615\modifyed'


# listdir=os.listdir(fo1)
# numorder=[int(l.split('_')[0] for l in listdir]
listdir=[str(i+1)+'_1.jpg' for i in range(20)]
# listdir.sort()
for file in listdir:
    doc.add_heading('bookMarks'+file.split('_')[0], level=1)
    table1 = doc.add_table(rows=rows_n, cols=clos_n)
    table1.style = 'Normal Table'
    count = 1;
    control = 1
    sec.left_margin = Cm(1.2)
    sec.right_margin = Cm(1.2)
    for row in range(rows_n):
        cells = table1.rows[row].cells
        if row % 2 == 1:
            for col in range(clos_n):
                ph = cells[col].paragraphs[0]  # 表格本身有一个paragraph,引用即可；添加pra:add_paragraph()
                # ph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                run = ph.add_run()
                try:
                    if col==1:
                        print(os.path.join(fo1,file))
                        run.add_picture(os.path.join(fo1,file), width=Cm(10))
                    else:
                        print(os.path.join(fo2, file))
                        run.add_picture(os.path.join(fo2, file), width=Cm(10))
                    # count += 1
                except FileNotFoundError:
                    break
        else:
            for col in range(clos_n):
                ph = cells[col].paragraphs[0]
                # ph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                if col==0:
                    run = ph.add_run(f'gpkg新的')
                else:
                    run = ph.add_run(f'dwg旧的')
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10.5)
                control += 1

    # break
# run=table1.cell(2,1).add_paragraph('Add_one',style='List Bullet')
# run=table1.cell(2,1).paragraphs[1].add_run()
# pic=run.add_picture('D:/1project/ABAQUS/S3.png')
# pic.height=Cm(2)
# pic.width=Cm(2)

doc.save(file_name)
