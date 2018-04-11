from Component_py.stubs import require, __pragma__  # __:skip
React = require("react")

def Home():
    return __pragma__("xtrans", None, "{}", """ (
        <div className="home">
            <h1>Welcome Home!!</h1>
        </div>
    ); """)
