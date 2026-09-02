import os
import collections
import datetime

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None

try:
    import pytz # pyright: ignore[reportMissingModuleSource]r
except ImportError:
    pytz = None


class WeatherApp:
    """Retrieve and display weather information from OpenWeatherMap."""

    def __init__(self, api_key=None):
        try:
            from pyowm import OWM # type: ignore
        except ImportError as error:
            raise RuntimeError("Install PyOWM with: pip install pyowm") from error

        self.api_key = api_key or os.getenv("OPENWEATHERMAP_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Set the OPENWEATHERMAP_API_KEY environment variable or pass an API key."
            )

        self.owm = OWM(self.api_key)
        self.weather_manager = self.owm.weather_manager()
        self.air_pollution_manager = self.owm.airpollution_manager()
        self.city_registry = self.owm.city_id_registry()

    def city_id(self, city, country=None):
        """Return the first matching OpenWeatherMap city ID."""
        matches = self.city_registry.ids_for(city, country=country)
        if not matches:
            raise ValueError(f"City not found: {city}")
        return matches[0][0]

    def current_weather(self, city_id):
        """Return current weather for a city ID."""
        return self.weather_manager.weather_at_id(city_id).weather

    def forecast(self, city_id):
        """Return the 3-hour forecast for a city ID."""
        return self.weather_manager.forecast_at_id(city_id, "3h").get_forecast()

    def air_pollution(self, weather):
        """Return air pollution data using the weather observation coordinates."""
        latitude = weather.location.lat
        longitude = weather.location.lon
        return self.air_pollution_manager.airpollution_at_coords(latitude, longitude)

    @staticmethod
    def get_local_timezone():
        """Return Paris timezone using zoneinfo or pytz, with UTC fallback."""
        if ZoneInfo is not None:
            try:
                return ZoneInfo("Europe/Paris")
            except Exception:
                pass
        if pytz is not None:
            try:
                return pytz.timezone("Europe/Paris")
            except Exception:
                pass
        return datetime.timezone.utc

    @staticmethod
    def format_weather(weather, city_name):
        """Format current conditions, wind, sunrise, and sunset."""
        wind = weather.wind()
        local_timezone = WeatherApp.get_local_timezone()
        sunrise = datetime.datetime.fromtimestamp(
            weather.sunrise_time(), datetime.timezone.utc
        ).astimezone(local_timezone)
        sunset = datetime.datetime.fromtimestamp(
            weather.sunset_time(), datetime.timezone.utc
        ).astimezone(local_timezone)
        temperature = weather.temperature("celsius")

        return (
            f"\n--- WEATHER IN {city_name.upper()} ---\n"
            f"Condition: {weather.detailed_status.title()}\n"
            f"Temperature: {temperature.get('temp', 0):.1f} C "
            f"(feels like {temperature.get('feels_like', 0):.1f} C)\n"
            f"Humidity: {weather.humidity}%\n"
            f"Wind: {wind.get('speed', 0):.1f} m/s, "
            f"direction {wind.get('deg', 'unknown')} degrees\n"
            f"Sunrise (Paris time): {sunrise:%Y-%m-%d %H:%M}\n"
            f"Sunset (Paris time): {sunset:%Y-%m-%d %H:%M}"
        )

    @staticmethod
    def format_air_pollution(air_pollution) -> str:
        """Format the air quality index and pollution level."""
        values = getattr(air_pollution, "current_aqi", "N/A")
        components = getattr(air_pollution, "current_pollution_level", "N/A")
        return (
            "\n--- AIR POLLUTION ---\n"
            f"Air quality index: {values}\n"
            f"Pollution level: {components}"
        )

    @staticmethod
    def humidity_by_day(forecast, days=3):
        """Group the first humidity readings by local calendar day."""
        grouped = collections.defaultdict(list)
        for item in forecast:
            date = datetime.datetime.fromtimestamp(
                item.reference_time(), datetime.timezone.utc
            ).date()
            if len(grouped) < days or date in grouped:
                grouped[date].append(item.humidity)
            if len(grouped) == days and date not in grouped:
                break

        return {
            date: sum(values) / len(values)
            for date, values in grouped.items()
        }


def init_plot(axis):
    """Set labels and title for the humidity chart."""
    axis.set_ylabel("Average humidity (%)")
    axis.set_title("Three-day humidity forecast")
    axis.set_ylim(0, 100)


def write_humidity_on_bar_chart(axis, bars, values):
    """Write humidity percentages above each bar."""
    for bar, value in zip(bars, values):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{value:.0f}%",
            ha="center",
        )


def plot_temperatures(humidity_data):
    """Display the three-day humidity bar chart."""
    import matplotlib.pyplot as plt # type: ignore

    dates = list(humidity_data)
    values = list(humidity_data.values())
    figure, axis = plt.subplots(figsize=(8, 5))
    bars = axis.bar([date.strftime("%a\n%d %b") for date in dates], values)
    init_plot(axis)
    write_humidity_on_bar_chart(axis, bars, values)
    figure.tight_layout()
    plt.show()


def display_city_weather(app, city, country=None):
    """Retrieve and print weather details for a city."""
    city_id = app.city_id(city, country)
    weather = app.current_weather(city_id)
    print(app.format_weather(weather, city))
    print(app.format_air_pollution(app.air_pollution(weather)))

    forecast = app.forecast(city_id)
    print(f"\nForecast entries available: {len(forecast)}")
    return forecast


def prompt_for_api_key():
    """Read the API key from the environment or ask the user for it."""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if api_key:
        return api_key

    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    if api_key:
        os.environ["OPENWEATHERMAP_API_KEY"] = api_key
    return api_key


def main():
    try:
        api_key = prompt_for_api_key()
        if not api_key:
            raise ValueError("No API key provided. Set OPENWEATHERMAP_API_KEY or enter one.")

        app = WeatherApp(api_key)

        paris_forecast = display_city_weather(app, "Paris", "FR")

        city = input("\nEnter a city to check: ").strip()
        if city:
            display_city_weather(app, city)

        show_chart = input("Show the three-day humidity chart? (y/n): ").strip().lower()
        if show_chart == "y":
            plot_temperatures(app.humidity_by_day(paris_forecast))

    except (RuntimeError, ValueError, OSError, ImportError, AttributeError) as error:
        print(f"Weather app error: {error}")


if __name__ == "__main__":
    main()
