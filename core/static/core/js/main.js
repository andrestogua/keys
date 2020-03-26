$(document).ready(function(){
    let spin = document.getElementById("spin");
    let accordion = document.getElementById("acordion");
    setTimeout(function(){
        spin.setAttribute("style",("display:none"));
            accordion.removeAttribute("style");
    },3000);
});
