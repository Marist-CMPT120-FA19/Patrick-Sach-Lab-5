def sentencestatistics ():
    words = input("Please enter a sentance: ").lower() #Input a sentence
    number = len(words) #Counts the length of the sentance
    print("The number of characters in your sentance is: ", number)
    count=len(words.split())#Splits the sentence and counts the words
    print("The number of words is: ", count)
    average= float(number/count) # divides the number of characters by the number of words
    print("The average word length is: ", average)
sentencestatistics()
