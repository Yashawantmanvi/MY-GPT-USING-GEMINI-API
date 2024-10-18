document.getElementById('qa_chatbot').addEventListener('click', () => {
    window.location.href = 'qa_chatbot.html';
});

document.getElementById('chat_with_pdf').addEventListener('click', () => {
    window.location.href = 'chat_with_pdf.html';
});

document.getElementById('image-intel').addEventListener('click', () => {
    window.location.href = 'image_intel.html';
});

document.getElementById('ninja-gpt').addEventListener('click', () => {
    window.location.href = 'index.html'; // This should already be correct
});

document.getElementById('toggle-personalization').addEventListener('click', () => {
    const button = document.getElementById('toggle-personalization');
    if (button.textContent === 'Turn off') {
        button.textContent = 'Turn on';
    } else {
        button.textContent = 'Turn off';
    }
});

document.getElementById('next-btn').addEventListener('click', () => {
    const carousel = document.querySelector('.carousel-content');
    carousel.scrollBy({ left: carousel.offsetWidth, behavior: 'smooth' });
});

document.getElementById('prev-btn').addEventListener('click', () => {
    const carousel = document.querySelector('.carousel-content');
    carousel.scrollBy({ left: -carousel.offsetWidth, behavior: 'smooth' });
});
