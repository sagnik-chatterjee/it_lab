function selectimage1() {
    var canvas = document.getElementById("myCanvas");
    canvas.height = canvas.width * 16 / 9;
    var ctx = canvas.getContext("2d");
    var img = document.getElementById("img1");
    ctx.drawImage(img, 10, 10, 500, 750);
};
function selectimage2() {
    var canvas = document.getElementById("myCanvas");
    canvas.height = canvas.width * 16 / 9;
    var ctx = canvas.getContext("2d");
    var img = document.getElementById("img2");
    ctx.drawImage(img, 10, 10, 500, 750);
};
function selectimage3() {
    var canvas = document.getElementById("myCanvas");
    canvas.height = canvas.width * 16 / 9;
    var ctx = canvas.getContext("2d");
    var img = document.getElementById("img3");
    ctx.drawImage(img, 10, 10, 500, 750);
};
function selectiamge4() {
    var canvas = document.getElementById("myCanvas");
    canvas.height = canvas.width * 16 / 9;
    var ctx = canvas.getContext("2d");
    var img = document.getElementById("img4");
    ctx.drawImage(img, 10, 10, 500, 750);
};

function fontSelect() {
    var nam = document.getElementById("magName").value;
    var fsize = document.getElementById("size").value;
    var fname = document.getElementById("inputGroupSelect01").value;
    var fcolor = document.getElementById("inputGroupSelect02").value;
    var byline = document.getElementById("byline").value;
    var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d");
    ctx.font = fsize + "px " + fname;
    ctx.fillStyle = fcolor;
    ctx.textAlign = "center";
    ctx.fillText(nam, canvas.width / 2, canvas.height / 2);
    ctx.font= "30px Times New Roman"
    ctx.fillText(byline, canvas.width / 2, canvas.height*4 / 5);
};