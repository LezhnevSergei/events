import React from 'react';
import './Event.css'

const Event = ({data, key}) => {
	return (
		<li
			className='event_list__event event'
			key={key}
		>
			<div className="event__name event__row">
				Name: {data.name}
			</div>
			<div className="event__start_at event__row">
				Start at: {data.start_at}
			</div>
			<div className="event__end_at event__row">
				End at: {data.end_at}
			</div>
			<div className="event__themes event__row">
				Themes: {data.themes.map(theme => theme.name).join(', ')}
			</div>
			<div className="event__city event__row">
				City: {data.city.name}
			</div>
		</li>
	);
};

export default Event;