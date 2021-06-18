import Login from "./pages/Login/Login";
import {Switch, Route} from "react-router-dom";
import Register from "./pages/Register/Register";
import Main from "./pages/Main/Main";
import EventCreate from "./pages/EventCreate/EventCreate";

function App() {
	return (
		<div className='container'>
			<Switch>
				<Route exact path='/' component={Main}/>
				<Route exact path='/login' component={Login}/>
				<Route exact path='/register' component={Register}/>
				<Route exact path='/add_event' component={EventCreate}/>
			</Switch>
		</div>
	)
}

export default App;
