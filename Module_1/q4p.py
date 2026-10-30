def analyze_attendance(workshops):

    count={}


    for workshop in workshops:
        for student in  workshop:
            count[student]=count.get(student,0) + 1


    unique=len(count) 

    C_attendees=[]        
    
    for student in count:
        if count[student] == len(workshop):
            C_attendees.append(student)
    
    E_attendace=[]        

    for student in count:
        if count[student]== 1:
            E_attendace.append(student)

    R_attendees=[]

    for student in count:
        if count[student] >=2:
            R_attendees.append(student)
    
    Etwo_attendees=[]        

    for student in count:
        if count[student] == 2:
            Etwo_attendees.append(student)

    max_overlap=-1
    best_pair=None


    for i in range(len(workshops)):
        for j in range(i+1,len(workshops)):
            overlap=len(set(workshops[i]) & set(workshops[j]))
            if overlap > max_overlap:
                max_overlap=overlap
                best_pair=(i+1,j+1)

    if best_pair is  None:
        max_overlap=0

    return {
                "Unique attendees": unique,
                "Common attendees": C_attendees,
                "Exclusive attendees": E_attendace,
                "Repeat attendees": R_attendees,
                "Exactly-two attendees": Etwo_attendees,
                "Maximum overlap": (best_pair, max_overlap)
            }
        
        
workshops = [
            [101, 102, 103, 104],
            [102, 103, 105],
            [102, 103, 106]
        ]
        
result = analyze_attendance(workshops)
        
for key, value in result.items():
            print(key, ":", value)          