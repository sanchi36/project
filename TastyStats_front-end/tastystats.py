from flask import Flask, render_template, url_for
from forms import getFoodForm
from reader import getFoods

# Global Variables, don'r instantiate reader again
foods = []
uniqueFoods = []

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
    print("Yes, listening")
    form = getFoodForm()
    pred = {}
    act = {}
    your_input = ""
    allFoods, uniqueFoods = getFoods()
    print("Validating form...")
    if form.validate_on_submit():
        print(form.food.data)
        act = getSimilarFoods(form.food.data)
        your_input = form.image.data
        print("We found", len(act), "actual foods")
        # get prediction
        # string output from our model get a string output
        #pred = {}
        pred = "Burger" # hardcoding temporarily
        pred = getSimilarFoods(pred) #get all related entries from our csv
        print("and, we found", len(pred), "matching predictions")

    return render_template('getStats.html', form=form, input=your_input,
                           pred=pred, actual=act, foods=allFoods,
                           title="Ok, let's crunch the food...")


def getSimilarFoods(name):
    simFoods = []
    for f in foods:
        if f['Food'] == name:
            simFoods.append(f)

    return simFoods


if __name__ == '__main__':
    if len(foods) == 0:
        foods, uniqueFoods = getFoods()
    print("wassup")
    app.run(debug=True)