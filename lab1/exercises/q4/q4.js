$(document).ready(function () {
  $("#bill").click(function () {
    let brand_name = $("#brand-choice").val();
    let quan = $("#quantity").val();
    console.log({ quan });
    let amt = 0;
    let price = 0;
    if (brand_name == "HP") {
      if (
        $("#laptop").prop("checked") == true &&
        $("#mobile").prop("checked") == true
      ) {
        price = 800;
      } else if ($("#laptop").prop("checked") == true) {
        price = 750;
      } else {
        price = 50;
      }
    } else if (brand_name == "Nokia") {
      if (
        $("#laptop").prop("checked") == true &&
        $("#mobile").prop("checked") == true
      ) {
        price = 6000;
      } else if ($("#laptop").prop("checked") == true) {
        price = 5550;
      } else {
        price = 450;
      }
    } else if (brand_name == "Samsung") {
      if (
        $("#laptop").prop("checked") == true &&
        $("#mobile").prop("checked") == true
      ) {
        price = 700;
      } else if ($("#laptop").prop("checked") == true) {
        price = 600;
      } else {
        price = 100;
      }
    } else if (brand_name == "Motorola") {
      if (
        $("#laptop").prop("checked") == true &&
        $("#mobile").prop("checked") == true
      ) {
        price = 150;
      } else if ($("#laptop").prop("checked") == true) {
        price = 25;
      } else {
        price = 125;
      }
    } else {
      if (
        $("#laptop").prop("checked") == true &&
        $("#mobile").prop("checked") == true
      ) {
        price = 700;
      } else if ($("#laptop").prop("checked") == true) {
        price = 200;
      } else {
        price = 500;
      }
    }
    let n = parseInt(quan);
    amt = n * price;
    if (isNaN(amt)) {
      alert("Please select something to buy!!!");
    } else {
      alert("Price = " + amt);
    }
  });
});
