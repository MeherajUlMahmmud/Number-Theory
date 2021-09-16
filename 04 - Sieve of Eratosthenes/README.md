# Sieve of Eratosthenes

The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so.

## Explanation with Example: 
Let us take an example when n = 50. So we need to print all prime numbers smaller than or equal to 50.

We create a list of all numbers from 2 to 50.
```
2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50
```

According to the algorithm we will mark all the numbers which are divisible by 2 and are inside the range of 2 to 50 (In this case, for marking, we are replacing the numbers with ZERO).
And our list will be:
```
2, 3, 0, 5, 0, 7, 0, 9, 0,
11, 0, 13, 0, 15, 0, 17, 0, 19, 0,
21, 0, 23, 0, 25, 0, 27, 0, 29, 0,
31, 0, 33, 0, 35, 0, 37, 0, 39, 0,
41, 0, 43, 0, 45, 0, 47, 0, 49, 0
```

And then we will mark all the numbers which are divisible by 3 and are inside the range of 2 to 50.
And our list will be:
```
2, 3, 0, 5, 0, 7, 0, 0, 0,
11, 0, 13, 0, 0, 0, 17, 0, 19, 0,
0, 0, 23, 0, 25, 0, 0, 0, 29, 0,
31, 0, 0, 0, 35, 0, 37, 0, 0, 0,
41, 0, 43, 0, 0, 0, 47, 0, 49, 0
```


We will continue this process, and final list will be:
```
2, 3, 0, 5, 0, 7, 0, 0, 0,
11, 0, 13, 0, 0, 0, 17, 0, 19, 0,
0, 0, 23, 0, 0, 0, 0, 0, 29, 0,
31, 0, 0, 0, 0, 0, 37, 0, 0, 0,
41, 0, 43, 0, 0, 0, 47, 0, 0, 0, 0, 0
```

So the prime numbers are the unmarked ones: ```2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47```