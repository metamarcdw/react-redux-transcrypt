from Component_py.stubs import require, __pragma__  # __:skip
from Component_py.component import destruct
React = require("react")

def UserProfile(props):
    user_profile = props.user_profile
    title, first, last = \
        destruct(user_profile["name"], "title", "first", "last")
    full_name = f"{title.capitalize()}. {first.capitalize()} {last.capitalize()}"

    if not user_profile:
        return __pragma__("xtrans", None, "{}", """ (
            <h1>Looks like you haven't selected a user</h1>
        ); """)

    return __pragma__("xtrans", None, "{}", """ (
        <div className="container">
            <img src={user_profile.picture.large} />
            <span>{full_name}</span>
            <span>{user_profile.email}</span>
        </div>
    ); """)
