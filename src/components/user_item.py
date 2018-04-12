from Component_py.stubs import require, __pragma__  # __:skip
React = require("react")
Link = require("react-router").Link

def UserItem(props):
    thumbnail = props.user.picture.thumbnail
    username = props.user.login.username
    to_path = f"/user:{username}"

    return __pragma__("xtrans", None, "{}", """ (
        <Link
            className="box"
            onClick={props.onClick}
            to={to_path}
        >
            <img src={thumbnail} />
            <span>{username}</span>
        </Link>
    ); """)
