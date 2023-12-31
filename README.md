# Telegram Reactions Bot  

## Introduction  

This is a Python-based Telegram bot designed to handle reactions in group messages.  
Users can add reactions (cheer or boo) to messages within a group, and the bot will manage  and display these reactions.

<br>
<br>

# Getting started  

## Prerequisites  

1. **Database Setup:**
  - Create a PostgreSQL database.
  - Inside the database, create a table with the following columns: 'group_name',  
    'idgroup', 'username', 'userid', 'reaction_type'.
2. **Configure Database Connection:**
  - Open the **data/connection.py** file.
  - Modify the values of the variables 'database_name', 'user_name', 'password',  
    'host', and 'port' with your database connection details.
3. **Telegram API Credentials:**
    - Obtain API credentials ('API id' and 'API hash') from the [Telegram API website](https://my.telegram.org/auth).
    - Replace the placeholders in the **telegramReactV2.py** file with your  
      obtained credentials for 'api_id' and 'api_hash'.

## Installation
1. **Clone the repository:**
  ```
git clone https://github.com/AntonioCarlos2501/Telegram-reaction.git
```

2. **Install the required Python libraries:**
  ```
pip install pyrogram psycopg2
```

## Usage

1. **Run the bot:**
```
python3 telegramReactV2.py
```
2. **Use the following commands in the Telegram group:**
  - `/addUser cheer`: Reply a message from a user in the group to add a positive reaction to all next messages from the user.
  - `/addUser boo`: Reply a message from a user in the group to add a negative reaction to all next messages from the user.

## License
This project is licensed under the MIT License.


