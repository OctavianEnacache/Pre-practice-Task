if (typeof msg.payload === 'object' && msg.payload !== null && 'temperature' in msg.payload && 'humidity' in msg.payload) {
    // Extract temperature and humidity values
    let temperature = msg.payload.temperature;
    let humidity = msg.payload.humidity;

    // Create a new message suitable for InfluxDB
    let influxMessage = {
        measurement: "sensor_data",
        fields: {
            temperature: temperature,
            humidity: humidity
        },
        tags: {
            device: "Octavian-Enacache"
        },
        timestamp: new Date().getTime() * 1000000 // Convert to nanoseconds
    };

    // Set the new message as the output
    msg.payload = influxMessage;
    return msg;
} else {
    // Log an error if the payload is not as expected
    node.error("Payload is not a valid object or missing required fields", msg);
    return null; // Stop further processing
}
