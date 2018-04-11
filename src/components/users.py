from Component_py.stubs import __pragma__, require  # __:skip
from Component_py.component import Component, destruct
from components.button import Button
from components.user_item import UserItem
React = require("react")

class Users(Component):
    def render(self):
        data, fetch_users, set_user = \
            destruct(self.props, "data", "fetch_users", "set_user")

        def render_item(enum_):
            i, user = enum_
            on_click = lambda: set_user(user)
            return __pragma__("xtrans", None, "{}", """ (
                <UserItem
                    key={i}
                    user={user}
                    onClick={on_click} />
            ); """)

        return __pragma__("xtrans", None, "{}", """ (
            <div className="container">
                <Button
                    onClick={fetch_users}
                    text="Fetch Users"
                    className="btn btn-blue" />
                <div id="users">
                    { map(render_item, enumerate(data.users)) }
                </div>
            </div>
        ); """)
