# Запись слов в питон
#my_file = open("my_file" , "w")
#my_words = ["Вылетаем" , "сегодня" , "вечером"]
#for i in range (0, 3):
#    my_file.write(my_words[i] + "\n")
#my_file.close()

# Вывод данных с файла
spisok = []
my_file = open("my_file" , "r")
print(my_file.read())
for line in my_file:
    spisok.append(line)
for i in range(0, len(spisok)):
    print(spisok[i])