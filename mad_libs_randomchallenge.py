# Python Mad Libs Warm-Up Activity
    
# Welcome message
print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.")

#Import a story generator
import random

# Gather user inputs
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
name = input("Enter a name: ")
place = input("Enter a place: ")

if input() == "":
    adjective = "mysterious"
    noun = "object"
    adverb = "quietly"
    verb = "do something"
    name = "Blank"
    place = "outer space"

# Build the story using an f-string
story_1 = (f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}. I asked the {noun} for their name. The {noun} said their name was {name}. {name} told me that they are from {place}. I have a new friend named {name}!")

story_2 = (f"There was a {adjective} {noun} named {name}. {name} lived in {place} for a long time. {name} likes to {adverb} {verb} as a hobby. Say hello to {name}!")

story_3 = (f"Hello, my name is {name}, and I am from {place}! Many people say that I'm a {adjective} {noun} who likes to {adverb} {verb}. Nice to meet you!")

stories = [story_1, story_2, story_3]

#Print a random story from the story generator
print(random.choice(stories)) 