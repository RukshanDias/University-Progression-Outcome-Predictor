# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1912792
# Date: 10.04.2022 

progressList=[]
trailerList=[]
excludedList=[]
retrieverList=[]

def input_credits(type):
    creditsRange=list(range(0,121,20))
    while True:
        try:
            credit=int(input("Please enter your credits at "+type+' :'))
            if credit not in creditsRange:
                print("Out of range")
                continue
            else:
                break
        except ValueError:
            print("Integer Required")
            continue
    return credit


def progression_generator():
    while True:
        passCredit=input_credits(type="pass")
        deferCredit=input_credits(type="defer")
        failCredit=input_credits(type="fail")

        if passCredit+deferCredit+failCredit != 120:
            print("Total incorrect")
            continue
        else:
            break

    global retrieverList,trailerList,progressList,excludedList

    if passCredit==120:
        progressList.append((passCredit,deferCredit,failCredit))
        print("Progress\n")
    elif passCredit==100:
        trailerList.append((passCredit,deferCredit,failCredit))
        print("Progress (module trailer)\n")
    elif failCredit>=80:
        excludedList.append((passCredit,deferCredit,failCredit))
        print("Exclude\n")
    else:
        retrieverList.append((passCredit,deferCredit,failCredit))
        print("Module retriever\n")

    return progressList,trailerList,excludedList,retrieverList


def list_to_str(list):
    "Convert list into str to print list without brackets"
    output_list=','.join(str(e) for e in list)
    return output_list

def output_text():
    "Printing Progression Outcome with data"
    output_text=f"Progress - {list_to_str(progressList)}\nTrailing - {list_to_str(trailerList)}\nRetriever - {list_to_str(retrieverList)}\nExcluded - {list_to_str(excludedList)}"
    return output_text