import numpy
import pandas
import statsmodels.api as sm

def main():
    simple_heuristic('titanic_data.csv')

def simple_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female' or passenger['Pclass'] == 1 and passenger['Age'] < 18 or passenger['Parch'] == 'C':
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

    count = 0.0
    for passenger_index, passenger in df.iterrows():
        if predictions[passenger['PassengerId']] == passenger['Survived']:
            count += 1
    print count / df['PassengerId'].count() * 100
        
    return predictions

main()
