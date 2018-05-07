var table = document.getElementById('browser-info');

function addRow(label, value){
  var new_row = table.insertRow(table.rowIndex);
  new_row.insertCell(0).innerHTML = label;
  new_row.insertCell(1).innerHTML = value;
}

function getScreenResolution(){
	if (window.screen.width < window.screen.height)
		return [window.screen.height, window.screen.width, window.screen.colorDepth];
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

function getFontsSupported(){
	var detector = new Detector();
	var fonts = [
          'Andale Mono', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial MT', 'Arial Narrow', 'Arial Rounded MT Bold', 'Arial Unicode MS',
          'Bitstream Vera Sans Mono', 'Book Antiqua', 'Bookman Old Style',
          'Calibri', 'Cambria', 'Cambria Math', 'Century', 'Century Gothic', 'Century Schoolbook', 'Comic Sans', 'Comic Sans MS', 'Consolas', 'Courier', 'Courier New',
          'Geneva', 'Georgia',
          'Helvetica', 'Helvetica Neue',
          'Impact',
          'Lucida Bright', 'Lucida Calligraphy', 'Lucida Console', 'Lucida Fax', 'LUCIDA GRANDE', 'Lucida Handwriting', 'Lucida Sans', 'Lucida Sans Typewriter', 'Lucida Sans Unicode',
          'Microsoft Sans Serif', 'Monaco', 'Monotype Corsiva', 'MS Gothic', 'MS Outlook', 'MS PGothic', 'MS Reference Sans Serif', 'MS Sans Serif', 'MS Serif', 'MYRIAD', 'MYRIAD PRO',
          'Palatino', 'Palatino Linotype',
          'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Symbol',
          'Tahoma', 'Times', 'Times New Roman', 'Times New Roman PS', 'Trebuchet MS',
          'Verdana', 'Wingdings', 'Wingdings 2', 'Wingdings 3'
        ];
	detected = "";
	fonts.forEach(function(font){
		if (detector.detect(font))
			detected += font + ', ';
	});
	if (detected != "")
		detected = detected.slice(0,-2);
	return detected;
}

addRow("Screen Size and Color Depth", getScreenResolution().join('x'));
addRow("Platform", getPlatform());
addRow("Language", getLanguage());
addRow("Time Zone", getTimeZone());
addRow("Touch Capable", getTouchCapability());
addRow("Cookie Supported", getCookieSupport());
addRow("Fonts Supported", getFontsSupported());
addRow("Canvas Fingerprint", x64hash128(getCanvasFingerprint(),42));
addRow("WebGL Fingerprint", x64hash128(getWebglFingerprint(),42));




var plat = getPlatform();
var screen = getScreenResolution().join('x');
var lang = getLanguage();
var time = getTimeZone();
var touch = getTouchCapability();
var cookie = getCookieSupport();
var fonts = x64hash128(getFontsSupported(),42);
var canvas = x64hash128(getCanvasFingerprint(),42);
var webgl = x64hash128(getWebglFingerprint(),42);
var hash = x64hash128(plat+screen+lang+time+touch+cookie+fonts+canvas+webgl,42);


$.ajax({
	url: '/results',
	type: 'POST',
	contentType: 'application/json',
	data: JSON.stringify({
		"platform" : plat,
		"screen": screen,
		"lang": lang,
		"time": time,
		"touch": touch,
		"cookie": cookie,
		"fonts": fonts,
		"canvas": canvas,
		"webgl": webgl,
        "hash": hash
		}),
	dataType: 'json',
	success: function(result){
		var visitor = result["visitor"];
		var seen = result["seen"];
		console.log(result)
		var display = "Visitor Number: " + visitor;
		if (seen)
			display += " - You have been here before!";
		$('#visitor').text(display);
	}
});

