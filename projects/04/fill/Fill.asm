// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


// Set @coord to @SCREEN
(reset_coord) 
    @SCREEN
    D=A
    @coord
    M=D

// If a keypress is registered,
// jump to @isinput. Otherwise,
// proceed to @noinput
(chkinput)     
    @KBD
    D=M
    @setblack
    D;JNE



(setwhite)
    @0
    D=A
    @color
    M=D
    @paint
    0;JMP
(setblack)
    @0
    D=!A
    @color
    M=D


(paint)
    @color
    D=M
    @coord
    A=M
    M=D



    

    D=A+1


    @coord
    M=D
   
    @KBD
    D=D-A 
    @reset_coord
    D;JEQ

    @chkinput
    0;JMP
