// Solar System - DOM Creation Challenge
// Array of planet objects with moon information
const planets = [
  { name: "Mercury", moons: 0, color: "mercury" },
  { name: "Venus", moons: 0, color: "venus" },
  { name: "Earth", moons: 1, color: "earth" },
  { name: "Mars", moons: 2, color: "mars" },
  { name: "Jupiter", moons: 79, color: "jupiter" },
  { name: "Saturn", moons: 83, color: "saturn" },
  { name: "Uranus", moons: 27, color: "uranus" },
  { name: "Neptune", moons: 14, color: "neptune" },
];

// Define planet colors
const planetStyles = `
  .mercury { background-color: #8c7853; }
  .venus { background-color: #ffc649; }
  .earth { background-color: #4a90e2; }
  .mars { background-color: #e27b58; }
  .jupiter { background-color: #c88b3a; }
  .saturn { background-color: #fad5a5; }
  .uranus { background-color: #4fd0e7; }
  .neptune { background-color: #4166f5; }
`;

// Add styles to the document
if (typeof document !== "undefined") {
  const styleSheet = document.createElement("style");
  styleSheet.textContent = planetStyles;
  document.head.appendChild(styleSheet);

  // Get the section to append planets
  const listPlanetsSection = document.querySelector(".listPlanets");

  if (listPlanetsSection) {
    // Loop through each planet
    planets.forEach((planet) => {
      // Create planet div
      const planetDiv = document.createElement("div");
      planetDiv.classList.add("planet", planet.color);
      planetDiv.textContent = planet.name;
      planetDiv.style.color = "white";
      planetDiv.style.fontSize = "12px";
      planetDiv.style.fontWeight = "bold";

      // Create moons for this planet
      if (planet.moons > 0) {
        // Position moons in a circle around the planet
        for (let i = 0; i < planet.moons; i++) {
          const moon = document.createElement("div");
          moon.classList.add("moon");

          // Calculate position in a circle around the planet
          const angle = (i / planet.moons) * Math.PI * 2;
          const radius = 50;
          const x = Math.cos(angle) * radius + 50 - 15; // Center moon
          const y = Math.sin(angle) * radius + 50 - 15; // Center moon

          moon.style.left = x + "px";
          moon.style.top = y + "px";

          planetDiv.appendChild(moon);
        }
      }

      // Append planet to section
      listPlanetsSection.appendChild(planetDiv);
    });
  }
}
