from flask import Flask ,request,jsonify
from database import get_db,create_student

app = Flask(__name__)
create_student()

@app.route("/student",methods=["POST"])
def add_student():
    data=request.json
    conn=get_db()
    name=data["name"]
    email=data['email']
    emailist = conn.execute(""" select * from students where email=? """,(email,))
    count=len(emailist.fetchall())
    course=data['course']
    if count>0:
        return jsonify({"messaeg":"Data already exists in Database"})
    query=""" INSERT INTO students( name, email,course) VALUES (?,?,?) """
    conn.execute(query,(name,email,course))
    conn.commit()
    conn.close()

    return jsonify({"message":"DB created successfully"}),201

@app.route("/student",methods=["GET"])
def get_user():
    conn=get_db()
    cursor =conn.execute(""" SELECT * FROM students """)
    lst=cursor.fetchall()
    student_lst=[]
    for student in lst:
        student_lst.append(dict(student))
    conn.close()
    return jsonify(student_lst)

@app.route("/student/<int:id>",methods=["GET"])
def get_one():
    conn=get_db()
    cursor=conn.execute(""" select * from students where id=? """,(id,))
    student=cursor.fetchone()
    conn.close()

@app.route("/student/<int:id>",methods=["PUT"])
def update_one():
    conn=get_db()
    data=request.json
    conn.execute(""" UPDATE students SET name = ?, email=? , course=? where
                  id=? """,(data['name'],data['email'],data['course'],id))
    conn.commit()
    conn.close()
    return jsonify({"message":"Data updated"})

@app.route("/student/<int:id>",methods=["DELETE"])
def delete_one():
    conn=get_db()
    conn.execute("""  DELETE FROM students WHERE id=? """,(id,))
    conn.commit()
    conn.close()
    return jsonify({"message" :"student deleted succussfully"})



if __name__=="__main__":
    app.run(debug=True)
