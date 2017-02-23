# Solving DP Problems

## Finding if DP is Applicable

The strongest check for DP is to look for optimal substructure and overlapping subproblems. 
	
DP is used where a complex problem can be divided in subproblems of the same type and theses subproblems overlap in some way(either fully or partially).

Most of times, we may also be trying to optimize something, maximize something, or finding the total number of ways of doing something and the optimal solution for larger parameter depends on optimal solutions of same problems with smaller parameter. 

## Solving DP problems

There's no one fool-proof plan that we can use to solve all DP questions because not every problem is the same, but one should be able to solve most DP problems following below steps:

1. __See if DP is applicable.__ If problem can be defined in terms of smaller subproblems and the subproblems overlap then chances are that DP can be used.

2. __Define recursion.__ Having subproblems of similar kind means there is recursion.

	a) __Define problem in terms of subproblems,__ define it in a top down manner, do not worry about time complexity at this point.
	
	b) __Solve base case(leave rest to recursion).__ The subproblems are solved by recursion what is left is the base case.
	
	c) __Add a terminating condition.__ This step is relatively trivial. We need to stop somewhere. That will be the terminating conditions.
	
	After this step we have a working solution using recursion.
	
3. __Try memoization (optional).__ If a subproblem is solved multiple times, then try to cache its solution and use the cached value when same subproblem is encountered again.

4. __Try solving Bottom-up.__ This is the step where we try to eliminate recursion and redefine our solution in forward direction starting from the most basic case. In the process we store only those results that will be required later.
