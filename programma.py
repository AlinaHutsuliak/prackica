import string

def strip_punctuations(text):
    for character in string.punctuation:
        text = text.replace(character, "")
    return text.strip().lower()
    
filepath = "D:\\test.txt"
word_count = {}

with open(filepath, 'r') as fi:
    text = fi.read()#зчитуємо весь зміст файлу
    text = strip_punctuations(text) #очищуємо від розділових знаків, зайвих пробілів і щоб літери були всі малі
    unique_words = set(text.split()) #формуємо список унікальних слів у тексті

    for word in unique_words:
        word_count[word] = text.count(word) #записуємо у словник слово та його кількість у тексті

sorted_word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True) #сортуємо
for (word, count) in sorted_word_count:
    print(word, '=' ,count)

        
        





