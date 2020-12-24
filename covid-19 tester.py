import time
name = input("Enter your name: ")
country = input("Enter your country: ")

print(f"Welcome {name.capitalize()}!")
time.sleep(1)
print("You have to enter all the fields without leaving blank: ")

Q1 = input("Did you travel to anywhere outside your country")

if Q1.upper() ==  "YES":
    yes = True
    print("Stay in quarantine!")
elif Q1.upper() == 'NO':
    yes = False
    print("Stay home, stay safe")

Q2 = input("Were you in a close proximity of a person who tested +ve for covid 19?")
if Q2.lower() == "yes":
    print("Stay in quarantine!")
elif Q2.lower() == "no":
    print("Stay home, stay safe")

symptoms = input("""Which of these symptoms do you have? :
Fever
Dry cough
All of the symptoms of Covid 19
None of these""").lower()

if symptoms == "fever":
    print("Seek medical attention!")

elif symptoms == "dry cough":
    print("You should stay home as more symptoms may appear")

elif symptoms == "all of these" or "all of the symptoms of covid 19":
    print("Seek medical attention!")

elif symptoms == "None of these":
    print("Stay home")

else:
    print("Enter a proper value!")

result = "By taking the test, you oblige to the instructions given"
print(result)

time.sleep(1)

print(f"Bye, {name}")
