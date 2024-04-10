# quickpoll
QuickPoll is a web application that allows users to create, participate in, and view the results of polls. Users can sign up, log in, and log out to access the full functionality of the application. Admin users have access to an admin interface to manage polls and user accounts.

# Installation
To run QuickPoll locally, follow these steps:

# Clone the repository:
git clone https://github.com/shivampandey811/quickpoll.git
Navigate into the project directory:

cd quickpoll
# Install dependencies using pip:

bash
Copy code
pip install -r requirements.txt fcor this project only run `pip3 install django`

# Set up the database:
python manage.py migrate
Create a superuser (admin user):

python manage.py createsuperuser

# Start the development server:
python manage.py runserver
Open your web browser and navigate to http://localhost:8000 to access QuickPoll.

# Features
User Authentication
Users can sign up, log in, and log out.
Only authenticated users can create, view, and participate in polls.
# Poll Creation
Authenticated users can create new polls.
Each poll has a question and multiple choices.
Poll creators can set a deadline for the poll (optional).
# Poll Listing
All users can view a list of available polls.
Polls display their question, choices, and deadline (if set).
# Poll Participation
Authenticated users can select a choice and submit their vote for a poll.
Users cannot vote on a poll after its deadline (if set).
# Results Display
After voting, users can view the results of the poll, including the percentage of votes for each choice.
