// Loads the whatsapp fragment and then the widget logic.
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const res = await fetch('whatsapp.html');
    if (!res.ok) return;
    const html = await res.text();
    // Insert widget fragment at end of body
    document.body.insertAdjacentHTML('beforeend', html);

    // Load external widget behaviour (whatsapp.js)
    const s = document.createElement('script');
    s.src = 'assets/js/whatsapp.js';
    s.defer = true;
    document.body.appendChild(s);
  } catch (err) {
    console.error('Failed to load WhatsApp widget:', err);
  }
});