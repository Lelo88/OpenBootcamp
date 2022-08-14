let markers, map;

function initMap() {
  const posicion = {
    lat: -25.363,
    lng: 131.044,
  };

  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: posicion,
  });

  markers.push(
    new google.maps.Marker({
      position: {
        lat: 37.439686729054216, //37.439686729054216, 25.36270586926207
        lng: 25.36270586926207,
      },
      map,
      title: "Mykonos",
    })
  );
  markers.push(
    new google.maps.Marker({
      position: {
        lat: 64.14492028287056, // 64.14492028287056, -21.931452917532045
        lng: -21.931452917532045,
      },
      map,
      title: "Reikjavik",
    })
  );
  markers.push(
    new google.maps.Marker({
      position: {
        lat: 46.9564240151278,  //46.9564240151278, 7.857789029310217
        lng:  7.857789029310217,
      },
      map,
      title: "Suiza",
    })
  );
}