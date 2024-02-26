// import { initializeApp } from "@firebase/app";
import cart from "./cart.js";
console.log("CART contents is:", cart);
let products = [];

$(document).ready(function () {
  const app = $("#app");
  const temporaryContent = $("#temporaryContent");

  const loadTemplate = () => {
    $.ajax({
      url: "http://localhost:5000/template",
      method: "GET",
      success: function (html) {
        app.html(html);
        $("#contentTab").html(temporaryContent.html());
        temporaryContent.html("");
        cart();

        initApp();
      },
      error: function (error) {
        console.error("Error loading template:", error);
      },
    });
  };
  console.log("executing loadtemplate");
  loadTemplate();

  const initApp = async () => {
    try {
      products = await fetchProducts();
      const idProduct = new URLSearchParams(window.location.search).get("id");
      const info = products.find((value) => value.id == idProduct);
      console.log("initapp info", info);

      if (!info) {
        window.location.href = "http://localhost:5000/";
      }

      const detail = $(".detail");
      console.log("details detail:", detail);
      detail.find(".image img").attr("src", info.image);
      detail.find(".name").text(info.name);
      detail.find(".price").text("$" + info.price);
      detail.find(".description").text(info.description);
      detail.find(".addCart").attr("data-id", idProduct);

      const listProduct = $(".listProduct");
      listProduct.html("");
      $.each(products, function (index, product) {
        console.log("products: ", products);
        if (product.id != idProduct) {
          const newProduct = $("<div>", { class: "item" }).html(`
            <a href="http://localhost:5000/detail?id=${product.id}">
              <img src="${product.image}"/>
            </a>
            <h2>${product.name}</h2>
            <div class="price">$${product.price}</div>
            <button class="addCart" data-id="${product.id}">
              Add To Cart
            </button>
          `);
          console.log("tHE NEWproduct: ", newProduct);
          listProduct.append(newProduct);
        }
      });
      //   $(".addCart").on("click", addToCart);
    } catch (error) {
      console.error("Error initializing app:", error);
    }
  };

  const fetchProducts = () => {
    return $.ajax({
      url: "http://localhost:5000/products",
      method: "GET",
      dataType: "json",
    });
  };
  //   const addToCart = (event) => {
  //     const productId = $(event.target).data("id");

  //     //logic
  //     console.log("Adding product with ID", productId, "to cart");
  //   };
});
