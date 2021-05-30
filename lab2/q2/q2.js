function showAlert() {
  if ($("#myAlert").find("div#myAlert2").length == 0) {
    $("#myAlert").append(
      "<div class='alert alert-success alert-dismissable' id='myAlert2'> <button type='button' class='close' data-dismiss='alert'  aria-hidden='true'>&times;</button> About to Edit!!</div>"
    );
  }
  $("#myAlert").css("display", "");
  Window.alert();
}
function showDelete() {
  if ($("#myAlert").find("div#myAlert2").length == 0) {
    $("#myAlert").append(
      "<div class='alert alert-success alert-dismissable' id='myAlert2'> <button type='button' class='close' data-dismiss='alert'  aria-hidden='true'>&times;</button> About to Delete!!</div>"
    );
  }
  $("#myAlert").css("display", "");
  Window.alert();
}
