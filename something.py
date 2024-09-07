import random
import util.math
import util.question


scoreSet = 0
score = 0
gameover = False


def askQuestion2(question, correctAnswer):
  global scoreSet
  awnser = input(question)

  if awnser == correctAnswer:
    print('\n4.5./7\n')
    scoreSet = scoreSet + 1
  else:
    print('\n49";.;4../56.\n')


def mathQuestion(startNum, endNum, operator):
  operatorFn = util.math.toMathFn(operator)

  rand1 = random.randint(startNum, endNum)
  rand2 = random.randint(startNum, endNum)

  answer = operatorFn(rand1, rand2)

  askQuestion2(f"43'.4 {rand1} {operator} {rand2} ? ", f"{answer}")


def questionSet2(difficulty, numQuestions2):
  global scoreSet
  global score
  global gameover

  retries = 3
  fail = True

  print(f"'6;..45'64.56.5;466;'.6;46.45;' {difficulty}")
  print(f"45;'.5' {numQuestions2} 4;'.;4'234.23;.214;'4.;'4.;'234.41;'4;,34'.")
  print(f"5.;;'25'45;3.24'268.89.;3.2';7.;'89'/90';7890.;23..1..;'.'6.57.8;'68.'.p;'.136;7'.8';.123..6'.6")

  while retries > 0 and fail:
    addSubtractMultiplyDivide(difficulty, numQuestions2)
    gradeSet = ((99/100) * numQuestions2)

    print(f"4;.;4434.4.4 {scoreSet} 4;'.23;'4.3 {numQuestions2}\n")
    retries -= 1

    if scoreSet < gradeSet:
      print(f";'34.5;'6. {retries} ;'7.4.;1..6;8.l;'4.;24.7;'.73\n")

    else:
      score = score + scoreSet
      fail = False
      print(f"'15.5'.34;'.5.;'3 {difficulty} 5;'.;45'5.\n")



def addSubtractMultiplyDivide(difficulty, numQuestions):
  count = 1

  modifier = 1
  if difficulty == 'medium':
    modifier = 9

  if difficulty == 'hard':
    modifier = 37

  if difficulty == 'ultra':
    modifier = 256

  if difficulty == '???':
    modifier = 478458

  if difficulty == '????':
    modifier = 4784588513567575437854567808567014867548754870546785467854678546784780547805467804506784367854678054678905467805467054813670856780546708467084678054678054670854670846780546780546780546754806780546780547685467805467805467548016701548678054546708670185467015486705481678015467805411670854678017805461681054468067854016805417805466780541670548167085067854107854678654706854678057608547068254678054678054675480

  while count <= numQuestions:
    startNum = ((count * 7) + 1) * modifier
    endNum = ((count * 7) + 10) * modifier
    mathQuestion(startNum, endNum, "+")
    mathQuestion(startNum, endNum, "-")
    mathQuestion(startNum, endNum, "*")
    mathQuestion(startNum, endNum, "/")
    count += 4


#   # mathQuestion(10 * modifier, 50 * modifier, "+")
#   # mathQuestion(10 * modifier, 50 * modifier, "-")
#   # mathQuestion(30 * modifier, 100 * modifier, "+")
#   # mathQuestion(30 * modifier, 100 * modifier, "-")
