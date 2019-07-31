var domain = 0;
var xmax = 0;
var xmin = 0;
var sim = false;
var remainder;

function linearClc (){
aprVarTtlAB();
setXmnNorm();
document.getElementById("Abox").value = 1;
document.getElementById("Bbox").value = 0;
setDomNorm();
}
function quadClc (){
aprVarTtlABC();
setXmnNorm
document.getElementById("Abox").value = 1;
document.getElementById("Bbox").value = 0;
document.getElementById("Cbox").value = 0
setDomNorm();
}
function cubicClc (){
aprVarTtlABCD();
setXmnNorm();
document.getElementById("Abox").value = 1;
document.getElementById("Bbox").value = 0;
document.getElementById("Cbox").value = 0;
document.getElementById("Dbox").value = 0;
setDomNorm();
}
function sinClc (){
aprVarTtlABCD();
setXmnNorm();
document.getElementById("Abox").value = 1;
document.getElementById("Bbox").value = 1;
document.getElementById("Cbox").value = 0;
document.getElementById("Dbox").value = 0;
setDomNorm();
}
function cosClc (){
aprVarTtlABCD();
setXmnNorm();
document.getElementById("Abox").value = 1;
document.getElementById("Bbox").value = 1;
document.getElementById("Cbox").value = 0;
document.getElementById("Dbox").value = 0;
setDomNorm();
}
function exClc (){
aprVarTtlAB();
setXEx();
document.getElementById("Abox").value = 1;
document.getElementById("Bbox").value = 0;
document.getElementById("xmin").value = 0;
document.getElementById("xmax").value = 5;
}
function natlgClc (){
aprVarTtlAB();
setXmnZero();
document.getElementById("Abox").value = 1;
document.getElementById("Bbox").value = 0;
document.getElementById("xmin").value = .1;
document.getElementById("xmax").value = 5;
}
function ABRequired() {
    document.getElementById("Cbox").required = false;
    document.getElementById("Dbox").required = false;
}

function ABCRequired() {
    document.getElementById("Cbox").required = true;
    document.getElementById("Dbox").required = false;
}

function ABCDRequired() {
    document.getElementById("Cbox").required = true;
    document.getElementById("Dbox").required = true;
}

function aprVarTtlAB() {
    document.getElementById("var").style.display = "block";
    document.getElementById("varABC").style.display = "block";
    document.getElementById("CLbl").style.display = "none";
    document.getElementById("Cbox").style.display = "none";
    document.getElementById("DLbl").style.display = "none";
    document.getElementById("Dbox").style.display = "none";
    ABRequired();
}

function aprVarTtlABC() {
    document.getElementById("var").style.display = "block";
    document.getElementById("varABC").style.display = "block";
    document.getElementById("CLbl").style.display = "inline";
    document.getElementById("Cbox").style.display = "inline";
    document.getElementById("DLbl").style.display = "none";
    document.getElementById("Dbox").style.display = "none";
    ABCRequired();
}

function aprVarTtlABCD() {
    document.getElementById("var").style.display = "block";
    document.getElementById("varABC").style.display = "block";
    document.getElementById("CLbl").style.display = "inline";
    document.getElementById("Cbox").style.display = "inline";
    document.getElementById("DLbl").style.display = "inline";
    document.getElementById("Dbox").style.display = "inline";
    ABCDRequired();
}

function getMinMax() {
    xmax = Number(parseFloat(document.getElementById("xmax").value));
    xmin = Number(parseFloat(document.getElementById("xmin").value));
    domain = (xmax - xmin) / 2;
    if (isNaN(domain)) {
        document.getElementById("widthMessage").innerHTML = "Please fill in x-min and x-max";
        document.getElementById("domainMessage").innerHTML = "Please fill in x-min and x-max";
    } else if (xmin >= xmax) {
        document.getElementById("widthMessage").innerHTML = "x-max must be greater than x-min";
        document.getElementById("domainMessage").innerHTML = "x-max must be greater than x-min";
    } else if (xmax > 5000) {
        document.getElementById("widthMessage").innerHTML = "x-max must be less than 5000";
        document.getElementById("domainMessage").innerHTML = "x-max must be less than 5000";
    } else if (xmin < -5000) {
        document.getElementById("widthMessage").innerHTML = "x-min must be greater than -5000";
        document.getElementById("domainMessage").innerHTML = "x-min must be greater than -5000";
    } else {
        document.getElementById("domainMessage").innerHTML = "";
        document.getElementById("widthMessage").innerHTML = "Width must be greater than 0 and less than " + domain;
        document.getElementById("widthbox").max = domain;
    }
}

function minGreaterMax() {
    if (1 > 10) {
        border = "2px solid red";
    }
}

