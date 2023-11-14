# Execute your methods here.
from src import *



def main():
    # people_list.sort(key=lambda p: p['name'])
    # print(people_list)
    # new_list = list(filter(lambda p: p['sex'] == "male", people_list))
    # print(new_list)
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
        ]


def ex4():
    
    def get_people(people_list):
        new_list = [p['name'] for p in people_list if p['age'] >= 15]
        print(new_list)





if __name__ == '__main__':
    main()
