one_dic = {'color':'green','points':5}
two_dic = {'color':'yellow','points':10}

number = [one_dic,two_dic]

###########################################
for i in number:
    for key,value in i.items():
        print("KEY: ",key,"\t","Value :",value)