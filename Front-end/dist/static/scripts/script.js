const url = "http://127.0.0.1:8000/"
let url_id = new URL(window.location.href).searchParams.get("value");
let urlPath = window.location.pathname; // Different function executed based on the page
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
        case "/index.html":
            index_page();
            break;
        case "/items-list.html":
            item_listing();
            break;
        case "/item-list-detail.html":
            item_details();
            break;
        case "/login.html":
            login();
            break;
        default:
            console.log("No page found")
            break;
    }
});



index_page = () => {
    $.ajax({
        method: "GET",
        url: url + "items/",
        success: (data) => {
            console.log("Sucess")
            items_lost_number.innerText = data.length;
            items_found_number.innerText = data.length;
            items_connected.innerText = data.length;
        },
    })
}

item_listing = () => {
    $.ajax({
        method: "GET",
        url: url + "items",
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

item_details= () => {
    $.ajax({
        url: url + "items/" + url_id,
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


