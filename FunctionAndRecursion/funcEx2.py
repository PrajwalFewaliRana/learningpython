#waf to print the elements of a list in a single line.(list in the parameter)
movies=["bahubali",'khatta mitha',"baagwaan","phir hera feri","heraferi"]
num =[1,2,3,4,5,6]

def print_list(list):
    for el in list:
        print(el,end=" ")
print_list(movies)
print_list(num)