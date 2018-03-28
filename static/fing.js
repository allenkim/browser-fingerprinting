var table = document.getElementById('browser-info');

function addRow(label, value){
  var new_row = table.insertRow(table.rowIndex);
  new_row.insertCell(0).innerHTML = label;
  new_row.insertCell(1).innerHTML = value;
}

function getScreenResolution(){
  return [window.screen.width, window.screen.height, window.screen.colorDepth]
}

addRow("Screen Size and Color Depth", getScreenResolution().join('x'));
addRow("A","B")
addRow("C","D")
