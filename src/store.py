from Component_py.stubs import require, __pragma__  # __:skip
from Component_py.component import destruct
from reducers.users import users_reducer
from reducers.user_profile import user_profile_reducer

createStore, combineReducers, applyMiddleware = \
    destruct(require("redux"),
             "createStore", "combineReducers", "applyMiddleware")

logger = require("redux-logger").createLogger
promise = require("redux-promise-middleware").js_default

users_store = createStore(
    combineReducers({
        "users": users_reducer,
        "user_profile": user_profile_reducer
    }),
    applyMiddleware(
        logger(),
        promise()
    )
)
