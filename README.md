# Evocative-Algorithm-Generator
A program working on memory to design an algorithm


"EVOCATION - The act of bringing or recalling a feeling, memory, or image to the conscious mind."


What is it?\n
It is an alogorithm that learns to make an algorithm , for some purpose. Here I identify a program as being 
synonymous to a biological organism having a set of well defined functions.It is very important to note that
every possible function of the organim is known , and defined in the program.
Any possible outcome that this organism will ever produce is thus clearly a manifestation of one or more functions
of this organism. No outcome is thus possible outside the domain of the organism .

Given a desired outcome from the organism on a given stimuli , how can the organism produce the outcome ? And why ?
The organism can no be thought to execute any random sequence of operations on the stimuli , and expected to give an outcome.
If the given outcome is favourable to the environemnt , the organism survives .
This can be furthur extended on the program . If it gives a correct outcome , it shall survive (regardless of the ways it produced the output)

Now , we shall assume that the organism is able to store its encounters in a memory.Thus , every action that it ever did for some kind of stimuli is being stored in memory.
It follows a simple principle "What happened so in past could possibily happen so in the future". So , in the future if it encounters a similar stimuli , 
the organism would react in the same way as it did in the past.This effectively creates the organism's purpose and thus the organism is able to program itself 
in order to get a human desired output.

One of the most important things to note here is that this algorithm consideres that all possible functions of the organism are known (That is an obvious case 
considering the nature of any natural organism ). This is thus inapplicable in circumstances where all the functions of the program are not known.
For example , A program that plays pool has all its functions known (keeping an angle , hittling , knowing the scores  ), there are no 'hidden' functions involved
but a program that plays chess does not have all its functions known (It has rather complex functions like , 'which piece is in danger' , 'why should/shouldnt i move this piece')
Although it might seem plausible that all the functions involved in it can be marked , it isn't as simple as knowing the functions of a pool player , the complexity actually much higher that what we readily see and complexity of the functions does certainly affect its deployment.
It is very necessary that all the possible funtions of the program are actually known with the obvious condition that the outcome expected is possible with the given set of functions. A program that only knows to scan documents cannot calculate the average number of pages .



This program is a very simple implementation of the algorithm above defined . 
It is an organism that :\n
Prints true if the stimuli is 1\n
Prints false if the stimuli is 0\n

You can also extend the very same code to a NOT gate without any changed to the code. All  you have to do is to erase the memory and re-train the algorithm .


Again , this is a very small and simple implentation of the concept , there is a major element missing in this example , "the way it tries to find similarity between given stimuli" .This hasn't been included due to the nature of this example . In a more realistic program , each stimuli will be defined not explictly , but by it's Type , Location of Stimulation and Size and so on. But in this case , the stimuli does not have a location , say 'Mouth' , it has no 'Size' either , it is more appropriate to make it work statically on direct instaces of stimuli rather than executing the functions in response to  identified , dynamic kind of stimuli that is 'similar' to a previous stimuli , based on these characteristics like 'Size' or 'Location' . An example based on this 'dynamic' stimuli is expected to come soon , in a more realistic example , one having a physical context . 

How to use it :
The program takes in a stimuli , and gives some output.
Based on whatever u like , give a score to the output it gave , say , 0 or 5 or 10 .

The scores are compared in memory everytime . Once a particular sequence of  functions is identifed to have a significantly larger score than all its counterparts , the program does not generate a random output , it will directly apply the same sequence of functions , and gives the output instantly.
Random Output making is done though 'PF' , 'Process Function'
The one based on memory is done through 'EPF' , Evocative Process Function'

You can choose to skip the score by pressing Enter. In this case , the session is not recorded in memory .



I know that the algorithm hasn't been explained well and so the code . If you are genuinely intrested to know how it works and what it does , feel free to mail me on
tejaskannampuzha@gmail.com and I will be more than happy to explain you everything in great detail . I will try my best to make a documentation soon , but there's no guarentee.
