//const APIProvider = window.location.protocol + "//" + window.location.host + "/";
const APIProvider = "https://" + window.location.host + "/";

/*********************************************************/
/* Standard Functions 									 */
/*********************************************************/
function dynamicGETQuery (RequestURL) {
	return $.ajax({
        url: RequestURL,
        type: 'GET',
        dataType: 'json', // added data type
    });
}

function dynamicPostQuery (RequestURL, JSONData) {
    console.log(JSON.stringify(JSONData));
	return $.ajax({
		type: 'POST',
		async: true,
        contentType: 'application/json',
		url: RequestURL,
		data: JSON.stringify(JSONData),
	});
}

function viewcase()
{
	var cta = document.getElementById("cta-case-id").value;
	alert(cta);
}