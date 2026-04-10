function validateForm() {
    let email = document.querySelector("input[name='email']").value;
    if (!email.includes("@")) {
        alert("Invalid Email!");
        return false;
    }
    return true;
}

function searchEvents() {
    let input = document.getElementById("search").value.toLowerCase();
    let cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.style.display = card.innerText.toLowerCase().includes(input)
            ? "block"
            : "none";
    });
}

/* DARK MODE */
function toggleDark() {
    document.body.classList.toggle("dark");
}