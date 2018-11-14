# PASS1
- 모든 문에 LOCCTR 배정 -> INTFILE 생성
- 모든 레이블에 배정된 LOCCTR 값 저장 -> SYMTAB 생성
- 어셈블러 지시자(BYTE, RESW)의 데이터 길이 결정

#Intfile
- 배정된 주소, 오류 플래그

# PASS2
- 명령어 어셈블( 연산자 코드 번역, 주소 조사)
- BYTE, WORD 등 정의되는 데이터 값 생성
- 어셈블러 지시자 처리
- 목적 프로그램과 어셈블러 리스트 출력

 
# LOCCTR
- 주석 처리
- start 감지


# OPTAB
- Ofinfo 리스트=[opcode, formatbytes, operandNum]
- 정적 해쉬테이블 형태로 obtab={'opkey':[ofinfo]}
- p1:
연상 명령어 조사하는 데 사용
명령어의 길이만큼 LOCCTR 증가
- p2:
명령어->기계어 번역

# SYMTAB
- p1:
레이블 이름과 주소를 SYMTAB에 입력
- p2:
피연산자 symbol을 SYMTAB에서 찾는 데 사용
operand 주소로 symtab의 값 저장