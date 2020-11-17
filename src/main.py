from src.features.show_main_menu_feature import ShowMainMenuFeature
from src.user_interface import Interface

if __name__ == "__main__":
    interface = Interface()
    ShowMainMenuFeature().run(interface)
