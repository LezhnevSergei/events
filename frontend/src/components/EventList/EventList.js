import React, {useEffect, useState} from 'react';
import {get_events} from "../../api";
import Event from "../Event/Event";
import "./EventList.css"
import {Link} from "react-router-dom";

const EventList = () => {
	const [events, setEvents] = useState(null)

	useEffect(() => {
		get_events().then(data => {
			setEvents(data.items)
		})
	}, [])

	if (events?.length === 0) {
		return (
			<div>
				Events not exist
			</div>
		)
	}

	return (
		<>
			<ul className='event_list'>
				{
					events?.map((event, i) => (
						<Event
							data={event}
							key={i}
						/>
					))
				}
			</ul>
		</>
	)
}

export default EventList;