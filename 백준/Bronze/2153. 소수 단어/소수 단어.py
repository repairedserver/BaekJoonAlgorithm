def check_primary(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "It is not a prime word."
    return "It is a prime word."
def change_word(word):
    num = 0
    
    for char in word:
        if ord('a') <= ord(char) <= ord('z'):
            num += ord(char) - 96
        elif ord('A') <= ord(char) <= ord('Z'):
            num += ord(char) - 38
    return num

if __name__ == "__main__":
    word = input()
    word_num = change_word(word)
    print(check_primary(word_num))