let products = [];
const cart = () => {
  $(document).ready(function () {
    const $iconCart = $(".icon-cart");
    const $closeBtn = $(".cartTab .close");
    const $body = $("body");
    let cart = [];

    // Toggle the cart visibility
    $iconCart.on("click", () => {
      $body.toggleClass("activeTabCart");
    });

    $closeBtn.on("click", () => {
      $body.toggleClass("activeTabCart");
    });

    // setting products in the cart
    const updateCartItem = (idProduct, quantity, position) => {
      if (quantity > 0) {
        if (position < 0) {
          cart.push({
            product_id: idProduct,
            quantity: quantity,
          });
        } else {
          cart[position].quantity = quantity;
        }
      } else {
        cart.splice(position, 1);
      }
      console.log("cart contents:", cart);
      localStorage.setItem("cart", JSON.stringify(cart));
      refreshCartHTML();
    };

    // refreshes the cart
    const refreshCartHTML = () => {
      let listHTML = document.querySelector(".listCart");
      if (listHTML !== null) {
        console.log("listHTML:", listHTML);
        //   let totalHTML = $(".icon-cart span");
        let totalHTML = document.querySelector(".icon-cart span");

        let totalQuantity = 0;
        let cartTotal = 0;
        listHTML.innerHTML = "";

        cart.forEach((item) => {
          totalQuantity += item.quantity;

          let position = products.findIndex(
            (value) => value.id == item.product_id
          );
          console.log("The products:", products);
          console.log("The following cart items: ", item);
          console.log("item quanity:", item.quantity);
          console.log("item id:", item.product_id);
          console.log("The position:", position);
          console.log("productsion:", products);
          let info = products[position];
          console.log("This is the info: ", info);
          console.log("info.price", info.price);
          let price = info.price;
          let itemTotalPrice = price * item.quantity;
          cartTotal += itemTotalPrice;
          let newItem = document.createElement("div");
          newItem.classList.add("item");

          newItem.innerHTML = `
                <div class="image">
                  <img src="${info.image}" />
                </div>
                <div class="name">${info.name}</div>
                <div class="totalPrice">$${itemTotalPrice}</div>
                <div class="quantity">
                  <span class="minus" data-id="${info.id}">-</span>
                  <span>${item.quantity}</span>
                  <span class="plus" data-id="${info.id}">+</span>
                </div>
            `;
          listHTML.appendChild(newItem);
        });
        totalHTML.innerText = totalQuantity;
        //   $totalHTML.text(totalQuantity);
        $("#cartTotal").text(cartTotal);
      } else {
        console.log("listHTML is null. Cnnot refresh cart");
      }
    };

    // Event delegation for click events
    $(document).on("click", ".addCart, .plus, .minus", function () {
      let idProduct = $(this).data("id");
      console.log("idProduct", idProduct);
      let position = cart.findIndex((value) => value.product_id == idProduct);
      console.log("click position:", position);
      let quantity = position < 0 ? 0 : cart[position].quantity;

      if ($(this).hasClass("addCart") || $(this).hasClass("plus")) {
        quantity++;
      } else if ($(this).hasClass("minus")) {
        quantity--;
      }
      updateCartItem(idProduct, quantity, position);
    });
    const fetchProducts = () => {
      return $.ajax({
        url: "http://localhost:5000/products",
        method: "GET",
        dataType: "json",
        success: function (data) {
          return data;
        },
        error: function (error) {
          console.error("Error fetching products:", error);
          throw error;
        },
      });
    };

    const initApp = async () => {
      try {
        products = await fetchProducts();
        if (localStorage.getItem("cart")) {
          cart = JSON.parse(localStorage.getItem("cart"));
          console.log("new cart contents", cart);
        }
        refreshCartHTML();
      } catch (error) {
        console.error("Error initializing app:", error);
      }
    };

    initApp();
  });
};
export default cart;
