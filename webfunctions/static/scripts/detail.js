import cart from "./cart.js";
// import products from "./products.mjs";
let products = [];
$(document).ready(function () {
  let app = document.getElementById("app");
  let temporaryContent = document.getElementById("temporaryContent");

  const loadTemplate = () => {
    fetch("http://localhost:5000/template")
      .then((response) => response.text())
      .then((html) => {
        app.innerHTML = html;
        let contentTab = document.getElementById("contentTab");
        contentTab.innerHTML = temporaryContent.innerHTML;
        temporaryContent.innerHTML = "";
        cart();
        initApp();
      });
  };
  loadTemplate();

  const initApp = async () => {
    products = await fetchProducts();
    let idProduct = new URLSearchParams(window.location.search).get("id");
    let info = products.filter((value) => value.id == idProduct)[0];
    console.log("info", info);

    if (!info) {
      //   window.location.href = "/webfunctions/templates/";
      window.location.href = "http://localhost:5000/";
    }

    let detail = document.querySelector(".detail");
    console.log("detail .img: ", detail);
    console.log("image:", info.image);
    detail.querySelector(".image img").src = info.image;
    detail.querySelector(".name").innerText = info.name;
    detail.querySelector(".price").innerText = "$" + info.price;
    detail.querySelector(".description").innerText = info.description;
    detail.querySelector(".addCart").dataset.id = idProduct;
    console.log("products: ", products);

    // products similare
    const listProduct = document.querySelector(".listProduct");
    listProduct.innerHTML = "";
    products
      .filter((value) => value.id != idProduct)
      .forEach((product) => {
        let newProduct = document.createElement("div");
        newProduct.classList.add("item");
        // <a href="http://localhost:5000/details.html?id=${product.id}"></a>
        newProduct.innerHTML = `
            <a href="http://localhost:5000/detail">
                <img src="${product.image}"/>
            </a>

            <h2>${product.name}</h2>
            <div class="price">$${product.price}</div>
            <button class="addCart" data-id="${product.id}">
                Add To Cart
             </button>
        `;
        listProduct.appendChild(newProduct);
      });
  };

  const fetchProducts = () => {
    return $.ajax({
      url: "http://localhost:5000/products",
      method: "GET",
      dataType: "json",
    })
      .then((data) => {
        return data;
      })
      .fail((error) => {
        console.error("Error fetching products:", error);
        throw error;
      });
  };
});
