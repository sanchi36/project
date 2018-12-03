from flask import Flask, render_template
from forms import getFoodForm
from reader import getFoods
import glob, os

# Global Variables, don'r instantiate reader again
foods = []
uniqueFoods = []
path = "C:/Users/anuba/Desktop/Grad_School/4_Fall-2018/CV/Project/TastyStats/project"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'da50f45e806d34c2f51f4baf9c1f7350'
app.config['DATA_IMAGE_PATH'] = "C:/Users/anuba/Desktop/Grad_School/4_Fall-2018/CV/Project/TastyStats/project/challenge/"

print("Static path:", app.static_url_path)
foods_dummy = [
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

@app.route('/test/<path:filename>')
def custom_images(im_file):
    return app.send_from_directory(app.config['DATA_IMAGE_PATH'], im_file)

@app.route("/explore", methods=['GET','POST'])
@app.route("/getStats", methods=['GET','POST'])
def getStats():
    form = getFoodForm()
    pred = {}
    act = {}
    
    user_input = ""
    im_path = ""
    allFoods, uniqueFoods = getFoods()
    fnf_error = ""
    if form.validate_on_submit():
        user_input = form.filename.data
        im_path = "static/" + user_input
        '''
        im_path = getFilePath(user_input)
        print("Im_path before cropping:", im_path)
        cropidx = im_path.index("test\\")
        im_path = im_path[cropidx+5:]
        
        im_path = "challenge/test/" + im_path.replace('\\', '/')
        print("final rel path:", im_path)
        #abs_path = os.path.abspath(im_path) + im_path
        

        im_path = im_path.replace('\\', '/')
        if len(im_path) == 0:
            fnf_error = "Could not find the test image file. Please try again."

        # get prediction from im_path variable
        # predicted food (string)
        #---------add prediction code here-----------

        '''
        #pred = {}
        #pred = "Burger" # hardcoding temporarily

        pred = getSimilarFoods(pred) #get all related entries from our csv
    return render_template('getStats.html', form=form, err=fnf_error, input=user_input,
                           impath=im_path, pred=pred, actual=act, foods=allFoods,
                           title="Ok, let's crunch up the food...")

def getFilePath(filename):
    path = ""
    print("Given name:", filename)
    #for file in glob.iglob('test/**/*', recursive=True):
    for file in glob.iglob('../challenge/test/**/*', recursive=True):
        if filename in file:
            print("Yay, found the image:", file)
            path = file
            break
    return path

def getSimilarFoods(name):
    simFoods = []
    for f in foods:
        if f['Food'] == name:
            simFoods.append(f)

    return simFoods

if __name__ == '__main__':
    if len(foods) == 0:
        foods, uniqueFoods = getFoods()
    app.run(debug=True)