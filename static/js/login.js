// Handle "Continue Without Login" button click
document.getElementById("continue-btn").addEventListener("click", function () {
    window.location.href = "{% url 'home' %}"; // Replace 'home' with the name of your home page URL
});
