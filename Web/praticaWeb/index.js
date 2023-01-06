let botaoMenu = document.querySelector('.menu_icon');
let Ul = document.getElementById("listaLinks");
let Ul_links = Ul.children;


botaoMenu.addEventListener('click', () => {
    let currentDisplay = Ul.style.display
    if (currentDisplay == "flex") {
        Ul.style.display = "none"
        for (const elemento of Ul_links) {
            elemento.style.display = "none"
        }
    }else {
        Ul.style.display = "flex"
        Ul.style.animation = "abrir_menu 2s forwards"
        Ul.addEventListener("animationend", () => {
            for (const elemento of Ul_links) {
                elemento.style.display = "flex"
            }
            
        })
    }
    
})