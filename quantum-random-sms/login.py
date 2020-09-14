import shelve 

def insertToken(reference, token):
    try:
        db_token = shelve.open('./db/tokens.db')
        db_token[reference] = token
        db_token.close()
        return True
    except Exception as error:
        print(error)
        return False

def getToken(reference):
    db_token = shelve.open('./db/tokens.db')
    token = db_token[reference]
    db_token.close()
    return token

if __name__ == '__main__':
    login_to = input('Login para o qual quer guardar o token:\n')
    token = input('\nDigite o token:\n')
    if insertToken(login_to, token):
        print('Sucess')
    else:
        print('Fail')