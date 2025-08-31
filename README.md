# Meemoo Assignment

This is the technical follow-up assignment as part of the application process for the Backend Developer position at meemoo. The purpose of this assignment is to assess the applicants’ technical skills in producing clear code and their analytical thinking ability.

## How to install

This project assumes you have Python 3.12 installed on your computer.

1. Unpack the code in your preferred location.
2. Open a terminal in that location.
3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Initialize the database:

   ```bash
   python database/database_init.py
   ```

7. Start the application:

   ```bash
   fastapi dev main.py
   ```
