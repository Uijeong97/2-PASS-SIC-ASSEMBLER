
# coding: utf-8

# In[ ]:


class OPTAB:
    def __init__(self):
        self.optab={}
        inf=open("opTable.txt","r")
        for line in inf.readlines():
            print(line)
            
            a=line.split()
            opKey=a[0]
            opCode=a[1]
            formatBytes=a[2]
            operandsNum=a[3]
            opInfo=[opCode,formatBytes,operandsNum]
            self.optab[opKey]=opInfo
            
    def findO(self,opcode):
        if opcode in self.optab:
            return True
        else:
            return False
        

