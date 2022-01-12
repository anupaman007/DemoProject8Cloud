import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\user\PycharmProjects\pythonProject\pythonProject\8Cloud\Configurations\Config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('Common Info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('Common Info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Common Info', 'password')
        return password


