from enum import Enum, auto


class EventTypes(Enum):
    ANSWER_KNOWN = auto()
    ANSWER_UNKNOWN = auto()
    PREVIOUS = auto()
    NEXT = auto()
    QUIT = auto()
    NEXT_NOT_PROCESSED = auto()
    PREVIOUS_NOT_PROCESSED = auto()
    HELP = auto()