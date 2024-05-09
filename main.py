from gui import *


def main():
    window = Tk()
    window.title('Distance Calculator')
    window.geometry('400x300')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
