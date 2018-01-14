var map, infoWindow;
function initMap() {
  var myLatLng = {lat: 57.723219, lng: -100.898438};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 5,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Canada'
  });
  infoWindow = new google.maps.InfoWindow;

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

	  var map = new google.maps.Map(document.getElementById('map'), {
		    zoom: 13,
		    center: pos
	  });
	  var marker = new google.maps.Marker({
	    position: pos,
	    map: map,
	    draggable: true,
	    title: 'My current location'
	  });
      
      //Add listener
google.maps.event.addListener(marker, "click", function (event) {
    var latitude = event.latLng.lat();
    var longitude = event.latLng.lng();
    infoWindow.setContent('<div>Current Location: </div><div>' + latitude + ', ' + longitude + '</div>');
    infoWindow.open(map, marker);
    addLocation(latitude + ',' + longitude);
}); //end addListener
      
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}

function addLocation(location){
	$("#id_location").text(location);
}

