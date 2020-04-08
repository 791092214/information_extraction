import os
mather_file = 'CA达州' #输入你的一级文件夹名称
address_of_yourPC = 'limen' #输入你特有的路径名

def name_list(address): #写个函数，返回特定路径下，所有文件的名称
    
    filePath = address
    file_name_box = os.listdir(filePath)
    return file_name_box

file_name_box = name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\") #这里是一级文件夹下有哪些文件
if  len(name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\"+file_name_box[0])[0]) == 8: #第一种情况
    name_and_time = []
    for i in file_name_box:
        child_file_name = name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\"+i) #二级文件夹下有哪些文件
        grandson_file_name = name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\"+i+"\\"+child_file_name[0]) #三级文件下有哪些文件
        data = []
        for line in open("C:/Users/"+address_of_yourPC+"/Desktop/"+mather_file+"/"+i+"/"+child_file_name[0]+"/"+grandson_file_name[0],"r",encoding = 'utf-8'): #读取文件
            data.append(line)
        #读取txt文档之后，发现读取出来的文件的形式，是这样的，“[[sdfsdfsdf],[lkjljlkjlk]]”，所以需要逐步进入每个list进行处理
        length = len(data)
        for j in range(0,length):
            length_2 = len(data[j])
            for k in range(0,length_2):
                if data[j][k] == '有' and data[j][k+1] =='效' and data[j][k+2] == '期' and data[j][k+3] == '从': # “有效期从” 这四个字连续出现
                        name_and_time.append(i)
                        name_and_time.append(data[j][k+4:k+23]) # 提取我们要的信息
                        name_and_time.append('\n')
                        break
#下面的代码与上面几乎相同，唯一不一样的，是要将原文件修改成txt文件，以方便读取。
else: #第二种情况
    name_and_time = []
    for i in file_name_box:
        child_file_name = name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\"+i)
        data = []
        srcFile = 'C:/Users/'+address_of_yourPC+'/Desktop/'+mather_file+'/'+i+'/'+child_file_name[0]
        dstFile = 'C:/Users/'+address_of_yourPC+'/Desktop/'+mather_file+'/'+i+'/'+child_file_name[0]+'.txt'
        os.rename(srcFile, dstFile) #将原文件修改成txt文档
        for line in open("C:/Users/"+address_of_yourPC+"/Desktop/"+mather_file+"/"+i+"/"+child_file_name[0]+'.txt',"r",encoding = 'utf-8'):
            data.append(line)
        length = len(data)
        for j in range(0,length):
            length_2 = len(data[j])
            for k in range(0,length_2):
                if data[j][k] == '有' and data[j][k+1] =='效' and data[j][k+2] == '期' and data[j][k+3] == '从':
                        name_and_time.append(i)
                        name_and_time.append(data[j][k+4:k+23])
                        name_and_time.append('\n')
                        os.rename(dstFile, srcFile) # 再把文件名改回来
                        break
for i in name_and_time: #打印结果
    print(i)

'''
返回的信息是类似于这样的信息：

张三
2012-10-27 10:00:27

李四
2012-10-28 10:00:28

王五
2012-10-29 10:00:29
'''
