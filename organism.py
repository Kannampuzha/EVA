#An organism having the following functions
#This organism is expected to print True if stiumuli is 1 and Print False if stimuli is 0

#The organism can be defined in terms of the following
from random import randint , choice
#reading memory
from typing import Any, Generator
from time import time


memory=[]
with open("memory.mem", 'r') as memory1:
    string_memory = memory1.readline()
    exec(f"memory={string_memory}")
print("Memory :")
print(memory)




class Organism():
    def __init__(self):
        self.stimuli=None
        self.default_stimuli=None
        self.response=None
        self.default_response=None

        self.memory=memory#refer line 10

        self.session_memory=[]#The memory of the session
        self.functions=['print_on','print_off']
        self.actual_functions=[self.print_on,self.print_off]
        self.chosen_function=None


    def print_on(self):
        self.chosen_function='print_on'
        print('Result : True')
        self.response='True'

    def print_off(self):
        self.chosen_function='print_off'
        print('Result : False')
        self.response='False'


    #EPF code beings here . This has little to do with the organism.
    def PF(self):
        memory_chunk=[self.stimuli]
        #selecting a random function
        id_of_random_function=randint(0,(len(self.functions)-1))
        #putting function name in memory
        memory_chunk.append(self.functions[id_of_random_function])
        #executing the function
        self.actual_functions[id_of_random_function]()

        #putting response into memory chunk
        memory_chunk.append(self.response)

        #put memory chunk into session memory
        self.session_memory.append(memory_chunk)

        #Now select a random number 0 or 1 . If 0 , terminate PF , If 1 , invoke EPF
        recurse_or_terminate=randint(0,1)
        if recurse_or_terminate==0:


            #--------code to terminate EPF---------

            self.time_at_ending_epf = time()
            print("Time taken =", (self.time_at_ending_epf - self.time_at_session_beginning))

            print('Terminating EPF')
            # Put these things at each termination
            self.session_memory.append(self.response)
            print("Session :")
            print(self.session_memory)
            try:
                score = float(input("Enter Score :"))
                self.session_memory.append(score)
                self.memory.append(self.session_memory)
                # writing memory
                with open("memory.mem", 'w') as memory:
                    memory.write(f"{self.memory}")



                self.stimuli = self.default_stimuli
                self.response = self.default_response
                self.session_memory = []
                return ()
            except:
                self.stimuli = self.default_stimuli
                self.response = self.default_response
                self.session_memory = []
                return ()

        else:

            print("Evoking PF again")
            #Select a random number 0 or 1 . If 0  stimuli and response are unchanged . If 1 , stimuli will become response and response becomes None.
            #That means , if 0 , then further possible function will work on the same stimuli as before . If 1 , then
            #future function will work on a new stimuli , which was the response from this current function .
            #we are assuming this here.
            new_stimuli_or_old=randint(0,1)
            if new_stimuli_or_old == 1:
                self.stimuli = self.response
                self.response = None
            else:
                pass

            #evoking EPF again , recursing .
            self.PF()
            return()
    def non_PF(self):
        past_instances=[x for x in self.memory if x[0]==self.stimuli]

        #making its set , where everyon is unique
        past_instances_as_set= []
        past_instances_with_score=[]

        for x in past_instances:

            if x[:len(x) - 1] not in past_instances_as_set:
                past_instances_as_set.append(x[:len(x) - 1])
                past_instances_with_score.append([x[:len(x) - 1], x[-1]])
                # This would be [session , cumlulative_score]
            else:
                past_instances_with_score[past_instances_as_set.index(x[:len(x) - 1])][-1] += x[-1]


        #seleccing one with highest score
        difrence_threshold = 5  # cahnege this to increase diffrnece . It is an added bias to the alogoritm , roughly translating to "the good one should be atleast 3 scores ahead of all the other ones"

        self.selected_instance=None;self.selected_score=0
        multiple_instances_having_same_score = []
        for x in past_instances_with_score :
            if x[1]>self.selected_score:
                self.selected_instance=x[0]
                self.selected_score=x[1]


        #checking if the gap between chosen function and others is equal or greater than the diffence thershold.
        for x in past_instances_with_score:

            if x[0] != self.selected_instance and self.selected_score != 0:
                if self.selected_score - x[1] ==0 :
                    multiple_instances_having_same_score.append(x)
                    continue
                    #This means 2 or more sessions are equal . We can choose one randomly fromm them
                if self.selected_score - x[1] < 5:
                    self.selected_instance = None
                    self.selected_score = 0

                    # This means that the diffrence isnt large enough . So we evoke PF
            else :

                pass

        if self.selected_score == 0 :
            print("Difrence isnt significant . Evoking PF.")


        if len(multiple_instances_having_same_score)>0:
            multiple_instances_having_same_score.append(self.selected_instance)
            self.selected_instance=choice(multiple_instances_having_same_score)#choose one randomly among equal scoring functions




        print("Highest Scoring session : ",self.selected_instance)
        print("Score of highest Scoring function : ",self.selected_score)


        if self.selected_instance == None :
            print("Evoking PF")
            self.PF()
            return()

        else:
            print("Evaluating from Memory")

        # now we have to take each memory chunk from it and re-run them.


        selected_past_instace=self.selected_instance[1:(len(self.selected_instance)-1)]


        self.selected_score=0;self.selected_instance=None
        initial_stimuli = self.stimuli
        operations_to_be_performed = []
        for x in selected_past_instace:
            # if it is not self.stimuli , then that means here the further function worked on an older response
            # So we map this in operations_to_be_performed , to direct in afterwards to to work on self.response and not self.stimuli .

            if x[1] in self.functions:  # x[1] would be a function .
                operations_to_be_performed.append(x[1])
            elif x != self.stimuli:
                operations_to_be_performed.append(1)
            elif x == self.stimuli:
                operations_to_be_performed.append(0)

        # performing the operations as per the sequnece . Wherever its 1 , the stimuli is changed to the eariler response . Wherever it is 0 , stimuli is turned bak to the initial stimuli .
        for x in operations_to_be_performed:
            memory_chunk = [self.stimuli]
            if x != 1 and x != 0:
                memory_chunk.append(x)
                self.actual_functions[self.functions.index(x)]()
                memory_chunk.append(self.response)

                self.session_memory.append(memory_chunk)  # put memory chunk into session memory
            elif x == 1:
                self.stimuli = self.response
            elif x == 0:
                self.stimuli = initial_stimuli



        # --------code to terminate EPF---------


        self.time_at_ending_epf=time()
        print("Time taken =", (self.time_at_ending_epf - self.time_at_session_beginning))


        print('Terminating EPF')
        # Put these things at each termination
        self.session_memory.append(self.response)
        print("Session :")
        print(self.session_memory)
        try :
            score = float(input("Enter Score :"))
            self.session_memory.append(score)
            self.memory.append(self.session_memory)
            # writing memory
            with open("memory.mem", 'w') as memory:
                memory.write(f"{self.memory}")



            self.stimuli = self.default_stimuli
            self.response = self.default_response
            self.session_memory = []
            return ()
        except:
            self.stimuli = self.default_stimuli
            self.response = self.default_response
            self.session_memory = []
            return ()


    def EPF(self):#Evocation Processing Function
        print("Memory :", self.memory)
        #put initial stimuli into session memory
        self.time_at_session_beginning=time()
        self.session_memory.append(self.stimuli)

        if len(self.memory) !=0 :
            self.non_PF()#The first step is carried out in non_PF function . If you want you can write it here instread for clarity
        else :
            print('Evoking PF')
            self.PF()

    def initialise(self,argument_for_organism):
        #Actual initialisation of EPF . EPF is the carrier of all functions of the organism
        self.stimuli=argument_for_organism
        self.EPF()
        return(self.response)


on_off_printer=Organism()

for x in range(100):
    on_off_printer.initialise(1)
