var slideshow = document.querySelector(".slide");
var count = 0;
var img = ['1.jpg','2.jpg','3.jpg'];
var limit = img.length-1;

window.addEventListener("load",()=>{
    setInterval( () => {
        if (count == limit) {
            count=0;
        } else {
            count++;
        }
        slideshow.style.backgroundImage = `url(./../source/img/${img[count]})`;
    },4000);
})