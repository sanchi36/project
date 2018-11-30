from flask import Flask, render_template, url_for
from forms import getFoodForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'da50f45e806d34c2f51f4baf9c1f7350'

foods = [
    {
        'Food': 'Ice Cream 0',
        'FoodSubcategory': 'Sundae',
        'ServingSize': '2-3 ',
        'Fat(g)': '30',
        'Calories': '250',
        'Ingredients': 'Milk, cream, berries'
    },
    {
        'Food': 'Cookies',
        'FoodSubcategory': 'Easy Chocolate Chip',
        'ServingSize': '1 dozen',
        'Fat(g)': '32',
        'Calories': '250',
        'Ingredients': 'Flour, milk, chocolate chips, sugar'
    },
    {
        'Food': 'Ice Cream',
        'FoodSubcategory': 'Chocolate!',
        'ServingSize': 'unlimited :) ',
        'Fat(g)': '30',
        'Calories': '200',
        'Ingredients': 'Milk, cream, chocolate - what else?'
    },
    {
        'Food': 'Chips',
        'FoodSubcategory': 'Crunchy Crispy',
        'ServingSize': '2 cups? ',
        'Fat(g)': '32',
        'Calories': '320',
        'Ingredients': 'Potatoes, oil, salt, crispy fun'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/explore", methods=['GET','POST'])
@app.route("/getStats", methods=['GET','POST'])
def getStats():
    form = getFoodForm()
    pred = {}
    act = {}
    if form.validate_on_submit():
        act = foods[1]

        #get prediction
        pred = foods[0]
    return render_template('getStats.html', form=form, pred=pred, actual=act, foods=foods[2:], title="Ok, let's crunch some numbers.")


if __name__ == '__main__':
    app.run(debug=True)