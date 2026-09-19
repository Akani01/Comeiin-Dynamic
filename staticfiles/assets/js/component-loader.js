// Loads header/footer (and optional whatsapp.html) and initializes nav hamburger behavior.
async function loadComponent(elementId, filePath) {
    try {
        const res = await fetch(filePath);
        if (!res.ok) throw new Error(res.statusText);
        const html = await res.text();
        document.getElementById(elementId).innerHTML = html;
        return true;
    } catch (err) {
        console.error('loadComponent error:', filePath, err);
        return false;
    }
}

function initNavigation() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (!hamburger || !navLinks) return;

    // Toggle menu
    hamburger.addEventListener('click', (e) => {
        e.stopPropagation();
        const opened = navLinks.classList.toggle('active');
        hamburger.setAttribute('aria-expanded', opened ? 'true' : 'false');
        navLinks.dataset.visible = opened ? 'true' : 'false';
    });

    // Close when a link is clicked
    navLinks.querySelectorAll('a').forEach((a) => {
        a.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
            navLinks.dataset.visible = 'false';
        });
    });

    // Close on outside click
    document.addEventListener('click', (ev) => {
        if (!ev.target.closest('.nav-container') && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
            navLinks.dataset.visible = 'false';
        }
    });

    // Ensure menu resets on resize (desktop -> mobile)
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768 && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
            navLinks.dataset.visible = 'false';
        }
    });
}

document.addEventListener('DOMContentLoaded', async () => {
    // ensure placeholders exist in all pages: header-placeholder, footer-placeholder, whatsapp-placeholder
    await loadComponent('header-placeholder', 'header.html');
    await loadComponent('footer-placeholder', 'footer.html');

    // optional: load whatsapp fragment if you use it
    // await loadComponent('whatsapp-placeholder', 'whatsapp.html');

    // init nav AFTER header is injected
    initNavigation();

    // If you have whatsapp.js behavior file, load it now (optional)
    // const s = document.createElement('script'); s.src = 'assets/js/whatsapp.js'; s.defer = true; document.body.appendChild(s);
});