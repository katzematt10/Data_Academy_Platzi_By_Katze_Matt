# This program works to identify if a word is or not a palindrome

def Palindrome(word):
    word = word.replace(' ',''  )
    word = word.lower()
    UPDN_Word = word[::-1]
    if word == UPDN_Word:
        return True
    else:
        return False

def run(): # Main function
    word = input("Type a word or phrase: ")
    Is_palindrome = Palindrome(word)
    if Is_palindrome == True:
        print("The word/phrase is palindrome")
    else:
        print("The word/phrase is NOT palindrome")
if __name__ == '__main__':
    run()
