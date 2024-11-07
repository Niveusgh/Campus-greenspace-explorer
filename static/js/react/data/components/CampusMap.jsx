import React, { useState } from 'react';

const CampusMap = () => {
  const [selectedSpace, setSelectedSpace] = useState(null);

  return (
    <div className="relative h-screen bg-[#191A1C]"> {/* Using your dark theme background */}
      {/* Simple SVG Map Container */}
      <div className="absolute inset-0 z-0">
        <div className="relative w-full h-full">
          {/* Base layers */}
          <img 
            src="/static/images/map/Buildings.svg" 
            className="absolute inset-0 w-full h-full" 
            alt="Campus Buildings"
          />
          <img 
            src="/static/images/map/Paths.svg" 
            className="absolute inset-0 w-full h-full" 
            alt="Campus Paths"
          />
          {/* Interactive Green Spaces */}
          <img 
            src="/static/images/map/Green-Spaces.svg" 
            className="absolute inset-0 w-full h-full hover:cursor-pointer" 
            alt="Green Spaces"
            onClick={() => setSelectedSpace('demo-space')}
          />
        </div>
      </div>

      {/* Simple Info Panel for Demo */}
      {selectedSpace && (
        <div className="absolute bottom-4 left-4 right-4 bg-white rounded-lg shadow-lg p-4 mx-4">
          <h3 className="text-lg font-semibold">Demo Green Space</h3>
          <p className="text-gray-600">This is a demo description. Tree data coming soon!</p>
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