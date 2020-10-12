#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

The function is dependent on the input of n. It performs a single operation using the values of a and n.
```python
a) a = 0 # 0(n)
    while (a < n * n * n): # this section is O(1)
      a = a + n * n
```

The runtime for this function is O(2^n). It is also referred to as a quadratic function, because it is a loop nested inside of another loop.
The first loop sets up the conditions for the second loop. The second loop will run a complete execution for every iteration i in range(n). j will continue to grow with each iteration of the inner loop until the value of j is greater than the value of n. At that point, the first loop will iterate to the next value and the cycle repeats.
```
b) sum = 0
    for i in range(n): # this loop is O(n)
      j = 1
      while j < n: # this loop is O(n)
        j *= 2 # this is O(1)
        sum += 1 # this is O(1)
```

The runtime of this function is O(n). This recursive function will be called from within the function as many times as the value we pass into the function as an argument.
```
c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

It would be a good idea to start by dividing the total number of floors by 2.
See if the egg will break if it is dropped from the middle floor.
```
firstFloor = 0
lastFloor = len(n)
middleFloor = (firstFloor + lastFloor) // 2
```

If the egg is dropped from the middle floor and breaks, we need to keep going down in floors until the egg won't break.
```
lastFloor = middleFloor - 1
middleFloor = (firstFloor + lastFloor) // 2
```

If the egg finally doesn't break, we could test if the egg can be dropped from one more floor to find the last floor where it can be dropped without breaking.
```
start = middleFloor + 1
end = len(x)
middleFloor = (start + end) // 2
```

This function run in O(log n).

