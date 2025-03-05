def vowels_count(text):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

input_text = "Мама ушла на работу"
vowel_count = vowels_count(input_text)

print(f"В предложении '{input_text}' содержится {vowel_count} гласных.")
