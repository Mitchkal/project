import cart from "./carts.js";
import products from "./products.js";
$(document).ready(function () {
  const app = document.getElementById("app");
  const temporaryContent = document.getElementById("temporaryContent");

  const loadTemplate = () => {
    fetch("../templates/template.html")
      .then((response) => response.text())
      .then((html) => {
        app.innerHTML = html;
        const contentTab = document.getElementById("contentTab");
        contentTab.innerHTML = temporaryContent.innerHTML;
        temporaryContent.innerHTML = null;

        cart();
        initApp();
      });
  };
  loadTemplate();
  const initApp = () => {
    //loads the product list
    console.log(products);
    const listProduct = document.querySelector(".listProduct");
    listProduct.innerhtml = null;
    products.forEach((product) => {
      let newProduct = document.createElement("div");
      newProduct.classList.add("item");
      newProduct.innerHTML = `
            <a href="../templates/details.html?id=${product.id}">
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
});
