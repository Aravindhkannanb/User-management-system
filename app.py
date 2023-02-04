from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']="Aravindh"
app.config['MYSQL_PASSWORD']="12345"
app.config['MYSQL_DB']="crud"
mysql=MySQL(app)
@app.route("/")
def home():
    cur=mysql.connection.cursor()
    cur.execute("select * from detail")
    res=cur.fetchall()
    return render_template('index.html',jinja=res)
@app.route('/add',methods=["GET","POST"])
def add():
    if(request.method=='POST'):
        name=request.form.get('name')
        age=request.form.get('age')
        city=request.form.get('city')
        con=mysql.connection.cursor()
        con.execute("insert into detail(name,age,city)values(%s,%s,%s)",(name,age,city))
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("register.html")
@app.route('/edit/<string:id>',methods=["GET","POST"])
def edit(id):
    cons=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form.get("name")
        city=request.form.get("city")
        age=request.form.get('age')
        cons.execute("update detail set name=%s,age=%s,city=%s where id=%s",(name,age,city,id))
        mysql.connection.commit()
        cons.close()
        return redirect(url_for('home'))
    cons.execute("select * from detail where id=%s",(id))
    res=cons.fetchone()
    return render_template('update.html',data=res)
@app.route("/delete/<string:id>",methods=["POST","GET"])
def delete(id):
    con=mysql.connection.cursor()
    con.execute("delete from detail where id=%s",(id))
    con.connection.commit()
    con.close()
    return redirect(url_for('home'))
if __name__=="__main__":
    app.run(debug=True,port=8000)