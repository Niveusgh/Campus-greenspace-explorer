// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {
    // Function to initialize the application
    function initApp() {
        console.log('CampusGreen application initialized');
        setupNavigation();
        setupMapIfPresent();
    }

    // Function to set up responsive navigation
    function setupNavigation() {
        const navToggle = document.querySelector('.nav-toggle');
        const navMenu = document.querySelector('nav ul');

        if (navToggle && navMenu) {
            navToggle.addEventListener('click', function() {
                navMenu.classList.toggle('show');
            });
        }
    }

    // Function to set up the map if the map container is present
    function setupMapIfPresent() {
        const mapContainer = document.getElementById('map-container');
        if (mapContainer) {
            // Here you would typically initialize your map
            // For example, if using Leaflet.js:
            // const map = L.map('map-container').setView([38.0406, -84.5037], 13);
            // L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
            console.log('Map container found. Map would be initialized here.');
        }
    }

    // Function to fetch green space data (placeholder)
    function fetchGreenSpaceData() {
        // This would typically be an API call
        console.log('Fetching green space data...');
        // Simulating an API call with setTimeout
        setTimeout(() => {
            console.log('Green space data fetched!');
        }, 1000);
    }

    // Initialize the application
    initApp();

    // Expose functions to global scope if needed
    window.CampusGreen = {
        fetchGreenSpaceData: fetchGreenSpaceData
    };
});