(function () {
    const init = () => {
        const whatsappButton = document.getElementById('whatsappButton');
        const chatBox = document.getElementById('chatBox');
        const messageOptions = document.querySelectorAll('.message-option');
        const customMessageInput = document.getElementById('customMessage');
        const sendMessageButton = document.getElementById('sendMessage');

        // TODO: replace with your full phone number without the plus sign, e.g. "27636340952"
        const phoneNumber = "27635440952";

        if (!whatsappButton || !chatBox) return;

        whatsappButton.addEventListener('click', function (e) {
            e.stopPropagation();
            const open = chatBox.classList.toggle('active');
            chatBox.setAttribute('aria-hidden', !open);
            if (open) customMessageInput && customMessageInput.focus();
        });

        messageOptions.forEach(option =>
            option.addEventListener('click', function () {
                openWhatsApp(this.dataset.message || '');
            })
        );

        sendMessageButton && sendMessageButton.addEventListener('click', function () {
            const msg = (customMessageInput.value || '').trim(); if (msg) openWhatsApp(msg);
        });

        customMessageInput && customMessageInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                const msg = (customMessageInput.value || '').trim(); if (msg) openWhatsApp(msg);
            }
        });

        function openWhatsApp(message) {
            const encoded = encodeURIComponent(message || '');
            const url = `https://wa.me/${phoneNumber}?text=${encoded}`;
            window.open(url, '_blank');
            chatBox.classList.remove('active');
            chatBox.setAttribute('aria-hidden', 'true');
            if (customMessageInput) customMessageInput.value = '';
        }

        document.addEventListener('click', function (ev) {
            if (!ev.target.closest('#waWidget') && chatBox.classList.contains('active')) {
                chatBox.classList.remove('active'); chatBox.setAttribute('aria-hidden', 'true');
            }
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && chatBox.classList.contains('active')) {
                chatBox.classList.remove('active'); chatBox.setAttribute('aria-hidden', 'true');
            }
        });
    };

    // If element already present, init now; otherwise wait for DOM ready
    if (document.getElementById('waWidget')) init();
    else document.addEventListener('DOMContentLoaded', init);
})();