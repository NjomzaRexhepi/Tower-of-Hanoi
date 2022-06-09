# Tower of Hanoi

The Tower of Hanoi (also called the Tower of Brahma or Lucas' Tower) was invented by the French mathematician Édouard Lucas in 1883.

There is a story about an Indian temple which contains a large room with three old posts and 64 golden disks. Brahmin priests, acting out the command of an ancient prophecy, have been moving these disks for countless years. According to the legend, when the last move of the puzzle will be completed, the world will end!


The Tower of Hanoi is a mathematical Puzzle that consists of three towers(pegs) and multiple disks. Initially, all the disks are placed on one rod. And these disks are arranged on one over the other in ascending order of size.


## Steps to be followed as below

- Step 1 − Move n-1 disks from source to aux
- Step 2 − Move nth disk from source to dest
- Step 3 − Move n-1 disks from aux to dest


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

So, total time taken T (n) = T (n-1)+ 1 + T(n-1)


````

### Our Equation will be

````

T(n) = 2T(n-1) + 1

T(n) = 2T(n-1) + 1 ———- (1)

after putting n = n-1 in eq 1, Equation will become

T(n-1) = 2T(n-2) + 1 ———— (2)

after putting n = n-2 in eq 1, Equation will become

T(n-2) = 2T(n-3) + 1 ———— (3)

Put the value of T(n-2) in the equation–2 with help of equation-3

T(n-1) = 2T(2T(n-3) + 1) + 1

Put the value of T(n-1) in equation-1 with help of equation-4

T(n) = 2(2(2T(n-3)+1)+1)+1

T(n) = 2^3T(n-3) + 2^2 + 2^1 + 1

After Generalization

T(n) = 2^k T(n-k) + 2^(k-1) + 2^(k-2) + ………. + 2^2 + 2^1 + 2^0

From our base condition T(1) =1

n – k = 1
k = n-1

Now put k = n-1 in above equation

T(n) = 2^(n-1) T(n-(n-1)) + 2^(k-1) + 2^(k-2) + ………. + 2^2 + 2^1 + 2^0

T(n) = 2^(k)(1) + 2^(k-1) + 2^(k-2) + ………. + 2^2 + 2^1 + 2^0

It is in a GP with Common ratio r = 2

First term, a=(2^0).1

Sum of G.P. = Sn = a(1-r^n) / (1-r)

T(n) = 1.(1-2^(i+1))/(1-2)

T(n) = 2^(i+1) – 1

From the above equation

T(n) = 2^ (n-1+1) – 1

T(n) = 2^n – 1 (this is the equation which will give the number of disk movement is required )

````
 
 
 ### Time Complexity
 
 ````
 It is a GP series, and the sum is 2^n – 1

T(n)= O( 2^n – 1) , or We can say time complexity is O(2^n) which is exponential.
````
### Space Complexity
````
Space Complexity:
Space for parameter for each call is independent of n i.e., constant. Let it be k .
When we do the 2nd recursive call 1st recursive call is over . So, we can reuse the space of
1st call for 2nd call . Hence ,

T(n) = T(n-1) + k
T(0) = k
T(1) = 2k
T(2) = 3k
T(3) = 4k
So the space complexity is O(n).


````
[Diellza Berisha](https://github.com/Dielllza1)
[Ereblina Berisha](https://github.com/erblinaberisha)
[Nida Islami](https://github.com/nidaislami)
[Njomza Rexhepi](https://github.com/NjomzaRexhepi)

