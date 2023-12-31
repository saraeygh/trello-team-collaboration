# Trello - Collaborative project management with your team

A Trello-like collaborative project management web app; **Daneshkar** *Python/Django* bootcamp final project.

***

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Models Designed Based On Below ERD](#models-designed-based-on-below-erd)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
- [License](#license)
- [Contact](#contact)

## Introduction

In this app you can easily manage your project tasks with your team. You and all your team members should register their accounts. Then you can create a new team (a.k.a *Workspace*) and add your team members. You can define multiple projects (a.k.a *Projects*) for each workspace or team. Then you start to define project tasks and assign tasks to members. Each task has name, description, start date, end date, due date, status (include *To-DO*, *Doing*, *Done* and *suspend*) and a label. You can define as many labels as you want and allocate tasks to these labels.

## Features

- Projects: Create projects to represent different projects or teams. Each projects can have multiple lists.
- Lists: Organize tasks using lists. Customize list names to fit your workflow (e.g., "To Do," "In Progress," "Done").
- Labels: Categorize task with customizable labels, such as priority levels or task types.
- Comments and Attachments: Collaborate on cards by adding comments and attaching files.
- Search and Filter: Quickly find cards using search and filter options.
- User Accounts: Create user accounts to manage personal boards and tasks.

## Models Designed Based On Below ERD

![trello-team-collaboration](erd.jpg)

The ERD illustrates the entities, relationships, and attributes within the database. It serves as a reference for understanding how the data is organized and connected in the application.

## Technologies Used

- Django 4.2.3
- Django-rest framework 3.14.0
- Python 3.11


## Installation

To run the Project Management Tool locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/saraeygh/trello-team-collaboration.git
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   - On mscOS and linux: source venv/bin/activate
   - On Windows: venv/Scripts/activate.bat
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements/base.txt
   pip install -r requirements/development.txt
   ```

5. Run database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000//` in your browser.

## Usage

- Create an account or log in to an existing one.

- Create a new Project for your project.

- Add tasks to your prpject (e.g., "To Do," "In Progress," "Done").

- Within each list, create cards representing individual tasks.

- Customize cards and task with descriptions, due dates, and assignees.

- Collaborate with team members by adding comments and attachments to cards.

## Contributing

We welcome contributions from the community! To contribute to the project, follow these steps:

1. Fork the repository and create your branch:

 ```bash
    - git clone https://github.com/saraeygh/trello-team-collaboration.git

    - cd trello-team-collaboration

    - git checkout -b feature/your-feature-name 
   ```

2. Make your changes and commit them:

 ```bash
    - git add .
    - git commit -m "Add your commit message here"
   ```

3. Push your changes to your forked repository:

 ```bash
    git push origin feature/your-feature-name
   ```

Create a pull request to the main branch of the original repository.

## Bug Reports and Feature Requests

If you encounter any bugs or have ideas for new features, please submit an issue on our issue tracker.

## License

The Project Management Tool is open-source and distributed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.
***

## Contact

If you have any questions or inquiries, please feel free to contact any of the following:

- **Reza Saraey.** (Project Lead)
  - Email: <saraeygh@gmail.com>
  - GitHub: [saraeygh](https://github.com/saraeygh)

- **Mahdieh Soleimani.** (Developer)
  - Email: <Mahdieh.soleimani2000@gmail.com>
  - GitHub: [MahdiehSoleimani](https://github.com/MahdiehSoleimani)

- **Hossein Asghari.** (Developer)
  - Email: <ho3ein.m1991@gmail.com>
  - GitHub: [hosseinasgharii](https://github.com/hosseinasgharii)

- **Reza Rashidian.** (Developer)
  - Email: <Rezabitaj@gmail.com>
  - GitHub: [RezaRashidian](https://github.com/RezaRashidian)  

You can reach out to any of the team members listed above for assistance or further information about the project.
