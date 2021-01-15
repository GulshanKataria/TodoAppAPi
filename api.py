#!flask/bin/python
from flask import Flask
from flask_restful import Resource,Api,reqparse,abort

app = Flask(__name__)

api=Api(app)



todos= {

    1: {"task" : "widhya internship ", " summary": "complete task1 and submit the code"},
     2: {"task" : "widhya internship ", " summary": "complete task2 and submit the code"},
      3: {"task" : "widhya internship ", " summary": "complete task3 and submit the code"},
       4: {"task" : "widhya internship ", " summary": "complete task4 and submit the code"},
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task",type=str ,help="task is required", required=True)
task_post_args.add_argument("summary",type=str ,help="task is required", required=True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task",type=str )
task_put_args.add_argument("summary",type=str)


class ToDo(Resource):
    def get(self,todo_id):
        return todos[todo_id]

    def post(self,todo_id):
        args=task_post_args.parse_args()
        if todo_id in todos:
            abort(489,"Task id already taken")
        todos[todo_id]={"task":args["task"],"summary":args["summary"]}
        return todos[todo_id]

    def put(self,todo_id):
        args =task_post_args.parse_args()
        if todo_id not in todos:
            abort(404,"task doesnt exist")
        if args["task"]:
            todos[todo_id]["task"] = args["task"]
        if args["summary"]:
            todos[todo_id]["summary"] = args["summary"]
        return todos[todo_id]

    def delete(self,todo_id):
        del todos[todo_id]
        return todos


'''
class HelloWorld(Resource):
    def get(self):
        return {'data' :'Hello World'}

api.add_resource(HelloWorld,'/helloworld')

'''

class ToDoList(Resource):
    def get(self):
        return todos

api.add_resource(ToDo, '/todos/<int:todo_id>')

api.add_resource(ToDoList, '/todos')




if __name__ == '__main__':
    app.run(debug=True)