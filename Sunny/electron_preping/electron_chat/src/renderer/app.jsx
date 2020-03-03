import React from "react";
import { render } from "react-dom";
import { Router, Route, hashHistory } from "react-router";
import Login from "./Login";
import Signup from "./Signup";
import Rooms from "./Rooms";
import Room from "./Room";

// Routing 정의하기
const appRouting = (
    <Router history={hashHistory}>
        <Route path="/">
            <Route path="login" component={Login}/>
            <Route path="signup" component={Signup} />
            <Route path="rooms" component={Rooms}>
                <Route path=":roomId" component={Room} />
            </Route>
        </Route>
    </Router>
);

//Routing 초기화하기

if (!location.hash.length) {
    location.hash = "#/login";
}

// Application 렌더링 하기
render(appRouting, document.getElementById("app"));


//render(<div>Hello, Electron and React JSX</div>, document.getElementById("app"));
