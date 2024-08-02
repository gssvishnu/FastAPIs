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
    $('#profileclass').css('display','none');
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


/*********************************************************/
/* Generate Verdict, Affidavit based on inputs 			 */
/*********************************************************/
const myInput = document.getElementById('claim-amount-2');
myInput.onpaste = e => e.preventDefault();
 
var form = document.getElementById("upload-newcase-form");
form.addEventListener('submit', GenerateVerdict);

const button = document.getElementById('submitCase');
button.addEventListener('click', SubmitCase);

const datePicker = document.getElementById('processingDate');
datePicker.valueAsDate = new Date();

/*
const inputElement = document.getElementById('days-Left');
inputElement.addEventListener('input', (event) => {
	var DaysLeft = parseInt($("#days-Left").val().trim(), 10);
	var currentDate = new Date();
	currentDate.setDate(currentDate.getDate() + DaysLeft);
	const Deadline = document.getElementById('initialDeadline');
	Deadline.valueAsDate = currentDate;
});
*/

const inputElement = document.getElementById('initialDeadline');
inputElement.addEventListener('input', (event) => {
	oneDay	= 1000 * 60 * 60 * 24;
	date1	= new Date($("#initialDeadline").val().trim()).getTime();
	date2	= new Date($("#processingDate").val().trim()).getTime();
	
	$("#days-Left").val(Math.abs((date1 - date2) / (oneDay)));
	
});
		
function GetFormData ()
{
	var JSONData = Object();
	
	JSONData['processingDate']				= $("#processingDate").val().trim();
	JSONData['cta_case_id']					= $("#cta-case-id").val().trim();
	JSONData['cta_case_single_multiple']	= $('input[name="cta-case-single-multiple"]:checked').val();
	JSONData['additional_cta_ids']			= $("#additional-cta-ids").val().trim();
	JSONData['any_other_cta']				= $('input[name="any-other-cta"]:checked').val();
	JSONData['applicant_name']				= $("#applicant-name").val().trim();
	JSONData['cas_id_yes_no']				= $('input[name="cas-id-yes-no"]:checked').val();
	JSONData['number_cas_ids']				= $("#number-cas-ids").val().trim();
	JSONData['additional_cas_ids']			= $("#additional-cas-ids").val().trim();
	JSONData['initialDeadline']				= $("#initialDeadline").val().trim();
	JSONData['days_Left']					= $("#days-Left").val().trim();
	JSONData['reason_claim']				= $("#reason-claim :selected").text();
	JSONData['baggage_claim_number']		= $("#baggage-claim-number").val().trim();
	JSONData['primary_reason']          	= $("#primary-reason :selected").text();
	JSONData['secondary_reason']          	= $("#secondary-reason :selected").text();
	JSONData['claim_amount']				= $("#claim-amount").val().trim();
	JSONData['total_delay']					= $("#total-delay").val().trim();
	JSONData['flight_date']					= $("#flight-date").val().trim();
	JSONData['additional_docs']				= $("#additional-docs").val().trim();
	JSONData['duplicate_case_yes_no']		= $('input[name="duplicate-case-yes-no"]:checked').val();
	
	return JSONData;
}

function GenerateVerdict (event)
{
	event.preventDefault();
	var ClaimAmount1 = $("#claim-amount").val().trim();
	var ClaimAmount2 = $("#claim-amount-2").val().trim();
	if (ClaimAmount1 != ClaimAmount2) {
		alert("Verify Claim amount entered in both the textboxes..!!");
		return;
	}
	$('#LoaderForGenerate').css('visibility', 'visible');
	JSONData = GetFormData();
	console.log(JSONData);
	RequestURL = APIProvider + "GetVerdict";
	console.log(RequestURL);
	var Request = dynamicPostQuery(RequestURL, JSONData);
	Request.done(function (response) {
		console.log(response);
		$('#verdict').val(response['verdict']);
		$("input[name=affidavit-required-yes-no][value=" + response['IsAffidavit'] + "]").prop('checked', true);
		$('#affidavit-type').val(response['AffidavitType']);
		/* Copy additional_docs to evidenceMissing */
		$('#evidenceMissing').val(JSONData['additional_docs']);
		$('#submitButtonArea').css("visibility", "visible");
		$('#LoaderForGenerate').css('visibility', 'hidden');
	});
}

function SubmitCase (event)
{
	event.preventDefault();
	$('#LoaderForSubmit').css('visibility', 'visible');
	
	JSONData = GetFormData();
	JSONData['verdict'] 						= $("#verdict").val().trim();
	JSONData['affidavit_required_yes_no']		= $('input[name="affidavit-required-yes-no"]:checked').val();
	JSONData['affidavit_type'] 					= $("#affidavit-type").val().trim();
	JSONData['evidenceMissing'] 				= $("#evidenceMissing").val().trim();
	
	RequestURL = APIProvider + "SubmitCase";
	console.log(RequestURL);
	var Request = dynamicPostQuery(RequestURL, JSONData);
	Request.done(function (response) {
		console.log(response);
		$('#LoaderForSubmit').css('visibility', 'hidden');
		if (response == "success") {
			$('#submissionStatus').empty().append("<font color=\"green\">New Case Uploaded successfully, page will reload in 5 seconds!!</font>");
			setTimeout(function() {
				window.location.reload();
			}, 5000);
		}
		else
			$('#submissionStatus').empty().append("<font color=\"red\">Failed to upload case to Backend DB, contact Admin..!!</font>");
	});
}
