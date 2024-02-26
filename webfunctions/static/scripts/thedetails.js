import cart from "./cart.js";

$(document).ready(function () {
  let products = [];
  let app = $("#app");

  const temporaryContent = $("#temporaryContent");

  const loadTemplate = () => {
    fetch("http://localhost:5000/template")
      .then((response) => response.text())
      .then((html) => {
        app.innerhtml = html;
        // let contentTab = document.getElementById("contentTab");
        // contentTab.innerHTML = temporaryContent.innerHTML;
        // temporaryContent.innerHTML = "";
        $("#contentTab").html(temporaryContent.html());
        // temporaryContent.html("");

        // = document.getElementById("contentTab");
        // console.log("contentTab", contentTab);

        // contentTab.innerHTML = temporaryContent.innerHTML;

        // temporaryContent.innerHTML = "";

        cart();
        initApp();
      });
  };
  loadTemplate();

  const initApp = async () => {
    products = await fetchProducts();
    let idProduct = new URLSearchParams(window.location.search).get("id");
    console.log("idProduct", idProduct);
    let info = products.find((value) => value.id == idProduct);

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

        listProduct.append(newProduct);
      }
    });
  };

  const fetchProducts = () => {
    return $.ajax({
      url: "http://localhost:5000/products",
      method: "GET",
      dataType: "json",
    });
  };

  //   console.log("the contentTab is:", contentTab);
  //   console.log("now app is:", app);
});
