import React, {useEffect, useState} from 'react';
import Header from "../../components/Header/Header";
import './EventCreate.css'
import {create_event, get_cities, get_themes} from "../../api";
import DateTimePicker from 'react-datetime-picker';
import {useHistory} from "react-router-dom";

const EventCreate = () => {
	const [themes, setThemes] = useState([])
	const [cities, setCities] = useState([])
	const [themeIds, setThemeIds] = useState([1])
	const [fields, setFields] = useState({
		name: "",
		theme_ids: themeIds,
		city_id: 1,
	})
	const history = useHistory()

	useEffect(() => {
		get_themes().then(themes => {
			setThemes(themes)
		})
		get_cities().then(cities => {
			setCities(cities)
		})
	}, [])

	return (
		<>
			<Header/>
			<div className="create_event">
				<div className="create_event__heading">
					Create event
				</div>
				<div className="create_event__name">
					Name
					<input
						type="text"
						className="create_event__input"
						onChange={e => {
							setFields({...fields, name: e.target.value})
						}}
					/>
				</div>
				<div className="create_event__start_at">
					Start at
					<DateTimePicker
						onChange={date => {
							setFields({...fields, start_at: date})
						}}
						value={fields.start_at}
					/>
				</div>
				<div className="create_event__end_at">
					End at
					<DateTimePicker
						onChange={date => {
							setFields({...fields, end_at: date})
						}}
						value={fields.end_at}
					/>
				</div>
				<div className="create_event__themes">
					Themes
					<div
						className="create_event__add_theme"
						style={{"cursor": "pointer", "margin": "2px"}}
						onClick={() => {
							setThemeIds([...themeIds, 1])
							setFields({...fields, theme_ids: [...fields.theme_ids, 1]})
						}}
					>+</div>
					{
						themeIds.map((_, i) => {
							return (
								<select
									className="create_event__select"
									onChange={(event) => {
										fields.theme_ids[i] = Number(event.target.value)
										setFields({...fields})
									}}
								>
									{
										themes?.length > 0 ?
											themes.map(theme => {
												return (
													<option
														key={theme.id}
														value={theme.id}
													>
														{theme.name}
													</option>
												)
											})
											: null
									}
								</select>
							)
						})
					}
				</div>
				<div
					className="create_event__city"
					onChange={(event) => {
						setFields({...fields, city_id: Number(event.target.value)})
					}}
				>
					City
					<select className="create_event__select">
						{
							cities?.length > 0 ?
								cities.map(city => {
									return (
										<option
											key={city.id}
											value={city.id}
										>
											{city.name}
										</option>
									)
								})
								: null
						}
					</select>
				</div>
				<button
					className="create_event__button"
					onClick={() => {
						fields.theme_ids = Array.from(new Set(fields.theme_ids))
						create_event(fields)
						history.push('/')
					}}
				>
					add
				</button>
			</div>
		</>

	);
};

export default EventCreate;