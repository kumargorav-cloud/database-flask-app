from flask import render_template,request,redirect,url_for
from flask_login import login_user,logout_user,login_required,current_user
from models import User

def register_routes(app,db,bcrypt):
    # @app.route("/",methods=['GET','POST'])
    # def index():
    #     if current_user.is_authenticated:
    #         return str(current_user.uname)
    #     else:
    #         return "No user logged in!!"
    @app.route("/")
    def index():
        return render_template('index.html')
    
    # @app.route("/login/<uid>")
    # def login(uid):
    #     user = User.query.get(uid)
    #     login_user(user)
    #     return "Success"

    @app.route('/signup',methods=['GET','POST'])
    def sign_up():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            uname = request.form.get('uname')
            password = request.form.get('password')

            hashed_password = bcrypt.generate_password_hash(password)
            user = User(uname=uname,password=hashed_password)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))


    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            uname = request.form.get('uname')
            password = request.form.get('password')

            user = User.query.filter(user.uname == uname).first()

            if bcrypt.check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for('index'))
            
            else:
                return "Invaild Username or Password!!"


    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for('index'))
    

    @app.route('/secret')
    @login_required
    def secret():
        return "My secret key"

        # if request.method == 'GET':
        #     people = Person.query.all()
        #     return render_template('index.html',people=people)
        
    #     elif request.method == 'POST':
    #         name = request.form.get('name')
    #         age = int(request.form.get('age'))
    #         job = request.form.get('job')

    #         person = Person(name=name,age=age,job=job)

    #         db.session.add(person)
    #         db.session.commit()
    #         people = Person.query.all()
    #         return render_template('index.html',people=people)


    # @app.route("/delete/<pid>",methods=['DELETE'])
    # def delete(pid):
    #     Person.query.filter(Person.pid == pid).delete()

    #     db.session.commit()
    #     people = Person.query.all()

    #     return render_template('index.html',people=people)

    # @app.route("/details/<pid>")
    # def details(pid):
    #     person = Person.query.filter(Person.pid == pid).first()
    #     return render_template('details.html',person=person)




