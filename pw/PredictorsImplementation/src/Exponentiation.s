	.file	"Exponentiation.c"
	.text
	.globl	global_history
	.bss
	.align 8
	.type	global_history, @object
	.size	global_history, 8
global_history:
	.zero	8
	.globl	cmpt
	.align 32
	.type	cmpt, @object
	.size	cmpt, 32
cmpt:
	.zero	32
	.text
	.globl	exponentiation
	.type	exponentiation, @function
exponentiation:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movl	%esi, -8(%rbp)
	movl	global_history(%rip), %eax
	cmpl	$1, %eax
	jle	.L2
	cmpl	$1, -8(%rbp)
	jne	.L2
	movsd	8+cmpt(%rip), %xmm1
	movsd	.LC0(%rip), %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, 8+cmpt(%rip)
	movl	global_history(%rip), %eax
	cmpl	$2, %eax
	jg	.L3
	movl	global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, global_history(%rip)
.L3:
	movl	-4(%rbp), %eax
	jmp	.L4
.L2:
	cmpl	$1, -8(%rbp)
	jne	.L5
	movsd	cmpt(%rip), %xmm1
	movsd	.LC0(%rip), %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, cmpt(%rip)
	movsd	8+cmpt(%rip), %xmm1
	movsd	.LC0(%rip), %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, 8+cmpt(%rip)
	movl	global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, global_history(%rip)
	movl	-4(%rbp), %eax
	jmp	.L4
.L5:
	movl	global_history(%rip), %eax
	testl	%eax, %eax
	jle	.L6
	movl	global_history(%rip), %eax
	subl	$1, %eax
	movl	%eax, global_history(%rip)
.L6:
	movl	4+global_history(%rip), %eax
	cmpl	$1, %eax
	jle	.L7
	movl	-8(%rbp), %eax
	andl	$1, %eax
	testl	%eax, %eax
	jne	.L7
	movsd	24+cmpt(%rip), %xmm1
	movsd	.LC0(%rip), %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, 24+cmpt(%rip)
	movl	4+global_history(%rip), %eax
	cmpl	$2, %eax
	jg	.L8
	movl	4+global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, 4+global_history(%rip)
.L8:
	movl	-8(%rbp), %eax
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	sarl	%eax
	movl	%eax, %edx
	movl	-4(%rbp), %eax
	imull	%eax, %eax
	movl	%edx, %esi
	movl	%eax, %edi
	call	exponentiation
	jmp	.L4
.L7:
	movl	-8(%rbp), %eax
	andl	$1, %eax
	testl	%eax, %eax
	jne	.L9
	movsd	16+cmpt(%rip), %xmm1
	movsd	.LC0(%rip), %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, 16+cmpt(%rip)
	movsd	24+cmpt(%rip), %xmm1
	movsd	.LC0(%rip), %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, 24+cmpt(%rip)
	movl	4+global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, 4+global_history(%rip)
	movl	-8(%rbp), %eax
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	sarl	%eax
	movl	%eax, %edx
	movl	-4(%rbp), %eax
	imull	%eax, %eax
	movl	%edx, %esi
	movl	%eax, %edi
	call	exponentiation
	jmp	.L4
.L9:
	movl	4+global_history(%rip), %eax
	testl	%eax, %eax
	jle	.L10
	movl	4+global_history(%rip), %eax
	subl	$1, %eax
	movl	%eax, 4+global_history(%rip)
.L10:
	movl	-8(%rbp), %eax
	subl	$1, %eax
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	sarl	%eax
	movl	%eax, %edx
	movl	-4(%rbp), %eax
	imull	%eax, %eax
	movl	%edx, %esi
	movl	%eax, %edi
	call	exponentiation
.L4:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	exponentiation, .-exponentiation
	.section	.rodata
.LC1:
	.string	"Res exp %d^%d : %d\n"
	.align 8
.LC2:
	.string	"State of first if predictor : %d\nState of second if predictor : %d\n"
	.align 8
.LC3:
	.string	"Stat of mispredictions of the predictor 1 : %f\nStat of mispredictions of the predictor 2 : %f\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$0, %edi
	call	time@PLT
	movl	%eax, %edi
	call	srand@PLT
	call	rand@PLT
	movslq	%eax, %rdx
	imulq	$550857529, %rdx, %rdx
	shrq	$32, %rdx
	movl	%edx, %ecx
	sarl	$7, %ecx
	cltd
	subl	%edx, %ecx
	movl	%ecx, %edx
	imull	$998, %edx, %edx
	subl	%edx, %eax
	movl	%eax, %edx
	leal	2(%rdx), %eax
	movl	%eax, -12(%rbp)
	call	rand@PLT
	movslq	%eax, %rdx
	imulq	$1125899907, %rdx, %rdx
	shrq	$32, %rdx
	movl	%edx, %ecx
	sarl	$18, %ecx
	cltd
	subl	%edx, %ecx
	movl	%ecx, %edx
	imull	$1000000, %edx, %edx
	subl	%edx, %eax
	movl	%eax, %edx
	leal	2(%rdx), %eax
	movl	%eax, -8(%rbp)
	movl	-8(%rbp), %edx
	movl	-12(%rbp), %eax
	movl	%edx, %esi
	movl	%eax, %edi
	call	exponentiation
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %ecx
	movl	-8(%rbp), %edx
	movl	-12(%rbp), %eax
	movl	%eax, %esi
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	4+global_history(%rip), %edx
	movl	global_history(%rip), %eax
	movl	%eax, %esi
	leaq	.LC2(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movsd	16+cmpt(%rip), %xmm0
	movq	cmpt(%rip), %rax
	movapd	%xmm0, %xmm1
	movq	%rax, %xmm0
	leaq	.LC3(%rip), %rdi
	movl	$2, %eax
	call	printf@PLT
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.section	.rodata
	.align 8
.LC0:
	.long	0
	.long	1072693248
	.ident	"GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
