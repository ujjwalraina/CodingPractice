import pandas
import glob2
"""
with open("/home/ujjwal/Desktop/1.txt",'w') as file:
    file.write("values\n100\n200\n300")
with open("/home/ujjwal/Desktop/2.txt",'w') as file:
    file.write("values\n100\n200\n300")
with open("/home/ujjwal/Desktop/3.txt",'w') as file:
    file.write("values\n100\n200\n300")

pandas_obj1 = pandas.read_csv("/home/ujjwal/Desktop/1.txt")
print(pandas_obj1.mean())

pandas_obj2 = pandas.read_csv("/home/ujjwal/Desktop/2.txt")
print(pandas_obj2.mean())

pandas_obj3 = pandas.read_csv("/home/ujjwal/Desktop/3.txt")
print(pandas_obj3.mean())
"""

file_list1=["/home/ujjwal/Desktop/1.txt","/home/ujjwal/Desktop/2.txt","/home/ujjwal/Desktop/3.txt"]
file_list2 = glob2.glob("/home/ujjwal/Desktop/*.txt")
print(file_list2)
file_content= "values\n100\n200\n300"
for i in file_list1:
    with open(i,'w') as file:
        file.write(file_content)
    data_frame = pandas.read_csv(i)
    print(data_frame.mean())
for i in file_list2:
    with open(i,'w') as file:
        file.write(file_content)
    data_frame = pandas.read_csv(i)
    print(float(data_frame.mean()))