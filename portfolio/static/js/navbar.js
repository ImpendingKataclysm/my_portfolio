/* Nav display values */
const openSize = "10rem"
const closedSize = "0"

/* Page Elements */
const navOpenBtn = document.getElementById("nav-openbtn");
const navCloseBtn = document.getElementById("nav-closebtn");
const navSidebar = document.getElementById("nav-sidebar");
const mainContent = document.getElementById("main-content");

navOpenBtn.addEventListener("click", openNav);
navCloseBtn.addEventListener("click", closeNav);

function openNav()
{
    navSidebar.style.width = openSize;
    mainContent.style.marginLeft = openSize;
}


function closeNav()
{
    navSidebar.style.width = closedSize;
    mainContent.style.marginLeft = closedSize;
}