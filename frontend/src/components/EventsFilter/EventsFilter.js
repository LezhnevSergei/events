import React, {useEffect, useState} from 'react';
import {get_cities, get_filters, get_themes, save_filter} from "../../api";
import "./EventsFilter.css"
import DateTimePicker from "react-datetime-picker";
import moment from "moment/moment";

const EventsFilter = ({filters, setFilters}) => {
	const [savedFilters, setSavedFilters] = useState([])
	const [themes, setThemes] = useState([])
	const [cities, setCities] = useState([])
	const [themeCount, setThemeCount] = useState(1)

	useEffect(() => {
		get_themes().then(themes => {
			setThemes(themes)
		})
		get_cities().then(cities => {
			setCities(cities)
		})
		get_filters().then(filters => {
			setSavedFilters(filters)
		})
	}, [])

	const saveFilterHandler = () => {
		save_filter(filters)
	}

	console.log(filters);

	return (
		<div className="filters">
			<div className="filters__city">
				City:
				<select
					className="filters__cities"
					onChange={(event) => {
						if (event.target.value === "all") {
							setFilters({...filters, city_id: null})
							return
						}
						const city_id = Number(event.target.value)
						setFilters(prev => ({...filters, city_id}))
					}}
				>
					<option
						key={0}
						value="all"
					>
						All
					</option>
					{
						cities?.map(city => {
							return (
								<option
									key={city.id}
									value={city.id}
									selected={city.id === filters?.city_id}
								>
									{city.name}
								</option>
							)
						})
					}
				</select>
			</div>

			<div className="filters__theme">
				Theme
				{
					filters?.theme_ids?.length ? (
						<span className="filters__add_theme" onClick={() => {
							setThemeCount(themeCount + 1)
						}}>
							+
						</span>
					) : null
				}
				:
				{
					new Array(themeCount).fill().map((_, i) => {
						return (
							<select
								className="filters__themes"
								onChange={(event) => {
									const theme_id = Number(event.target.value)
									let theme_ids = filters ? filters.theme_ids : []

									if (event.target.value === "all") {
										theme_ids = []
										setFilters({...filters, theme_ids})
										return
									}
									if (theme_ids?.length) {
										theme_ids[i] = theme_id
									} else {
										theme_ids = [theme_id]
									}
									setFilters(prev => ({...filters, theme_ids}))
								}}
							>
								{
									i === 0 ? (
										<option
											key={0}
											value="all"
										>
											All
										</option>
									) : null
								}

								{
									themes?.map(theme => {
										return (
											<option
												key={theme.id}
												value={theme.id}
												selected={filters?.theme_ids?.includes(theme.id)}
											>
												{theme.name}
											</option>
										)
									})
								}
							</select>
						)
					})
				}
			</div>
			<div className="filters__datetime">
				<div className="filters__start">
					Start at
					<DateTimePicker
						onChange={date => {
							setFilters({...filters, start_at: date})
						}}
						value={filters?.start_at}
						dateFormat={"DD-MM-YYYY hh:mm:ss"}
					/>
				</div>
				<div className="filters__end">
					End at
					<DateTimePicker
						onChange={date => {
							setFilters({...filters, end_at: date})
						}}
						value={filters?.end_at}
						dateFormat={"DD-MM-YYYY hh:mm:ss"}
					/>
				</div>

			</div>

			<div className="filters__saved_filters">
				Filters:
				<select
					className="filters__saved_filters_select"
					onChange={(event) => {
						if (event.target.value === "null") {
							setFilters({})
							return
						}
						const filter_id = Number(event.target.value)
						const saved_filter = savedFilters.filter(filter => filter.id === filter_id)[0]
						if (saved_filter.start_at) {
							saved_filter.start_at = moment(saved_filter.start_at, "DD-MM-YYYY hh:mm:ss").toDate()
						}

						if (saved_filter.end_at)
							saved_filter.end_at = moment(saved_filter.end_at, "DD-MM-YYYY hh:mm:ss").toDate()
						console.log(saved_filter);
						setFilters(saved_filter)
					}}
				>
					<option
						key={0}
						value="null"
					>
					</option>
					{
						savedFilters?.map(filter => {
							const themes_ = themes.filter(theme => filter.theme_ids.includes(theme.id))
							const themes_str = themes_.map(theme => theme.name).join(', ')
							const city = cities.filter(city => city.id === filter.city_id)[0]
							let result = []
							if (city?.name) {
								result.push(`City ${city?.name}`)
							}
							if (themes_str) {
								result.push(`Themes ${themes_str}`)
							}

							if (filter.start_at) {
								result.push(`Start ${filter.start_at}`)
							}

							if (filter.end_at) {
								result.push(`End ${filter.end_at}`)
							}

							return (
								<option
									key={filter.id}
									value={filter.id}
								>
									{result.join(', ')}
								</option>
							)
						})
					}
				</select>
			</div>

			<div
				className="filters__save_filter"
				onClick={saveFilterHandler}
			>
				Save
			</div>
		</div>
	);
};

export default EventsFilter;