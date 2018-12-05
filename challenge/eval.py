import numpy as np
import time
#from sample_model import Model
from data_loader import data_loader
from generator import Generator
import csv
import prettytable
import csv




def evaluate(label_indices = {'FrenchFries': 0, 'Pizza': 1, 'VegBurger': 2, 'spaghetti':3,'Salad':4},
             channel_means = np.array([147.12697, 160.21092, 167.70029]),
             data_path = 'test',
             minibatch_size = 32,
             num_batches_to_test = 1,
             checkpoint_dir = 'checkpoints'):

    
    #print("A. Loading data")
    data = data_loader(label_indices = label_indices, 
               		   channel_means = channel_means,
               		   train_test_split = 0, 
               		   data_path = 'test')

    #print("B. Starting the model")
    M = Model(mode = 'test')

    #Evaluate on test images:
    GT = Generator(data.test.X, data.test.y, minibatch_size = minibatch_size)
    
    num_correct = 0
    num_total = 0
    
    #print("C. Evaluating ")
    for i in range(num_batches_to_test):
        GT.generate()
        yhat = M.predict(X = GT.X, checkpoint_dir = checkpoint_dir)
        #print(yhat)
        correct_predictions = (np.argmax(yhat, axis = 1) == np.argmax(GT.y, axis = 1))
        length = len(yhat)
        
        for i in range(0,length):
            recordlist=[]
            if(np.argmax(yhat[i])==0):
                print("\n"+"The food item is FRENCH FRIES.")
                food_name ='French Fries'
            elif(np.argmax(yhat[i])==1):
                print("\n"+"The food item is PIZZA.")
                food_name ='Pizza'
            elif(np.argmax(yhat[i])==2):
                print("\n"+"The food item is VEG BURGER.")
                food_name ='Burger'
            elif(np.argmax(yhat[i])==3):
                print("\n"+"The food item is SPAGHETTI.")
                food_name ='Spaghetti'
            elif(np.argmax(yhat[i])==4):
                print("\n"+"The food item is SALAD.")
                food_name ='Salad'
            with open('calorie_dataset.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if row[0] ==food_name:
                        recordlist.append(row)
            t = prettytable.PrettyTable(['Food Item', 'Food Subcategory', 'Serving Size(g)','Fat(g)','Calories','Ingredients'])
            t.align['Ingredients'] = "l"
            t.align['Food Subcategory'] = "l"
            t.max_width=30
            t.hrules = prettytable.ALL
            for record in recordlist:
                t.add_row(record)
            print(t)
            
        num_correct += np.sum(correct_predictions)
        num_total += len(correct_predictions)
    
    accuracy =  round(num_correct/num_total,4)

    return accuracy

if __name__ == '__main__':
    program_start = time.time()
    accuracy = evaluate()
    program_end = time.time()
    total_time = round(program_end - program_start,2)
    print()
    print("Execution time (seconds) = ", total_time)
    print('Accuracy = ' + str(accuracy))
    print()
