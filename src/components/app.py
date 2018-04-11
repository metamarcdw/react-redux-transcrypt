from Component_py.stubs import require, __pragma__  # __:skip
from components.navbar import Navbar
React = require("react")

def App(props):
    return __pragma__("xtrans", None, "{}", """ (
        <div className="appComp">
            <Navbar />
            <div>
                <h1>This is our App component</h1>
                {props.children}
            </div>
        </div>
    ); """)
