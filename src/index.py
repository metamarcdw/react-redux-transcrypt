from Component_py.stubs import require, __pragma__, document  # __:skip
from Component_py.component import destruct

from store import users_store
from containers.users import UsersContainer
from containers.user_profile import UserProfileContainer
from components.app import App
from components.home import Home

React = require("react")
ReactDOM = require("react-dom")
Provider = require("react-redux").Provider
Router, Route, IndexRoute, hash_history = \
    destruct(require("react-router"),
             "Router", "Route", "IndexRoute", "hashHistory")

app = __pragma__("xtrans", None, "{}", """ (
    <Provider store={users_store}>
        <Router history={hash_history}>
            <Route path="/" component={App}>
                <IndexRoute component={Home} />
                <Route path="users" component={UsersContainer} />
                <Route path="user(:user_name)" component={UserProfileContainer} />
            </Route>
        </Router>
    </Provider>
); """)

ReactDOM.render(app, document.getElementById("root"))
