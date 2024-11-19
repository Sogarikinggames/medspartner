const navbar = document.querySelector(".navbar");
const menu = document.querySelector(".menu");
            //ヘッダーがulタグの位置に来たら、ヘッダーを固定する。
window.addEventListener("scroll",() =>{
    if(window.scrollY >= menu.offsetTop){
        navbar.classList.add("sticky");
    } 
    else
    {
        navbar.classList.remove("sticky");
    }
});

const burger = document.querySelector(".burger")

burger.addEventListener("click",() => {
    menu.classList.toggle("nav-active");
})