# Generar el HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
/* Estilos CSS aquí */
body {
    background: url('Wallpaper3_1920x1080.png');
    background-size: cover;
    margin: 0;
    padding: 0;
}

.wrapper {
    position: absolute;
    top: 80px;
    left: 50%;
    transform: translateX(-50%);
    transform: scale(1);
}

input {
    position: absolute;
    width: 500px;
    height: 30px;
    border: 0px solid #fff;
    top: 130px;
    left: calc(50% - 250px);
    font-size: 20px;
    color: rgba(255,255,255,0.8);
    background: transparent;
    border-bottom: 1px solid rgba(255,255,255,0.2);
    font-family: Helvetica Neue, Arial;
    font-weight: 300;
    text-align: center;
}

input:focus {
    outline: none;
    border-bottom: 1px solid rgba(66, 78, 255, 1);
}

.flip {
    position: relative;
    float: left;
    margin-left: 5px;
    width: 20px;
    height: 35px;
    border-radius: 3px;
    background: #111;
    color: rgba(255, 204, 1, 1);
    font-family: Helvetica Neue, Arial;
    font-size: 18px;
    padding-left: 4px;
    overflow: hidden;
}

.flip:after {
    content: '';
    position: absolute;
    top: 0px;
    left: 0px;
    width: 100%;
    height: calc(50% - 1px);
    border-bottom: 1px solid #000;
    background: linear-gradient(rgba(0,0,0,0) 0%, rgba(0,0,0,0.45) 100%);
    box-shadow: 0 1px 0 rgba(255,255,255,0.1);
}

.flip:before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0px;
    width: 100%;
    height: 50%;
    background: linear-gradient(to bottom, rgba(0,0,0,0.45) 0%,rgba(0,0,0,0) 100%);
    z-index: 2;
}

.flip ul {
    list-style: none;
    margin: 0;
    padding: 0;
    position: absolute;
    top: 0px;
}

.flip ul li {
    height: 63px;
    width: 16px;
    text-align: center;
    padding-top: 7px;
}
</style>
</head>
<body>
<div class='wrapper'>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
    <div class='flip'></div>
</div>
<input placeholder='FLIP TEXT' type='text'>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
var charList = [" ","0","1","2","3","4","5","6","7","8","9","!","\"","$","%","&","/","(",")","=","?","+","*","#","'",":",";","-",".","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];

// Lectura del archivo S30-SOW1092.TXT
$.get("S30-SOW1092.TXT", function(data) {
    var lines = data.split("\\n");
    var randomAirportNames = [];
    for (var i = 0; i < lines.length; i++) {
        var parts = lines[i].split(";");
        if (parts.length > 3) {
            randomAirportNames.push(parts[3].trim());
        }
    }
    animateText(randomAirportNames);
});

function animateText(randomAirportNames) {
    $(".flip").each(function(index){
        $(this).append("<ul></ul>");
        $(this).attr("value"," ");
        for(var i=0; i < charList.length; i++){
            var char = charList[i];
            $("ul", this).append("<li>"+char+"</li>");
        }
    });
    $("input").focus();
    var msg = "EDINBURGH";
    $("input").val(msg);
    var msgEx = msg.split("");
    for(var k=0; k < msgEx.length; k++){
        switchChar(msgEx[k],k); 
    }
    setInterval(function(){
        if($("input").val() == "EDINBURGH"){
            var random = Math.round(Math.random()*randomAirportNames.length);
            var msg = randomAirportNames[random]+"                                    ";
            var msgEx = msg.split("");
            for(var k=0; k < msgEx.length; k++){
                switchChar(msgEx[k],k); 
            }
        }
    }, 8000);
}

function switchChar(char,n){
    var current = $(".flip").eq(n).attr("value");
    var start = 0;
    for(var i=0; i < charList.length; i++){
        if(charList[i] == current){
            start = i;
            break;
        } 
    }
    var complete = false;
    for(var i=start; i < charList.length; i++){
        if(charList[i] == char){
            complete = true;
            break;
        }
        $(".flip").eq(n).attr("value",char);
        $(".flip").eq(n).find("ul").animate({top: "-=70px"},100);
    }
    if(complete == false){
        $(".flip").eq(n).find("ul").animate({top: "0px"},100);
        start = 0;
         for(var i=start; i < charList.length; i++){
            if(charList[i] == char){
                break;
                complete = true;
            }
            $(".flip").eq(n).attr("value",char);
            $(".flip").eq(n).find("ul").animate({top: "-=70px"},100);
        }
    }
}

$("input").keyup(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
        var msg = $("input").val().toUpperCase()+"                  ";
        var msgEx = msg.split("");
        for(var k=0; k < msgEx.length; k++){
            switchChar(msgEx[k],k); 
        }
    }
});
</script>
</body>
</html>
"""

# Guardar el contenido HTML en un archivo
with open("out.html", "w") as file:
    file.write(html_content)

# Abrir el archivo en el navegador web
import webbrowser
webbrowser.open("out.html")

