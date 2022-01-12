import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=r"C:\Users\user\PycharmProjects\pythonProject\pythonProject\8Cloud"
                                                r"\Logs\Automation.log",
                                       mode="a")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
