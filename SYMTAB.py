
# coding: utf-8

# In[ ]:


'''
# SYMTAB
- p1:
레이블 이름과 주소를 SYMTAB에 입력
- p2:
피연산자 symbol을 SYMTAB에서 찾는 데 사용
operand 주소로 symtab의 값 저장

sym은 해쉬테이블 역할로 딕셔너리 형태
{'label':[LOCCTR,flag]}
'''
class SYMTAB:
    def __init__(self,srcfile):
        self.f=open(srcfile+"_symbolTab","w")
        self.sym={}
    def findL(self, label):
        if label in self.sym:
            return True
        else:
            return False
    def setError(self, label):
        sym[label][1]="Error"
    def w(self,label,LOCCTR,flag):
        self.sym[label]=[LOCCTR,flag]
        self.f.write(label+'\t'+LOCCTR+'\t'+flag)
    def close(self):
        self.f.close()

