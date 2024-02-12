const url = 'http://localhost:5001/test';

// Function to render a card display for a single object
function cardDisplay(value) {
    return `
        <div class="col-md-4 mb-3">
            <div class="card">
                <h3 class="text-center card-header" id="item-name">${value.first_name}</h3>
                <p class="text-center" id="description">${value.last_name}</p>
                <a href="./items-lost.html" class="btn btn-dark mx-auto" role="button">View</a>
            </div>
        </div>
    `;
}

$(document).ready(() => {
    $.get(url, (data, status) => {
        if (status === 'success') {
            // Render card display for the received data
            console.log(data)
            $("#item-details-column").append(cardDisplay(data));
        }
    });
});
