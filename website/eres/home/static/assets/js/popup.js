
(function() {
    var dialog = document.getElementById('window');
    document.getElementById('formRastr').onsubmit = function() {

    };
  	 document.getElementById('exit').onclick = function() {
        dialog.close();
    };
})();

//function dados{
//    $ajax(){
//        url="home/preco"
//        type="post"
//    }
//    function(result)
//    {
//        alert(result.mensagem);
//    }
//    }
//}

$(function() {
    //----- OPEN
    $('[data-popup-open]').on('submit', function(e)  {
        var targeted_popup_class = jQuery(this).attr('data-popup-open');
        $('[data-popup="' + targeted_popup_class + '"]').fadeIn(1000);

        e.preventDefault();
    });

    //----- CLOSE
    $('[data-popup-close]').on('click', function(e)  {
        var targeted_popup_class = jQuery(this).attr('data-popup-close');
        $('[data-popup="' + targeted_popup_class + '"]').fadeOut(1000);

        e.preventDefault();
    });
});
