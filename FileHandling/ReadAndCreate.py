import os


srcFilePath=r"C:\Users\hanshik\Documents\Python Scripts\Dict.txt"

destFilePath=r"C:\Users\hanshik\Documents\Python Scripts\dest.txt"

# file1=open(srcFilePath,'r')
# file2=open(destFilePath,'r+')
#
# # #print(file.read())
# #
# # # print()
# # #
# # # data=file.readline()
# # #
# # # while len(data)>0:
# # #     print(data)
# # #     data=file.readline()
# #
# #
# # data=str(file.readlines()).split("\n")
# #
# # print(data)
# 
#
# file2.write(file1.read())


# os.remove(destFilePath)

# check if the file is exist n the dest path

if os.path.exists(destFilePath):

    print("File Exist in the destination path....!!!")
else:
    print("No File Exist")