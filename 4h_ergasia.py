#4h ergasia
print("Dwste arithmous sthn idia seira xwrismenous me keno p.x.1 2 3 4 5 6");
s = raw_input();
List = map(int, s.split());
print("Entered List: " + str(List));
List.sort();
print("Sorted List: " + str(List));
#H lista xwris tis 2 megaliteres kai 2 mikroteres times
List = List[2:len(List)-2]
print ("H lista xwris tis 2 megaliteres kai 2 mikroteres times einai: " + str(List));
average = sum(List)/len(List)
print("O mesos oros twn timwn einai: " + str(average))
for i in range(len(List)):
    List[i] = (List[i]-average)**2;
variance = sum(List)/(len(List)-1);	
print("H diafora einai: " + str(variance));
standardDeviation = variance**0.5;
print("H typiki apoklisi einai: " + str(standardDeviation));