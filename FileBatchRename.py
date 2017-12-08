import os
basePath ='D:\EFECWork\MSSQL\ProjectScript\ApolloDWDataSource'
fileList = os.listdir(basePath)
for file in fileList:
    newFile = file.replace('[','').replace(']','')
    # print(newFile)
    fileX = basePath+'\\' + file
    fileY =  basePath+'\\' + newFile
    #print(fileX)
    os.rename(fileX,fileY)