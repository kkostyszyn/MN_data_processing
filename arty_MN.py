import re
import sys
from partic import Participant

def clean(file_name):
	#Open file in filepath 
    f = open(file_name)
    f = f.readlines()
        
    line = f[0]
    x = re.split(r",|\n", line)
    #print("LINE:", line)
    #print("SPLIT:", x)
    
    #In first line - find necessary columns, save their positions  
    col_partic = '' #M
    col_react_time = '' #AK
    col_condition = '' #BB 
    col_filter = '' #AN
    col_correct = '' #AP
    
    for i in range(len(x)):
        if x[i] == "Participant Private ID":
            col_partic = i 
        elif x[i] == "Reaction Time":
            col_react_time = i
        elif x[i] == "condition":
            col_condition = i 
        elif x[i] == "Response":
            col_filter = i 
        elif x[i] == "Correct":
            col_correct = i 
    
    #populate list of reaction times, etc., based on 'filter' column
    p_list = {}
    partic = ''
    
    for l in f[1:]:
    #generate dictionary of participants
        x = re.split(r",", l)
        if len(x) > 1:
        
            if not partic:
                partic = x[col_partic]
                p_list[partic] = Participant(partic)
            elif partic != x[col_partic]:
                print("Participant: ", partic)
            if x[col_filter] in ['word', 'nonword']:
                p_list[partic].update(x[col_react_time], 
                                        x[col_condition],
                                        x[col_correct])
                                        
    for i in p_list:
        #Write all values for participant 
        print("Opening values for", p_list[i].p())
        p_list[i].write_all("processed_data/" +p_list[i].p()+"_values.csv")
        #new_file.write(partic + "\t" + temp + "\t" + react_time[i] +"\t"+ correct[i] +"\n")
        #new_file.close()
        print("Closing values for", p_list[i].p())

        
        rep, sim, wrd = p_list[i].aggregate()

        #Write sums for participant
        print("Opening means for", p_list[i].p())
        sum = open("processed_data/" +p_list[i].p()+"_means.txt", "w+")
        sum.write(partic + "\trepPSW\t"
                + str(round((rep[0] / rep[1]))) + "\n")
        sum.write(partic + "\tsimPSW\t" 
                + str(round((sim[0] / sim[1]))) + "\n")
        sum.write(partic + "\tsimWRD\t" 
                + str(round((sim[0] / sim[1]))))
        round((rep[0] / rep[1]))
        sum.close()
        print("Closing means for", p_list[i].p())
        
        
        #Write averages for participant 
        print("Opening accuracy for", p_list[i].p())
        acc = open("processed_data/" +p_list[i].p()+"_acc.txt", "w+")
        acc.write(partic + "\trepPSW\t"
                + str(round((rep[2] / rep[3]) * 100)) + "\n")
        acc.write(partic + "\tsimPSW\t" 
                + str(round((sim[2] / sim[3]) * 100)) + "\n")
        acc.write(partic + "\tsimWRD\t" 
                + str(round((sim[2] / sim[3]) * 100)))
                
        round((rep[2] / rep[3]))
        acc.close()
        print("Closing accuracy for", p_list[i].p())

        
        
        
    #Open new file, add values to new file 


    """
    for i in range(len(react_time)):
        temp = condition[i].strip("\n")
        new_file.write(partic + "\t" + temp + "\t" + react_time[i] +"\t"+ correct[i] +"\n")
        
        #Aggregation
        if correct[i] == '1':
            if temp == 'repPSW':
                repPSW_mean += float(react_time[i])
                repPSW_count+=1
                repPSW_acc_count+=1
                if correct[i] == '1':
                    repPSW_correct +=1
            elif temp == 'simPSW':
                simPSW_mean += float(react_time[i])
                simPSW_count+=1
                simPSW_acc_count+=1
                if correct[i] == '1':
                    simPSW_correct +=1
            elif temp == 'simWRD':
                simWRD_mean += float(react_time[i])
                simWRD_count+=1
                simWRD_acc_count+=1
                if correct[i] == '1':
                    simWRD_correct +=1
                    
        else:
            if temp == 'repPSW':
                repPSW_acc_count+=1
            elif temp == 'simPSW':
                simPSW_acc_count+=1
            elif temp == 'simWRD':
                simWRD_acc_count+=1
    """  
     
    
    

    
    
def round(x):
    """
    One function purely for rounding our reaction times.
    """
    y = int(x)
    
    dec = x - y

    if dec - .5 > 0:
        #round up
        y+=1
    print("Rounding " + str(x) + " to " + str(y))
    return y


if __name__ == "__main__":

	print("Number:", len(sys.argv))
	print("Args:", str(sys.argv))
	
	
	clean(sys.argv[1])