# def transform(person):
#     result ={
#         # 'id': person['id'],
#         # 'name': person['name'],
#         # 'weight_kg': person['weight_kg'],
#         # 'height_meters': person['height_meters'],
#         **person,
#         'bmi': round((person['weight_kg']/person['height_meters'] ** 2), 1)
#     }
#     return result

# def main():
#     people_list = [
#         {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
#         {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
#     ]
#     new_list = list(map(transform, people_list))
#     print(new_list)

# def main():
#     people_list = [
#     {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
#     {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
#     {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
#     ]

#     new_list = [p['name'] for p in people_list if p['age'] >= 15]
#     print(new_list)

# class WordCounter:
#     def __init__(self, sentence):
#         self.words = sentence.split(" ")
#     def count_words(self):
#         return len(self.words)
#     def get_word_count(self):
#         return len(self.words)
#     def get_shortest_word(self):
#         return len(min(self.words, key = len))
#     def get_longest_word(self):
#         return len(max(self.words, key = len))
    
# # Without key=len, Python would compare words like this: "apple" < "banana" < "orange" < "grape" (based on the first letters).
# # With key=len, Python looks at the lengths: len("apple") < len("banana") < len("orange") < len("grape"). Now it's comparing the number of letters in each word.


# def main():
#     sentence = "This is a test of the emergency broadcast system"
#     word_counter = WordCounter(sentence)
#     word_counter.count_words()
#     print(word_counter.get_word_count())    # Returns the number of all the words.
#     print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
#     print(word_counter.get_longest_word())  # Returns the length of the longest word.



# class TaxMan:
#     def __init__(self, items, tax_rate):
#         self.items = items
#         self.tax_rate = float(tax_rate.strip('%')) / 100 
#         self.total = 0

#     def calc_total(self):
#         sum = 0
#         for item in self.items:
#              sum += item.get('price')
#         self.total += (sum * (1 + self.tax_rate))

#     def get_total(self):
#         return self.total


# def main():
#     items = [
#         {"id": 1, "desc": "clock", "price": 1.00},
#         {"id": 2, "desc": "socks", "price": 2.00},
#         {"id": 3, "desc": "razor", "price": 3.00},
#     ]
#     tm = TaxMan(items, "10%")
#     tm.calc_total()
#     print(tm.get_total())


# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         self.result = 0

#     def add(self):
#         self.result = self.num1 + self.num2

#     def get_result(self):
#         return self.result

# def main():
#     calculator1 = Calculator(4, 3)
#     calculator1.add()
#     print(calculator1.get_result())

#     # calculator2 = Calculator(4, 3)
#     # calculator2.sub()
#     # print(calculator2.get_result())

#     # calculator3 = Calculator(2, 3)
#     # calculator3.mul()
#     # print(calculator3.get_result())

#     # calculator4 = Calculator(8, 2)
#     # calculator4.div()
#     # print(calculator4.get_result())

# class CarCollector:
#     car_list = [
#         {"id": 1, "price": 10000},
#         {"id": 2, "price": 20000},
#         {"id": 3, "price": 30000},
#     ]
#     car_dict = {
#         1: "Ford",
#         2: "Mazda",
#         3: "Chevy"
#     }

#     @staticmethod
#     def get_data():
#         return list(map(CarCollector._combine, CarCollector.car_list))
    
#     @staticmethod
#     def _combine(c):
#         rectum = {
#             **c,
#             "make": CarCollector.car_dict[c['id']]
#         }
#         return rectum

# def main():
#     print(CarCollector.get_data())















if __name__ == '__main__':
    main()


