text = []
with open("Challenge#01/message_01.txt", "r") as file:
    f = list(file)
    for word in f:
        word = word.lower()
        text += word.split(" ")

result = []
response = ""
for word in text:
    if word not in result:
        result.append(word)
        response += word
        response += str(text.count(word))
print(response)
