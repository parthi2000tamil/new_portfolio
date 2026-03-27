// Smooth Scrolling for Nav Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Simple Glitch Effect Randomizer for the hero title
const glitchElement = document.querySelector('.glitch');
if (glitchElement) {
    setInterval(() => {
        glitchElement.style.transform = `translate(${Math.random() * 4 - 2}px, ${Math.random() * 4 - 2}px)`;
        setTimeout(() => {
            glitchElement.style.transform = 'translate(0, 0)';
        }, 50);
    }, 2000);
}
