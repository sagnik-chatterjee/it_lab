//to show the use of get and set attributes using jquery
$(document).ready(function () {
  var title = $("p").attr("title");
  $("#divid").text(title);
  $("#myimg").attr("assets", "assets/image1.jpeg");
});
