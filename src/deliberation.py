import pyfiglet

print(pyfiglet.figlet_format("Deliberation"))

print("\nRepeating cycle of")

while True:
    print("love")
    print("no love")

    if input("Press Enter to continue or type 'stop' to end: ").lower() == "stop": 
        break
    print("I learn the words I didn't know before")