#prompt the user to enter the text
text1 = input("Please Enter your text : ")
#counts the total number of words in the text
total = 1

#for loop to iterate through each character in the text, and checks if there is a space
#if there is a space, the number of words is incremented
for i in range(len(text1)):
    if(text1[i] == ' ' or text1 == '\n' or text1 == '\t'):
        total = total + 1

print("Total Number of Words in this text = ", total)