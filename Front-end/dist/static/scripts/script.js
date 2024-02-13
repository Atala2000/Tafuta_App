const URL_PATH = "https://jsonplaceholder.typicode.com/"
let url_id = new URL(window.location.href).searchParams.get("value"); 
/*
Gets ID from key-value pair that will be used to dynamically set data for the item list detail page
*/
// Selectors for the index page
const items_found_number = document.getElementById("items-reported-found");
const items_lost_number = document.getElementById("items-reported-lost");
const items_connected = document.getElementById("items-connected-index");
// Selectors for the item listing page
const items_column = document.getElementById("item-column");

function index_page() {
    $.ajax({
        method: "GET",
        url: URL_PATH + "posts",
        success: (data) => {
            console.log("Sucess")
            items_lost_number.innerText = data.length;
            items_found_number.innerText = data.length;
            items_connected.innerText = data.length;
        },
    })
}

function item_listing() {
    $.ajax({
        method: "GET",
        url: URL_PATH + "posts",
        success: (data) => {
            console.log("Sucess")
            data.forEach((item) => {
                items_column.innerHTML += `
                <div class="card col-md-4 m-2" style="width: 18rem;">
                    <img class="card-img-top" src="..." alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title">${item.title}</h5>
                        <p class="card-text">${item.body}</p>
                        <a href="./item-list-detail.html?value=${item.id}" >Go somewhere</a>
                    </div>
                </div>
                `
            })
        },

    })
}

document.addEventListener("DOMContentLoaded", () => {
    index_page();
    item_listing();
    
});
