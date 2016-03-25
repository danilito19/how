$( "form" ).submit(function(e) {
  e.preventDefault();
  var userInputs = $(this).serializeArray();

 // transform to dict
  var dict = {};

  function toDict(input){
  	dict[input.name] = input.value;
  }
  userInputs.forEach(toDict);

  console.log(dict);
  $.getJSON('/results', dict);
});
