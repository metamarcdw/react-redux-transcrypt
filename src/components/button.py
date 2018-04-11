from Component_py.stubs import require, __pragma__  # __:skip
React = require("react")

def Button(props):
    return __pragma__("xtrans", None, "{}", """ (
        <button
            onClick={props.onClick}
            className={props.className}
        >{props.text}</button>
    ); """)
