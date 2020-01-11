function openSlideMenu() {
    document.getElementById('menu').style.width = '100vw';
    document.getElementById('navigation-bar').style.marginLeft = 'auto';
    document.getElementById('navigation-bar').style.marginRight = 'auto';
    document.getElementById('menu-toggle').style.display = 'none';

}

function closeSlideMenu() {
    document.getElementById('menu').style.width = '0';
    document.getElementById('navigation-bar').style.marginLeft = '0';
    document.getElementById('menu-toggle').style.display = 'block';
}


// Cart Menu
function openCartSlideMenu() {
    document.getElementById('cart-menu').style.width = '375px';
    document.getElementById('cart-bar').style.marginLeft = '50vw';
    document.getElementById('menu-toggle').style.display = 'none';
    
}

function closeCartSlideMenu() {
    document.getElementById('cart-menu').style.width = '0';
    document.getElementById('cart-bar').style.marginLeft = '0';
    document.getElementById('menu-toggle').style.display = 'block';
    
}

function selectNavItem() {
    document.getElementById('menu').style.width = '0';
    document.getElementById('navigation-bar').style.marginLeft = '0';
    document.getElementById('menu-toggle').style.display = 'block';
}