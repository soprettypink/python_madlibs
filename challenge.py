# Python Mad Libs Warm-Up Activity
    
# Welcome message
print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.")

# Gather user inputs
adjective_1 = input("Enter an adjective: ")
noun_1 = input("Enter a noun: ")
verb_1 = input("Enter a verb: ")
adverb_1 = input("Enter an adverb: ")
name_1 = input("Enter a name: ")
place_1 = input("Enter a place: ")
adjective_2 = input("Enter an adjective: ")
noun_2 = input("Enter a noun: ")
verb_2 = input("Enter a verb: ")
adverb_2 = input("Enter an adverb: ")
name_2 = input("Enter a name: ")
place_2 = input("Enter a place: ")

# Build the story
story = (f"Once upon a time, there was 
         a {adjective_1} {noun_1} named 
         {name_1}. {name_1} lived in {place_1}. 
         One day, {name_1} went out for a walk. 
         The sun was shining bright, so {name_1} 
         went back home to {adverb_1} {verb_1}. 
         'I wish I had a friend.', 
         said {name_1}. {name_1} was really sad. 
         The next day, {name_1} went out for a walk 
         once again. The weather wasn't as hot as the 
         day before. Suddenly, {name_1} saw a 
         {adjective_2} {noun_2}. {name_1} said, 
         'Hello! My name is {name_1}! What is your name?' 
         The {adjective_2} {noun_2} responded, 
         'My name is {name_2}. I am from {place_2}. '
         'Nice to meet you!'. {name_1} and {name_2} 
         became good friends.")

# Display the completed story
print("Here is your story: ")
print(story)