

var init=function init(){
    var $botoes=$(".btn-danger");
    $botoes.click(function(){
        $("#fluido").slideUp()
    });

    $("#loader").hide();

    $(".btn-primary").click(function(){
        $("#fluido").slideDown()
    });

    $("#enviar").click(function(){
        $("#loader").fadeIn();
        var $inp=$("#in");
        var texto=$inp.val();
        var retornoDoServidor=function retornoDoServidor(objJs){
            $inp.val("");
            var $msg=$("<h3>"+objJs.data+" - "+objJs.texto+"</ h3>");
            $msg.hide();
            $("#msg").prepend($msg);
            $msg.slideDown();
            $("#loader").fadeOut();
        }


        $.post("/ajax",{"texto":texto},retornoDoServidor,
            "json").error(function(){
                $("#loader").fadeOut();
                alert("Erro");
            });


    });
}

$(document).ready(init);