# reading the story from the text file
with open("story.txt","r") as file:
    story =file.read()

# declaring words set
words =set()

start_of_the_word =-1

target_start ='<'
target_end ='>'

# identifying the workds to be replaced
for i,char in enumerate(story):
    if char == target_start:
        start_of_the_word = i
    
    if char == target_end:
        end_of_the_word = i+1
        words.add(story[start_of_the_word:end_of_the_word])

dict_words={}

# taking input from user to replace words and storing them in dictionary
for word in words:
    answer = input("Enter a word to replace "+ word +": ")
    dict_words[word]=answer

#replacing words
for word in words:
    story = story.replace(word,dict_words[word])

print()
print(story)

    

