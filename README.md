# PythonBowlingKata
Standard bowling kata for python

# Purpose
I use the bowling kata to learn new languages. It helps me to fix one side of the problem (the "business" side) so I can focus on learning the new ("language") side.  

The bowling kata is helpful because it provides clear opportunties to exerice the *RED/GREEN/REFACTOR* cycle and exercises common elements of the new language (class, method, loops, arrays (or lists)).  

This repository has a series of commits that reflect steps in the kata.  

## Kata
Kata is a term often found in Japanese martial arts. The English word "form" is analgous. The idea is a set of steps you practice to demonstrate a grasp of fundamentals, remind your mind of the flow of a thing, and to separate you from the world outside of practice and prepare for a new practice sesssion.  

Martin Fowler, among many others, have promoted the idea of "coding kata" for the same reason.  

The goal would be to do this kata daily (or for up to 20 minutes a day). Some people who are learning this kata will work on part for 20 minutes, then pick up the next day at that point and continue. Others will just bang through it, it getting a bit farther each day. I have found the latter technique more useful. You may find something different.

## the Python
I'm a self (mis)taught developer who has worked in a variety of languages going back to dBase III. Much of my coding time has been spent in C#. To the degree the code here isn't *pythonic*, that's just my ignorance (which I am hoping to decrease).

## Prereqs
VS Code with Python Extension

I originally installed VSCode on my MacBook Air, then added the MS Python Extension. After a few weeks of using this, I actually removed it all, installed Anaconda, and had the Anaconda Navigator install VSCode. This seemed to resolve a few small annoyances.

## using this repo
I created this repo to share the steps. The best way to use it is to view the change sets in your browser and then replicate the enter the code (or steps) to get from current state to what you see in the change set. You should not need to clone or pull this repository.

Throughout the Readme.md I've embedded links to the various changesets to try and help view the code in order.

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

