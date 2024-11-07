import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Polygon, Marker, Tooltip, useMapEvents } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { greenSpaces } from '../data/greenSpaces';

// Helper component to capture clicks for defining new areas
const PolygonCreator = ({ onPointAdded }) => {
  useMapEvents({
    click: (e) => {
      const { lat, lng } = e.latlng;
      onPointAdded([lat, lng]);
    },
  });
  return null;
};

const CampusMap = () => {
  const [selectedSpace, setSelectedSpace] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [currentPolygon, setCurrentPolygon] = useState([]);
  const [trees, setTrees] = useState([]); // Will hold tree data from your CSV

  // Function to handle adding points to create a new green space
  const handlePointAdded = (point) => {
    if (isEditing) {
      setCurrentPolygon([...currentPolygon, point]);
    }
  };

  // Function to complete polygon creation
  const completePolygon = () => {
    if (currentPolygon.length >= 3) {
      console.log('New Green Space Coordinates:', currentPolygon);
      // You can copy these coordinates to your greenSpaces.js file
      setCurrentPolygon([]);
    }
    setIsEditing(false);
  };

  return (
    <div className="relative h-screen">
      {/* Editor Controls */}
      <div className="absolute top-4 right-4 z-[1000] bg-white p-4 rounded-lg shadow">
        <button
          onClick={() => setIsEditing(!isEditing)}
          className="px-4 py-2 bg-blue-500 text-white rounded"
        >
          {isEditing ? 'Cancel' : 'Define New Area'}
        </button>
        {isEditing && (
          <button
            onClick={completePolygon}
            className="ml-2 px-4 py-2 bg-green-500 text-white rounded"
          >
            Complete Area
          </button>
        )}
      </div>

      <MapContainer
        center={[38.038, -84.504]} // UK campus center
        zoom={17}
        className="h-full"
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; OpenStreetMap contributors'
        />

        {/* Show existing green spaces */}
        {greenSpaces.map((space) => (
          <Polygon
            key={space.id}
            positions={space.coordinates}
            pathOptions={{
              color: selectedSpace === space.id ? '#2c5282' : '#48bb78',
              fillColor: selectedSpace === space.id ? '#2b6cb0' : '#68d391',
              fillOpacity: 0.5,
            }}
            eventHandlers={{
              click: () => setSelectedSpace(space.id),
            }}
          >
            <Tooltip>{space.name}</Tooltip>
          </Polygon>
        ))}

        {/* Show current polygon being created */}
        {isEditing && currentPolygon.length > 0 && (
          <Polygon
            positions={currentPolygon}
            pathOptions={{
              color: '#e53e3e',
              fillColor: '#fc8181',
              fillOpacity: 0.5,
            }}
          />
        )}

        {/* Markers for polygon points being created */}
        {isEditing && currentPolygon.map((point, index) => (
          <Marker key={index} position={point}>
            <Tooltip permanent>Point {index + 1}</Tooltip>
          </Marker>
        ))}

        <PolygonCreator onPointAdded={handlePointAdded} />
      </MapContainer>

      {/* Info Panel */}
      {selectedSpace && !isEditing && (
        <div className="absolute bottom-4 left-4 right-4 bg-white rounded-lg shadow-lg p-4 mx-4">
          <h3 className="text-lg font-semibold">
            {greenSpaces.find(s => s.id === selectedSpace)?.name}
          </h3>
          <p className="text-gray-600">
            {greenSpaces.find(s => s.id === selectedSpace)?.description}
          </p>
          <button
            onClick={() => setSelectedSpace(null)}
            className="mt-2 text-sm text-blue-600"
          >
            Close
          </button>
        </div>
      )}
    </div>
  );
};

export default CampusMap;