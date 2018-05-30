'''
Not going to code it out, too long.

Basically each third of the array is a stack. Each third delimits the rest of the array in both directions 
Use pointers to manage each stack
Each push and pop would invovle a check of the pointers pointer location making sure it doesn't try to go beyond its alloted space.
peek() contents where pointer is currently is
isEmpty() would checks data in first slot in each array third, if None then array returns True else return False
push() would check if next slot is avaliable to that particular stack first not allowing push() if it is. If it's not then it moves pointer up one and places data in that slot.
pop() check if pointer spot before it is avaliable and if it is move pointer back otherwise keep pointer in the same spot. Then return content of slot. Can include special condition to differentiate between None being stored in first slot on purpose if necessary.
