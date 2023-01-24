from flask import Flask, jsonify, render_template, request

app= Flask(__name__)
courses=[
    {
        'courseID': 1,
        'courseName': 'Python Proramming Certification Course'
    },
    {
        'courseID': 2,
        'courseName': 'Data Science Certification'

    },
    {
        'courseID':3,
        'courseName': 'Python Api Development'
    }

]

@app.route('/')
def index():
    return render_template('index.html')

@app. route('/app/api/courses/all')
def show():
    return jsonify(courses)

@app. route('/app/api/courses', methods=['GET'])
def id():
    if 'id' in request.args:
        id=int(request.args['id'])
    else:
        return "unknown request"

    result =[]

    for course in courses:
        if course['courseID'] == id:
            result.append(course)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)









