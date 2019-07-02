import os
import tempfile

class File:
    def __init__(self,filename):
        self.filename=filename
        
    def write(self,string):
        with open(self.filename, 'w') as f:
            f.write(string)
        
    def __add__(self,obj):
        storage_path = os.path.join(tempfile.gettempdir(), 'magic_test.txt')
        content=None
        with open(self.filename, 'r') as f:
            content=f.read()
        with open(obj.filename, 'r') as f:
            content+=f.read()
        with open(storage_path, 'w') as f:
            f.write(content)
            
    def __str__(self):
        return self.filename
    
    def __iter__(self):
        return open(self.filename, 'r')
    
    def __next__(self):      
        return self.next()


first = File("D:\Semi\magic_example1.txt")
second = File("D:\Semi\magic_example2.txt")
#first.write('line1\nline1\n')
##second.write('line2\nline2\n')
##new_obj = first + second
#print(first)

for line in first:
    print(line)
    
for line in second:
    print(line)


