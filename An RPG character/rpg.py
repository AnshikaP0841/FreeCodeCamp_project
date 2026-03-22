full_dot = '●'
empty_dot = '○'

def create_character(name, strength,intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"
    
    if " " in name:
        return "The character name should not contain spaces"
    
    # for i in range(0, len(name)-1):
    #     if name[i] == " ":
    #         return "The character name should not contain spaces"
    #     i += 1
    
    stats = (strength, intelligence, charisma)
    if not all(isinstance(x, int) for x in stats):
        return "All stats should be integers"
    
    if any(x < 1 for x in stats):
        return "All stats should be no less than 1"
    
    if any(x > 4 for x in stats):
        return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points" 
    
    return name + "\nSTR " + full_dot * strength + empty_dot * (10 - strength) + "\nINT " + full_dot * intelligence + empty_dot *(10 - intelligence) + "\nCHA " + full_dot * charisma + empty_dot * (10 - charisma)
