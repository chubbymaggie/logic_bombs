# A Dataset of Logic Bombs
## Project Overview
This project includes a set of small programs with logic bombs.  The logic bomb can be triggered when certain conditions are met. 
We release the dataset for benchmarking purposes.  Any dynamic testing tools (especially symbolic execution) can employ the dataset to benchmark their capabilities. 
The dataset is originally realeased with our paper:

[1] "Concolic Execution on Small-Size Binary Codes: Challenges and Empirical Study," Hui Xu, Yangfan Zhou, Yu Kang, and Michael R. Lyu, in the 47th IEEE/IFIP International Conference on Dependable Systems and Networks (DSN 2017)
 

To find out more details, please visit our [wiki](https://github.com/hxuhack/logic_bombs/wiki).

## Details of the bombs
Below we list these programs and the conditions to trigger each bomb. 

| Type | Case  | Trigger Condition |
|---|---|---|
| Symbolic Variable Declaration | stdin_svd.c | user inputs 7 |
|  				| cpu_svd.c | the program runs on an Intel CPU |
|       			| time_svd.c | current time is after Jan 1st, 2050 |
|       			| pid_svd.c | the process id is 4096 |
|       			| vm_svd.c | the program runs on an virtual machine |
|       			| web_svd.c | if a remote website contains the string "trigger the bomb" |
|       			| syscall_ls_svd.c | the number of files under a current directory is 7 |
| Contextual Symbolic Value  	| file_csv.c | if argv[1] points to a file |
|       			| pid_csv.c | if argv[1][0]-48 equals the process id%78 |
| 			  	| ping_csv.c | if argv[1] points to a live IP |
| 			  	| syscall_csv.c | if argv[1] is a valid Linux command |
| Covert Propagation  		| file_cp.c | data propagate via a file (expected argv[1][0]: '7') | 
| 		  		| stack_cp.c | data propagation via direct push/pop (expected argv[1][0]: '7') | 
| 		  		| echo_cp.c | data propagation via echo (expected argv[1][0]: '7') | 
| 		  		| df2cf_cp.c | data propagation via control flow (expected argv[1][0]: '7') | 
| 		  		| echofile_cp.c | data propagation via echo and file (expected argv[1][0]: '7') | 
| 		  		| socket_cp.c | data propagation via socket (expected argv[1][0]: '7') | 
| 		  		| toy_eh_cp.cpp | data propagation via exception handling (expected argv[1][0]: '7') | 
| 		  		| div0_eh_cp.cpp | raise an exceptions when divided by 0 (expected argv[1][0]: '7') | 
| 		  		| file_eh_cp.cpp | expected argv[1]: an existed file | 
| Symbolic Memory  		| stackarray_sm_l1.c | if stdin points to an array element (expected argv[1][0]: '4') |
| 		  		| malloc_sm_l1.c | allocate memory with malloc (expected argv[1][0]: '7')|
| 		  		| realloc_sm_l1.c | allocate memory with realloc (expected argv[1][0]: '7')|
| 		  		| vector_sm_l1.cpp | with std::vector (expected argv[1][0]: '7')|
| 		  		| list_sm_l1.cpp | with std::list (expected argv[1][0]: '7')|
| 		  		| stackarray_sm_l2.c | two arrays (expected argv[1][0]: '2') |
| 		  		| stackoutofbound_sm_l2.c | if array index equal array size (expected argv[1][0]: '7')|
| 		  		| heapoutofbound_sm_l2.c | if array index equals array size (expected argv[1][0]: ':')|
| Parallel Program 		| 2thread_pp_l1.c | two-thread program (expected argv[1][0]: '7')  |
| 		 		| forkpipe_pp_l1.c | two-process program with pipe (expected argv[1][0]: '7')  |
| 		 		| forkshm_pp_l1.c | two-process program with shared memory (expected argv[1][0]: '7')  |
| 		 		| 2thread_pp_l2.c | two-thread program with random result (high chance argv[1][0]: '9') |
| 		 		| mthread_pp_l2.c | multi-thread program with random result (high chance argv[1][0]: '9') |
| Floating-point Number  	| float1_fp_l1.c | expected argv[1][0]: '7' |
| 	       		  	| float2_fp_l1.c | expected argv[1][0]: '7' |
| 	       		  	| float3_fp_l2.c | expected argv[1]: "0.1"  |
| 	       		  	| float4_fp_l2.c | expected argv[1]: "-0.1"  |
| 	       		  	| float5_fp_l2.c | expected argv[1]: "0.41421"  |
| Symbolic Jump 		| jmp_sj_l1.c | jump to an address related to stdin (expected argv[1][0]: 'U')|
| 		 		| arrayjmp_sj_l2.c | a more complex case with an array (expected argv[1][0]: '7')|
| 		 		| vectorjmp_sj_l2.c | a more complex case with an vector (expected argv[1][0]: '7')|
| Data Overflow 		| plus_do.c | a + 2147483640 < 0 && a > 0 (expected argv[1][0]: '8')  |
| 			  	| multiply_do.c | 254748364 * a < 0 && a > 0 (expected argv[1][0]: '9')|
| Buffer Overflow 		| stack_bo_l1.c | expected stdin: \`python -c 'print "AAAAAAAA\x01\x00\x00\x00"'\`|
| 		 		| stack_bo_l2.c | expected stdin: TO FIGURE OUT |
| 		 		| heap_bo_l1.c | expected stdin: TO FIGURE OUT|
| External Function Call  	| printint_ef_l1.c | expected argv[1][0]: '7' |
| 			  	| printfloat_ef_l1.c | expected argv[1][0]: '7' |
| 			  	| atoi_ef_l2.c | expected argv[1][0]: '7' |
| 			  	| atof_ef_l2.c | expected argv[1][0]: '7' |
|  				| rand_ef_l2.c | rand()%100 == 7, random result |
| 			  	| pow_ef_l2.c | pow(i, 2) == 49, argv[1][0] = '7' |
| 			  	| sin_ef_l2.c | sin(i * PI / 30) > 0.5 argv[1][0] = '6' |
| 			  	| ln_ef_l2.c | 1.94 < log(i) && log(i) < 1.95, argv[1][0] = '7' |
| Crypto Function 		| sha_cf.c | if sha1(i) equals to a predefined value, expected argv[1][0] = '7' |
| 		 		| aes_cf.c | if aes(i, plaintext) equals to a ciphertext |
| Loop 				| collaz_lo_l1.c  | if it loops 25 times (example argv[1][0]: '7') |
|  				| 5n+1_lo_l1.c  | if it loops 25 times (example argv[1][0]: '7') |
|  				| 7n+1_lo_l1.c  | if it loops 50 times (example argv[1][0]: '7') |
|  				| collaz_lo_l2.c  | if it loops 986 times (example argv[1][0]: '7') |
|  				| paraloop_lo_l2.c  | a loop terminated by another thread (expected argv[1][0]: '7') |
