// main.js
// 41.805307040904246, -72.25443342893335

const mapViewOptions = {
    element: document.getElementById('map'),
    center: { lat: 41.805307040904246, lng: -72.25443342893335 }, // Gampel Pavilion
    zoom: 20,
    maxZoom: 25,
  };
const mapViewInstance = new mapsindoors.mapView.GoogleMapsView(mapViewOptions);
const mapsIndoorsInstance = new mapsindoors.MapsIndoors({ mapView: mapViewInstance });
const googleMapsInstance = mapViewInstance.getMap();

// Floor Selector
const floorSelectorElement = document.createElement('div');
new mapsindoors.FloorSelector(floorSelectorElement, mapsIndoorsInstance);
googleMapsInstance.controls[google.maps.ControlPosition.RIGHT_TOP].push(floorSelectorElement);