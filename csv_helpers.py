

def find_session(time_open):
    if time_open.strip()[:2] == "22":
        session_entry = "Sydney"
    elif int(time_open.strip()[:2]) >= 23 or int(time_open.strip()[:2]) <= 7:
        session_entry = "Asia"
    elif int(time_open.strip()[:2]) >= 8 and int(time_open.strip()[:2]) <= 12:
        session_entry = "New York"
    elif int(time_open.strip()[:2]) >= 18 and int(time_open.strip()[:2]) <= 22:
        session_entry = "London" 
    elif int(time_open.strip()[:2]) >= 13 and int(time_open.strip()[:2]) <= 17:
        session_entry = "Crossover" 
    return session_entry