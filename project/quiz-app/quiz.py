question = [["1. What is the largest planet of the solar system","a. Sun","b. Earth"],["2. what is full form of IP","a. Internet Protocol","b.  Inter Protocol"]]
answers = ["a","b"]



def quizRender(arr):
    score = 0
    for i in range(len(arr)):
        print(str(arr[i]),end="")
        ans = input("Enter you answer: ")
        if(ans==answers[i]):
            score += 1
    print(score)

quizRender(question)            




