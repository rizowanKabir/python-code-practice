def weekly(n):

    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 2: return "Wednesday"
        case 3: return "Thursday"
        case 4: return "Friday"
        case 5: return "saturday"
        case 6: return "Sunday"
        case _: return "Invalid Day"
print(weekly(2))  
print(weekly(7))      

