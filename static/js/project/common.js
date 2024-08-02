/*********************************************************/
/* Standard Functions 									 */
/*********************************************************/
function LogOut()
{
	let text="Are you sure to Logout..!!\nPress Either Ok or Cancel.";
	if (confirm(text) == true) {
		window.location = "https://" + window.location.host + "/logout";
	} 
}
