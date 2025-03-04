import random

def get_names():
    """Get a list of names from the user."""
    names = input("Enter names separated by commas: ")
    return [name.strip() for name in names.split(',')]

def get_questions():
    """Get a dictionary of questions from predefined scenarios."""
    questions = {
        "Financial Decision-Making": "You are 25 years old and have just started earning a stable income. You want to buy a car but don’t have enough savings. The bank offers you a loan with high interest rates. Do you take the loan and buy the car now, or wait until you save enough money? Why?",
        "Conflict Resolution": "A close friend borrows money from you but hasn’t repaid it after months. You need the money back but don’t want to damage your friendship. How would you approach this situation? What would you say to your friend?",
        "Time Management": "You have an important exam tomorrow but also promised to help a friend move into their new apartment today. How do you manage your time? Do you prioritize studying or helping your friend?",
        "Health and Wellness": "You’ve been feeling stressed due to work and haven’t exercised in months. Your doctor advises regular exercise for better health. How would you incorporate exercise into your busy schedule? What changes would you make?",
        "Ethical Dilemma": "You witness someone shoplifting at a store. The person looks like they are struggling financially. Do you report them to the store manager or let it go? Why?",
        "Career Choices": "You are offered two job opportunities—one with a high salary but long hours, and another with lower pay but better work-life balance. Which job would you choose and why?",
        "Unforeseen Events": "A natural disaster damages your home, and your insurance only covers part of the repair costs. What steps would you take to recover financially? How would you prepare for similar events in the future?",
        "Personal Growth": "You realize you have a habit that is holding you back from achieving your goals (e.g., procrastination). How would you identify and change this habit? What strategies would you use?",
        "Social Responsibility": "You notice a social issue in your community that needs attention (e.g., lack of recycling facilities). How would you address this issue? What actions would you take?",
        "Relationship Building": "You are new to a city and want to make friends but are shy about approaching people. How would you go about meeting new people and forming friendships?",
        "Goal Setting": "You want to achieve a long-term goal (e.g., running a marathon) but have never trained for such an event. How would you set up a plan to achieve this goal? What steps would you take?",
        "Resilience": "You face a series of setbacks in your personal or professional life (e.g., job loss, health issues). How would you cope with these challenges? What strategies would you use to stay positive?",
        "Environmental Awareness": "You realize that your daily habits are contributing to environmental issues (e.g., using single-use plastics). How would you change your habits to live more sustainably? What impact do you hope to make?",
        "Mentorship": "You are given the opportunity to mentor someone who is just starting in your field. How would you approach this role? What advice would you give?",
        "Cultural Exchange": "You are invited to spend a month in a foreign country with a host family. How would you prepare for this experience? What do you hope to learn or achieve?",
        "Self-Reflection": "You realize that you have been focusing on external validation rather than internal happiness. How would you shift your focus to prioritize self-satisfaction? What changes would you make?",
        "Teamwork": "You are part of a team working on a project, but one member is not contributing equally. How would you address this issue without damaging team morale?",
        "Risk-Taking": "You have the opportunity to start your own business but are afraid of failure. How would you weigh the risks and benefits? What steps would you take to mitigate risks?",
        "Forgiveness": "Someone has wronged you in the past, and you are struggling to forgive them. How would you approach forgiveness? What steps would you take to heal and move forward?",
        "Legacy": "You are asked to think about what you want your legacy to be after you are gone. What kind of impact do you hope to leave on the world? How would you start working towards that goal?"
    }
    
    return questions

def match_name_with_question(names, questions):
    """Randomly match a name with a question."""
    name = random.choice(names)
    heading, question = random.choice(list(questions.items()))
    
    return name, heading, question

def main():
    names = get_names()
    questions = get_questions()
    
    while True:
        name, heading, question = match_name_with_question(names, questions)
        
        print(f"\n**Name:** {name}")
        print(f"**Heading:** {heading}")
        print(f"**Question:** {question}\n")
        
        input("Press Enter to continue...")
        
        choice = input("Do you want to quit? (yes/no): ")
        if choice.lower() == "yes":
            break

if __name__ == "__main__":
    main()
