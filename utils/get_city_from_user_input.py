def get_city_from_user_input(data):
    user_input = data.split()
    try:   
        return user_input[1] 
    except IndexError:
        return 'Введіть команду правильно: /команда назва міста'

if __name__=='__main__':
    get_city_from_user_input('/weather')