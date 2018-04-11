from Component_py.stubs import require  # __:skip
from actions.types import FETCH_USERS, SET_USER
axios = require("axios")

def fetch_users():
    return {
        "type": FETCH_USERS,
        "payload": axios.js_get("https://randomuser.me/api/?results=10")
    }

def set_user(user):
    return {
        "type": SET_USER,
        "payload": user
    }
