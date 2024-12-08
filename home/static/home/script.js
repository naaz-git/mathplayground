function generateQuestions() {
    // Get the questions container
    const questionsContainer = document.getElementById('questionsContainer');
    questionsContainer.innerHTML = ''; // Clear previous questions

    // Define operations
    const operations = [
        { id: 'addition', symbol: '+', questionsInput: 'additionQuestions', digitsInput: 'additionDigits' },
        { id: 'subtraction', symbol: '-', questionsInput: 'subtractionQuestions', digitsInput: 'subtractionDigits' },
        { id: 'multiplication', symbol: '×', questionsInput: 'multiplicationQuestions', digitsInput: 'multiplicationDigits' },
        { id: 'division', symbol: '÷', questionsInput: 'divisionQuestions', digitsInput: 'divisionDigits' }
    ];

    // Loop through each operation
    operations.forEach(operation => {
        const isChecked = document.getElementById(operation.id).checked;
        if (isChecked) {
            const numberOfQuestions = parseInt(document.getElementById(operation.questionsInput).value) || 5;
            const numberOfDigits = parseInt(document.getElementById(operation.digitsInput).value) || 2;

            let row;
            for (let i = 0; i < numberOfQuestions; i++) {
                if (i % 4 === 0) {
                    // Create a new row every 4 questions
                    row = document.createElement('div');
                    row.className = 'row';
                    questionsContainer.appendChild(row);
                }

                const num1 = generateRandomNumber(numberOfDigits);
                const num2 = generateRandomNumber(numberOfDigits);
                const questionHTML = `
                    <div class="question">
                        <div class="digit">${num1}</div>
                        <div class="operation">${operation.symbol} ${num2}</div>
                        <div class="line">----</div>
                    </div>
                `;
                row.innerHTML += questionHTML;
            }
        }
    });

    document.getElementById('welcomePage').style.display = 'none';
    document.getElementById('questionsPage').style.display = 'block';
}

// Function to generate a random number with the specified number of digits
function generateRandomNumber(digits) {
    const min = Math.pow(10, digits - 1);
    const max = Math.pow(10, digits) - 1;
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function showAnswers() {
    const questionsContainer = document.getElementById('questionsContainer');
    const rows = questionsContainer.querySelectorAll('.row'); // Get all rows of questions

    rows.forEach(row => {
        const questions = row.querySelectorAll('.question'); // Get all questions in the row
        questions.forEach(question => {
            // Extract question details
            const num1 = parseInt(question.querySelector('.digit').textContent);
            const operationText = question.querySelector('.operation').textContent.trim();
            const operator = operationText.charAt(0);
            const num2 = parseInt(operationText.slice(2));

            // Calculate the answer
            let answer;
            switch (operator) {
                case '+':
                    answer = num1 + num2;
                    break;
                case '-':
                    answer = num1 - num2;
                    break;
                case '×':
                    answer = num1 * num2;
                    break;
                case '÷':
                    answer = (num1 / num2).toFixed(2); // 2 decimal places for division
                    break;
            }

            // Append the answer below the question
            const answerDiv = document.createElement('div');
            answerDiv.className = 'answer';
            answerDiv.textContent = answer; // Display only the numeric value
            question.appendChild(answerDiv);
        });
    });
}

function printQuestions() {
    // Ensure both questions and answers are displayed
    const questionsPage = document.getElementById('questionsPage');
    const originalContent = document.body.innerHTML; // Backup original content

    // Temporarily set the page content to just the questions page
    document.body.innerHTML = questionsPage.innerHTML;

    // Trigger the print dialog
    window.print();

    // Restore original content
    document.body.innerHTML = originalContent;

    // Reattach event listeners (if needed)
    window.location.reload();
}

