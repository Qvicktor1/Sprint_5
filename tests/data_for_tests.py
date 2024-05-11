import random as r


class CommonData:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    test_user_email = 'test_user_burgers123@ya.ru'
    test_user_password = '123456'
    invalid_password = '12345'

    @staticmethod
    def reg_data():
        name_seq = ['А', 'Б', 'В', 'Г', 'Д', 'Е']
        name = f'{r.choice(name_seq)}{r.choice(name_seq)}{r.choice(name_seq)}'
        login = f'viktorkovalew8{r.randint(100, 1000)}@ya.ru'
        password = f'sosiska{r.randint(100, 10000)}'
        return {'name': name, 'login': login, 'password': password}
