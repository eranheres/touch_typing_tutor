## main.py
from user import User
from session import Session
from statistics import Statistics
from database import Database

def main():
    # Create a database object
    db = Database()

    # Create a user
    username = input("Enter your username: ")
    language = input("Enter your language (English/Hebrew): ")
    user = User(username, language, db)

    # Load the user's progress
    user.load_progress()

    # Create a typing session
    session = Session(user, db)

    # Generate text for the session
    session.generate_text()

    # Get user input
    session.get_input()

    # End the session
    session.end_session()

    # Create a statistics object
    statistics = Statistics(user, db)

    # Collect data from the session
    statistics.collect_data(session)

    # Display the data
    statistics.display_data()

if __name__ == "__main__":
    main()
