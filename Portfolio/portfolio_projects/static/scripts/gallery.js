var images = document.querySelectorAll(".images img");
var dot_items = document.querySelectorAll(".dotnav-item");

var observer = new IntersectionObserver( (entries) => {
    if(entries[0].isIntersecting === true){
        let target = entries[0].target;
        let dot = dot_items[target.index];
        set_current(dot);
    }
}, { threshold: [0.9] });

function set_current(dot) {
        let __curr = document.querySelector(".current");
        if (__curr)
            __curr.classList.remove("current");
    dot.classList.add("current");
}

function dot_click(){
    images[this.index].scrollIntoView({ behavior: 'auto', block: 'nearest', inline: 'start' });
    set_current(this);
}

dot_items.forEach((dot, index) => {
    dot.index = index;
    dot.onclick = dot_click;
});

images.forEach((image, index)=>{
    image.index = index;
    observer.observe(image);
})