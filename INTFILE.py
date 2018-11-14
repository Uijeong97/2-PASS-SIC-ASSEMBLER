
# coding: utf-8

# In[2]:


class INTFILE:
    def __init__(self,srcfile):
        self.f=open(srcfile+"_intfile","w")
        self.lines=[]
    def w(self,LOCCTR,label,opcode,operand,flag):
        d={}
        self.f.write(LOCCTR+'\t'+label+'\t'+opcode+'\t'+operand+'\t'+flag+'\n')
        d['LOCCTR']=LOCCTR
        d['label']=label
        d['opcode']=opcode
        d['operand']=operand
        d['flag']=flag
        self.lines.append(d)
    def setError(self, opcode):
        self.f.write(opcode+' is not fount in optab')
    def close(self):
        self.f.close()

