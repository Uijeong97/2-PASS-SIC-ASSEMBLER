
# coding: utf-8

# In[1]:


'''import LOCCTR'''
from OPTAB import OPTAB
from SYMTAB import SYMTAB
from INTFILE import INTFILE


# In[4]:


'''
# PASS1
- 모든 문에 LOCCTR 배정 -> INTFILE 생성
- 모든 레이블에 배정된 LOCCTR 값 저장 -> SYMTAB 생성
- 어셈블러 지시자(BYTE, RESW)의 데이터 길이 결정
- 연상 명령어 조사하기 위해 OPTAB 불러온다.
'''

class Pass1:
    def __init__(self, srcfile):
        self.srcname=srcfile
        self.srcfile=open(srcfile,"r")
        self.intfile=INTFILE(srcfile)
        self.symtab=SYMTAB(srcfile)
        self.optab=OPTAB()
        self.pass1()
    
    def pass1(self):
        first=self.srcfile.readline()
        label,opcode,operand,flag=first[:8].replace(" ",""),first[9:16].replace(" ",""),first[17:].replace(" ","").replace("\n",""),''
        if opcode=='start' or 'START':
            startAddress=operand
            self.LOCCTR=startAddress
            self.intfile.w(hex(int(self.LOCCTR,16)),label,opcode,operand,flag)
            if label != "":
                self.symtab.w(label,hex(int(self.LOCCTR,16)),'')
        else:
            self.LOCCTR=0
        for line in self.srcfile.readlines():
            if line[0]!='.':
                label,opcode,operand,flag=line[:8].replace(" ",""),line[9:16].replace(" ","").replace("\n",""),line[17:].replace(" ","").replace("\n",""),''
                self.intfile.w(hex(int(self.LOCCTR,16)),label,opcode,operand,flag)
                
                if label != "":
                    found=self.symtab.findL(label)
                    if found:
                        self.symtab.setError(label)
                    else:
                        self.symtab.w(label,hex(int(self.LOCCTR,16)),'f')
                found=self.optab.findO(opcode)
                if found:
                    self.LOCCTR=str(hex(int(self.LOCCTR,16)+(3)))
                elif opcode=="word" or opcode=="WORD":
                    self.LOCCTR=str(hex(int(self.LOCCTR,16)+(3)))
                elif opcode=="resw" or opcode=="RESW":
                    self.LOCCTR=str(hex(int(self.LOCCTR,16)+(int(operand)*3)))
                elif opcode=="resb" or opcode=="RESB":
                    self.LOCCTR=str(hex(int(self.LOCCTR,16)+int(operand)))
                elif opcode=="byte" or opcode=="BYTE":
                    if operand[0]=="c" or operand[0]=="C":
                        self.LOCCTR=str(hex(int(self.LOCCTR,16)+(len(operand)-3)))
                    elif operand[0]=="x" or operand[0]=="X":
                        self.LOCCTR=str(hex(int(self.LOCCTR,16)+(len(operand)-3)/2))
                else:
                    if opcode=="end" or opcode=="END":
                        if label != "":
                            self.symtab.w(label,hex(int(self.LOCCTR,16)),'f')
                        break
                    self.intfile.setError(opcode)
                    flag='Error'

            
        self.progLength=hex(int(self.LOCCTR,16)-int(startAddress,16))
        self.srcfile.close()
        self.intfile.close()
        self.symtab.close()
        
                    


# In[5]:


