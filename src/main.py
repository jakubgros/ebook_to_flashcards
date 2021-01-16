from src.features.show_main_menu_feature import ShowMainMenuFeature
from src.console_app_framework.interface import Interface

if __name__ == "__main__":
    interface = Interface()
    ShowMainMenuFeature().run(interface)



#making flashcards:
# it should be possible to quit in the middle
# crash save
# if only one option of translation, accept it without asking user
# separtor between translations


#Bug reporter - all commands that goes through interface are logged

# interrogation to mark known words:
"""
plural to singular


to remove
ll
ve
st
numbers as words
names and surnames


to fix-
doesn -> 'nt is separated
isn
aren
shouldn
didn


going backward should be easier
enter as answer should treat as adding to bulk answer and then any valid answer should mark everything entered so far as the answer

"""

