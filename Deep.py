print("Sua resposta:")
reposta = input()

if reposta.casefold() == "42":
    print("Yes")
elif reposta.casefold() == "forty-two":
    print("Yes")
elif reposta.casefold() == "forty two":
    print("Yes")
else:
    print("No")