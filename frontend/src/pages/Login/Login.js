import React, {useEffect, useState} from 'react';
import {Link, useHistory} from 'react-router-dom';
import {login as loginMethod} from "../../api";

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
			Login Page
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
			<button
				onClick={loginHandler}
			/>
			<Link to='/register'>Sign Up</Link>
		</div>
);
};

export default Login;