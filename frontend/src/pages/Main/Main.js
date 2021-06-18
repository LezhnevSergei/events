import React, {useEffect, useState} from 'react';
import {useHistory} from "react-router-dom";
import {me} from "../../api";
import Header from "../../components/Header/Header";
import './Main.css'
import EventList from "../../components/EventList/EventList";

const Main = () => {
	const [isLoading, setIsLoading] = useState(true)
	const [isLogined, setIsLogined] = useState(false)
	const [user, setUser] = useState(null)
	const history = useHistory()

	const checkLogin = async () => {
		setIsLoading(true)
		const meData = await me()
		setIsLoading(false)
		setUser(meData)
		setIsLogined(!!meData)
		if (!meData) {
			history.push('/login')
		}
	}

	useEffect(() => {
		checkLogin()
	}, [])

	if (isLoading) {
		return (
			<div className="App">
				Загрузка...
			</div>
		)
	}

	return (
		<>
			<Header hasAddEventButton={true}/>
			<EventList/>
		</>
	)
};

export default Main;