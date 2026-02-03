temperature=int(input("whatis temperature? "))
if temperature > 85:
    print("wear something light")
else:
    print("A jacket might be a good idea")
    if temperature > 50:
        print("Heavy jacket")
    elif 50<= temperature <=70:
        print("Wear heavy jacket")
    elif 70 <= temperature <=85:
        print("T-shirt weather")


