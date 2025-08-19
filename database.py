from typing import List
from models import Note

notes_db: List[Note] = []
_current_id = 1

def get_next_id():
    global _current_id
    next_id = _current_id
    _current_id += 1
    return next_id
