/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */

/* Script for courses dropdown */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
  var myDropdown = document.getElementById("myDropdown");
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }
}

/* Script for placement dropdown */
function myPlacement() {
  document.getElementById("myPlacement").classList.toggle("p-show");
}
window.onclick = function(e) {
  if (!e.target.matches('.drpbtn-placement')) {
  var placement = document.getElementById("myPlacement");
    if (placement.classList.contains('p-show')) {
      placement.classList.remove('p-show');
    }
  }
}
