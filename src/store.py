from Component_py.stubs import require, __pragma__  # __:skip
from reducers.users import users_reducer
from reducers.user_profile import user_profile_reducer

Redux = require("redux")
logger = require("redux-logger").createLogger

__pragma__("noalias", "default")
promise = require("redux-promise-middleware").default
__pragma__("alias", "default", "py_default")

users_store = Redux.createStore(
    Redux.combineReducers({
        "users": users_reducer,
        "user_profile": user_profile_reducer
    }),
    Redux.applyMiddleware(
        logger(),
        promise()
    )
)
