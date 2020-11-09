# Function that checks whether an input is a palindrome, the funtion is resilient to certain polluting characters such as spaces and commas.
# Unsure what the last instruction "and loop" means but I'll do as if it means we prompt the user for new text until he input a palindrome

palindrome_found = False
while palindrome_found == False:

    text = str(input("Please enter the text that you would like to check :\n"))
    test_text = ""
    clean_text = text.lower().replace(" ", "").replace(",", "")

    for i in reversed(clean_text):
        test_text += i

    if clean_text == test_text:
        print(f'"{text}" is a palindrome')
        palindrome_found = True

    else:
        print(f'{text} is not a palindrome, try again.')
