const firstInput = document.getElementById("first-number");
const secondInput = document.getElementById("second-number");
const result = document.getElementById("result");

function sum() {
    const firstNumber = Number(firstInput.value);
    const secondNumber = Number(secondInput.value);

    if (firstInput.value.trim() === "" || secondInput.value.trim() === "" || Number.isNaN(firstNumber) || Number.isNaN(secondNumber)) {
        result.textContent = "Ошибка: введите числа";
        return;
    }

    result.textContent = firstNumber + secondNumber;
}

function difference() {
    const firstNumber = Number(firstInput.value);
    const secondNumber = Number(secondInput.value);

    if (firstInput.value.trim() === "" || secondInput.value.trim() === "" || Number.isNaN(firstNumber) || Number.isNaN(secondNumber)) {
        result.textContent = "Ошибка: введите числа";
        return;
    }

    result.textContent = firstNumber - secondNumber;
}

function product() {
    const firstNumber = Number(firstInput.value);
    const secondNumber = Number(secondInput.value);

    if (firstInput.value.trim() === "" || secondInput.value.trim() === "" || Number.isNaN(firstNumber) || Number.isNaN(secondNumber)) {
        result.textContent = "Ошибка: введите числа";
        return;
    }

    result.textContent = firstNumber * secondNumber;
}

function division() {
    const firstNumber = Number(firstInput.value);
    const secondNumber = Number(secondInput.value);

    if (firstInput.value.trim() === "" || secondInput.value.trim() === "" || Number.isNaN(firstNumber) || Number.isNaN(secondNumber)) {
        result.textContent = "Ошибка: введите числа";
        return;
    }

    result.textContent = firstNumber / secondNumber;
}

document.getElementById("sum").addEventListener("click", sum);
document.getElementById("difference").addEventListener("click", difference);
document.getElementById("product").addEventListener("click", product);
document.getElementById("division").addEventListener("click", division);
