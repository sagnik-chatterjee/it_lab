$(document).ready(function () {
  $(
    "#1,#2,#3,#4,#5,#6,#7,#8,#9,#0,#add,#subtract,#multiply,#divide,#power,#decimal,#para1,#para2"
  ).click(function () {
    var v = $(this).val();
    var total = $("textarea").val($("textarea").val() + v);
  });

  $("#equal").click(function () {
    $("textarea").val(eval($("textarea").val()));
  });

  $("#clear").click(function () {
    $("textarea").val("");
  });

  $("#backspace").click(function () {
    $("textarea").val(
      $("textarea")
        .val()
        .substring(0, $("textarea").val().length - 1)
    );
  });
});
