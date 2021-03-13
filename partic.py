class Participant:
    """
    Participant class, storing participant ID number, and ordered lists of reaction times, trial conditions, and correct value for M&N experiment.
    """
    partic = 0
    
    react_time = []
    condition = []
    correct = []
    
    def __init__(self, partic):
        self.partic = partic
        
    def __str__(self):
    
        return self.partic + "\n" + str(self.react_time) + "\n" + str(self.condition) +"\n" + str(self.correct)
        
    def p(self):
        """
        Shortcut for returning participant ID as string.
        """
        return(str(self.partic))
        
    def update(self, react, cond, correct):
        """
        Add new trial info to list of values.
        """
        self.react_time.append(react)
        self.condition.append(cond)
        self.correct.append(correct) 
        
    def write_all(self, path):
        """
        Write all values to list, given a file path.
        """
        new_file = open(path, "w+")
        
        
        for i in range(len(self.react_time)):
            #print("Writing value line.")
            temp = self.condition[i].strip("\n")
            new_file.write(self.partic + "\t" + temp + "\t" + self.react_time[i] +"\t"+ self.correct[i] +"\n")
        
        new_file.close()
    
    def aggregate(self):
        """
        Based on listed values, define mean and accuracy for each condition.
        """
        #Define all mean values needed for aggregation
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
        
        
        for i in range(len(self.react_time)):
            temp = self.condition[i].strip("\n")
            #new_file.write(partic + "\t" + temp + "\t" + react_time[i] +"\t"+ correct[i] +"\n")
        
            #Aggregation
            if self.correct[i] == '1':
                if temp == 'repPSW':
                    repPSW_mean += float(self.react_time[i])
                    repPSW_count+=1
                    repPSW_acc_count+=1
                    if self.correct[i] == '1':
                        repPSW_correct +=1
                elif temp == 'simPSW':
                    simPSW_mean += float(self.react_time[i])
                    simPSW_count+=1
                    simPSW_acc_count+=1
                    if self.correct[i] == '1':
                        simPSW_correct +=1
                elif temp == 'simWRD':
                    simWRD_mean += float(self.react_time[i])
                    simWRD_count+=1
                    simWRD_acc_count+=1
                    if self.correct[i] == '1':
                        simWRD_correct +=1
                    
            else:
                if temp == 'repPSW':
                    repPSW_acc_count+=1
                elif temp == 'simPSW':
                    simPSW_acc_count+=1
                elif temp == 'simWRD':
                    simWRD_acc_count+=1
        
        rep_tuple = [repPSW_mean, repPSW_count, repPSW_correct, repPSW_acc_count]
        sim_tuple = [simPSW_mean, simPSW_count, simPSW_correct, simPSW_acc_count]
        wrd_tuple = [simWRD_mean, simWRD_count, simWRD_correct, simWRD_acc_count]
        
        return (rep_tuple, sim_tuple, wrd_tuple)
        
        