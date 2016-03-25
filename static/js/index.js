// $('button').click(function(e){
//     e.preventDefault();



// 	console.log(home);

// 	// document.getElementById('priorities').value = priority_list;
// 	// $('#priorities-form').attr('action', "./preferences_citysize/").submit();
// });
// console.log('loaded index.js');
// var myButton = document.querySelector('button');
// myButton.onclick = function(e) {
// 	e.preventDefault();
//   console.log('hello');
// }

$( "form" ).submit(function(e) {
  e.preventDefault();
  var userInputs = $(this).serializeArray();
  // [{name: 'homezip', value: 75989}, {name: 'workzip', value: 83729}]

  // userInputs.map(function(input){return input.values;})
  // this returns only values: [38923, 839483, 238]

 // transform to dict
  var dict = {};

  function toDict(input){
  	dict[input.name] = input.value;
  }
  userInputs.forEach(toDict);

  // function dictToString(inputDict) {
  // 	var outputString = '';
  // 	Object.keys(inputDict).forEach(function(key){
  // 		outputString = outputString + inputDict[key] + ' ';
  // 	});
  // 	return outputString;
  // }

  console.log('about to send ajax request');
  console.log(dict);
  $.getJSON('/results', dict, function (data) {
  	console.log('got back the ajax request: ', data);
	});
});
