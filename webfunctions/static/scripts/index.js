import cart from "./cart.js";
// import products from "./products.js";
$(document).ready(function () {
  const app = document.getElementById("app");
  const temporaryContent = document.getElementById("temporaryContent");

  const fileURL = "http://localhost:5000/template";
  const loadTemplate = () => {
    fetch(`${fileURL}`)
      .then((response) => response.text())
      .then((html) => {
        app.innerHTML = html;
        const contentTab = document.getElementById("contentTab");
        contentTab.innerHTML = temporaryContent.innerHTML;
        temporaryContent.innerHTML = "";

        cart();
        initApp();
      });
  };
  loadTemplate();
  const initApp = () => {
    //loads the product list
    $.ajax({
      url: "http://localhost:5000/products",
      method: "GET",
      dataType: "json",
      success: function (products) {
        const listProduct = document.querySelector(".listProduct");
        listProduct.innerHTML = "";
        $.each(products, function (_, product) {
          let newProduct = document.createElement("div");
          newProduct.classList.add("item");
          // <a href="../templates/detail.html?id=${product.id}">
          newProduct.innerHTML = `
            <a href="http://localhost:5000/detail?id=${product.id}">
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
      },
      error: function (error) {
        console.error("Error fetching products:", error);
      },
    });
  };
});
