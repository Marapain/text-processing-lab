# Перший студент: (Клепач Костянтин)
# Код обробки тексту

# Вхідний текст
text = "Python is a versatile and widely used programming language known for its simplicity and readability. It has numerous applications in web development, data analysis, artificial intelligence, and more."

# 1. Заміна слова 'Python' на 'Programming'
modified_text = text.replace("Python", "Programming")

# 2. Перетворення всього тексту на великий регістр
uppercase_text = modified_text.upper()

# 3. Підрахунок кількості слів у тексті
word_count = len(modified_text.split())

# Виведення результатів
print("Modified Text:", modified_text)
print("Uppercase Text:", uppercase_text)
print("Word Count:", word_count)