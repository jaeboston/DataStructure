Objective: find squar root of an integer without using a library
Constraint: O(logN)

Divide the input by 2 using // operator then square it until matches the input.
Or if the number goes greater than the input, then the first number goes uner the input return the root value.
 
Pseudo code

1. Divide the input integer (`number`) by 2 using the // operator and save the result as `root`
2. Square `root` and save it as `sq`
3. If `sq` eqals to `number`, return `root`
4. Else, we are entering a loop until the condition is met
5. Create a variable `ceiling_flag` as boolean default to False, indicating `sq` has been greater than `number`.
6. In the loop, if `ceiling_flag` is False, we increase `root` by 1 until `ceiling_flag` is True
7. As soon as we have `sq` is less than `number` and `ceiling_flag` is True, return `root`

