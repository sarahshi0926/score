#coding=utf-8
#使用windows系统  python3.7

import openpyxl    #方便将数据存入excel
fr=open('xyj.txt','rb')  
'''
r:默认值，表示从文件读取数据。返回的是str
w:表示要向文件写入数据，并截断以前的内容
a:表示要向文件写入数据，添加到当前内容尾部
r+:表示对文件进行可读写操作（删除以前的所有数据）
r+a：表示对文件可进行读写操作（添加到当前文件尾部）
b:表示要读写二进制数据，返回的是bytes
'''
cha=[]         #将不同的字存在列表中
stat={}        #将字和出现的次数存在字典中
fuhao=['，','。','：','“','”','！','？','【','】','；','《','》','’','、','‘']
for line in fr:
 	line=line.decode('utf-8').strip()        #decode将读取的内容解码成utf-8   strip()去掉行两边的空格
 	if len(line)==0:
 		continue

 	for x in range(len(line)):
 		if line[x] not in cha:
 			if line[x] not in fuhao:
 				cha.append(line[x])

 		if line[x] not in stat.keys():
 			if line[x] not in fuhao:
 				stat[line[x]]=0
 		else:
 			stat[line[x]]+=1

stat=sorted(stat.items(),key=lambda d:d[1],reverse=True)   #将字典根据值降序排列
#stat.items()将stat转换为可迭代对象，items()方法将字典的元素转换为元组，而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
#若对key值进行排序，sorted(stat.keys())即可
'''
sort和sorted的比较
用sort函数对列表排序时会影响列表本身，而sorted不会。(list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。)
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
sorted用法：
sorted(iterable, key=None, reverse=False)  
       可迭代对象，进行比较的元素，
'''
'''
python3读写excel
2007版以前的Excel（xls结尾的），需要使用xlrd读，xlwt写。 
2007版以后的Excel（xlsx结尾的），需要使用openpyxl来读写。   pip install openpyxl
'''
wb=openpyxl.Workbook()     #新建excel       三步走：打开Workbook，定位Sheet，操作Cell
sheet=wb.active            #找到活动的sheet页
sheet.title='西游记'     #sheet的名字，空的excel表默认的sheet页的名字就叫Sheet，如果想改名字，直接给title赋值
for i in range(len(stat)):
	for j in range(len(stat[i])):
		sheet.cell(row=i+1,column=j+1,value=stat[i][j])      
		''' row：单元格所在的行
			column：单元格坐在的列
			value：单元格的值'''

wb.save(r'C:\Users\ZLC\Desktop\data\xyj.xlsx')     #保存路径
print('写入数据成功！')

fr.close()
