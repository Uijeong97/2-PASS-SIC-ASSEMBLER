# PASS1
- ��� ���� LOCCTR ���� -> INTFILE ����
- ��� ���̺� ������ LOCCTR �� ���� -> SYMTAB ����
- ����� ������(BYTE, RESW)�� ������ ���� ����

#Intfile
- ������ �ּ�, ���� �÷���

# PASS2
- ��ɾ� �����( ������ �ڵ� ����, �ּ� ����)
- BYTE, WORD �� ���ǵǴ� ������ �� ����
- ����� ������ ó��
- ���� ���α׷��� ����� ����Ʈ ���

 
# LOCCTR
- �ּ� ó��
- start ����


# OPTAB
- Ofinfo ����Ʈ=[opcode, formatbytes, operandNum]
- ���� �ؽ����̺� ���·� obtab={'opkey':[ofinfo]}
- p1:
���� ��ɾ� �����ϴ� �� ���
��ɾ��� ���̸�ŭ LOCCTR ����
- p2:
��ɾ�->���� ����

# SYMTAB
- p1:
���̺� �̸��� �ּҸ� SYMTAB�� �Է�
- p2:
�ǿ����� symbol�� SYMTAB���� ã�� �� ���
operand �ּҷ� symtab�� �� ����