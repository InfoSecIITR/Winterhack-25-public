const display = document.querySelector('.display');
const buttons = Array.from(document.querySelectorAll('button'));

buttons.map(button => {
    button.addEventListener('click', (e) => {
        if (e.target.innerText === '=') {
            // Extract the expression from the display
            const expression = display.value;
            // Send a POST request to the /calculate endpoint
            fetch('/calculate/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ expression }),
            })
            .then(response => response.json())
            .then(data => {
                // Assuming the server responds with the result
                display.value = data.result;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        } else if(e.target.innerText === 'C') {
            display.value = "";
        } else {
            display.value += e.target.innerText;
        }
    });
});

