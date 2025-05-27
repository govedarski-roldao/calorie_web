from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, IntegerField
from temperature import Temperature
from calorie import Calorie

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template("calories_form_page.html", caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)
        weight = calories_form.weight.data
        height = calories_form.height.data
        age = calories_form.age.data
        country = calories_form.country.data
        city = calories_form.city.data

        temperature = Temperature(country, city)
        print(temperature.get())
        calories = Calorie(weight, height, age, temperature.get())
        print(calories.calculate())

        return render_template("calories_form_page.html", calories=calories.calculate(), caloriesform=calories_form)


class CaloriesForm(Form):
    weight = IntegerField("Add your weight: ", default=95)
    height = IntegerField("Add your height: ", default=183)
    age = IntegerField("Add your age: ", default=35)
    country = StringField("Which country do you live?", default="Bulgaria")
    city = StringField("In which city do you live?", default="Sofia")
    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/calories_form", view_func=CaloriesFormPage.as_view("calories_form_page"))

app.run(debug=True)
