	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 14	sdk_version 10, 14
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3               ## -- Begin function min_max
LCPI0_0:
	.quad	4607182418800017408     ## double 1
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_min_max
	.p2align	4, 0x90
_min_max:                               ## @min_max
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$64, %rsp
	movl	$2, %eax
	movl	%eax, %ecx
	movl	$4, %eax
	movl	%eax, %edx
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movq	%rcx, %rdi
	movq	%rdx, %rsi
	callq	_calloc
	movl	$4, %r8d
	movl	%r8d, %edi
	movl	$8, %r8d
	movl	%r8d, %esi
	movq	%rax, -24(%rbp)
	callq	_calloc
	movl	$16, %r8d
	movl	%r8d, %edi
	movq	%rax, -32(%rbp)
	callq	_malloc
	movq	%rax, -40(%rbp)
	movq	-8(%rbp), %rax
	movl	(%rax), %r8d
	movq	-40(%rbp), %rax
	movl	%r8d, (%rax)
	movq	-40(%rbp), %rax
	movl	$0, 4(%rax)
	movq	-8(%rbp), %rax
	movl	(%rax), %r8d
	movq	-40(%rbp), %rax
	movl	%r8d, 8(%rax)
	movq	-40(%rbp), %rax
	movl	$0, 12(%rax)
	movl	$1, -44(%rbp)
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	movl	-44(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jge	LBB0_26
## %bb.2:                               ##   in Loop: Header=BB0_1 Depth=1
	movq	-24(%rbp), %rax
	cmpl	$2, (%rax)
	jl	LBB0_7
## %bb.3:                               ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-44(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-40(%rbp), %rax
	cmpl	(%rax), %edx
	jge	LBB0_7
## %bb.4:                               ##   in Loop: Header=BB0_1 Depth=1
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	-32(%rbp), %rax
	addsd	8(%rax), %xmm0
	movsd	%xmm0, 8(%rax)
	movq	-24(%rbp), %rax
	cmpl	$3, (%rax)
	jge	LBB0_6
## %bb.5:                               ##   in Loop: Header=BB0_1 Depth=1
	movq	-24(%rbp), %rax
	movl	(%rax), %ecx
	addl	$1, %ecx
	movl	%ecx, (%rax)
LBB0_6:                                 ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-44(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-40(%rbp), %rax
	movl	%edx, (%rax)
	movl	-44(%rbp), %edx
	movq	-40(%rbp), %rax
	movl	%edx, 4(%rax)
	jmp	LBB0_13
LBB0_7:                                 ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-44(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-40(%rbp), %rax
	cmpl	(%rax), %edx
	jge	LBB0_9
## %bb.8:                               ##   in Loop: Header=BB0_1 Depth=1
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	-32(%rbp), %rax
	movaps	%xmm0, %xmm1
	addsd	(%rax), %xmm1
	movsd	%xmm1, (%rax)
	movq	-32(%rbp), %rax
	addsd	8(%rax), %xmm0
	movsd	%xmm0, 8(%rax)
	movq	-24(%rbp), %rax
	movl	(%rax), %ecx
	addl	$1, %ecx
	movl	%ecx, (%rax)
	movq	-8(%rbp), %rax
	movslq	-44(%rbp), %rdx
	movl	(%rax,%rdx,4), %ecx
	movq	-40(%rbp), %rax
	movl	%ecx, (%rax)
	movl	-44(%rbp), %ecx
	movq	-40(%rbp), %rax
	movl	%ecx, 4(%rax)
	jmp	LBB0_12
LBB0_9:                                 ##   in Loop: Header=BB0_1 Depth=1
	movq	-24(%rbp), %rax
	cmpl	$0, (%rax)
	jle	LBB0_11
## %bb.10:                              ##   in Loop: Header=BB0_1 Depth=1
	movq	-24(%rbp), %rax
	movl	(%rax), %ecx
	subl	$1, %ecx
	movl	%ecx, (%rax)
LBB0_11:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_12
LBB0_12:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_13
LBB0_13:                                ##   in Loop: Header=BB0_1 Depth=1
	movq	-24(%rbp), %rax
	cmpl	$2, 4(%rax)
	jl	LBB0_18
## %bb.14:                              ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-44(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-40(%rbp), %rax
	cmpl	8(%rax), %edx
	jle	LBB0_18
## %bb.15:                              ##   in Loop: Header=BB0_1 Depth=1
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	-32(%rbp), %rax
	addsd	24(%rax), %xmm0
	movsd	%xmm0, 24(%rax)
	movq	-24(%rbp), %rax
	cmpl	$3, 4(%rax)
	jge	LBB0_17
## %bb.16:                              ##   in Loop: Header=BB0_1 Depth=1
	movq	-24(%rbp), %rax
	movl	4(%rax), %ecx
	addl	$1, %ecx
	movl	%ecx, 4(%rax)
LBB0_17:                                ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-44(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-40(%rbp), %rax
	movl	%edx, 8(%rax)
	movl	-44(%rbp), %edx
	movq	-40(%rbp), %rax
	movl	%edx, 12(%rax)
	jmp	LBB0_24
LBB0_18:                                ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-44(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-40(%rbp), %rax
	cmpl	8(%rax), %edx
	jle	LBB0_20
## %bb.19:                              ##   in Loop: Header=BB0_1 Depth=1
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	-32(%rbp), %rax
	movaps	%xmm0, %xmm1
	addsd	16(%rax), %xmm1
	movsd	%xmm1, 16(%rax)
	movq	-32(%rbp), %rax
	addsd	24(%rax), %xmm0
	movsd	%xmm0, 24(%rax)
	movq	-24(%rbp), %rax
	movl	4(%rax), %ecx
	addl	$1, %ecx
	movl	%ecx, 4(%rax)
	movq	-8(%rbp), %rax
	movslq	-44(%rbp), %rdx
	movl	(%rax,%rdx,4), %ecx
	movq	-40(%rbp), %rax
	movl	%ecx, 8(%rax)
	movl	-44(%rbp), %ecx
	movq	-40(%rbp), %rax
	movl	%ecx, 12(%rax)
	jmp	LBB0_23
LBB0_20:                                ##   in Loop: Header=BB0_1 Depth=1
	movq	-24(%rbp), %rax
	cmpl	$0, 4(%rax)
	jle	LBB0_22
## %bb.21:                              ##   in Loop: Header=BB0_1 Depth=1
	movq	-24(%rbp), %rax
	movl	4(%rax), %ecx
	subl	$1, %ecx
	movl	%ecx, 4(%rax)
LBB0_22:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_23
LBB0_23:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_24
LBB0_24:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_25
LBB0_25:                                ##   in Loop: Header=BB0_1 Depth=1
	movl	-44(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -44(%rbp)
	jmp	LBB0_1
LBB0_26:
	movq	-24(%rbp), %rax
	movl	(%rax), %esi
	movq	-24(%rbp), %rax
	movl	4(%rax), %edx
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movq	-32(%rbp), %rdi
	movsd	(%rdi), %xmm0           ## xmm0 = mem[0],zero
	movq	-32(%rbp), %rdi
	divsd	8(%rdi), %xmm0
	movq	-32(%rbp), %rdi
	movsd	16(%rdi), %xmm1         ## xmm1 = mem[0],zero
	movq	-32(%rbp), %rdi
	divsd	24(%rdi), %xmm1
	leaq	L_.str.1(%rip), %rdi
	movl	%eax, -48(%rbp)         ## 4-byte Spill
	movb	$2, %al
	callq	_printf
	movq	-40(%rbp), %rdi
	movl	%eax, -52(%rbp)         ## 4-byte Spill
	movq	%rdi, %rax
	addq	$64, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_complete_array         ## -- Begin function complete_array
	.p2align	4, 0x90
_complete_array:                        ## @complete_array
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	xorl	%eax, %eax
	movl	%eax, %ecx
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movq	%rcx, %rdi
	callq	_time
	movl	%eax, %esi
	movl	%esi, %edi
	callq	_srand
	movl	$0, -16(%rbp)
LBB1_1:                                 ## =>This Inner Loop Header: Depth=1
	movl	-16(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jge	LBB1_4
## %bb.2:                               ##   in Loop: Header=BB1_1 Depth=1
	callq	_rand
	cltd
	movl	$1000, %ecx             ## imm = 0x3E8
	idivl	%ecx
	movq	-8(%rbp), %rsi
	movslq	-16(%rbp), %rdi
	movl	%edx, (%rsi,%rdi,4)
## %bb.3:                               ##   in Loop: Header=BB1_1 Depth=1
	movl	-16(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -16(%rbp)
	jmp	LBB1_1
LBB1_4:
	addq	$16, %rsp
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
	movslq	-8(%rbp), %rsi
	shlq	$2, %rsi
	movq	%rsi, %rdi
	callq	_malloc
	movq	%rax, -16(%rbp)
	movl	-8(%rbp), %esi
	leaq	L_.str.2(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movq	-16(%rbp), %rdi
	movl	-8(%rbp), %esi
	movl	%eax, -28(%rbp)         ## 4-byte Spill
	callq	_complete_array
	movq	-16(%rbp), %rdi
	movl	-8(%rbp), %esi
	callq	_min_max
	movq	%rax, -24(%rbp)
	movq	-24(%rbp), %rax
	movl	(%rax), %esi
	movq	-24(%rbp), %rax
	movl	4(%rax), %edx
	movq	-24(%rbp), %rax
	movl	8(%rax), %ecx
	movq	-24(%rbp), %rax
	movl	12(%rax), %r8d
	leaq	L_.str.3(%rip), %rdi
	movb	$0, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -32(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"State of first if predictor : %d\nState of second if predictor : %d\n"

L_.str.1:                               ## @.str.1
	.asciz	"Stat of mispredictions of the predictor 1 : %f\nStat of mispredictions of the predictor 2 : %f\n"

L_.str.2:                               ## @.str.2
	.asciz	"len_array : %d\n"

L_.str.3:                               ## @.str.3
	.asciz	"Min : %d, at rank : %d\nMax : %d, at rank : %d\n"


.subsections_via_symbols
