# PythonBowlingKata
Standard bowling kata for python

# Purpose
I use the bowling kata to learning new languages. It helps me to fix one side of the problem (the "business" side) so I can focus on learning the new ("language") side.  

The bowling kata is helpful because it provides clear opportunties to exerices the RED/GREEN/REFACTOR cycle and exercises elements of the new language (class, method, loops, arrays (or lists)).  

This repository has a series of commits that reflect steps in the kata.  

## Kata
Kata is a term often found in Japanese martial arts. The English word "form" is analgous. The idea is a set of steps you practice to demonstrate a grasp of fundamentals, remind your mind of the flow of a thing, and to separate you from the world outside of practice and prepare for a new practice sesssion.  

Martin Fowler, among many others, have promoted the idea of "coding kata" for the same reason.  

The goal would be to do this kata daily (or for up to 20 minutes a day). Some people who are learning this kata will work on part for 20 minutes, then pick up the next day at that point and continue. Others will just bang through it, it getting a bit farther each day. I have found the latter technique more useful. You may find something different.

## the Python
I'm a self (mis)taught developer who has worked in a variety of languages going back to dBase III. Much of my coding time has been spent in C#. To the degree the code here isn't pythonic, that's just my ignorance (which I am hoping to decrease).

## Prereqs
VS Code with Python Extension

## using this repo
I created this repo to share the steps. The best way to use it is to view the change sets in your browser and then replicate the enter the code (or steps) to get from current state to what you see in the change set.

# First Test
## The simple case, I roll 20  gutter balls
### getting started and setting up testing
Open a new folder named bowlingkata (or something similar)  

Create a new file named game_test.py -- the _test.py is important. This is what the Python unittest package uses to detect tests. You can configure this when you enable testing.   



### write the test (red)
The first step in the TDD cycly is to write a failing test. In this case I want to verify the score after I roll 20 gutter balls (0 pins).

I start my test method with the string test_. This is how unittest identifies which methods are tests to be run inside a class that inheriets from unittest.TestCase (and who's name matches the test framework configuration)

As I write the test I need to create an instance of my Game() class. I use the variable target, as a personal convention, so I can keep my eye (and mind) on the thing I'm testing. (Your mileage may vary)  

When I create a reference to Game(), VSCode indicates a problem with a red squiggle. This is a FAILING test. I can now write the SIMPLEST CODE TO MAKE THIS TEST (and all others) PASS. So I make a new class file (game.py) and a class (Game) and import.

This resolves my red squiggle. 

Next I will create a for loop to roll zero pins twenty times. I again meet the red squiggle of test failure so I write the SIMPLEST CODE to make it pass. A method in Game() named roll that takes 1 parameter.

Finally, I assert that Game().score() is 0 and I resolve my red squiggle by ensuring Game().score() returns None.

I have a complete test (with my red / green cycle for resolving compiler errors)

I run all my unit tests (Commmand-Shift-P: Python: Run All Unit Tests) and get a box telling me to enable a Unit Test Framework. When you Enable a testing framework in VS Code (Python) you'll get prompted to configure the testing framework. Select unittest or the framework, root for the directory and *_test.py for the format of the file. (Note: you can configure VSCode for defaults for test framework and the rest. I leave it, as I'm still learning VSCode and this is part of the kata for me.)

I can see the failure by viewing the Output window (with Python Test Log selected in the drop down).  

AssertionError: 0 != None

### make it pass (green)
For me, writing small tests is often a challenge. Writing the smallest code that will make a failing test pass is more so. Its important. So I'll write the SMALLEST code that will make this test pass.

return 0

And in my output window I see the confirmation the test passed. 

test_when_all_rolls_are_0_score_is_0 (game_test.Game_Tests) ... ok

The VSCode status bar also shows me I have 1 passing test.

### refactor (including the test)
Everything is pretty simple so far, so I don't see any "Clean Code" refactorings.

# Second Test
## The next simplest case, I roll all 1s
Now for the next test. I just did one simple one, where all the rolls were the same. Now I'll pick the next simplest case, where all the rolls are still the same, but non zero (i.e. 1)

### write the test (red)
This test case looks a lot like my first one. I can rip through it because I don't have any more red squiggles. The only two differences are the number of pins I roll and the expected score. Lots of duplicated code here. 

I run this test and get 1 passing and 1 failing test in both my Output (Python Test Log) window and my VSCode status bar.

AssertionError: 20 != 0


The test code also has a decoration above the failing method.

This is exactly what I expect (and demand).

### make it pass (green)
The simplest thing I can do here is to add each roll to a variable and return that.

test_when_all_rolls_are_0_score_is_0 (game_test.Game_Tests) ... ok
test_when_all_rolls_are_1_score_is_20 (game_test.Game_Tests) ... ok


### refactor (including the test)
Now that I have a safety net in place, I can refactor. The production code (on the right) seems clean. The test code (which is first class, important code) has some duplication. So I'll clean that up.

I create a class variable for Game (_target) and reference that. I also ensure I create a new one on each test by using the unittest provided setUp() and tearDown() methods

After each small refactoring step I run my tests to ensure that I'm safe. 

I also see the for loop has a lot of repeated code, and I think I might it more, so I refactor that by extrating a method, again running my tests after each step. 

NOTE: I've had some differening experiences with the refactoring widget in VSCode via the Python Extension. Sometimes it works like I expect  and sometimes not. I haven't done enough research to get to a a root cause. This inconsistency causes me to run the tests more than I would if I trusted the refactoring tool

# Third Test
## first special handling case - A Spare
### write the test (red)

### make it pass (green)

### refactor (including the test)

# Fourth Test
## second special case -  A strike
### write the test (red)

### make it pass (green)

### refactor (including the test)

# Last Test
## special call - all 10s (a perfect game)
### write the test (red)



