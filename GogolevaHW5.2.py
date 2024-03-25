word = input('Напишите слово латинскими буквами: ')

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = sum(letter in vowels for letter in word)
consonant_count = len(word) - vowel_count

print('Гласных: ', vowel_count)
print('Согласных: ', consonant_count)

for i in vowels:
    vowel_count_i = word.count(i)
    if vowel_count_i > 0:
        print(f'{i}: ', vowel_count_i)
    else:
        print(f'{i}: False')