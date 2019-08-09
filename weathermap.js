var ourLoc;
var view;
var map;

function init(){
  //initialize things here
ourLoc=ol.proj.fromLonLat([0,0]);
view =new ol.View({
center: ourLoc,
zoom: 6});

  map = new ol.Map({
target: 'map',
layers: [
  new ol.layer.Tile({
      source: new ol.source.OSM()
      })
  ],
  loadTilesWhileAnimating: true,
  view: view
  });
  }
  function panHome(){
  view.animate({
    center: ourLoc,
    duration:10000
  })
  }
  function panToLocation(){
    var countryName=document.getElementById("country-name").value;
    if(countryName===""){
      alert("you didn't enter a country name!");
      return;
    }
var query ="https://restcountries.eu/rest/v2/name/"+countryName;
//step5.3
query = query.replace(/ /g, "%20")
alert(query);
//step5.1
var countryRequest =new XMLHttpRequest();
countryRequest.open('GET',query,false);
//step 5.2
countryRequest.send();

// alert("Ready State "+ countryRequest.readyState);
// alert("Status "+ countryRequest.status);
// alert("Response "+countryRequest.responseText);
//step 6.1: first we should only pan if the information was correct:
if(countryRequest.readyState !=4 || countryRequest.status !=200 || countryRequest.responseText== ""){
  windoe.console.error("request had an error!");
  return;
}
//step 6.2 funtion in order to use the data
var countryInformation = JSON.parse(countryRequest.responseText);
//6.3 figure out where this information is based
var lat= countryInformation[0].latlng[0];
var lon= countryInformation[0].latlng[1];
var lon= 0.0;
var lat=0.0;
//lat is index 0
window.console.log(countryName + ": lon " + lon + " & lat " + lat);
var location= ol.proj.fromLonLat([lon,lat]);
view.animate({
  center:location, //Location
  duration:2000//two seconds
});

   }
  window.onload=init;
