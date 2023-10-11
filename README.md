# Project Name
Temperature Alert Agent - 230550

## Description of the Project
Temperature Alert Agent - 230550 is a weather information retriever. It allows users to input a city and temperature preferences, fetches weather data for the chosen city, and provides feedback on whether the current temperature falls within the user's preferred range.

## Instructions to Run the Project
1. Ensure you have the prerequisites installed:
   - Python (3.10+ recommended)
   - Poetry: A dependency management tool for Python.
2. Clone the repository to your local machine.
3. Navigate to the main project directory:


## Instructions to Run the Project
1. Ensure you have the prerequisites installed:
   - Python (3.10+ recommended)
   - Poetry: A dependency management tool for Python.
2. Clone the repository to your local machine.
3. Navigate to the main project directory:

##cd path_to_your_project_directory
i.e: cd HACKAI_Hack-230550/src


4. Set up the environment variables by signing up at OneWeather and getting an API key for yourself, then set up the BASE URL and API KEY in the .ENV file. After that, run all the following commands in a bash environment:

##source .env

5. Install the dependencies:

##poetry install

6. Execute the main script: (depends on how your BASH environment recognizess the Python environment)

##poetry run python main.py

or

##python3 main.py

or

##python main.py

7. If you wish to interact with the agents using the client, in a new terminal:

##cd path_to_your_project_directory
##poetry run python client.py

## Special Considerations
- Ensure you have the correct API keys set up in the `.env` file.
- Always check the logs for important outputs and addresses when running the main script.

