import React, {useEffect, useState} from 'react';
import {get_cities, get_themes} from "../../api";
import "./EventsFilter.css"
import DateTimePicker from "react-datetime-picker";

const EventsFilter = ({filters, setFilters}) => {
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
	}, [])

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
						setFilters({city_id})
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
										setFilters({...filters, theme_ids: theme_ids})
										return
									}
									if (theme_ids?.length) {
										theme_ids[i] = theme_id
									} else {
										theme_ids = [theme_id]
									}
									setFilters({...filters, theme_ids})
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
					/>
				</div>
				<div className="filters__end">
					End at
					<DateTimePicker
						onChange={date => {
							setFilters({...filters, end_at: date})
						}}
						value={filters?.end_at}
					/>
				</div>

			</div>
		</div>
	);
};

export default EventsFilter;