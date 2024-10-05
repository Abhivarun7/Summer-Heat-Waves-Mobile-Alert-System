import React from 'react';
import './WeatherAlert.css';

const WeatherAlert = ({ alert }) => {
    return (
        <div className="alert">
            {alert}
        </div>
    );
};

export default WeatherAlert;
