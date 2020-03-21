$(document).ready(function(){
    $('.menu-bars').on("click",function () {
        $("nav ul").toggleClass("show");
    });
});

$(window).on("scroll", function() {
    if($(window).scrollTop()) {
          $('nav').addClass('transparent');
    }

    else {
          $('nav').removeClass('transparent');
    }
})