
from pyrogram import Client

#Modules
import config.config_functions as config
import modules.functions as func
#/Modules

database, database_conn = config.carrega_usuarios()
table_name = 'table_name'

#Creating an API connection

# app = Client( "my_session_name" ) #If you already have a section file replace 'my_session_name' with the name of your section file, otherwise comment out this line before the first execution


    ################################
###First API connection###
#You can get the ID & API Hash here: https://my.telegram.org/auth?to=apps


api_id = 12345 
api_hash = "012ui7j6678uyjtdef0123456789abcdef" 
app = Client("my_session_name", api_id=api_id, api_hash=api_hash)  # The first parameter is the session's name you want to create


#AFTER EXECUTING THIS CODE YOUR SECTION FILE WILL BE CREATED, SO COMMENT IT AGAIN AND UNCOMMENT the LINE 13
###First API connection###
   #################################

@app.on_message()
def main( client, message ):

    try:
        if message.from_user and message.from_user.is_self and '/' in message.text:

            if config.is_command( message.text.strip() ):

                config.save_user( client, message, database, database_conn, table_name )

        else:

            chat_type = str( message.chat.type )

            if chat_type in ["ChatType.CHANNEL", "ChatType.SUPERGROUP", "ChatType.GROUP" ] and message.chat.type:
                
                if message.from_user:
                    user_id = str( message.from_user.id )
                    chat_id = str( message.chat.id )
                    user_in_database = func.react( user_id, chat_id, database, table_name )
                    if user_in_database:

                        func.reagir_mensagem( app, message.id, user_in_database )
    
    except TypeError as e:

        print(f'Error while executing: {e}')

if __name__ == '__main__':
    app.run()
