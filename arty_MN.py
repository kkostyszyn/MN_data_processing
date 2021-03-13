import re
import sys

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
    
    partic = ''
    react_time = []
    condition=[]
    correct = []
    
    for l in f[1:]:
    
            
        x = re.split(r",", l)
        if len(x) > 1:
        
            if not partic:
                partic = x[col_partic]
                print("Participant: ", partic)
            if x[col_filter] in ['word', 'nonword']:
                react_time.append(x[col_react_time])
                condition.append(x[col_condition])
                correct.append(x[col_correct])
                #add_to_list(react_time, condition, correct, x)
        
    #print("Reaction times: ", react_time)
    
    #Open new file, add values to new file 
    new_file = open("processed_data/" +partic+"_values.csv", "w+")
    
    #(Save time by aggregating means at the same time)
    repPSW_mean = 0
    repPSW_count = 0
    repPSW_correct = 0
    repPSW_acc_count = 0
    
    simPSW_mean = 0
    simPSW_count = 0
    simPSW_correct = 0
    simPSW_acc_count = 0


    simWRD_mean = 0
    simWRD_count = 0
    simWRD_correct = 0
    simWRD_acc_count = 0



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
            
    new_file.close()
    
    #print("Accuracy:" + str(simPSW_correct) + " " + str(repPSW_correct) + " " + str(simWRD_correct) + " " )
    #print("Total:" + str(simPSW_acc_count) + " " + str(repPSW_acc_count) + " " + str(simWRD_acc_count) + " " )
    
    
    #write averages to file 
    sum = open("processed_data/" +partic+"_means.txt", "w+")
    #sum.write("ID, repPSW, simPSW, simWRD\n")
    sum.write(partic + "\trepPSW\t"
                + str(round((repPSW_mean / repPSW_count))) + "\n")
    sum.write(partic + "\tsimPSW\t" 
                + str(round((simPSW_mean / simPSW_count))) + "\n")
    sum.write(partic + "\tsimWRD\t" 
                + str(round((simWRD_mean / simWRD_count))))
                
    round((repPSW_mean / repPSW_count))
    sum.close()
    
    #once more for accuracy
    
    acc = open("processed_data/" +partic+"_acc.txt", "w+")
    #sum.write("ID, repPSW, simPSW, simWRD\n")
    acc.write(partic + "\trepPSW\t"
                + str(round((repPSW_correct / repPSW_acc_count) * 100)) + "\n")
    acc.write(partic + "\tsimPSW\t" 
                + str(round((simPSW_correct / simPSW_acc_count) * 100)) + "\n")
    acc.write(partic + "\tsimWRD\t" 
                + str(round((simWRD_correct / simWRD_acc_count) * 100)))
                
    round((repPSW_mean / repPSW_count))
    acc.close()
    
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