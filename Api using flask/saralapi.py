#importing flask(lightweight web frame of Python,provides the user with libraries, modules and tools to help build Web-Applications )
#importing jsonify() function in flask return an object that already has the appropriate content-type header
#importing abort as it properly wraps errors into a HTTPException so it will have the same behavior
#importing request as The data from a client's web page is sent to the server as a global request object. In order to process the request data
from flask import Flask,jsonify,abort,request 
import json # importing json to convert the python dictionary above into a JSON string that can be written into a file. 
import os.path # importing os.path in order to check whether a particular file exist or not in system or not

app1=Flask(__name__)   # giving instance of Flask class to a variable "app1"



details=[
		{"course_name":"bas ek galti",
	 	"details":"learning how to fix python errors",
	 	"course_id":1},

		{"course_name":"problem Solvinggss",
	 	"details":"some great problem solving challenges to keep you awake",
	 	"course_id":2}
	 	]

hint=[
	{"course_id":1,
	"hint":"no hint",
	"exercises_name":"debugging",
	"exercise_id":1,
	"content":"debugging is good"
	},
{
	"course_id":1,
	"hint":"no hint",
	"exercises_name":"hackathon",
	"exercise_id":2,
	"content":"the whole night you have to wake up"},
	{
	"course_id":2,
	"hint":"no hint",
	"exercises_name":"hackathon",
	"exercise_id":1,
	"content":"the whole night you have to wake up"

	},
	{
	"course_id":2,
	"hint":"no hint",
	"exercises_name":"learning by self",
	"exercise_id":2,
	"content":"learn to learn is the biggest tool"

	}
	
]






submission=[
			{"course_id":1,
			"exercise_id":1,
			 "name":"risabh",
			 "feedback":"this was really a good task"

			},
			{"course_id":2,
			"exercise_id":1,
			 "name":"vandana ",
			 "feedback":"this was really a good task to do hehehe"
			 }]




@app1.route("/saral/courses",methods=["GET"]) #get the details of all the courses  and storing them into a json file

def task():
	if os.path.isfile("file.json"):
		with open('file.json', 'r') as file1:
			read=file1.read()
			a=json.loads(read)
		return jsonify(a)
	with open("file.json","w") as file1:
			json.dump(details,file1)

	return jsonify({"courses":details})

@app1.route("/saral/courses/<int:course_id>",methods=["GET"])#accessing a particualr course from the course id

def tasks(course_id):
	with open ('file.json') as file1:
		read=file1.read()
		a=json.loads(read)
	for i in range(len(a)):
		if a[i]["course_id"]==course_id:
			return jsonify({"course":a[i]})





@app1.route("/saral/courses/<int:course_id>",methods=["PUT"]) # editing the details of  a particualr course using PUT method

def rename(course_id):
	# task=[task for task in details if course_id==task["course_id"]]
	# if len(task)==0:
	# 	abort(400)
	# task[0]["course_name"]=request.json["course_name"]
	# task[0]["details"]=request.json["details"]
	with open("file.json","r")as file:
		myfile=file.read()
		data=json.loads(myfile)
	data[course_id-1]["course_name"]=request.json["course_name"]
	data[course_id-1]["details"]=request.json["details"]
	with open("file.json","w")as file1:
		json.dump(data, file1)
	return jsonify({"details":data})
	




@app1.route("/saral/courses",methods=["POST"])# adding a new course in the list "details" using POST method
def update():

	if not request.json or not "course_name" in request.json:
		abort(404)
	task={
	"course_id":details[-1]["course_id"]+1,
	"course_name":request.json["course_name"],
	"details":request.json["details"]
	} 
	details.append(task)
	with open("file.json","w") as file1:
		json.dump(details,file1)
	return jsonify({"task":task})

@app1.route("/saral/courses/<int:course_id>/exercise")# accessing the sub exercises of all the course and storing it to a json file

def exercise(course_id):
	with open("file.json","r") as file1:
		read=file1.read()
		b=json.loads(read)
	task=[task for task in hint if task["course_id"]==course_id]
	b[course_id-1]['exercise']=task
	return jsonify({"exercise":task})

	with open("file.json","w") as file1:
		json.dump(task,file1)
	return jsonify({"exercises":task})

	if len(task)==0:
		abort(404)

	


@app1.route("/saral/courses/<int:course_id>/exercise/<int:exercise_id>")#accessing  the particualr sub exercises of a course using GET method

def particular_exercises(exercise_id,course_id):
	task=[task  for task in hint if task["exercise_id"]==exercise_id and course_id==task["course_id"]]
	if len(task)==0:
		abort(404)
	return jsonify({"exercise":task})

@app1.route("/saral/courses/<int:course_id>/exercise",methods=["POST"]) #adding a new sub exersies into a course uisng post method

def update_exercise(course_id):
	task1=[task for task in hint if task["course_id"]==course_id] 
	if not request.json or not "exercises_name" in request.json:
		abort(400)
	task={
	"course_id":(course_id),
	"exercise_id":task1[-1]["exercise_id"]+1,
	"exercises_name":request.json["exercises_name"],
	"content":request.json["content"],
	"hint":request.json["hint"]
			}
	hint.append(task)
	return jsonify({"exericse":task})



@app1.route("/saral/courses/<int:course_id>/exercise/<int:exercise_id>/feedback")#accessing the feedback of a particular sub exercise of a course using GET 
def getsubmision(course_id,exercise_id):
	sub=[sub for sub in submission if  sub["course_id"]==course_id and sub["exercise_id"]==exercise_id]
	if len(sub)==0:
		return jsonify({"submission":sub})
	return jsonify({"submission":sub})



@app1.route("/saral/courses/<int:course_id>/exercise/<int:exercise_id>/feedback",methods=["POST"])#adding new feedback to a particukar sub exercise using POST method
def posting_submission(course_id,exercise_id):
	task=[task for task in submission if task["course_id"]==course_id and task["exercise_id"]==exercise_id]
	feedback={
	"exercise_id":(exercise_id),
	"course_id":(course_id),
	"name":request.json["name"],
	"feedback":request.json["feedback"]
	}

	submission.append(feedback)
	return jsonify({"submission":feedback})

if __name__=="__main__":
	app1.run(debug=True,port=8000)
