// link a documentación oficial https://developers.google.com/maps/documentation/javascript/places

// Se utiliza para entregar las coordenadas de la ubicación ingresada y entregar un autocompletado para garantizar la precisión de esta
function initialize() {
    var form = document.getElementById('id_direccion');
    var autocomplete = new google.maps.places.Autocomplete(form);
    google.maps.event.addListener(autocomplete, 'place_changed', function () {
        var place = autocomplete.getPlace();
        document.getElementById('id_ciudad').value = place.name;
        document.getElementById('id_lat').value = place.geometry.location.lat();
        document.getElementById('id_lng').value = place.geometry.location.lng();
        //alert("This function is working!");
        //alert(place.name);
       // alert(place.address_components[0].long_name);

    });
}
google.maps.event.addDomListener(window, 'load', initialize); 