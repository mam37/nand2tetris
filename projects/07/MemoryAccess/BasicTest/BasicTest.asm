@256
D=A
@SP
M=D
@$$BEGIN
0;JMP
($$EQ)
@R13
M=D
@SP
A=M
D=M
A=A-1
D=M-D
@$$EQ.TRUE
D;JEQ
($$EQ.FALSE)
D=0
@$$EQ.END
0;JMP
($$EQ.TRUE)
D=-1
($$EQ.END)
@SP
A=M-1
M=D
@R13
A=M
0;JMP
($$LT)
@R13
M=D
@SP
A=M
D=M
A=A-1
D=M-D
@$$LT.TRUE
D;JLT
($$LT.FALSE)
D=0
@$$LT.END
0;JMP
($$LT.TRUE)
D=-1
($$LT.END)
@SP
A=M-1
M=D
@R13
A=M
0;JMP
($$GT)
@R13
M=D
@SP
A=M
D=M
A=A-1
D=M-D
@$$GT.TRUE
D;JGT
($$GT.FALSE)
D=0
@$$GT.END
0;JMP
($$GT.TRUE)
D=-1
($$GT.END)
@SP
A=M-1
M=D
@R13
A=M
0;JMP
($$BEGIN)
//C_PUSH constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_POP local 0
@SP
M=M-1
@0
D=A
@LCL
D=M+D
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//C_PUSH constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_POP argument 2
@SP
M=M-1
@2
D=A
@ARG
D=M+D
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//C_POP argument 1
@SP
M=M-1
@1
D=A
@ARG
D=M+D
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//C_PUSH constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_POP this 6
@SP
M=M-1
@6
D=A
@THIS
D=M+D
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//C_PUSH constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_POP that 5
@SP
M=M-1
@5
D=A
@THAT
D=M+D
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//C_POP that 2
@SP
M=M-1
@2
D=A
@THAT
D=M+D
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//C_PUSH constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_POP temp 6
@SP
M=M-1
@SP
A=M
D=M
@R11
M=D
//C_PUSH local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH that 5
@5
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M+D
//C_PUSH argument 1
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M-D
//C_PUSH this 6
@6
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH this 6
@6
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M+D
//sub
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M-D
//C_PUSH temp 6
@R11
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M+D
