---
---


---
### Instruction pipelining 
ده احد انواع ال pipelining الي قولنا عليها في المحاضرة الاولي (arithmetic - instruction  ) ، و الهدف منها اني  اقسم ال incoming instructions  الي series of sequential steps   و انفذها في single processor عشان استغل كل جزء من موارد الجهاز . 


### pipeline Stages 
1. instruction fetch 
2. instruction decode and register fetch 
3. execute 
1. memory access (just load and store ) 
2. register write back : writing the result into the register file 
	\- the result may be come from memory if (load instruction ) or ALU if (ALU instruction) 

و في النهاية خلي بالك انو مش شرط ال 5 stages دول يتنفذوا يعني ممكن العملية مش محتاجه اعمل access to the memory مثلا او مش محتاجه يتعملها store in the memory  . 
### Cisc vs. Risc 
cisc for complex instructions , but risc for reduced instruction set (simple instructions) 
#### what is the properties of risc ? 
each instruction has 32 bits per register (4 layer because each layer have 8 bits (4 * 8 = 32 ))

#### what is the operations that affect on memory  ?
load (move data from mem to reg  ) and store (move data from reg to mem )  

#### what is the classes of instructions in Risc (3 classes ) ? 
##### ALU instruction 
add , sub , multiply , divide , logical operations (or , and  ) 
operates on two registers and store result in third register 
so , have there subcategories of Alu instruction : 
1. memory reference (base register + offset) 
2. register - register instructions (take the two values from registers )
3. register - immediate instruction (take the values from one register and constant value )
##### Load and store instruction (that affect memory )
steps : 
1. get memory address by add **base-register** and **offset**  (base register + offset = effective address )
2. second register 
	1. in loading : second register as the destination 
	2. in store : second register as the source 
	

##### branch and jumps instruction 
make the conditional transfer of control  , control the flow of execution of the program . 
the branch instruction have two phases : 
1. decide if the branch should take effect 
2. if first phase satisfied , second phase decide the branch destination 


#### Risc format ? 
**register (R)**
	\- specify three registers 
 **immediate (I)**
	 \- specify two registers (16 immediate value )  
 **Jump (J)**
	 follow the opcode with 26 bit jump target 

---
**Notes**:
\- pipelining called also instruction level parallelism (PLI)
\- memory stream and data stream are saved in separated memory location 
لتجنب اي عملية لغبطة في الداتا او الانستراكشن 
\- note that  in instruction format each instruction start with 6 opcode 
\- fully pipelined : معناها ان في كل مره او كل ستيب بيتم عمل فيتش ل انستراكشن جديده 
\- balanced pipelined : mean the CPU can receive more instruction (all busy )  
