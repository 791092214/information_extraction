# information_extraction
    这个小程序，是用于针对特定文件的信息提取。该文件由银行服务器返回，包含了，到期未还款客户，的信息。我们的任务是将里面特定的  
    信息提取出来，以便后期制作正式的起诉文件。由于IT部门给过来的数据是比较混乱的，人工手动提取信息会耗费大量的时间，所以编  
    写这个小程序以提高处理文件的效率。经过分析，IT部门返回的文件主要包含两种形式，下面以两个例子来说明，  
    
    第一种:
    IT部门返回一个文件夹，叫“CA达州”，这个文件夹下包含了一个，名称长度（length）,为8的文件夹，在这个length为8的文件夹里，又包
    含了几个文件夹，这些文件夹的名称是客户的名字，而在每个客户的文件夹下，又包含了几个文件，我们所需要的信息就要从这些文件的第
    一个文件中提取。
    
    第二种文件形式与第一种类似，但有两个不同点：1，第二种文件形式中的，包含所需信息的文件，不是txt格式，所以在处理时先将其改为
    txt格式，在进行信息提取后，再改回原来的格式。2，第二种文件形式中，没有那个长度(length)为8的文件夹。
    
    我们需要从每一位客户的文件夹下提取对应的信息。
    
    总体来说，这个小程序的逻辑就是，先区分返回的文件是属于第一种情况还是第二种情况，然后逐步进入对应的文件进行信息提取。
