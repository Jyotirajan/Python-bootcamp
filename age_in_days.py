from datetime import date

def calculate_age(born_date):
    today = date.today()
    
    # Check if born_date is in the future
    if born_date > today:
        return "Error: Birth date cannot be in the future."
    
    # Calculate age in days
    return (today - born_date).days

# Example usage:
born_date = date(1997, 9, 20)
age_in_days = calculate_age(born_date)

print(f"Age in Days: {age_in_days}")

