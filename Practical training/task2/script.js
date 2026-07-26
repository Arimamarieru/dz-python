const result = document.getElementById("result");
const plusButton = document.getElementById("plus");
const minusButton = document.getElementById("minus");
const message = document.getElementById("message");

let value = 0;

function updateCounter() {
    result.textContent = value;

    if (value > 0) {
        result.style.backgroundColor = "yellow";
    } else if (value < 0) {
        result.style.backgroundColor = "green";
    } else {
        result.style.backgroundColor = "red";
    }

    plusButton.disabled = value === 10;
    minusButton.disabled = value === -10;

    if (value === 10 || value === -10) {
        message.textContent = "вы достигли экстремального значения";
    } else {
        message.textContent = "";
    }
}

plusButton.addEventListener("click", function () {
    value += 1;
    updateCounter();
});

minusButton.addEventListener("click", function () {
    value -= 1;
    updateCounter();
});
