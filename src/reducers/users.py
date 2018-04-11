#pylint: disable-msg=E1121

from Component_py.stubs import Object  # __:skip
from actions.types import (
    FETCH_USERS_PENDING,
    FETCH_USERS_FULFILLED,
    FETCH_USERS_REJECTED
)

initial_state = {
    "users": [],
    "loading": False,
    "error": None
}

def users_reducer(state=initial_state, action=None):
    type_ = action["type"]
    if type_ == FETCH_USERS_PENDING:
        return Object.assign({}, state, {
            "loading": True
        })

    elif type_ == FETCH_USERS_FULFILLED:
        return Object.assign({}, state, {
            "users": action.payload.data["results"],
            "loading": False
        })

    elif type_ == FETCH_USERS_REJECTED:
        return Object.assign({}, state, {
            "error": action.payload["message"],
            "loading": False
        })

    return state
