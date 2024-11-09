import React from 'react'
import { MapContainer, TileLayer } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

function MapApp() {
  // Center coordinates for UK campus
  const position = [38.0406, -84.5037]
  
  return (
    <div style={{ height: "100vh", width: "100%" }}>
      <MapContainer 
        center={position} 
        zoom={16} 
        style={{ height: "100%", width: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
      </MapContainer>
    </div>
  )
}

export default MapApp