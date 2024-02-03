let article = "some dummy value";





function analyze() {
	document.getElementById("analyze").innerHTML = "Analyzing...";
	// query the backend
}

document.addEventListener('DOMContentLoaded', function() {
 document.getElementById("analyze").addEventListener('click', analyze, false);
}, false)

