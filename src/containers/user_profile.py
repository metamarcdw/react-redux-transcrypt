from Component_py.stubs import require  # __:skip
from components.user_profile import UserProfile
connect = require("react-redux").connect

def mapStateToProps(state):
    return { "user_profile": state["user_profile"] }

UserProfileContainer = connect(
    mapStateToProps
)(UserProfile)
