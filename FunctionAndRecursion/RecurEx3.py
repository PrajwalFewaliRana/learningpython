movies=["bahubali",'khatta mitha',"baagwaan","phir hera feri","heraferi"]
#own method 
# def print_list(i):
#     if i== len(movies):
#         return
#     print(movies[i])
#     print_list(i+1)
# print_list(0)

#youtube method using list as a parameter too, more convenient too
def print_list(list,idx):
    if idx== len(list):
        return
    print(list[idx])
    print_list(list,idx+1)
print_list(movies,0)