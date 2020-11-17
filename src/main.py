from src.features.show_main_menu_feature import ShowMainMenuFeature
from src.user_interface import Interface


def main():
    interface = Interface()
    #TODO change main menu to firstly let pick up a book which later on would be passed to the further options
    ShowMainMenuFeature().run(interface)

if __name__ == "__main__":
    main()
