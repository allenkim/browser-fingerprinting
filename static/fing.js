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

addRow("Screen Size and Color Depth", getScreenResolution().join('x'));
addRow("Platform", getPlatform());
addRow("Language", getLanguage());
addRow("Time Zone", getTimeZone());

