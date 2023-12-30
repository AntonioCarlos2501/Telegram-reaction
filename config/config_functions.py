

import data.connection as db 

def carrega_usuarios():
    try:

        conn = db.connect_database()

        cur = conn.cursor()

        return cur, conn

    except Exception as e:

        print(f'error while connect the database: {e}')


#Adiciona o usuário marcado na lista
def save_user( client, message, database, database_conn, table_name ):
    
    if message.reply_to_message and message.reply_to_message.from_user.id:

        try:
            chat_id = str(message.chat.id)
            user_id = str(message.reply_to_message.from_user.id)
            group_name = message.chat.title
            username = message.reply_to_message.from_user.username
            atividade = "cheer"

            database.execute( f"SELECT * FROM {table_name} WHERE idgroup = '{chat_id}' AND userid = '{user_id}'" )
            result = database.fetchone()

            if result:

                client.send_message( 'me', f"O usuário: {username} já está sendo monitorado no grupo {group_name}" )
            
            else:
                
                database.execute( f"INSERT INTO {table_name}(nome, idgroup, username, userid, atividade) VALUES ( '{group_name}', '{chat_id}', '{username}', '{user_id}', '{atividade}' )" )

                database_conn.commit()
                
                client.send_message( 'me', f"O usuário: {username} está sendo monitorado no grupo {group_name}, por padrão o usuário receberá reações positivas" )
        
        except Exception as e:

            print(f'Erro ao adicionar o usuário {user_id} no grupo {chat_id}: {e}')
            database_conn.rollback()

        


def is_command( mensagem ):#verify if the send message is a command
    
    if mensagem == '/addUser':
        
        return True
