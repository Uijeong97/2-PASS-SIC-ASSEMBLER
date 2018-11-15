
# coding: utf-8

# In[ ]:


class Objpgm:
    def __init__(self,srcfile):
        self.objpgm=open(srcfile+"_Objpgm","w")
        self.recordList=[]
        self.tempSTRAddr=[]
    def writeHR(self,progLen):
        line=self.recordList[0]
        self.objpgm.write("H"+line['label']+' '*(6-len(line['label']))+'0'*(6-len(line['operand']))+line['operand']+'0'*(6-len(progLen))+progLen+"\n")
   
    def writeTR(self,TRList):
        index=0
        trRecord=''
        while index < len(TRList):
            if TRList[index]=="-":
                index+=1
                continue
            self.LenTR=0
            self.objpgm.write("T"+'0'*(6-len(self.tempSTRAddr[index]))+self.tempSTRAddr[index].upper())
            while index <len(TRList) and self.LenTR+len(TRList[index])//2<=30 and TRList[index]!="-":
                trRecord+=TRList[index]
                self.LenTR+=len(TRList[index])//2
                index+=1
            strLenTR='0'*(2-len(format(int(self.LenTR),'X')))+format(int(self.LenTR),'X')
            trRecord=strLenTR+trRecord
            self.objpgm.write(trRecord.upper()+"\n")
            trRecord=""
           # index+=1
        
    def writeER(self,startAddr):
        startAddr=format(int(startAddr,16),'x') #0x 없애주기위해 작업
        self.objpgm.write("E"+'0'*(6-len(startAddr))+startAddr+"\n")
        
   # def checkFit(self):
        

