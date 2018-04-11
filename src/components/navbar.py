from Component_py.stubs import require, __pragma__  # __:skip
React = require("react")
Link = require("react-router").Link

def Navbar(props):
    return __pragma__("xtrans", None, "{}", """ (
        <nav>
            <Link to="/">Home</Link>
            <Link to="users">Users</Link>
        </nav>
    ); """)
