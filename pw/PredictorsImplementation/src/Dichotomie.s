	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 14	sdk_version 10, 14
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3               ## -- Begin function dichotomie
LCPI0_0:
	.quad	4607182418800017408     ## double 1
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_dichotomie
	.p2align	4, 0x90
_dichotomie:                            ## @dichotomie
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movq	%rdi, -16(%rbp)
	movl	%esi, -20(%rbp)
	movl	%edx, -24(%rbp)
	movl	%ecx, -28(%rbp)
	movl	-20(%rbp), %ecx
	addl	-24(%rbp), %ecx
	movl	%ecx, %eax
	cltd
	movl	$2, %ecx
	idivl	%ecx
	movl	%eax, -32(%rbp)
	cmpl	$2, _global_history(%rip)
	jl	LBB0_7
## %bb.1:
	movl	-20(%rbp), %eax
	cmpl	-24(%rbp), %eax
	je	LBB0_3
## %bb.2:
	movl	-20(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jne	LBB0_7
LBB0_3:
	movl	-28(%rbp), %eax
	movq	-16(%rbp), %rcx
	movslq	-32(%rbp), %rdx
	cmpl	(%rcx,%rdx,4), %eax
	je	LBB0_7
## %bb.4:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	addsd	_cmpt+8(%rip), %xmm0
	movsd	%xmm0, _cmpt+8(%rip)
	cmpl	$3, _global_history(%rip)
	jge	LBB0_6
## %bb.5:
	movl	_global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history(%rip)
LBB0_6:
	movl	$-1, -4(%rbp)
	jmp	LBB0_38
LBB0_7:
	movl	-20(%rbp), %eax
	cmpl	-24(%rbp), %eax
	je	LBB0_9
## %bb.8:
	movl	-20(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jne	LBB0_11
LBB0_9:
	movl	-28(%rbp), %eax
	movq	-16(%rbp), %rcx
	movslq	-32(%rbp), %rdx
	cmpl	(%rcx,%rdx,4), %eax
	je	LBB0_11
## %bb.10:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movaps	%xmm0, %xmm1
	addsd	_cmpt(%rip), %xmm1
	movsd	%xmm1, _cmpt(%rip)
	addsd	_cmpt+8(%rip), %xmm0
	movsd	%xmm0, _cmpt+8(%rip)
	movl	_global_history(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history(%rip)
	movl	$-1, -4(%rbp)
	jmp	LBB0_38
LBB0_11:
	cmpl	$0, _global_history(%rip)
	jle	LBB0_13
## %bb.12:
	movl	_global_history(%rip), %eax
	subl	$1, %eax
	movl	%eax, _global_history(%rip)
LBB0_13:
	jmp	LBB0_14
LBB0_14:
	jmp	LBB0_15
LBB0_15:
	cmpl	$2, _global_history+4(%rip)
	jl	LBB0_20
## %bb.16:
	movl	-28(%rbp), %eax
	movq	-16(%rbp), %rcx
	movslq	-32(%rbp), %rdx
	cmpl	(%rcx,%rdx,4), %eax
	jne	LBB0_20
## %bb.17:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	addsd	_cmpt+24(%rip), %xmm0
	movsd	%xmm0, _cmpt+24(%rip)
	cmpl	$3, _global_history+4(%rip)
	jge	LBB0_19
## %bb.18:
	movl	_global_history+4(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history+4(%rip)
LBB0_19:
	movl	-32(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	LBB0_38
LBB0_20:
	movl	-28(%rbp), %eax
	movq	-16(%rbp), %rcx
	movslq	-32(%rbp), %rdx
	cmpl	(%rcx,%rdx,4), %eax
	jne	LBB0_22
## %bb.21:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movaps	%xmm0, %xmm1
	addsd	_cmpt+16(%rip), %xmm1
	movsd	%xmm1, _cmpt+16(%rip)
	addsd	_cmpt+24(%rip), %xmm0
	movsd	%xmm0, _cmpt+24(%rip)
	movl	_global_history+4(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history+4(%rip)
	movl	-32(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	LBB0_38
LBB0_22:
	cmpl	$0, _global_history+4(%rip)
	jle	LBB0_24
## %bb.23:
	movl	_global_history+4(%rip), %eax
	subl	$1, %eax
	movl	%eax, _global_history+4(%rip)
LBB0_24:
	jmp	LBB0_25
LBB0_25:
	jmp	LBB0_26
LBB0_26:
	cmpl	$2, _global_history+8(%rip)
	jl	LBB0_31
## %bb.27:
	movl	-28(%rbp), %eax
	movq	-16(%rbp), %rcx
	movslq	-32(%rbp), %rdx
	cmpl	(%rcx,%rdx,4), %eax
	jge	LBB0_31
## %bb.28:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	addsd	_cmpt+40(%rip), %xmm0
	movsd	%xmm0, _cmpt+40(%rip)
	cmpl	$3, _global_history+8(%rip)
	jge	LBB0_30
## %bb.29:
	movl	_global_history+8(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history+8(%rip)
LBB0_30:
	movq	-16(%rbp), %rdi
	movl	-20(%rbp), %esi
	movl	-32(%rbp), %eax
	subl	$1, %eax
	movl	-28(%rbp), %ecx
	movl	%eax, %edx
	callq	_dichotomie
	movl	%eax, -4(%rbp)
	jmp	LBB0_38
LBB0_31:
	movl	-28(%rbp), %eax
	movq	-16(%rbp), %rcx
	movslq	-32(%rbp), %rdx
	cmpl	(%rcx,%rdx,4), %eax
	jge	LBB0_33
## %bb.32:
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movaps	%xmm0, %xmm1
	addsd	_cmpt+32(%rip), %xmm1
	movsd	%xmm1, _cmpt+32(%rip)
	addsd	_cmpt+40(%rip), %xmm0
	movsd	%xmm0, _cmpt+40(%rip)
	movl	_global_history+8(%rip), %eax
	addl	$1, %eax
	movl	%eax, _global_history+8(%rip)
	movq	-16(%rbp), %rdi
	movl	-20(%rbp), %esi
	movl	-32(%rbp), %eax
	subl	$1, %eax
	movl	-28(%rbp), %ecx
	movl	%eax, %edx
	callq	_dichotomie
	movl	%eax, -4(%rbp)
	jmp	LBB0_38
LBB0_33:
	cmpl	$0, _global_history+8(%rip)
	jle	LBB0_35
## %bb.34:
	movl	_global_history+8(%rip), %eax
	subl	$1, %eax
	movl	%eax, _global_history+8(%rip)
LBB0_35:
	jmp	LBB0_36
LBB0_36:
	jmp	LBB0_37
LBB0_37:
	movq	-16(%rbp), %rdi
	movl	-32(%rbp), %eax
	addl	$1, %eax
	movl	-24(%rbp), %edx
	movl	-28(%rbp), %ecx
	movl	%eax, %esi
	callq	_dichotomie
	movl	%eax, -4(%rbp)
LBB0_38:
	movl	-4(%rbp), %eax
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
	subq	$32, %rsp
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
	movl	-16(%rbp), %eax
	movl	%eax, -20(%rbp)         ## 4-byte Spill
	callq	_rand
	cltd
	movl	$2, %ecx
	idivl	%ecx
	movl	-20(%rbp), %ecx         ## 4-byte Reload
	addl	%edx, %ecx
	movq	-8(%rbp), %rsi
	movslq	-16(%rbp), %rdi
	movl	%ecx, (%rsi,%rdi,4)
## %bb.3:                               ##   in Loop: Header=BB1_1 Depth=1
	movl	-16(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -16(%rbp)
	jmp	LBB1_1
LBB1_4:
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
	callq	_rand
	cltd
	idivl	-8(%rbp)
	movl	%edx, -12(%rbp)
	movslq	-8(%rbp), %rsi
	shlq	$2, %rsi
	movq	%rsi, %rdi
	callq	_malloc
	movq	%rax, -24(%rbp)
	movq	-24(%rbp), %rdi
	movl	-8(%rbp), %esi
	callq	_complete_array
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	xorl	%esi, %esi
	movq	-24(%rbp), %rdi
	movl	-8(%rbp), %edx
	movl	-12(%rbp), %ecx
	movl	%eax, -32(%rbp)         ## 4-byte Spill
	callq	_dichotomie
	movl	%eax, -28(%rbp)
	movl	-28(%rbp), %esi
	movl	-12(%rbp), %edx
	movq	-24(%rbp), %rdi
	movslq	-28(%rbp), %r8
	movl	(%rdi,%r8,4), %ecx
	leaq	L_.str.1(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	_global_history(%rip), %esi
	movl	_global_history+4(%rip), %edx
	movl	_global_history+8(%rip), %ecx
	leaq	L_.str.2(%rip), %rdi
	movl	%eax, -36(%rbp)         ## 4-byte Spill
	movb	$0, %al
	callq	_printf
	movsd	_cmpt(%rip), %xmm0      ## xmm0 = mem[0],zero
	divsd	_cmpt+8(%rip), %xmm0
	movsd	_cmpt+16(%rip), %xmm1   ## xmm1 = mem[0],zero
	divsd	_cmpt+24(%rip), %xmm1
	movsd	_cmpt+32(%rip), %xmm2   ## xmm2 = mem[0],zero
	divsd	_cmpt+40(%rip), %xmm2
	leaq	L_.str.3(%rip), %rdi
	movl	%eax, -40(%rbp)         ## 4-byte Spill
	movb	$3, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -44(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_global_history         ## @global_history
.zerofill __DATA,__common,_global_history,12,2
	.globl	_cmpt                   ## @cmpt
.zerofill __DATA,__common,_cmpt,48,4
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"Array completed\n"

L_.str.1:                               ## @.str.1
	.asciz	"Found or not at pos : %d\n%d == %d\n"

L_.str.2:                               ## @.str.2
	.asciz	"State of first if predictor : %d\nState of second if predictor : %d\nState of third if predictor : %d\n"

L_.str.3:                               ## @.str.3
	.asciz	"Stat of mispredictions of the predictor 1 : %f\nStat of mispredictions of the predictor 2 : %f\nStat of mispredictions of the predictor 3 : %f\n"


.subsections_via_symbols
