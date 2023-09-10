document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('cityInput');
    const getWeatherButton = document.getElementById('getWeather');
    const weatherResult = document.getElementById('weatherResult');
    
    getWeatherButton.addEventListener('click', function() {
        const city = cityInput.value;
        if (city.trim() === '') {
            alert('Please enter a city name.');
            return;
        }
        
        
        const apiKey = '5faf06aa987d03f35face96a53edb0ac';
        const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const temperature = data.main.temp;
                const description = data.weather[0].description;
                const resultText = `Weather in ${city}: ${temperature}°C, ${description}`;
                weatherResult.textContent = resultText;
            })
            .catch(error => {
                console.error('Error fetching weather data:', error);
                weatherResult.textContent = 'An error occurred while fetching weather data.';
            });
    });
});
