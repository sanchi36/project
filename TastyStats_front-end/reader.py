import csv

# unique foods in the csv file
uniqueFoods = {}

def processData():
    with open('../data/calorie_dataset.csv') as csv_file:
        # each entry in the csv file
        foods = []

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            tmp = {}
            if line_count == 0 or len(row[0].strip()) == 0:
                line_count += 1
            else:
                tmp["Food"] = row[0].strip()
                tmp["SubCategory"] = row[1].strip()
                tmp["ServingSize"] = row[2].strip()
                tmp["Fat(g)"] = row[3].strip()
                tmp["Calories"] = row[4].strip()
                tmp["Ingredients"] = row[5].strip()
                foods.append(tmp)

                # add to the option list as well
                uniqueFoods[row[0].strip()] = 0
        return foods

def getFoods():
    foods = processData()
    foodOptions = []
    for key, value in uniqueFoods.items():
        foodOptions.append(key)
    print("Found", len(foods), "types of food and", len(foodOptions), "unique foods")
    return foods, foodOptions

if __name__ == '__main__':
    processData()
