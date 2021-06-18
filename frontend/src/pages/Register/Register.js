import React, {useState} from 'react';
import {register} from "../../api";
import {useHistory} from "react-router-dom";

const Register = () => {
	const [login, setLogin] = useState(null)
	const [email, setEmail] = useState(null)
	const [password, setPassword] = useState(null)
	const history = useHistory()

	const registerHandler = async () => {
		await register(login, email, password)
		history.push('/login')
	}

	return (
		<div className="page_login">
			Register Page
			login:
			<input
				type='text'
				onChange={event => setLogin(event.target.value)}
			/>
			email:
			<input
				type='email'
				onChange={event => setEmail(event.target.value)}
			/>
			password:
			<input
				type='password'
				onChange={event => setPassword(event.target.value)}
			/>
			<button
				onClick={registerHandler}
			/>
		</div>
	);
};

export default Register;