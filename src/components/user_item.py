from Component_py.stubs import require, __pragma__  # __:skip
React = require("react")
Link = require("react-router").Link

def UserItem(props):
    thumbnail = props.user.picture.thumbnail
    username = props.user.login.username
    return __pragma__("xtrans", None, "{}", """ (
        <Link
            className="box"
            onClick={props.onClick}
            to={`/user:${username}`}
        >
            <img src={thumbnail} />
            <span>{username}</span>
        </Link>
    ); """)
