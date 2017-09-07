from cryptography.fernet import Fernet
import json

class Encoder():
    '''Класс который шифрует рекорд и отправляет его в json файл
    или разшифровывает и выводит обратно для сравнения'''

    # Передаёт рекорд и ключ если нужно в конструктор
    def __init__(self, record, key = b''):
        #Строка для шифрования
        self.record = record
        #Ключ для шифрования
        self.key = key

    def seve_record(self):
        '''Метод шифрования рекорда и сохранения в файл'''
        
        #Переводим строку рекорда в байты
        self.record = bytes(self.record, encoding = 'utf-8')
        #Генерируем новый ключ для шифрования
        self.key = Fernet.generate_key()
        #Создаём функцию шифрвоания на основе ключа
        self.cipher = Fernet(self.key)
        #Создание зашифрованной копии рекорда
        self.record = self.cipher.encrypt(self.record)
        #Имя файла для записи, если нет создаётсяавтматически
        self.filename = 'record.json'
        #Перевод рекорда из байтовых в строковые значения для записи
        self.record = str(self.record.decode('utf-8'))
        #Перевод ключа из байтовых в строковые значения для записи
        self.key = str(self.key.decode('utf-8'))
        #Всё это кладём в массив
        self.save_arr = [self.key, self.record]
        #Функция записи в файл
        with open(self.filename, 'w') as self.f_obj:
            json.dump(self.save_arr , self.f_obj)

    def load_record(self):
        '''Метод расшифровки рекорда и загрузка его из файла'''
        
        #Имя файла для загрузки, если нет создаётсяавтматически
        self.filename = 'record.json'
        #Функция чтения из файла
        with open(self.filename) as self.f_obj:
            self.load_arr = json.load(self.f_obj) 
        #Перевод значений из считенного массива в байты
        self.key = bytes(self.load_arr[0], encoding = 'utf-8')
        self.record = bytes(self.load_arr[1], encoding = 'utf-8')
        #Создание нового шифровальщика на основе старого считанного ключа
        self.cipher = Fernet(self.key)
        #Расшифровка сообщения создание расшифрованной копии
        self.record = self.cipher.decrypt(self.record)
        self.record = self.record
        return self.record.decode('utf-8')
    
string_to_encrypt = input('Введите строку для шифрования: ')
enkoder = Encoder(string_to_encrypt)
enkoder.seve_record()
string_to_decrypt = enkoder.load_record()
print(string_to_decrypt)
