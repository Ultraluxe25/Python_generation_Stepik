"""
Самое тяжёлое слово 🗿
Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова. 
Напишите программу, которая принимает 4 слова и находит среди них самое тяжёлое слово. 
Если самых тяжёлых слов будет несколько, то программа должна вывести первое из них.

Формат входных данных
На вход программе подаются 4 слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое тяжёлое слово в строке.

Тестовые данные 🟢

Sample Input 1:

строки
списки
кортежи
множества

Sample Output 1:

множества


Sample Input 2:

az
by
cx
122

Sample Output 2:

az
"""

def find_most_heavy() -> str:
    """
    This function returns word with biggest Unicode sum of chars
    among 4 words
    """
    most_heavy_weight: int = 0
    most_heavy_word: str = ''
        
    for _ in range(4):
        word = input()
        current_weight: int = 0
        
        for char in word:
            current_weight += ord(char)
            
        if current_weight > most_heavy_weight:
            most_heavy_weight = current_weight
            most_heavy_word = word
            
    return most_heavy_word


result = find_most_heavy()
print(result)
