### Visionect Python tutoring, group 1

# Results --- Jon `75%`



`(7/10%)`
#### Import (manually typing is OK) [recent results](https://en.wikipedia.org/wiki/Cavaliers%E2%80%93Warriors_rivalry#Results_(2014%E2%80%9315_season%E2%80%93present)) into suitable data structure. Use games from 1-26.
These results will be used as a learning set for our predictions.

**Correct results** `50/50%`

**Style** `0/30%`

Overcomplicated by using external (.xlsx) data source. When using program one must manually type the
correct path for the file and install libraries (pandas, xlrd).
Using arrays would be much simpler solution.

**Code readability** `20/20%`


**Surprise me** `0/10%` (bonus)


----
`(14/15%)`

#### Let's make some statistics first:

 -Print out, how many times Golden State and Cleveland won overall.

 -Print out, how many times each team won at home and away.

 -Average points scored by each team.

 -Trend, which team is better lately? (feel free to find a way how to do it)

 no output

**Correct results** `50/50%`

**Style** `30/30%`

**Code readability** `18/20%`

[Functions and variables should be lowercase, with words separated by underscores as necessary to improve readability.] (https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)

**Surprise me** `0/10%` (bonus)

----
`(30/35%)`

#### Create an algorithm that will print out the prediction for the next game. Use games 27 and 28 to test the predictions. The result should be logical (e.g. 32:18, or 174:198 don't make sense.)

 -There will be min 2 and max 3 more games until the deadline. Test your predictions against these matches too by including games 27 and 28 into learning set. Are predictions any better?

**Correct results** `50/50%`

**Style** `20/30%`

Though it does well what is intended, there is missing second part of exercise. This part is for optimisation purposes so it
is not that important. What you had to do, is just add games 27-29 to the Zvezek1.xlsx and test if results are better with bigger set. I suppose you misunderstood instructions. **(Up for discussion)**

**Code readability** `5/20%`

Variables are not informative, I don't understand while loop and #3 - 2nd indent. **(Up for discussion)**


**Surprise me** `10/10%` (bonus)
Well done algorithm for prediction.

----
`(0/10%)`
#### Run your algorithm 10 000 times and print out, what is average prediction.

**Correct results** `0/50%`

**Style** `0/30%`

**Code readability** `0/20%`

**Surprise me** `0/10%` (bonus)

----
`(24/30%)`
#### Create a betting system where user will input their prediction only once.

*{Use games 29,30,(31) as actual results}*

 -Print out the user's prediction

 -Print out the prediction your program calculated.

This is printed before user inputs its prediction. User could just copy it and earn 510€ everytime.
But it is not explicitly mentioned so its technically OK.

 Check the actual result and test your program and user's prediction:

 -If winner is correctly predicted, award is 10€.

 -If winner is correctly predicted and points of one team are missed by less than 8%, award is additional 15€.
 **or**
 -If winner is correctly predicted and points of both teams are missed by less than 8%, award is additional 40€

 -If result of one team is totally correct, award is additional 100€.
 **or**
 -If result of the game is totally correct, award is additional 500€.

**Correct results** `50/50%`

**Style** `30/30%`

**Code readability** `5/20%`

Very hard to understand variable names

**Surprise me** `0/10%` (bonus)

------

#### Criteria
 `0% - 49%` : Didn't pass.

 `50% - 64%`: **Talk about the test solution, if there is insufficient knowledge about solved test, didn't pass.**

 `65% - 100%`: Passed

 `101% - 110%`: Passed and you get a 6pack of some good beer. Choose dark or light :)
