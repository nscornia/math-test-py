import random
import util.math
import util.question


scoreSet = 0
score = 0
gameover = False


def askQuestion(question, correctAnswer):
  global scoreSet
  awnser = input(question)

  if awnser == correctAnswer:
    print('\nCorrect\n')
    scoreSet = scoreSet + 1
  else:
    print('\nIncorrect\n')


def mathQuestion(startNum, endNum, operator):
  operatorFn = util.math.toMathFn(operator)

  rand1 = random.randint(startNum, endNum)
  rand2 = random.randint(startNum, endNum)

  answer = operatorFn(rand1, rand2)

  if (operator == "/"):
    answer = round(answer, 1)

  askQuestion(f"What is {rand1} {operator} {rand2} ? ", f"{answer}")


def questionSet(difficulty, numQuestions):
  global scoreSet
  global score
  global gameover

  retries = 3
  fail = True

  print(f"This set's difficulty is {difficulty}")
  print(f"There are {numQuestions} questions in , you have three tries to pass the set.")
  print(f"You must have a score of 80% or higher to pass the set. Each question is worth one point to your score")

  while retries > 0 and fail:
    addSubtract(difficulty, numQuestions)
    gradeSet = ((80/100) * numQuestions)

    print(f"Your score is {scoreSet} out of {numQuestions}\n")
    retries -= 1

    if scoreSet < gradeSet:
      print(f"You failed, you have {retries} attempts left to pass this set\n")

    else:
      score = score + scoreSet
      fail = False
      print(f"You passed {difficulty} difficulty\n")

    scoreSet = 0
    if retries == 0:
      gameover = True


def questionSet3(difficulty, numQuestions):
  global scoreSet
  global score
  global gameover

  retries = 3
  fail = True

  print(f"This set's difficulty is {difficulty}")
  print(f"There are {numQuestions} questions in {difficulty}")
  print(f"You have three tries to pass the set.")
  print(f"You must have a score of 80% or higher to pass the set.")
  print(f"Each question is worth one point to your score")

  while retries > 0 and fail:
    multiplyDivide(difficulty, numQuestions)
    gradeSet = ((80/100) * numQuestions)

    print(f"Your score is {scoreSet} out of {numQuestions}\n")
    retries -= 1

    if scoreSet < gradeSet:
      print(f"You failed, you have {retries} attempts left to pass this set\n")

    else:
      score = score + scoreSet
      fail = False
      print(f"You passed {difficulty} difficulty\n")

    scoreSet = 0
    if retries == 0:
      gameover = True


def addSubtract(difficulty, numQuestions):
  count = 1

  modifier = 1
  if difficulty == 'medium':
    modifier = 9

  if difficulty == 'hard':
    modifier = 37

  if difficulty == 'ultra':
    modifier = 256

  if difficulty == 'ultimintistist':
    modifier = 1024

  if difficulty == 'Super Ultimint':
    modifier = 4096

  while count <= numQuestions:
    startNum = ((count * 7) + 1) * modifier
    endNum = ((count * 7) + 10) * modifier
    mathQuestion(startNum, endNum, "+")
    mathQuestion(startNum, endNum, "-")
    count += 2


def multiplyDivide(difficulty, numQuestions):
  count = 1

  modifier = 1
  if difficulty == 'medium':
    modifier = 9

  if difficulty == 'hard':
    modifier = 37

  if difficulty == 'ultra':
    modifier = 256

  if difficulty == 'ultimintistist':
    modifier = 1024

  if difficulty == 'Super Ultimint':
    modifier = 4096

  while count <= numQuestions:
    startNum = ((count * 7) + 1) * modifier
    endNum = ((count * 7) + 10) * modifier
    mathQuestion(startNum, endNum, "*")
    mathQuestion(startNum, endNum, "/")
    count += 2

  # mathQuestion(10 * modifier, 50 * modifier, "+")
  # mathQuestion(10 * modifier, 50 * modifier, "-")
  # mathQuestion(30 * modifier, 100 * modifier, "+")
  # mathQuestion(30 * modifier, 100 * modifier, "-")
