import os
mather_file = 'CA达州' #输入你的母文件夹名称
address_of_yourPC = 'limen' #输入你特有的路径名

def name_list(address): #写个函数，返回路径下文件的名称列表
    
    filePath = address
    file_name_box = os.listdir(filePath)
    return file_name_box

file_name_box = name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\") #这里是母文件夹下有哪些人名
if  len(name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\"+file_name_box[0])[0]) == 8:
    name_and_time = []
    for i in file_name_box:
        child_file_name = name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\"+i) #子文件夹名称
        grandson_file_name = name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\"+i+"\\"+child_file_name[0]) #孙子文件夹名称,就是有txt文档那个位置的文件名称列表
        data = []
        for line in open("C:/Users/"+address_of_yourPC+"/Desktop/"+mather_file+"/"+i+"/"+child_file_name[0]+"/"+grandson_file_name[0],"r",encoding = 'utf-8'): #设置文件对象并读取每一行文件
            data.append(line)
        length = len(data)
        for j in range(0,length):
            length_2 = len(data[j])
            for k in range(0,length_2):
                if data[j][k] == '有' and data[j][k+1] =='效' and data[j][k+2] == '期' and data[j][k+3] == '从':
                        name_and_time.append(i)
                        name_and_time.append(data[j][k+4:k+23])
                        name_and_time.append('\n')
                        

else:
    name_and_time = []
    for i in file_name_box:
        child_file_name = name_list("C:\\Users\\"+address_of_yourPC+"\\Desktop\\"+mather_file+"\\"+i) #同样是母文件夹的路径加上，子文件，的名称
        data = []
        srcFile = 'C:/Users/'+address_of_yourPC+'/Desktop/'+mather_file+'/'+i+'/'+child_file_name[0]
        dstFile = 'C:/Users/'+address_of_yourPC+'/Desktop/'+mather_file+'/'+i+'/'+child_file_name[0]+'.txt'
        os.rename(srcFile, dstFile)
        for line in open("C:/Users/"+address_of_yourPC+"/Desktop/"+mather_file+"/"+i+"/"+child_file_name[0]+'.txt',"r",encoding = 'utf-8'): #设置文件对象并读取每一行文件
            data.append(line)
        length = len(data)
        for j in range(0,length):
            length_2 = len(data[j])
            for k in range(0,length_2):
                if data[j][k] == '有' and data[j][k+1] =='效' and data[j][k+2] == '期' and data[j][k+3] == '从':
                        name_and_time.append(i)
                        name_and_time.append(data[j][k+4:k+23])
                        name_and_time.append('\n')
                        os.rename(dstFile, srcFile)
                        break
for i in name_and_time:
    print(i)