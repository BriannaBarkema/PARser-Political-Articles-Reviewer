let article = 'El Salvador voters stand poised to re-elect their current president and self-styled "world’s coolest dictator" Nayib Bukele in a landslide victory after he rehabilitated his country’s crime-ridden reputation.'
const URL = "PARser.com/analyze"
function analyze() {
	// query the backend
	document.getElementById("analyze").innerHTML = "Analyzing...";
	fetch(URL, {
		method: "POST",
		body: JSON.stringify({
			article: article
		}),
		headers: {
			"Content-type": "application/json; charset-UTF-8"
		}
	}).then((response) => response.json())
	  .then((json) => console.log(json));
}



document.addEventListener('DOMContentLoaded', function() {
 document.getElementById("analyze").addEventListener('click', analyze, false);
}, false)


