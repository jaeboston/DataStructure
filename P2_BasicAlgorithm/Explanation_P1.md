Objective: find squar root of an integer without using a library
Constraint: O(logN)

Description
Divide the input by 2 using // operator then square it until matches the input.
If the squared number is greater than the input, then the first number goes uner the input return the root value.

Time complexity: O(logN)
Space complexcity: O(1)


Pseudo code

1. Divide the input integer (`number`) by 2 using the // operator and save the result as `root`
2. Square `root` and save it as `sq`
3. If `sq` eqals to `number`, return `root`
4. Else, we are entering a loop increasing `root` value at every iteration until the condition (`sq` eqals to `number`) is satisfied.

5. We create a variable `ceiling_flag` as boolean and set its default to False, indicating `sq` value has not seen a value greater than `number` to handle the edge cases when the first `sq` value equals to 1.

6. In the loop, if `ceiling_flag` is False, we increase `root` by 1 until `ceiling_flag` is set to True

