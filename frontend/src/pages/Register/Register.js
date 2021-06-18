import React, {useState} from 'react';
import {register} from "../../api";
import {Link, useHistory} from "react-router-dom";

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
			<div className="page_login__heading">
				Register Page
			</div>
			<div className="page_login__inputs">
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
			</div>

			<button
				type='submit'
				className='page_login__button'
				onClick={registerHandler}
			>
				Register
			</button>
			<Link to='/login' className='page_login__sign_up_link'>Login</Link>
		</div>
	);
};

export default Register;