vowel_list = ["a","e","i","o","u"]
word = input("Enter a word: ").lower()
count = 0

for c in word:
    for v in vowel_list:
        if c ==v:
            count=count+1
print(count)   

