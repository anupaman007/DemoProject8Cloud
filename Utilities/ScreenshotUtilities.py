import time


def screenshot(d):
    folder = r"C:\Users\user\PycharmProjects\pythonProject\pythonProject\8Cloud\Screenshot\pic.png"
    time_string = time.asctime().replace(":", " ")
    filename = folder + time_string + ".png"
    d.save_screenshot(filename)


