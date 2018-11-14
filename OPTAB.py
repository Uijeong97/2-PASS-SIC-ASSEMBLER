
# coding: utf-8

# In[ ]:
'''
# OPTAB
- Ofinfo 리스트=[opcode, formatbytes, operandNum]
- 해쉬테이블 형태로 obtab={'opkey':[ofinfo]}
- p1:
연상 명령어 조사하는 데 사용
명령어의 길이만큼 LOCCTR 증가
- p2:
명령어->기계어 번역
'''

class OPTAB:
    def __init__(self):
        self.opt={}
        inf=open("opTable.txt","r")
        for line in inf.readlines():
            opKey,opCode,formatBytes,operandsNum=line.split()
            opInfo=[opCode,int(formatBytes),int(operandsNum)]
            self.opt[opKey]=opInfo
            
    def findO(self,opcode):
        return opcode.upper() in self.opt


