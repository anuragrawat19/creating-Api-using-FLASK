from flask import Flask,jsonify,abort,request
import json
import os.path
app1=Flask(__name__)



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




@app1.route("/saral/courses",methods=["GET"])

def task():
	if os.path.isfile("file.json"):
		with open('file.json', 'r') as file1:
			read=file1.read()
			a=json.loads(read)
		return jsonify(a)
	with open("file.json","w") as file1:
			json.dump(details,file1)

	return jsonify({"courses":details})

@app1.route("/saral/courses/<int:course_id>",methods=["GET"])

def tasks(course_id):
	with open ('file.json') as file1:
		read=file1.read()
		a=json.loads(read)
	for i in range(len(a)):
		if a[i]["course_id"]==course_id:
			return jsonify({"course":a[i]})





@app1.route("/saral/courses/<int:course_id>",methods=["PUT"])

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
	




@app1.route("/saral/courses",methods=["POST"])
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

@app1.route("/saral/courses/<int:course_id>/exercise")

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

	


@app1.route("/saral/courses/<int:course_id>/exercise/<int:exercise_id>")

def particular_exercises(exercise_id,course_id):
	task=[task  for task in hint if task["exercise_id"]==exercise_id and course_id==task["course_id"]]
	if len(task)==0:
		abort(404)
	return jsonify({"exercise":task})

@app1.route("/saral/courses/<int:course_id>/exercise",methods=["POST"])

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



@app1.route("/saral/courses/<int:course_id>/exercise/<int:exercise_id>/feedback")
def getsubmision(course_id,exercise_id):
	sub=[sub for sub in submission if  sub["course_id"]==course_id and sub["exercise_id"]==exercise_id]
	if len(sub)==0:
		return jsonify({"submission":sub})
	return jsonify({"submission":sub})



@app1.route("/saral/courses/<int:course_id>/exercise/<int:exercise_id>/feedback",methods=["POST"])
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
