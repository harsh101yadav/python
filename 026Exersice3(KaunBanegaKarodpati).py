#Create a program capable of displaying questions to the user like KBC. 
#Use List data type to store the questions and their correct answers. 
#Display the final amount the person is taking home after playing the game.

questions = ("Which city is known as Pink City in India?",
             "Who wrote India's National Anthem?",
             "How many states are there in India",
             "Which of the following is not a state of India?",
             "The language of Lakshadweep. a Union Territory of India, is",
             "Current Railway Minister of India is",
             "Which one of these countries was created first?",
             "What is the capital of Bhutan?",
             "Who discovered penicillin?",
             "Who is credited with the invention of the World Wide Web?",
             "Who painted 'The Scream'?",
             "Which scientist formulated the laws of motion and universal gravitation?",
             "Who discovered radium and polonium?",
             "What is the most abundant element in the universe?",
             "Which country has the longest coastline in the world?",
             "What is the rarest blood type?",
             "Which African country was formerly known as Abyssinia?")
options = ("Banglore","Maysore","Jaipur","Noida",
           "Rabindranath Tagore","Lal Bahadur Shastri","Lal Bahadur Shastri","Ayush Taunk",
           "29","30","28","31",
           "Vrindachal","Goa","Jharkhand","Chattisgarh",
           "Tamil","Hindi","Malayalam","Telugu",
           "Mamta Banarjee","Ram Vilash","Piyush Goyal","Ashwini Vaishnaw",
           "India","San Marino","Italy","England",
           "Kathmandu","Thimphu","Ulaanbaatar","Dushanbe",
           "Robert Koch","Marie Curie","Alexander Fleming","Louis Pasteur",
           "Shubham Bankar","Bill Gates","Tim Berners-Lee","Larry Page",
           "Pablo Picasso","Claude Monet","Vincent van Gogh","Edvard Munch",
           "Isaac Newton", "Galileo Galilei", "Albert Einstein", "Johannes Kepler",
           "Niels Bohr", "Albert Einstein", "Isaac Newton", "Marie Curie",
           "Hydrogen", "Oxygen", "Carbon", "Helium",
          "Australia", "Russia", "Norway", "Canada",
           "A-positive","B-negative","AB-negative","O-positive",
           "Ethiopia", "Kenya", "Tanzania", "Uganda")
answers = ("c","a","c","a","c","d","b","b","c","c","d","a","d","a","d","c","a")
Wamt = (0,1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000)
milestone =(0,10000,320000,7500000)


print("Welcome to KBC")
for i in range(len(questions)):
    print(f"Q{i+1}",questions[i])
    # for j in len(options):
    print(options[4*i:(4*i+4)])
    x = input("Choose a,b,c,d: ")
    if(x == answers[i]):
        print(" Correct!!!!! You won", Wamt[i+1])
    else:
        print("Wrong answer, The game ends here.Your winnig amount is", Wamt[i])
        break

print("Thanks for playing")