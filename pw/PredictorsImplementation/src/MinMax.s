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
	subq	$32, %rsp
	movl	$16, %eax
	movl	%eax, %ecx
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movq	%rcx, %rdi
	callq	_malloc
	movq	%rax, -24(%rbp)
	movq	-8(%rbp), %rax
	movl	(%rax), %esi
	movq	-24(%rbp), %rax
	movl	%esi, (%rax)
	movq	-24(%rbp), %rax
	movl	$0, 4(%rax)
	movq	-8(%rbp), %rax
	movl	(%rax), %esi
	movq	-24(%rbp), %rax
	movl	%esi, 8(%rax)
	movq	-24(%rbp), %rax
	movl	$0, 12(%rax)
	movl	$1, -28(%rbp)
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	movl	-28(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jge	LBB0_26
## %bb.2:                               ##   in Loop: Header=BB0_1 Depth=1
	cmpl	$2, _global_history(%rip)
	jl	LBB0_7
## %bb.3:                               ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-28(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-24(%rbp), %rax
	cmpl	(%rax), %edx
	jge	LBB0_7
## %bb.4:                               ##   in Loop: Header=BB0_1 Depth=1
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	addsd	_cmpt+8(%rip), %xmm0
	movsd	%xmm0, _cmpt+8(%rip)
	cmpl	$3, _global_history(%rip)
	jge	LBB0_6
## %bb.5:                               ##   in Loop: Header=BB0_1 Depth=1
	movl	_global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history(%rip)
LBB0_6:                                 ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-28(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-24(%rbp), %rax
	movl	%edx, (%rax)
	movl	-28(%rbp), %edx
	movq	-24(%rbp), %rax
	movl	%edx, 4(%rax)
	jmp	LBB0_13
LBB0_7:                                 ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-28(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-24(%rbp), %rax
	cmpl	(%rax), %edx
	jge	LBB0_9
## %bb.8:                               ##   in Loop: Header=BB0_1 Depth=1
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movaps	%xmm0, %xmm1
	addsd	_cmpt(%rip), %xmm1
	movsd	%xmm1, _cmpt(%rip)
	addsd	_cmpt+8(%rip), %xmm0
	movsd	%xmm0, _cmpt+8(%rip)
	movl	_global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history(%rip)
	movq	-8(%rbp), %rcx
	movslq	-28(%rbp), %rdx
	movl	(%rcx,%rdx,4), %eax
	movq	-24(%rbp), %rcx
	movl	%eax, (%rcx)
	movl	-28(%rbp), %eax
	movq	-24(%rbp), %rcx
	movl	%eax, 4(%rcx)
	jmp	LBB0_12
LBB0_9:                                 ##   in Loop: Header=BB0_1 Depth=1
	cmpl	$0, _global_history(%rip)
	jle	LBB0_11
## %bb.10:                              ##   in Loop: Header=BB0_1 Depth=1
	movl	_global_history(%rip), %eax
	subl	$1, %eax
	movl	%eax, _global_history(%rip)
LBB0_11:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_12
LBB0_12:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_13
LBB0_13:                                ##   in Loop: Header=BB0_1 Depth=1
	cmpl	$2, _global_history+4(%rip)
	jl	LBB0_18
## %bb.14:                              ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-28(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-24(%rbp), %rax
	cmpl	8(%rax), %edx
	jle	LBB0_18
## %bb.15:                              ##   in Loop: Header=BB0_1 Depth=1
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	addsd	_cmpt+24(%rip), %xmm0
	movsd	%xmm0, _cmpt+24(%rip)
	cmpl	$3, _global_history+4(%rip)
	jge	LBB0_17
## %bb.16:                              ##   in Loop: Header=BB0_1 Depth=1
	movl	_global_history+4(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history+4(%rip)
LBB0_17:                                ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-28(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-24(%rbp), %rax
	movl	%edx, 8(%rax)
	movl	-28(%rbp), %edx
	movq	-24(%rbp), %rax
	movl	%edx, 12(%rax)
	jmp	LBB0_24
LBB0_18:                                ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-28(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-24(%rbp), %rax
	cmpl	8(%rax), %edx
	jle	LBB0_20
## %bb.19:                              ##   in Loop: Header=BB0_1 Depth=1
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movaps	%xmm0, %xmm1
	addsd	_cmpt+16(%rip), %xmm1
	movsd	%xmm1, _cmpt+16(%rip)
	addsd	_cmpt+24(%rip), %xmm0
	movsd	%xmm0, _cmpt+24(%rip)
	movl	_global_history+4(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history+4(%rip)
	movq	-8(%rbp), %rcx
	movslq	-28(%rbp), %rdx
	movl	(%rcx,%rdx,4), %eax
	movq	-24(%rbp), %rcx
	movl	%eax, 8(%rcx)
	movl	-28(%rbp), %eax
	movq	-24(%rbp), %rcx
	movl	%eax, 12(%rcx)
	jmp	LBB0_23
LBB0_20:                                ##   in Loop: Header=BB0_1 Depth=1
	cmpl	$0, _global_history+4(%rip)
	jle	LBB0_22
## %bb.21:                              ##   in Loop: Header=BB0_1 Depth=1
	movl	_global_history+4(%rip), %eax
	subl	$1, %eax
	movl	%eax, _global_history+4(%rip)
LBB0_22:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_23
LBB0_23:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_24
LBB0_24:                                ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_25
LBB0_25:                                ##   in Loop: Header=BB0_1 Depth=1
	movl	-28(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -28(%rbp)
	jmp	LBB0_1
LBB0_26:
	movq	-24(%rbp), %rax
	addq	$32, %rsp
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
	subq	$48, %rsp
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
	leaq	L_.str(%rip), %rdi
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
	leaq	L_.str.1(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	_global_history(%rip), %esi
	movl	_global_history+4(%rip), %edx
	leaq	L_.str.2(%rip), %rdi
	movl	%eax, -32(%rbp)         ## 4-byte Spill
	movb	$0, %al
	callq	_printf
	movsd	_cmpt(%rip), %xmm0      ## xmm0 = mem[0],zero
	divsd	_cmpt+8(%rip), %xmm0
	movsd	_cmpt+16(%rip), %xmm1   ## xmm1 = mem[0],zero
	divsd	_cmpt+24(%rip), %xmm1
	leaq	L_.str.3(%rip), %rdi
	movl	%eax, -36(%rbp)         ## 4-byte Spill
	movb	$2, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -40(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	addq	$48, %rsp
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
	.asciz	"len_array : %d\n"

L_.str.1:                               ## @.str.1
	.asciz	"Min : %d, at rank : %d\nMax : %d, at rank : %d\n"

L_.str.2:                               ## @.str.2
	.asciz	"State of first if predictor : %d\nState of second if predictor : %d\n"

L_.str.3:                               ## @.str.3
	.asciz	"Stat of mispredictions of the predictor 1 : %f\nStat of mispredictions of the predictor 2 : %f\n"


.subsections_via_symbols
