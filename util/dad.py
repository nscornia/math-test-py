
def questionSetDad(difficulty, numQuestions, operator):
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
    mathQuestionDifficulty(difficulty, numQuestions, operator)
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


# if not util.question.gameover:
#   util.question.questionSetDad('easy', numQuestions, "+")

# if not util.question.gameover:
#   util.question.questionSetDad('medium', numQuestions, "+")

# if not util.question.gameover:
#   util.question.questionSetDad('hard', numQuestions, "+")

# if not util.question.gameover:
#   util.question.questionSetDad('ultra', numQuestions, "+")
