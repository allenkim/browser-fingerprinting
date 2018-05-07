var table = document.getElementById('browser-info');

function addRow(label, value){
  var new_row = table.insertRow(table.rowIndex);
  new_row.insertCell(0).innerHTML = label;
  new_row.insertCell(1).innerHTML = value;
  
}

function getScreenResolution(){
  return [window.screen.width, window.screen.height, window.screen.colorDepth];
}

function getPlatform(){
	return navigator.platform;
}

function getLanguage(){
	if (navigator.languages)
		return navigator.languages[0];
    return navigator.language || navigator.userLanguage;
}

function getTimeZone(){
	tz = jstz.determine()
	return tz.name();
}

function getTouchCapability(){
	return 'ontouchstart' in window ||
	window.DocumentTouch && document instanceof window.DocumentTouch ||
	navigator.maxTouchPoints > 0 ||
	window.navigator.msMaxTouchPoints > 0;
}

function getCookieSupport(){
    var cookieEnabled = navigator.cookieEnabled;
    if (navigator.cookieEnabled == null && !cookieEnabled){ 
        document.cookie = "test";
        cookieEnabled = document.cookie.indexOf("test") != -1;
    }
    return cookieEnabled;
}

addRow("Screen Size and Color Depth", getScreenResolution().join('x'));
addRow("Platform", getPlatform());
addRow("Language", getLanguage());
addRow("Time Zone", getTimeZone());
addRow("Touch Capable", getTouchCapability());
addRow("Cookie Supported", getCookieSupport());
var a = 5



//$(function() {
 //   $('button').click(function() {
//            var user = $('#txtUsername').val();
//            var pass = $('#txtPassword').val();
//            $.ajax({
//                url: '1247.0.0.1:5000/signUpUser',
//                data: $('form').serialize(),
//                type: 'POST',
//                success: function(response) {
 //                   console.log(response);
   //             },
     //           error: function(error) {
       //             console.log(error);
//                }
//            });
 //    });
//});

var a = 'apwoi'
$.ajax({
         url: 'http://127.0.0.1:5000/',
         type: 'POST',
         data: {'hello': 5}
        });
