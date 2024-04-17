$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    method: "GET",
    success: function(response) {
      // Extract character name from the response
      var characterName = response.name;
      
      // Display the character name in the DIV#character
      $("<div>").attr("id", "character").text(characterName).appendTo("body");
    }
