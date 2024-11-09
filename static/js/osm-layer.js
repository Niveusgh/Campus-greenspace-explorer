const osmFeatures = {
    trafficSignals: L.layerGroup(),
    roads: L.layerGroup(),
    buildings: L.layerGroup()
};

// Function to add OSM features to map
function addOSMFeatures(map) {
    // Traffic Signals
    const trafficSignalsCoords = [
        [38.0344394, -84.5068278],
        [38.0415300, -84.5038430],
        [38.0324040, -84.4990170]
        // Add more coordinates from your OSM data
    ];

    trafficSignalsCoords.forEach(coord => {
        L.marker(coord, {
            icon: L.divIcon({
                className: 'traffic-signal',
                html: '🚦',
                iconSize: [20, 20]
            })
        }).addTo(osmFeatures.trafficSignals);
    });

    // Roads (example path)
    const roadPath = [
        [38.0393634, -84.5046194],
        [38.0385410, -84.5037010],
        [38.0384000, -84.5035200],
        [38.0383170, -84.5034050]
        // Add more coordinates from your OSM data
    ];

    L.polyline(roadPath, {
        color: '#666',
        weight: 3
    }).addTo(osmFeatures.roads);

    // Add all layers to map
    Object.values(osmFeatures).forEach(layer => layer.addTo(map));
}

// Export for use in other files
export { osmFeatures, addOSMFeatures };