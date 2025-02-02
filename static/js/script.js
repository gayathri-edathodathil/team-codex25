document.addEventListener("DOMContentLoaded", function () {
    fetchSpendingAnalysis();
});

function fetchSpendingAnalysis() {
    fetch("http://127.0.0.1:8000/api/analyze-spending")
        .then(response => response.json())
        .then(data => {
            if (data.unusual_transactions && data.unusual_transactions.length > 0) {
                displayAlerts(data.unusual_transactions);
            }
        })
        .catch(error => console.error("Error fetching spending analysis:", error));
}

function displayAlerts(transactions) {
    let alertBox = document.getElementById("alerts");
    alertBox.innerHTML = "<h3>🚨 Unusual Spending Detected!</h3>";

    transactions.forEach(tx => {
        alertBox.innerHTML += `
            <p><strong>Category:</strong> ${tx.Category} | <strong>Amount:</strong> ₹${tx.Amount}</p>
        `;
    });
}
