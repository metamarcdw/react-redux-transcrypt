from actions.types import SET_USER

def user_profile_reducer(state=None, action=None):
    type_ = action["type"]
    if type_ == SET_USER:
        return action["payload"]
    return state
