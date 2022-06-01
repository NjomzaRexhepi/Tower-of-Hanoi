# Tower of Hanoi

The Tower of Hanoi (also called the Tower of Brahma or Lucas' Tower) was invented by the French mathematician Édouard Lucas in 1883.

There is a story about an Indian temple which contains a large room with three old posts and 64 golden disks. Brahmin priests, acting out the command of an ancient prophecy, have been moving these disks for countless years. According to the legend, when the last move of the puzzle will be completed, the world will end!


The Tower of Hanoi is a mathematical Puzzle that consists of three towers(pegs) and multiple disks. Initially, all the disks are placed on one rod. And these disks are arranged on one over the other in ascending order of size.


## Steps to be followed as below

Step 1 − Move n-1 disks from source to aux

Step 2 − Move nth disk from source to dest

Step 3 − Move n-1 disks from aux to dest


## Recursive algorithm to solve Tower Of Hanoi Puzzle

```c++
START
 Procedure TOH(disk, source, dest, aux)
 IF disk == 1, THEN
       move disk from source to dest             
    ELSE
       TOH(disk - 1, source, aux, dest)     // Step 1
       moveDisk(source to dest)          // Step 2
       TOH(disk - 1, aux, dest, source)     // Step 3
    END IF
 END Procedure
 STOP
```


## Complexity Analysis of Tower Of Hanoi

- Moving n-1 disks from source to aux means the first peg to the second peg (in our case). This can be done in T (n-1) steps.

- Moving the nth disk from source to dest means a larger disk from the first peg to the third peg will require 1 step.

- Moving n-1 disks from aux to dest means the second peg to the third peg (in our example) will require again T (n-1) step.


````
```
So, total time taken T (n) = T (n-1)+ 1 + T(n-1)

```
````
 
