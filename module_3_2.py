dog = '@'
ends = ('.com', '.ru', '.net')


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    flag = False
    if dog in recipient:
        for i in ends:
            if i in recipient:
                flag = True
    if flag is False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    flag = False
    if dog in sender:
        for i in ends:
            if i in sender:
                flag = True
                if sender != 'university.help@gmail.com':
                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
                elif recipient == 'university.help@gmail.com':
                    print('Нельзя отправить письмо самому себе!')
                elif sender == 'university.help@gmail.com':
                    print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    if flag is False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Hello', 'univesity.help@gmail.net', sender='aloo@mail.ru')
send_email('Hello', 'university.help@gmail.com')
send_email('Hello', 'university.help@gmail.ru', sender='alo@mail.fin')
send_email('Hello', 'university@gmail.ru')
