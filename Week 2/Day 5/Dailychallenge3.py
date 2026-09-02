from datetime import datetime, date, timedelta


class Airline:
    """Represents an airline company."""

    def __init__(self, id_code, name):
        self.id = id_code
        self.name = name
        self.planes = []


class Airplane:
    """Represents a plane belonging to an airline."""

    def __init__(self, plane_id, current_location, company):
        self.id = plane_id
        self.current_location = current_location
        self.company = company
        self.next_flights = []
        self.company.planes.append(self)

    def __repr__(self):
        return f"Airplane({self.id}, {self.company.id})"

    def fly(self, destination):
        """Take off and land if a flight is scheduled for this destination."""
        for flight in self.next_flights:
            if flight.destination == destination:
                flight.take_off()
                flight.land()
                return True
        return False

    def location_on_date(self, date_value):
        """Return the location of the plane on a given date."""
        current = self.current_location
        for flight in self.next_flights:
            if flight.date == date_value:
                if flight.origin == current:
                    return flight.destination
                return flight.origin
        return current

    def available_on_date(self, date_value, location):
        """Return True if the plane is in the given location and has no flight planned."""
        if self.location_on_date(date_value) != location:
            return False
        for flight in self.next_flights:
            if flight.date == date_value:
                return False
        return True


class Flight:
    """Represents a flight between two airports."""

    def __init__(self, date_value, destination, origin, plane):
        self.date = date_value
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f"{destination.city}-{plane.company.id}-{date_value.strftime('%Y%m%d')}"
        self.plane.next_flights.append(self)
        self.plane.next_flights.sort(key=lambda flight: flight.date)
        self.origin.scheduled_departures.append(self)
        self.destination.scheduled_arrivals.append(self)
        self.origin.scheduled_departures.sort(key=lambda flight: flight.date)
        self.destination.scheduled_arrivals.sort(key=lambda flight: flight.date)

    def take_off(self):
        """Mark the departure from the origin airport."""
        self.origin.planes.remove(self.plane)

    def land(self):
        """Update plane location after landing."""
        self.plane.current_location = self.destination
        self.destination.planes.append(self.plane)


class Airport:
    """Represents an airport with planes and scheduled flights."""

    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, flight_datetime):
        """Schedule a flight from this airport to another airport."""
        for airline in self.planes:
            pass

        # This is a simplified booking system.
        for plane in self.planes:
            if plane.available_on_date(flight_datetime.date(), self):
                flight = Flight(flight_datetime.date(), destination, self, plane)
                return flight
        return None

    def info(self, start_date, end_date):
        """Display every scheduled flight from start_date to end_date."""
        flights = []
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                flights.append(flight)
        if not flights:
            print(f"No scheduled flights from {self.city} between {start_date} and {end_date}.")
            return
        for flight in flights:
            print(
                f"{flight.id} | {flight.origin.city} -> {flight.destination.city} | "
                f"{flight.date}"
            )


# ----------------
# Example test code
# ----------------

if __name__ == "__main__":
    paris = Airport("Paris")
    london = Airport("London")
    eurowings = Airline("EW", "EuroWings")

    plane1 = Airplane(101, paris, eurowings)
    plane2 = Airplane(202, london, eurowings)

    flight_date = date(2025, 8, 15)
    flight = Flight(flight_date, london, paris, plane1)

    print(f"Flight created: {flight.id}")
    print(f"Plane 101 current location: {plane1.current_location.city}")
    print(f"Plane 101 location on {flight_date}: {plane1.location_on_date(flight_date).city}")
    print(f"Can plane 101 fly to London? {plane1.fly(london)}")
    print(f"Plane 101 current location after flight: {plane1.current_location.city}")

    # Testing airport scheduling
    paris.planes.append(plane1)
    london.planes.append(plane2)
    scheduled = paris.schedule_flight(london, datetime(2025, 8, 16, 10, 0))
    if scheduled:
        print(f"Scheduled flight: {scheduled.id}")
        paris.info(date(2025, 8, 15), date(2025, 8, 16))
