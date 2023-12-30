
import random

emoji_positivo = [ '👍', '👏' ]
emoji_negativo = [ '👎', '🤬' ]

def react( user_id, chat_id, database, table_name ):#Verify if the user will receive a reaction 

    try:
        database.execute( f"SELECT * FROM {table_name} WHERE idgroup = '{chat_id}' AND userid = '{user_id}'" )

        result = database.fetchone()
        
        if result:

            return result

    except Exception as e:

        print(f'Error checking if user {user_id} is monitored in the group {chat_id}: {e}')

def reagir_mensagem(app, message_id, user_in_database ):

    if user_in_database[4] == 'cheer':

        app.send_reaction(user_in_database[1], message_id, random.choice( emoji_positivo ))

    elif user_in_database[4] == 'boo':

        app.send_reaction(user_in_database[1], message_id, random.choice( emoji_negativo ))

    else:
        print( 'User is in monitoring state, not reacting' )
        
