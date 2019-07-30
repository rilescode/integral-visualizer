
var domain = 0;
var xmax = 0;
var xmin = 0;
var sim = false;
function ABRequired() {
  document.getElementById("Cbox").required == false;
  document.getElementById("Dbox").required == false;
}
function ABCRequired() {
  document.getElementById("Cbox").required == true;
  document.getElementById("Dbox").required == false;
}
function ABCDRequired() {
  document.getElementById("Cbox").required == true;
  document.getElementById("Dbox").required == true;
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
  domain = (xmax - xmin)/2;
  if (isNaN(domain)) {
    document.getElementById("widthMessage").innerHTML = "Please fill in x-min and x-max";
    document.getElementById("domainMessage").innerHTML = "Please fill in x-min and x-max";
  } else if (xmin >= xmax){
   document.getElementById("widthMessage").innerHTML = "x-max must be greater than x-min";
   document.getElementById("domainMessage").innerHTML = "x-max must be greater than x-min";
 } else if (xmax > 5000){
   document.getElementById("widthMessage").innerHTML = "x-max must be less than 5000";
   document.getElementById("domainMessage").innerHTML = "x-max must be less than 5000";
 } else if (xmin < -5000){
   document.getElementById("widthMessage").innerHTML = "x-min must be greater than -5000";
   document.getElementById("domainMessage").innerHTML = "x-min must be greater than -5000";
  } else {
  document.getElementById("domainMessage").innerHTML = "";
  document.getElementById("widthMessage").innerHTML = "Width must be greater than 0 and less than " + domain;
  }
}

function minGreaterMax() {
 if (1> 10){
   border="2px solid red";
 }
}
function hasAlpha() {
 if (1> 10){
   border="2px solid red";
 }
}
function hasNeg() {
 if (1> 10){
   border="2px solid red";
 }
}
 function hasNegInt() {
  if (1> 10){
  }
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
  domain = (xmax - xmin)/2;
  if (isNaN(domain)) {
    document.getElementById("widthMessage").innerHTML = "Please fill in x-min and x-max";
    document.getElementById("domainMessage").innerHTML = "Please fill in x-min and x-max";
  } else if (xmin >= xmax){
   document.getElementById("widthMessage").innerHTML = "x-max must be greater than x-min";
   document.getElementById("domainMessage").innerHTML = "x-max must be greater than x-min";
 } else if (xmax > 5000){
   document.getElementById("widthMessage").innerHTML = "x-max must be less than 5000";
   document.getElementById("domainMessage").innerHTML = "x-max must be less than 5000";
 } else if (xmin < -5000){
   document.getElementById("widthMessage").innerHTML = "x-min must be greater than -5000";
   document.getElementById("domainMessage").innerHTML = "x-min must be greater than -5000";
  } else {
  document.getElementById("domainMessage").innerHTML = "";
  document.getElementById("widthMessage").innerHTML = "Width must be greater than 0 and less than " + domain;
  }
}
function testWdth(evt){
isInNum(evt);
var char = String.fromCharCode(evt.which);
var numwidth = Number(parseFloat(document.getElementById("widthbox").value));
if (numwidth<=0 || numwidth> domain){
evt.preventDefault();
}
}
function testRect(evt){
isInInt(evt);
var char = String.fromCharCode(evt.which);
var numwidth = Number(parseFloat(document.getElementById("numrectbox").value));
if (numwidth<=0){
evt.preventDefault();
}
}
function isInPosNum(evt){
var char = String.fromCharCode(evt.which);
if (!(/[0-9.]/.test(char))){
evt.preventDefault();
}
}
function isInNum(evt){
var char = String.fromCharCode(evt.which);
if (!(/[0-9.-]/.test(char))){
evt.preventDefault();
}
}
function isInInt(evt){
var char = String.fromCharCode(evt.which);
if (!(/[0-9]/.test(char))){
evt.preventDefault();
}
}
function aprNumRect() {
  rectRequired();
  document.getElementById("numRect").style.display = "block";
  document.getElementById("widthNum").style.display = "none";
  if (sim == true) {
    document.getElementById("rectMessage").innerHTML = "# of rectangles must be an even integer between 2 and 1000";
  } else if (sim == false) {
    document.getElementById("rectMessage").innerHTML = "# of rectangles must be an integer between 2 and 1000";
  } else {
    document.getElementById("rectMessage").innerHTML = "error";
  }
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
   if (sim == true) {
     document.getElementById("rectMessage").innerHTML = "# of rectangles must be an even integer between 2 and 1000";
     checkOddEv();
   } else if (sim == false) {
     document.getElementById("rectMessage").innerHTML = "# of rectangles must be an integer between 2 and 1000";
   } else {
     document.getElementById("rectMessage").innerHTML = "error";
   }
   document.getElementById("rectangles").checked = true;
 }
 function checkOddEv() {
   rectNum = Number(parseFloat(document.getElementById("rectangles").value));

 }
 function OtherAllOpt() {
   sim = false;
   document.getElementById("widthRect").style.display = "block";
   document.getElementById("rectOpt").style.display = "block";
   document.getElementById("widthOpt").style.display = "block";
   if (sim == true) {
     document.getElementById("rectMessage").innerHTML = "# of rectangles must be an even integer between 2 and 1000";
   } else if (sim == false) {
     document.getElementById("rectMessage").innerHTML = "# of rectangles must be an integer between 2 and 1000";
   } else {
     document.getElementById("rectMessage").innerHTML = "error";
   }
 }
