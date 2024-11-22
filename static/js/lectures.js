document.addEventListener('DOMContentLoaded', function () {
    const subjectButtons = document.querySelectorAll('.subject-btn');

    subjectButtons.forEach(button => {
        button.addEventListener('click', function () {
            const lectures = document.querySelector(this.getAttribute('data-target'));
            if (lectures.classList.contains('collapse')) {
                lectures.classList.remove('collapse');
            } else {
                lectures.classList.add('collapse');
            }
        });
    });
});
