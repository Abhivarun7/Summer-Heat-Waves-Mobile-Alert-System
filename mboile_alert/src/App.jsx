import React, { useEffect, useState } from 'react';
import axios from 'axios';
import WeatherAlert from './WeatherAlert';
import './App.css';

const App = () => {
    const [alerts, setAlerts] = useState([]);
    const API_KEY = '4beed707e83d4decbcb141001240510'; // Your WeatherAPI key
    const CITY = 'Hyderabad'; // City for which you want alerts
    const BASE_URL = 'http://api.weatherapi.com/v1/current.json';

    const fetchWeatherData = async () => {
        try {
            const response = await axios.get(BASE_URL, {
                params: { key: API_KEY, q: CITY, aqi: 'no' }
            });
            const weather = response.data.current;
            checkForAlerts(weather);
        } catch (error) {
            console.error('Error fetching weather data:', error);
        }
    };

    const checkForAlerts = (weather) => {
        const newAlerts = [];
        if (weather.temp_c > 35) {
            newAlerts.push('High temperature alert! It is above 35°C.');
        }
        if (weather.humidity > 80) {
            newAlerts.push('High humidity alert! It is above 80%.');
        }
        if (weather.condition.text.includes('Rain')) {
            newAlerts.push('Rain alert! Carry an umbrella.');
        }
        setAlerts(newAlerts);
    };

    useEffect(() => {
        fetchWeatherData();
    }, []);

    return (
        <div className="App">
            <h1>Weather Alerts for {CITY}</h1>
            {alerts.length > 0 ? (
                alerts.map((alert, index) => (
                    <WeatherAlert key={index} alert={alert} />
                ))
            ) : (
                <p>No alerts at the moment.</p>
            )}
        </div>
    );
};

export default App;
