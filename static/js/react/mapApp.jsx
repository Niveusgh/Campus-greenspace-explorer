import React from 'react';
import { createRoot } from 'react-dom/client';
import CampusMap from './components/CampusMap';

const container = document.getElementById('map-root');
const root = createRoot(container);
root.render(<CampusMap />);