[Resolve Red Squiggle](https://github.com/radobson61/PythonBowlingKata/commit/e0c0926a9d794d98dd704f723554edc80c3a3096)

This resolves my red squiggle. 

Next I will create a for loop to roll zero pins twenty times. I again meet the red squiggle of test failure so I write the SIMPLEST CODE to make it pass. A method in Game() named roll that takes 1 parameter.

[Resolve second red squiggle (roll)](https://github.com/radobson61/PythonBowlingKata/commit/9100c3f838ece5b0a0f6009cbfefcec230189ed8)

Finally, I assert that Game().score() is 0 and I resolve my red squiggle by ensuring Game().score() returns None.

[Resolve third red squiggle (score) and failing test](https://github.com/radobson61/PythonBowlingKata/commit/313e3820eb675cf72ba5d335b5479fd8a82edb67)

I have a complete test (with my red / green cycle for resolving compiler errors)

I run all my unit tests (Commmand-Shift-P: Python: Run All Unit Tests) and get a box telling me to enable a Unit Test Framework. When you Enable a testing framework in VS Code (Python) you'll get prompted to configure the testing framework. Select unittest or the framework, root for the directory and *_test.py for the format of the file. (Note: you can configure VSCode for defaults for test framework and the rest. I leave it, as I'm still learning VSCode and this is part of the kata for me.)

I can see the failure by viewing the Output window (with Python Test Log selected in the drop down).  

`AssertionError: 0 != None`

I can  also see an indicator of a failing test in the status bar

![Test 1 Fails](/images/Test1Fails.png)

And finally, the test code has a decorator that both shows the status and allows me to re-run the test by double clicking it

![Test Method Decorator](/images/FailingTestDecorator.png)

### make it pass (green)
For me, writing small tests is often a challenge. Writing the smallest code that will make a failing test pass is more so. Its important. So I'll write the SMALLEST code that will make this test pass.

```python
return 0
```

And in my output window I see the confirmation the test passed. 

`test_when_all_rolls_are_0_score_is_0 (game_test.Game_Tests) ... ok`  

The VSCode status bar also shows me I have 1 passing test.

![Test 1 Passes](/images/Test1Passes.png)

### refactor (including the test)
Everything is pretty simple so far, so I don't see any "Clean Code" refactorings.

# Second Test
## The next simplest case, I roll all 1s
Now for the next test. I just did one simple one, where all the rolls were the same. Now I'll pick the next simplest case, where all the rolls are still the same, but non zero (i.e. 1)

### write the test (red)
This test case looks a lot like my first one. I can rip through it because I don't have any more red squiggles. The only two differences are the number of pins I roll and the expected score. Lots of duplicated code here. 

I run this test and get 1 passing and 1 failing test in both my Output (Python Test Log) window and my VSCode status bar.

`AssertionError: 20 != 0`  

The test code also has a decoration above the failing method.

This is exactly what I expect (and demand).

![Test 2 Fails](/images/Test2Fails.png)

### make it pass (green)
The simplest thing I can do here is to add each roll to a variable and return that.

`test_when_all_rolls_are_0_score_is_0 (game_test.Game_Tests) ... ok`  
`test_when_all_rolls_are_1_score_is_20 (game_test.Game_Tests) ... ok`  

And the status bar

![Test 2 Passes](/images/Test2Passes.png)

### refactor (including the test)
Now that I have a safety net in place, I can refactor. The production code (on the right) seems clean. The test code (which is first class, important code) has some duplication. So I'll clean that up.

I create a class variable for Game (_target) and reference that. I also ensure I create a new one on each test by using the *unittest* provided *setUp()* and *tearDown()* methods

After each small refactoring step I run my tests to ensure that I'm safe. 

I also see the for loop has a lot of repeated code, and I think I might use it more, so I refactor that by extrating a method, again running my tests after each step. 

*NOTE: I've had some differening experiences with the refactoring widget in VSCode via the Python Extension. Sometimes it works like I expect  and sometimes not. I haven't done enough research to get to a a root cause. This inconsistency causes me to run the tests more than I would if I trusted the refactoring tool*

# Third Test
## first special handling case - A Spare
Whew! 2 tests down. Both have been pretty simple. Now I need to tackle one of the special cases, a *Spare*. A Spare is when I get 10 pins in two rolls in a frame. So now I have to add the concept of a frame and some kind of test for a frame score.  

### write the test (red)
First I'll write the test. I roll a 5,  then another 5 (to make my Spare), then the 3 because I get to use the first ball of the next frame as my bonus for picking up the Spare. 

As soon as I write the test, I can see there isn't an easy way to make it pass. I  have to refactor my Game() class to create a simple way to make this test pass, so I comment out my recently added test and do a "giant" refactor of my Game() class. I get it working (running my two tests frequently) and then clean it up, to make it more readable.

Now I can uncomment my third test and run it, and it fails. Hooray!!

`AssertionError: 16 != 100`  

And I confirm all the others pass by inspecting the status bar

![Test 3 Fails](/images/Test3Fails.png)

### make it pass (green)
Now I have a simple if test I can do to make the 3rd test pass

`test_when_a_spare_is_followed_by_3_score_is_16 (game_test.Game_Tests) ... ok`  
`test_when_all_rolls_are_0_score_is_0 (game_test.Game_Tests) ... ok`  
`test_when_all_rolls_are_1_score_is_20 (game_test.Game_Tests) ... ok`  

![Test 3 Passes](/images/Test3Passes.png)

### refactor (including the test)
Green is good,  but I'm not done yet. I need to refactor my code, to make it more readable (to non python speakers). 

And I need to check my test code for cleanliness as well. 

# Fourth Test
## second special case -  A strike
Bowling has another special case, a *Strike*. A Strike is when I get 10 pins in the first roll in a frame. I get a different bonus for a Strike.
### write the test (red)
So I write my test, rolling a 10, then a 3 and a 4. My score for this should be 24. 

And the test fails, as it should.

`IndexError: list index out of range`

This time my status bar looks different. The triangle I saw before for a failing assertion is replaced by an X, indicating a failure to build

![Test 4 Fails](/images/TestFourFailsError.png)

### make it pass (green)
Based on experience, and because I know I just made a very small change, I'm going to ignore the index out of range error and just focus on the simplest thing I can do to make the test pass.

`test_when_a_spare_is_followed_by_3_score_is_16 (game_test.Game_Tests) ... ok`  
`test_when_a_strike_is_followed_by_3_and_4_score_is_24 (game_test.Game_Tests) ... ok`  
`test_when_all_rolls_are_0_score_is_0 (game_test.Game_Tests) ... ok`  
`test_when_all_rolls_are_1_score_is_20 (game_test.Game_Tests) ... ok`  

![Test 4 Passes](/images/TestFourPasses.png)

### refactor (including the test)
And then of course, check for opportunities to improve the design of the existing code (aka refactor)

And I won't forget to clean my test code either

# Last Test
## special case - all 10s (a perfect game)
The last special case in bowling is the *Perfect Game* where I roll all strikes. Becase I only get 1 roll in a frame where I get a strike, but I get two rolls after a frame with a strike, I get a total of 12 rolls of 10
### write the test (red)
This test case is fairly simple because of the amount of reuse I can do.

Unfortunately, this test didn't fail.

`test_a_perfect_game_is_300 (game_test.Game_Tests) ... ok`  
`test_when_a_spare_is_followed_by_3_score_is_16 (game_test.Game_Tests) ... ok`  
`test_when_a_strike_is_followed_by_3_and_4_score_is_24 (game_test.Game_Tests) ... ok`  
`test_when_all_rolls_are_0_score_is_0 (game_test.Game_Tests) ... ok`  
`test_when_all_rolls_are_1_score_is_20 (game_test.Game_Tests) ... ok`  

![Test 5 Passes](/images/TestFivePasses.png)

I double check with my business owner to ensure I understand the rules of scoring correctly. Once I confirm that, I realize my Game() is complete for all the normal cases in bowling, my code is clean (and tested).


