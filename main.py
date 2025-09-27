ememe_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in ememe_dict.keys():
    print(ememe_dict[word])
else:
    print("нету такова слова")
