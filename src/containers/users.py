from Component_py.stubs import require  # __:skip
from actions.users import fetch_users, set_user
from components.users import Users
connect = require("react-redux").connect

def mapStateToProps(state):
    return { "data": state["users"] }

def mapDispatchToProps(dispatch):
    return {
        "fetch_users": lambda: dispatch(fetch_users()),
        "set_user": lambda user: dispatch(set_user(user))
    }

UsersContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(Users)
