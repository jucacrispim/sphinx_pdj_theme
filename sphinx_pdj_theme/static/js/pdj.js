// function setMenuControls() {
//   // Shift nav in mobile when clicking the menu.
//   let toggles = document.querySelectorAll("[data-toggle='wy-nav-top']");
//   for (let t of toggles) {
//     t.onclick = function(){
//       for (let e of document.querySelectorAll("[data-toggle='wy-nav-shift']")){
// 	e.classList.toggle('shift');
//       }
//     };
//   }

//   // Close menu when you click a link.
//   let links = document.querySelectorAll(".wy-menu-vertical .current ul li a");
//   for (let l of links) {
//     l.onclick = function(){
//       for (let e of document.querySelectorAll("[data-toggle='wy-nav-shift']")){
// 	e.classList.toggle('shift');
//       }
//     };
//   }
// }

// document.addEventListener("DOMContentLoaded", (event) => {
//   setMenuControls();
// });


// Atualize seu pdj.js com este código:
document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.querySelector('.wy-nav-top i.fa-bars');
  const menuSidebar = document.querySelector('.wy-nav-side');
  const contentWrap = document.querySelector('.wy-nav-content-wrap');
  const menuOverlay = document.createElement('div');
  menuOverlay.className = 'menu-overlay';
  document.body.appendChild(menuOverlay);

  function toggleMenu() {
    const isOpening = !contentWrap.classList.contains('shift');

    contentWrap.classList.toggle('shift');
    menuSidebar.classList.toggle('shift');
    menuOverlay.classList.toggle('active');

    // Bloqueia scroll apenas no mobile
    if (window.innerWidth < 768) {
      document.body.style.overflow = isOpening ? 'hidden' : '';
    }

    // Adiciona/remove evento de clique no overlay
    if (isOpening) {
      menuOverlay.addEventListener('click', closeMenu);
    } else {
      menuOverlay.removeEventListener('click', closeMenu);
    }
  }

  function closeMenu() {
    contentWrap.classList.remove('shift');
    menuSidebar.classList.remove('shift');
    menuOverlay.classList.remove('active');
    document.body.style.overflow = '';
    menuOverlay.removeEventListener('click', closeMenu);
  }

  if (menuToggle) {
    menuToggle.addEventListener('click', toggleMenu);
  }

  // Fecha menu ao redimensionar para desktop
  window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
      closeMenu();
    }
  });

  // Fecha menu ao clicar em links do menu
  const menuLinks = document.querySelectorAll('.wy-menu-vertical a');
  menuLinks.forEach(link => {
    link.addEventListener('click', closeMenu);
  });
});
