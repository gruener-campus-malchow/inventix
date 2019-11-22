document.addEventListener("DOMContentLoaded", function(event) {



document.getElementById("benutzerbutton").addEventListener("click", function(e){
	document.getElementById("userinfos").style.visibility = "visible";
})    
document.getElementById("closeprofil").addEventListener("click", function(e){
	document.getElementById("userinfos").style.visibility = "hidden";
})    	

document.getElementById("userinfos").addEventListener("click", function(e){
	
	if(e.target.id == "userinfos"){
		document.getElementById("userinfos").style.visibility = "hidden";
	}
})

});