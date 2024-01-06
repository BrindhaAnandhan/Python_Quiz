#quiz game

Quiz = {
    'question1':{
    "question": 'What is the maximum length of a Python identifier?',
    "answer": "No fixed len"
},
'question2':{
    "question":"PVM stands for?",
    "answer": "Python visual Machine"
},
"question03":{
    "question":"Tuple is a mutable or immutable?",
    "answer": "immutable"
},
"question04":{
    "question":"string is a mutable or immutable?",
    "answer": "immutable"
},
"question05":{
    "question":"list is a mutable or immutable?",
    "answer": "mutable"
},
"question06":{
    "question":"list is a mutable or immutable?",
    "answer": "mutable"
},
"question07":{
    "question":"Dict is a mutable or immutable?",
    "answer": "Both"
},
}
score= 0
for key,value in Quiz.items():
    print(value["question"])
    answer= input("Answer: ")
    if answer.lower() == value['answer'].lower():
        print("Correct ")
        print("")
        score+=1
        print('Your score is:' + str(score))
        print(" ")
    else:
        print("Wrong")
        print("Correct answer is:" + value['answer'])
        print('your score is:' + str(score))
        print("")
print("You got " + str(score)+ " out of 7 ")
if score==7:
    print("Wow!!! Your percentage " + str(int(score / 7 * 100)) + "%")
else:
    print( "Your percentage " + str(int(score/7 *100))+ "%")
