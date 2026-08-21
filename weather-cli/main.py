import python_weather # type: ignore
import asyncio


async def main(city: str) -> None:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        try:
            weather = await client.get(city)

            print(f"The weather conditions in {weather.location}, {weather.country} are {weather.kind} with {weather.temperature}°C")
            print(f"{weather.humidity}% humidity with wind {weather.wind_speed}km/h in the {weather.wind_direction} direction")

        except python_weather.errors.RequestError:
            print('Couldn\'t find a city with that name')


if __name__ == '__main__':
    while True:
        city = input('Enter city (q to quit): ')

        if city.lower() == 'q':
            break

        asyncio.run(main(city))