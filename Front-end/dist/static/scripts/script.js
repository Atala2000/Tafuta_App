const url = "http://127.0.0.1:8000/"
let url_id = new URL(window.location.href).searchParams.get("value");
let urlpathname = window.location.pathname;
const lastSlashIndex = urlpathname.lastIndexOf('/')
const urlPath = urlpathname.substring(lastSlashIndex + 1) // Different function executed based on the page
let credentials;
/*
Gets ID from key-value pair that will be used to dynamically set data for the item list detail page
*/


// Selectors for the index page
const items_found_number = document.getElementById("items-reported-found");
const items_lost_number = document.getElementById("items-reported-lost");
const items_connected = document.getElementById("items-connected-index");
// Selectors for the item listing page
const items_column = document.getElementById("item-column");

document.addEventListener("DOMContentLoaded", () => {
    switch (urlPath) {
        case "index.html":
            index_page("items/");
            break;
        case "items-list.html":
            item_listing("items/");
            break;
        case "item-list-detail.html":
            item_details("items/");
            break;
        case "login.html":
            login();
            break;
        case "report.html":
            report_form();
            break
        default:
            console.log("No page found")
            break;
    }
});



function index_page (endpoint) {
    $.ajax({
        method: "GET",
        url: url + endpoint,
        success: (data) => {
            console.log("Sucess")
            items_lost_number.innerText = data.length;
            items_found_number.innerText = data.length;
            items_connected.innerText = data.length;
        },
    })
}

function item_listing (endpoint) {
    $.ajax({
        method: "GET",
        url: url + endpoint,
        success: (data) => {
            console.log("Sucess")
            data.forEach((item) => {
                items_column.innerHTML += `
                <div class="card col-md-4 m-2" style="width: 18rem;">
                    <img class="card-img-top img-fluid mt-2" style="height: 200px; width: 200px;" src="${item.image}" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title">${item.name}</h5>
                        <p class="card-text">${item.description}</p>
                        <a href="./item-list-detail.html?value=${item.id}" class="btn btn-primary">View</a>
                    </div>
                </div>
                `
            })
        },

    })
}

function item_details (endpoint) {
    $.ajax({
        url: url + endpoint + url_id,
        method: "GET",
        success: ((data) => {
            document.getElementById("item_name").innerText = data.name;
            document.getElementById("item_description").innerText = data.description;
            document.getElementById("item_image").src = data.image;
            document.getElementById("item_location").innerText = data.location_found;
            document.getElementById("date_found").innerText = data.date_found;
            document.getElementById("contact").innerText = data.contact;
        }),
        error: ((error) => {
            console.log("Error fetching Item details")
            alert("Error fetching Item details")
        }),
    })
}

login = () => {
    $.ajax({
        url: url + "login/",
        method: "POST",
        success: ((response) => {
            console.log("Success");

            credentials = {
                username: response.username
            }
        }),
        error: ((error) => {
            console.log("Error")
        }),
    })
}

function report_form() {
    // Select the form element
    const reportForm = document.querySelector('#report-form');

    // Add event listener for form submission
    reportForm.addEventListener('submit', (event) => {
        // Prevent the default form submission behavior
        event.preventDefault();
        // Create FormData object
        const formData = new FormData(reportForm);
        // for (item of formData) {
        //     console.log(item[0], item[1]);
        // }
        // Convert file input value to Blob object
        const fileInput = reportForm.querySelector('input[type="file"]');
        const file = fileInput.files[0];
        formData.set('image', file);

        // Send AJAX request to the server
        $.ajax({
            url: url + "items/",
            method: "POST",
            data: formData,
            processData: false, // Prevent jQuery from processing data
            contentType: false, // Prevent jQuery from setting contentType
            success: (response) => {
                console.log("Success:", response);
                alert("Form submitted successfully")
                // Optionally, display a success message or redirect to another page
            },
            error: (error) => {
                console.error("Error:", error);
                alert("Form could not be submitted")
                // Optionally, display an error message to the user
            },
        });
    });
}

<<<<<<< HEAD
function filter() {
    // Get all the dropdown items
    const dropdownItems = document.querySelectorAll(".dropdown-item");

    // Add click event listener to each dropdown item
    dropdownItems.forEach(item => {
        item.addEventListener("click", function() {
            // Get the text content of the clicked item
            const selectedItem = this.textContent;
            item_listing(selectedItem.toLowerCase() + "/")
            // Log or use the selected item value as needed
            console.log("Selected item:", selectedItem);

            // If you want to do something with the selected item value, you can call a function here or perform any other action
        });
    });
}

// Call the filter function when the DOM content is loaded
document.addEventListener("DOMContentLoaded", () => {
    filter();
});
=======
// function filter() {
//     // Get all the dropdown items
//     const dropdownItems = document.querySelectorAll(".dropdown-item");

//     // Add click event listener to each dropdown item
//     dropdownItems.forEach(item => {
//         item.addEventListener("click", function() {
//             // Get the text content of the clicked item
//             const selectedItem = this.textContent;
//             item_listing(selectedItem.toLowerCase() + "/")
//             // Log or use the selected item value as needed
//             console.log("Selected item:", selectedItem);

//             // If you want to do something with the selected item value, you can call a function here or perform any other action
//         });
//     });
// }

>>>>>>> 1e67d24 (revert changes)
