from flask import Flask, render_template, redirect, url_for, flash
from models import db, Cafe
from forms import CafeForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        flash("Cafe added successfully!")
        return redirect(url_for('home'))
    return render_template("add_cafe.html", form=form)

@app.route("/all")
def get_all_cafe():
    cafes = Cafe.query.all()
    return render_template("cafes.html", cafes=cafes)

@app.template_filter('yesno')
def yesno(value, true_value="Yes", false_value="No"):
    return true_value if value else false_value


if __name__ == '__main__':
    app.run(debug=True)
