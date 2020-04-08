# information_extraction
    这个小程序，是用于针对特定文件的信息提取。该文件由银行服务器返回，包含了，到期未还款客户，的信息。我们的任务是将里面特定的  
    信息提取出来，以便后期制作正式的起诉文件。由于IT部门给过来的数据是比较混乱的，人工手动提取信息会耗费大量的时间，所以编  
    写这个小程序以提高处理文件的效率。经过分析，IT部门返回的文件主要包含两种形式，下面以两个例子来说明，  
    第一种:
![](https://github.com/791092214/information_extraction/blob/master/1586338081(1).png?raw=true)
    
    IT部门返回一个文件夹，叫做“CA达州”，里面包含了几个文件夹，这些文件夹的名称是客户的名字，而在每个客户的文件夹  
    下，又包含了几个文件，我们所需要的信息就要从，文件1.txt，中提取。
    
    第二种文件形式与第一种类似，唯一的不同是，第二种文件形式中的，文件1，不是txt格式，所以在处理时将其改为txt格式，在进行信息  
    提取完成后，再改回原来的格式。
    
    文件1.txt，类似于服务器的日志。这个日志中的信息是比较混乱的，所以我们通过程序将需要的信息提取出来。
    
    总体来说，这个小程序的逻辑就是，先区分返回的文件是属于第一种情况还是第二种情况，然后逐步进入对应的文件进行信息提取。
    
    
