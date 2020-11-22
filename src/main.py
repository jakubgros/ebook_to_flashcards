from src.features.show_main_menu_feature import ShowMainMenuFeature
from src.console_app_framework.interface import Interface

if __name__ == "__main__":
    interface = Interface()
    ShowMainMenuFeature().run(interface)

#Bug reporter - all commands that goes through interface are logged