import random

# Lists of adjectives and nouns
adjectives = ["Happy", "Sunny", "Clever", "Brave", "Gentle", 
              "Wild", "Calm", "Eager", "Fierce", "Jolly"]

nouns = ["Tiger", "Dragon", "Bear", "Eagle", "Wolf", 
         "Phoenix", "Lion", "Owl", "Shark", "Fox"]

special_chars = ["!", "@", "#", "$", "%", "&", "*"]

def generate_basic_username():
    """Generate a basic username from random adjective + noun"""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return adjective + noun

def add_numbers(username, max_digits=3):
    """Add random numbers to username (0-999 by default)"""
    num = random.randint(0, 10**max_digits - 1)
    return username + str(num)

def add_special_char(username):
    """Add a random special character to username"""
    char = random.choice(special_chars)
    return username + char

def adjust_length(username, max_length):
    """Trim username if it exceeds max length"""
    if len(username) > max_length:
        return username[:max_length]
    return username

def get_user_choices():
    """Get user preferences for username generation"""
    print("Welcome to the Random Username Generator!")
    
    # Ask for options
    add_num = input("Add numbers? (y/n): ").lower() == 'y'
    add_special = input("Add special characters? (y/n): ").lower() == 'y'
    max_length = int(input("Max username length (e.g., 12): ") or 20)  # Default: 20
    
    return add_num, add_special, max_length

def save_username(username):
    """Save username to text file"""
    with open("usernames.txt", "a") as f:
        f.write(username + "\n")
    print(f"✅ Saved '{username}' to usernames.txt")

def main():
    """Main program function"""
    # Get user choices
    add_num, add_special, max_length = get_user_choices()
    
    # Generate base username
    username = generate_basic_username()
    
    # Add extras if selected
    if add_num:
        username = add_numbers(username)
    if add_special:
        username = add_special_char(username)
    
    # Ensure it fits length limit
    username = adjust_length(username, max_length)
    
    # Show & save
    print(f"\n✨ Your username: {username}")
    if input("Save it? (y/n): ").lower() == 'y':
        save_username(username)

if __name__ == "__main__":
    main()