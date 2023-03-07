# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1912792
# Date: 10.04.2022 

#modules
import sub.functions as fun
from sub.input_validation import input_validation as input_val

#set varaibles
replay='y'
star='*'
total_outcomes=0

progressList=[]
trailerList=[]
retrieverList=[]
excludedList=[]

#------------------Main Programe ---------------------------------
#calling func in module -- input validation
version_type=input_val([1,2],"Main Options:\n\t1.Student version\n\t2.Staff version")

if version_type==1:
    print("\n-- Student Version --\n")
    fun.progression_generator()

else:
    print("\n-- Staff Version --\n")
    #calling func in module -- input validation
    outputOption=input_val([1,2,3,4],"Staff Options\n\t1.Horizontal Histogram\n\t2.Vertical Histogram\n\t3.List/Tuple/Directory (extension) \n\t4.Text File\n")

    while replay=='y':
        progressList,trailerList,excludedList,retrieverList=fun.progression_generator()
        
        while True:
            replay=str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")).lower()
            if replay=="q" or replay=="y":
                break
            else:
                print("enter valid input")
                continue
        print()

    #------------------Histrogram----------------------
    progressCount=len(progressList)
    trailerCount=len(trailerList)
    retrieverCount=len(retrieverList)
    excludedCount=len(excludedList)

    print('-'*60)
    if outputOption==1:
        print("\nHorizontal Histogram\nProgress",progressCount,"\t:",progressCount*star,"\nTrailer",trailerCount,"\t:",trailerCount*star,"\nRetriever",retrieverCount,"\t:",retrieverCount*star,"\nExcluded",excludedCount,"\t:",excludedCount*star)
    elif outputOption==2:
        print("Progress\tTrailing\tRetriever\tExcluded")
        #https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
        
        for x in range(max(progressCount, trailerCount, retrieverCount, excludedCount)):
            print("{0}\t{1}\t{2}\t{3}".format(
                '*' if x < progressCount else ' ',
                '*' if x < trailerCount else ' ',
                '*' if x < retrieverCount else ' ',
                '*' if x < excludedCount else ' '
            ).expandtabs(16))

    elif outputOption==3:
        print(fun.output_text())
    else:
        text_file=open("output.txt","w")
        text_file.write(fun.output_text())
        text_file.close()
        print("Pls check the 'output.txt' file in the floder.")
    
    total_outcomes=progressCount+trailerCount+retrieverCount+excludedCount
    print("\n",total_outcomes,"outcomes in total.")
    print('-'*60)

print("\nThank you for using this program\nSee you again...")