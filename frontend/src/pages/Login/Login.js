import React, {useState} from 'react';
import {Link, useHistory} from 'react-router-dom';
import {login as loginMethod} from "../../api";
import "./Login.css"

const Login = () => {
	const [login, setLogin] = useState(null)
	const [password, setPassword] = useState(null)
	const [logined, setLogined] = useState(false)
	const history = useHistory()

	const loginHandler = async () => {
		const data = await loginMethod(login, password)
		if (!data) {
			return null
		}
		localStorage.setItem('identity', JSON.stringify(data))
		setLogined(prev => true)
		history.push('/')
	}

	return (
		<div className="page_login">
			<div className="page_login__heading">
				Login page
			</div>
			<div className="page_login__inputs">
				login:
				<input
					type='text'
					onChange={event => setLogin(event.target.value)}
				/>
				password:
				<input
					type='password'
					onChange={event => setPassword(event.target.value)}
				/>
			</div>

			<button
				className='page_login__button'
				onClick={loginHandler}
			>
				login
			</button>
			<Link to='/register' className='page_login__sign_up_link'>Sign Up</Link>
		</div>
	);
};

export default Login;