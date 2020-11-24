import json
from submission import theCalculator
import sys
from datetime import datetime

#Top level returns:
ret = {}
ret["output"] = "This was an example of how you will be graded in this course."
ret["visibility"] = "visible"
ret["stdout_visibility"] = "visible"
max_score = 1000

#Code Tests:
ret["tests"] = []
score = 0

startTime = datetime.now()

submissionCode = theCalculator()
#QUESTION 1
val = submissionCode.add(2,3)
question = {}
question["max_score"] = 250
question["name"] = "Testing if your code succesfully adds two values together."
question["output"] = ""

if(val == 5):
  question["score"] = 250
else:
  question["score"] = 0
  
question["output"] = "Your code provided the solution of 2+3 = " + str(val) + "."

score = score + question["score"]
ret["tests"].append(question)

#QUESTION 2 =====================
val = submissionCode.multiply(2,3)
question = {}
question["max_score"] = 250
question["name"] = "Testing if your code succesfully multiplies two values together."
question["output"] = ""

if(val == 6):
  question["score"] = 250
else:
  question["score"] = 0
  
question["output"] = "Your code provided the solution of 2*3 = " + str(val) + "."

score = score + question["score"]
ret["tests"].append(question)

#QUESTION 3 =====================
val = submissionCode.subtract(2,3)
question = {}
question["max_score"] = 250
question["name"] = "Testing if your code succesfully subtracts."
question["output"] = ""

if(val == -1):
  question["score"] = 250
else:
  question["score"] = 0
  
question["output"] = "Your code provided the solution of 2-3 = " + str(val) + "."

score = score + question["score"]
ret["tests"].append(question)

#QUESTION 4 =====================

question = {}
question["max_score"] = 250
question["name"] = "Testing if your code succesfully subtracts."
question["output"] = ""

try:
  val = submissionCode.divide(2,3)
except:
  question["score"] = 0
  question["output"] = "Your code provided the solution of 2/3 = " + str(sys.exc_info[0])

if(val == (2/3)):
  question["score"] = 250
else:
  question["score"] = 0
  
question["output"] = "Your code provided the solution of 2/3 = " + str(val) + "."

score = score + question["score"]
ret["tests"].append(question)


#LEADERBOARD
ret["leaderboard"] = []

acc = {}
acc["name"] = "Accuracy"
acc["value"] = score / max_score
ret["leaderboard"].append(acc)

tim = {}
tim["name"] = "Time"
tim["value"] = str(datetime.now() - startTime)
tim["order"] = "asc"
ret["leaderboard"].append(tim)

json.dumps(ret)
outF = open("/autograder/results/results.json", "w")
json.dump(ret, outF)
outF.close()
