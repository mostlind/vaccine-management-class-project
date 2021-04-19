# Vaccine Management Class Project

# Set up
* Make sure you're using python 3.9, `python --version`
* Create a virtual env: `python -m venv venv`
* Activate your virtual env: `source ./venv/bin/activate` (assuming you're using the bash shell)
* Install dependencies `pip install -r requirements.txt`
* run the example script `python main.py`

# Run Tests
`python -m unittest test.py`

# Usage
`python main.py <command> <subcommand> --argument value`

## Commands

### `facility`
Facility related commands
* `list`
Lists the name and id all of the created facilities


* `lookup` Lookup detailed information about a facility. Returns name, address, and number of vaccines
  * Required argument `--id <uuid of facility>`
  * Example: `python main.py facility lookup --id 1234-ab12-bacc-123aba`
* `register`
  Follow the prompts to register a new facility

### `appointment`
Appointment related commands
* `list` show all the scheduled appointments
* `schedule` follow the prompts to sign up for an appointment