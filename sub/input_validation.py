# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1912792
# Date: 10.04.2022 

def input_validation(condition,message):
    while True:
        try:
            print(message)
            user_input=int(input("\nSelect a number:"))
            if user_input in condition:
                break
            else:
                print("\nEnter a valid number..")
                continue
        except ValueError:
            print("\nEnter a number not a letter..")
            continue
    return user_input