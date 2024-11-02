phrase = input("What phrase do you want to see in reverse?")
for index in range(len(phrase) -1,-1,-1):
    print(phrase[index],end=" ")

print(f"\nPhrase:{phrase}")