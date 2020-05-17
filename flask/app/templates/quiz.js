document.getElementById("kek").onchange = function() {
  document.getElementById("additional").hidden = this.value !== "OK";
}