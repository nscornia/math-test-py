import time
import turtle
import random
import math
import util.math
import util.question
import util.turtle
import something


score = 0
sleepTime = 0
numQuestions = 2
numQuestions2 = 4
numSets = 12


print('Welcome\n')


time.sleep(sleepTime)
print('You will be tested shortly\n')

time.sleep(sleepTime)
print('Warning. only go down to tenths if your awnser has decimals\n')

time.sleep(sleepTime)
print('Enjoy the intermission\n')
time.sleep(sleepTime)


turtle.speed(0)
util.turtle.turtlePattern()
turtle.left(45)
turtle.forward(100)
util.turtle.turtlePattern()
turtle.bye()

time.sleep(sleepTime)
print('The test is starting\n')
time.sleep(sleepTime)
time.sleep(sleepTime)


if not util.question.gameover:
  util.question.questionSet('easy', numQuestions)

if not util.question.gameover:
  util.question.questionSet('medium', numQuestions)

if not util.question.gameover:
  util.question.questionSet('hard', numQuestions)

if not util.question.gameover:
  util.question.questionSet('ultra', numQuestions)

if not util.question.gameover:
  util.question.questionSet3('easy', numQuestions)

if not util.question.gameover:
  util.question.questionSet3('medium', numQuestions)

if not util.question.gameover:
  util.question.questionSet3('hard', numQuestions)

if not util.question.gameover:
  util.question.questionSet3('ultra', numQuestions)

if not util.question.gameover:
  util.question.questionSet('ultimintistist', numQuestions)

if not util.question.gameover:
  util.question.questionSet3('ultimintistist', numQuestions)

if not util.question.gameover:
  util.question.questionSet('Super Ultimint', numQuestions)

if not util.question.gameover:
  util.question.questionSet3('Super Ultimint', numQuestions)




if score == numQuestions * numSets:
  something.questionSet2('???', numQuestions2)


if score == numQuestions * numSets + numQuestions2:
  something.questionSet2('????', numQuestions2)


time.sleep(sleepTime)
print(f"Your total score is {util.question.score} out of 24\n")

time.sleep(sleepTime)


if util.question.score >= (99 / 100) * numQuestions * numSets + numQuestions2 + numQuestions2:
  print("Your grade is NULL")
if util.question.score >= (87 / 100) * numQuestions * numSets + numQuestions2 + numQuestions2:
  print("Your grade is S")
if util.question.score >= (70 / 100) * numQuestions * numSets + numQuestions2 + numQuestions2:
  print("Your grade is A")
elif util.question.score >= (60 / 100) * numQuestions * numSets + numQuestions2 + numQuestions2:
  print("Your grade is B")
elif util.question.score >= (40 / 100) * numQuestions * numSets + numQuestions2 + numQuestions2:
  print("Your grade is C")
elif util.question.score >= (30 / 100) * numQuestions * numSets + numQuestions2 + numQuestions2:
  print("Your grade is D")
else:
  print("Your grade is F")
