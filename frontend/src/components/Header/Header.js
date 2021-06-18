import React from 'react';
import './Header.css'
import {Link, useHistory} from "react-router-dom";

const Header = ({hasAddEventButton = false}) => {

	const history = useHistory()

	const logOutHandler = () => {
		history.push("/login")
		localStorage.removeItem("identity")
	}

	return (
		<header className='header'>
			<Link
				to="/"
				className="header__logo logo"
			>
				Events
			</Link>
			{
				hasAddEventButton && (
					<Link to='/add_event' className='header__add_event'>
						Add event
					</Link>
				)
			}

			<div
				className="header__log_out"
				onClick={logOutHandler}
			>LogOut
			</div>
		</header>
	);
};

export default Header;