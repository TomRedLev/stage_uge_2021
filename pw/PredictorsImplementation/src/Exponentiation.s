	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 14	sdk_version 10, 14
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3               ## -- Begin function exponentiation
LCPI0_0:
	.quad	4607182418800017408     ## double 1
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_exponentiation
	.p2align	4, 0x90
_exponentiation:                        ## @exponentiation
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movl	%edi, -8(%rbp)
	movl	%esi, -12(%rbp)
	cmpl	$2, _global_history(%rip)
	jl	LBB0_5
## %bb.1:
	cmpl	$1, -12(%rbp)
	jne	LBB0_5
## %bb.2:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	addsd	_cmpt+8(%rip), %xmm0
	movsd	%xmm0, _cmpt+8(%rip)
	cmpl	$3, _global_history(%rip)
	jge	LBB0_4
## %bb.3:
	movl	_global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history(%rip)
LBB0_4:
	movl	-8(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	LBB0_23
LBB0_5:
	cmpl	$1, -12(%rbp)
	jne	LBB0_7
## %bb.6:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movaps	%xmm0, %xmm1
	addsd	_cmpt(%rip), %xmm1
	movsd	%xmm1, _cmpt(%rip)
	addsd	_cmpt+8(%rip), %xmm0
	movsd	%xmm0, _cmpt+8(%rip)
	movl	_global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history(%rip)
	movl	-8(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	LBB0_23
LBB0_7:
	cmpl	$0, _global_history(%rip)
	jle	LBB0_9
## %bb.8:
	movl	_global_history(%rip), %eax
	subl	$1, %eax
	movl	%eax, _global_history(%rip)
LBB0_9:
	jmp	LBB0_10
LBB0_10:
	jmp	LBB0_11
LBB0_11:
	cmpl	$2, _global_history+4(%rip)
	jl	LBB0_16
## %bb.12:
	movl	-12(%rbp), %eax
	cltd
	movl	$2, %ecx
	idivl	%ecx
	cmpl	$0, %edx
	jne	LBB0_16
## %bb.13:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	addsd	_cmpt+24(%rip), %xmm0
	movsd	%xmm0, _cmpt+24(%rip)
	cmpl	$3, _global_history(%rip)
	jge	LBB0_15
## %bb.14:
	movl	_global_history+4(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history+4(%rip)
LBB0_15:
	movl	-8(%rbp), %eax
	imull	-8(%rbp), %eax
	movl	-12(%rbp), %ecx
	movl	%eax, -16(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	cltd
	movl	$2, %ecx
	idivl	%ecx
	movl	-16(%rbp), %edi         ## 4-byte Reload
	movl	%eax, %esi
	callq	_exponentiation
	movl	%eax, -4(%rbp)
	jmp	LBB0_23
LBB0_16:
	movl	-12(%rbp), %eax
	cltd
	movl	$2, %ecx
	idivl	%ecx
	cmpl	$0, %edx
	jne	LBB0_18
## %bb.17:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movaps	%xmm0, %xmm1
	addsd	_cmpt+16(%rip), %xmm1
	movsd	%xmm1, _cmpt+16(%rip)
	addsd	_cmpt+24(%rip), %xmm0
	movsd	%xmm0, _cmpt+24(%rip)
	movl	-8(%rbp), %eax
	imull	-8(%rbp), %eax
	movl	-12(%rbp), %ecx
	movl	%eax, -20(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	cltd
	movl	$2, %ecx
	idivl	%ecx
	movl	-20(%rbp), %edi         ## 4-byte Reload
	movl	%eax, %esi
	callq	_exponentiation
	movl	%eax, -4(%rbp)
	jmp	LBB0_23
LBB0_18:
	cmpl	$0, _global_history+4(%rip)
	jle	LBB0_20
## %bb.19:
	movl	_global_history+4(%rip), %eax
	subl	$1, %eax
	movl	%eax, _global_history+4(%rip)
LBB0_20:
	jmp	LBB0_21
LBB0_21:
	jmp	LBB0_22
LBB0_22:
	movl	-8(%rbp), %eax
	imull	-8(%rbp), %eax
	movl	-12(%rbp), %ecx
	subl	$1, %ecx
	movl	%eax, -24(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	cltd
	movl	$2, %ecx
	idivl	%ecx
	movl	-24(%rbp), %edi         ## 4-byte Reload
	movl	%eax, %esi
	callq	_exponentiation
	movl	%eax, -4(%rbp)
LBB0_23:
	movl	-4(%rbp), %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	xorl	%eax, %eax
	movl	%eax, %edi
	movl	$0, -4(%rbp)
	callq	_time
	movl	%eax, %ecx
	movl	%ecx, %edi
	callq	_srand
	callq	_rand
	cltd
	movl	$998, %ecx              ## imm = 0x3E6
	idivl	%ecx
	addl	$2, %edx
	movl	%edx, -8(%rbp)
	callq	_rand
	cltd
	movl	$10, %ecx
	idivl	%ecx
	addl	$2, %edx
	movl	%edx, -12(%rbp)
	movl	-8(%rbp), %edi
	movl	-12(%rbp), %esi
	callq	_exponentiation
	movl	%eax, -16(%rbp)
	movl	-8(%rbp), %esi
	movl	-12(%rbp), %edx
	movl	-16(%rbp), %ecx
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	_global_history(%rip), %esi
	movl	_global_history+4(%rip), %edx
	leaq	L_.str.1(%rip), %rdi
	movl	%eax, -20(%rbp)         ## 4-byte Spill
	movb	$0, %al
	callq	_printf
	movsd	_cmpt(%rip), %xmm0      ## xmm0 = mem[0],zero
	divsd	_cmpt+8(%rip), %xmm0
	movsd	_cmpt+16(%rip), %xmm1   ## xmm1 = mem[0],zero
	divsd	_cmpt+24(%rip), %xmm1
	leaq	L_.str.2(%rip), %rdi
	movl	%eax, -24(%rbp)         ## 4-byte Spill
	movb	$2, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -28(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_global_history         ## @global_history
.zerofill __DATA,__common,_global_history,8,2
	.globl	_cmpt                   ## @cmpt
.zerofill __DATA,__common,_cmpt,32,4
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"Res exp %d^%d : %d\n"

L_.str.1:                               ## @.str.1
	.asciz	"State of first if predictor : %d\nState of second if predictor : %d\n"

L_.str.2:                               ## @.str.2
	.asciz	"Stat of mispredictions of the predictor 1 : %f\nStat of mispredictions of the predictor 2 : %f\n"


.subsections_via_symbols
