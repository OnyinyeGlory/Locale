# Locale API

## Requirements

- Python 3.8 or higher

## Project setup

Follow these steps to run locally:

1. Clone the git repository:
    
    ```bash
    git clone https://github.com/OnyinyeGlory/Locale.git
    ```
    
2. cd into the locally cloned repository
    
    ```bash
    cd Locale
    ```
    
3. Create a `.env` file using the keys in `[.env.example](https://github.com/Onyenso/TantaAuth/blob/main/.env.example)`.
4. Fill in the missing variables in the `.env` file.
5. Create a Python virtual environment.
6. Install packages in `requirements.txt`.
    
    ```bash
    pip intall -r requirements.txt
    ```
    
7. Run migrations
    
    ```bash
    python manage.py migrate
    ```
    
8. Start up the server
