def count(str):
    chars = {}
    count = 1
    for i in str:
        if i in chars:
            count = chars[i]
            chars[i] = count + 1
        elif i != " ":
            chars[i] = count
    return chars


def find_ch_most(dictionary):
    b = dictionary.values()
    maximum = max(b)
    for key in dictionary:
        if dictionary[key] == maximum:
            return key


def common(str2, str3):
    l = []
    for i in str2:
        for j in str3:
            if i == j:
                if i not in l:
                    l.append(i)
    return l


def all_unique(str4, str5):
    t = ()
    lis = common(str4, str5)
    li = []
    for i in str4:
        if i not in lis and i not in li:
            li.append(i)
    for j in str5:
        if j not in lis and j not in li:
            li.append(j)
    t = tuple(li)
    return t


str1 = input("Enter a sentence:")
a = count(str1)
print(a)
b = find_ch_most(a)
print("\"" + b + "\"" + " has occurred the most in " + "\"" + str1 + "\"")


sentence = input("Enter your name:")
index = sentence.find(" ")
name = sentence[:index]
surname = sentence[index+1:]
commonLettersList = common(name, surname)
print("Common Letters in first name and last name: " + str(commonLettersList))

uniqueLettersTuple = all_unique(name, surname)
print("Unique characters in first name and last name: " + str(uniqueLettersTuple))