function hasAlpha() {
    if (1 > 10) {
        border = "2px solid red";
    }
}

function hasNeg() {
    if (1 > 10) {
        border = "2px solid red";
    }
}

function hasNegInt() {
    if (1 > 10) {}
}

function widthRequired() {
    document.getElementById("widthbox").required = true;
    document.getElementById("numrectbox").required = false;
}

function rectRequired() {
    document.getElementById("numrectbox").required = true;
    document.getElementById("widthbox").required = false;
}

function getMinMax() {
    xmax = Number(parseFloat(document.getElementById("xmax").value));
    xmin = Number(parseFloat(document.getElementById("xmin").value));
    domain = (xmax - xmin) / 2;
    if (isNaN(domain)) {
        document.getElementById("widthMessage").innerHTML = "Please fill in x-min and x-max";
        document.getElementById("domainMessage").innerHTML = "Please fill in x-min and x-max";
    } else if (xmin >= xmax) {
        document.getElementById("widthMessage").innerHTML = "x-max must be greater than x-min";
        document.getElementById("domainMessage").innerHTML = "x-max must be greater than x-min";
    } else if (xmax > 5000) {
        document.getElementById("widthMessage").innerHTML = "x-max must be less than 5000";
        document.getElementById("domainMessage").innerHTML = "x-max must be less than 5000";
    } else if (xmin < -5000) {
        document.getElementById("widthMessage").innerHTML = "x-min must be greater than -5000";
        document.getElementById("domainMessage").innerHTML = "x-min must be greater than -5000";
    } else {
        document.getElementById("domainMessage").innerHTML = "";
        document.getElementById("widthMessage").innerHTML = "Width must be greater than 0 and less than " + domain;
        document.getElementById("widthbox").max = domain;
    }
}

function testWdth(evt) {
    isInNum(evt);
    var char = String.fromCharCode(evt.which);
    var numwidth = Number(parseFloat(document.getElementById("widthbox").value));
    if (numwidth <= 0 || numwidth > domain) {
        evt.preventDefault();
    }
}

function testRect(evt) {
    isInInt(evt);
    var char = String.fromCharCode(evt.which);
    var numwidth = Number(parseFloat(document.getElementById("numrectbox").value));
    if (numwidth <= 0) {
        evt.preventDefault();
    }
}

function isInPosNum(evt) {
    var char = String.fromCharCode(evt.which);
    if (!(/[0-9.]/.test(char))) {
        evt.preventDefault();
    }
}

function isInNum(evt) {
    var char = String.fromCharCode(evt.which);
    if (!(/[0-9.-]/.test(char))) {
        evt.preventDefault();
    }
}

function isInInt(evt) {
    var char = String.fromCharCode(evt.which);
    if (!(/[0-9]/.test(char))) {
        evt.preventDefault();
    }
}
function rectBoxInpt(evt) {
    isInPosNum (evt);
}
function aprNumRect() {
    rectRequired();
    document.getElementById("numRect").style.display = "block";
    document.getElementById("widthNum").style.display = "none";
    ifSimtrue ();
}

function aprWidthNum() {
    widthRequired();
    document.getElementById("widthNum").style.display = "block";
    document.getElementById("numRect").style.display = "none";
    getMinMax();
}

function SimRectOnly() {
    sim = true;
    document.getElementById("widthRect").style.display = "block";
    document.getElementById("rectOpt").style.display = "block";
    document.getElementById("widthOpt").style.display = "none";
    aprNumRect();
    ifSimtrue ();
    document.getElementById("rectangles").checked = true;
}
function ifSimtrue () {
  if (sim == true) {
      document.getElementById("numrectbox").max = 20;
      document.getElementById("rectMessage").innerHTML = "# of rectangles must be an integer between 2 and 20";
  } else if (sim == false) {
      document.getElementById("numrectbox").max = 1000;
      document.getElementById("rectMessage").innerHTML = "# of rectangles must be an integer between 2 and 1000";
  } else {
      document.getElementById("rectMessage").innerHTML = "error";
  }
}

function setXEx() {
  document.getElementById("xmin").min = -100;
  document.getElementById("xmax").max = 100;
}
function setXmnZero() {
  document.getElementById("xmin").min = .001;
  document.getElementById("xmax").max = 5000;
}
function setXmnNorm() {
  document.getElementById("xmin").min = -5000;
  document.getElementById("xmax").max = 5000;
}
function setDomNorm() {
  document.getElementById("xmin").value = -10;
  document.getElementById("xmax").value = 10;
}

function OtherAllOpt() {
    sim = false;
    document.getElementById("widthRect").style.display = "block";
    document.getElementById("rectOpt").style.display = "block";
    document.getElementById("widthOpt").style.display = "block";
    ifSimtrue();
}

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}
