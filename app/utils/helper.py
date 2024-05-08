# Example utility function
def calculate_age(birth_year):
    current_year = 2024  # Replace with actual current year
    age = current_year - birth_year
    return age

def get_user_status(age):
    if age < 5:
        return "Toddler"
    elif age < 18:
        return "Student"
    else:
        return "Adult"