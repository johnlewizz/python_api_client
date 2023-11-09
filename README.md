# python_api_client
This is a client application that is used to interact with the elixir fizz buzz application
1. Create a new directory for your project:
mkdir fizz_buzz_client
cd fizz_buzz_client

2. Create a virtual environment for your project:
python -m venv venv

3. Activate the virtual environment:
On macOS and Linux:
source venv/bin/activate
On Windows:
venv\Scripts\activate

4. Install the required packages:
pip install requests argparse

5. Create a new file for your Python code:
touch fizz_buzz_client.py

6. Open the `fizz_buzz_client.py` file and add the code you provided.

# Run your script with the desired arguments. Here are some examples:
To get the homepage values:
python fizz_buzz_client.py get_homepage_values
To get the values between a specific range:
python fizz_buzz_client.py get_values_between --start_range 1 --end_range 20
To set a favorite:
python fizz_buzz_client.py set_favourite --number 3 --value "fizz"
To delete a favorite:
python fizz_buzz_client.py delete_favourite --number 3
