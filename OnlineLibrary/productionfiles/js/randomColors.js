function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

document.addEventListener('DOMContentLoaded', () => {
    const bookInfos = document.querySelectorAll('.book-info');
    bookInfos.forEach(bookInfo => {
        bookInfo.style.backgroundColor = getRandomColor();
    });
});
