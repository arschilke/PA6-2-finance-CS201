import string
a = "fnoisdnafoidh.,/;']'/;fhe89hfp/..//';.,,/l;';'????!!!!!!!"
print(string.punctuation)
for letter in string.punctuation:
    a = a.replace(letter, "")
print(a)
