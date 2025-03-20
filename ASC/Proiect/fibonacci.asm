global main
extern printf, scanf

section .data
format:    db '%15ld', 10, 0
title:     db 'Fibonacci numbers', 10, 0
prompt:    db 'Enter the number of Fibonacci numbers to display: ', 0
input_fmt: db '%d', 0

section .bss
num resd 1

section .text
main:
    push rbp

    ; afisam titlul
    mov rdi, title
    mov rax, 0
    call printf

    mov rdi, prompt
    call printf

    ; se citeste input-ul utilizatorului
    mov rdi, input_fmt
    lea rsi, [num]
    mov rax, 0
    call scanf

    ; incarcam numarul de numere fibonacci care trebuie afisate
    mov eax, [num]        ; incarcam input-ul utilizatorului
    mov ecx, eax          ; setam contorul in eax

    ; initializam variabilele de care avem nevoie pentru a printa numerele din sirul lui Fibonacci
    mov rax, 0            ; rax retine primul numar din sirul lui Fibonacci
    mov rbx, 1            ; rbx retine cel de-al doilea numar din sirul lui Fibonacci

print:
    ; salvam registrii rax si rcx inainte de printare
    push rax              ; salvam numarul curent
    push rcx              ; salvam contorul
    mov rdi, format
    mov rsi, rax
    mov eax, 0
    call printf

    ; reinitializam rcx si rax dupa printarea numerelor
    pop rcx               ; restabilim contorul
    pop rax               ; restabilim numarul curent

    ; actualizam sirul lui Fibonacci
    mov rdx, rax          ; salvam numarul curent in rdx
    mov rax, rbx          ; urmatorul numar devine numarul curent
    add rbx, rdx          ; calculam urmatorul numar

    ; scadem contorul cu 1 si verificam daca a ajuns la 0
    dec rcx               ; scadem contorul
    jnz print             ; daca contorul nu a ajuns la 0 => loop-ul continua

    pop rbp
    mov rax, 0
    ret
