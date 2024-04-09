from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sensitive import SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = "static/files"
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


def hash_password(password):
    return generate_password_hash(
        password,
        method="scrypt",
        salt_length=16
    )


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=hash_password(request.form.get("password"))
        )

        existing_user = db.session.query(User).filter(User.email == new_user.email).first()
        if not existing_user:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return render_template("secrets.html", username=new_user.name)
        else:
            flash("You've already signed in with that email! Log in instead.")
            return redirect(url_for('login'))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Retrieve form input
        submitted_email = request.form.get("email")
        submitted_password = request.form.get("password")

        user = db.session.query(User).filter(User.email == submitted_email).first()
        if not user:
            flash("The email does not exist. Please try again.")
            return redirect(url_for('login'))

        hashed_password = user.password

        if check_password_hash(hashed_password, submitted_password):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            flash("Password incorrect. Please try again.")
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", username=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout successful.")
    return redirect(url_for('home'))


@app.route('/download/<path:filename>')
@login_required
def download(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
