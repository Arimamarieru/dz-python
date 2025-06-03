word = input("Введите слово из маленьких латинских букв: ")

vowels = 'aeiou'
vowel_counts = {v: word.count(v) for v in vowels}
total_vowels = sum(vowel_counts.values())
total_consonants = len(word) - total_vowels

print("Гласных:", total_vowels)
print("Согласных:", total_consonants)

for v in vowels:
    count = vowel_counts[v]
    print(f"{v}: {count if count > 0 else False}")
