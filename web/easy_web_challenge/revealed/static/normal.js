document.addEventListener("DOMContentLoaded", function () {
    const addBtn = document.getElementById("addBtn");
    const subtractBtn = document.getElementById("subtractBtn");
    const resultDiv = document.getElementById("result");

    function sendRequest(endpoint) {
        const a = parseInt(document.getElementById("a").value);
        const b = parseInt(document.getElementById("b").value);

        if (isNaN(a) || isNaN(b)) {
            resultDiv.textContent = "Please enter valid numbers!";
            resultDiv.style.color = "red";
            return;
        }

        fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ a, b }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.result !== undefined) {
                    resultDiv.textContent = `Result: ${data.result}`;
                    resultDiv.style.color = "green";
                } else {
                    resultDiv.textContent = "Error: " + (data.error || "Unknown error");
                    resultDiv.style.color = "red";
                }
            })
            .catch((error) => {
                resultDiv.textContent = `Error: ${error.message}`;
                resultDiv.style.color = "red";
            });
    }

    addBtn.addEventListener("click", () => sendRequest("/add"));
    subtractBtn.addEventListener("click", () => sendRequest("/subtract"));
});
