
class User:
    def __init__(self, id, username, first_name) -> None:
        self.id = id
        self.username = username
        self.first_name = first_name
        self.Type_of_subject = ''
        self.Type_of_work = ''
        self.Date = ''
        self.Time = ''
        self.Tasks = ''
        self.Hours_to_write = ''
        self.Lectur = ''
        self.Info = ''
        self.Count = ''
        self.Photos = ''

    def to_dict(self):
        return {
            f'{self.id}': {
                'username': "Пользователь - " + str(self.username),
                'first_name': "Ник - " + str(self.first_name),
                'Type_of_subject' : "Прeдмет - " + str(self.Type_of_subject),
                'Type_of_work': "Тип работ - " + str(self.Type_of_work),
                'Date': "Дата - " + str(self.Date),
                'Time': "Время - " + str(self.Time),
                'Tasks': "Кол-во задач - " + str(self.Tasks),
                'Hours_to_write': "Времязатраты - " + str(self.Hours_to_write),
                'Lectur': "Лектор - " + str(self.Lectur),
                'Info' : "+Информация - " + str(self.Info),
                'Count' : "Кол-во обращений - " + str(self.Count),
                'Photos' : "Фотографии - " + str(self.Photos)
           }
        }

    def to_str(self):
        return f'[{self.id}] {self.username}({self.first_name}) \n Прeдмет - {self.Type_of_subject} \n Тип работ - {self.Type_of_work} \n Дата - {self.Date} \n Время - {self.Time} \n Задание - {self.Tasks} \n Времязатраты - {self.Hours_to_write} \n Лектор - {self.Lectur} \n Доп информация - {self.Info} \n Кол-во обращений - {self.Count}'
