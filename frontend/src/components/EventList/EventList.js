import React, {useEffect, useState} from 'react';
import {get_events} from "../../api";
import Event from "../Event/Event";
import "./EventList.css"
import EventsFilter from "../EventsFilter/EventsFilter";

const EventList = () => {
	const [events, setEvents] = useState(null)
	const [filters, setFilters] = useState()

	useEffect(() => {
		get_events(filters).then(data => {
			setEvents(data.items)
		})
	}, [filters])

	console.log(events);

	if (events?.length === 0) {
		return (
			<>
				<EventsFilter filters={filters} setFilters={setFilters}/>
				<div>
					Events not exist
				</div>
			</>
		)
	}

	return (
		<>
			<EventsFilter filters={filters} setFilters={setFilters}/>
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