words =  input()
cleaned_input = ''.join(char for char in words if char.isalnum())
sets = set(cleaned_input)
print(len(sets))