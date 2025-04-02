# 2. Напишите функцию, которая принимает предложение и определяет, заикается ли человек. Человек заикается,
# если в предложении есть хотя бы одно слово, за которым идёт слово, содержащее в начале первое слово.
# stutter('Я люблю ре решать задачки') => true //ре - решать
# stutter('Мои любимые тны животные - собаки') => false //тны - НЕ начало слова животные

def man (sentense):
    words = sentense.split()
    for i in range(len(words) -1):
        current_word = words[i]
        next_word = words[i + 1]
        if next_word.startswith(current_word):
            return True
    return False
print(man('Я люблю ре решать задачки'))