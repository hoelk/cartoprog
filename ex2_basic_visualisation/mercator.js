function deg_rad(ang) {
  return ang * (Math.PI/180.0);
}
// simple spherical mercator proj.: [lat,lng]->[[0..1],[0..1]]
function project_mercator(latlng) {
  var lat = deg_rad(latlng[0]);
  var lng = deg_rad(latlng[1]);
  var x = lng / 2.0 / Math.PI + 0.5;
  var y = Math.log((Math.sin(lat) + 1.0) /
          Math.cos(lat)) / 2.0 / Math.PI + 0.5;
  return [x, y];
}
