import products from "./products.js";
const cart = () => {
  $(document).ready(function () {
    const iconCart = document.querySelector(".icon-cart");
    const closeBtn = document.querySelector(".cartTab .close");
    const body = document.querySelector("body");
    // console.log(body);
    let cart = [];

    iconCart.addEventListener("click", () => {
      body.classList.toggle("activeTabCart");
      // alert("Icon cart clicked");
    });
    closeBtn.addEventListener("click", () => {
      body.classList.toggle("activeTabCart");
      // alert("close button clicked");
    });
    const setProductInCart = (idProduct, quantity, position) => {
      if (quantity > 0) {
        if (position < 0) {
          cart.push({
            product_id: idProduct,
            quantity: quantity,
          });
          console.log("idProduct", idProduct);
        } else {
          cart[position].quantity = quantity;
          console.log("idproduct:", idProduct);
        }
      } else {
        cart.splice(position, 1);
      }
      localStorage.setItem("cart", JSON.stringify(cart));
      refreshCartHTML();
    };

    const refreshCartHTML = () => {
      let listHTML = document.querySelector(".listCart");
      let totalHTML = document.querySelector(".icon-cart span");

      let totalQuantity = 0;
      listHTML.innerHTML = "";

      cart.forEach((item) => {
        console.log("item", item);
        totalQuantity = totalQuantity + item.quantity;
        // console.log("product id is:", product_id);
        let position = products.findIndex(
          (value) => value.id == item.product_id
        );
        // console.log("value.id", value.id);
        console.log("item product_id:", item.product_id);

        console.log("positionss is :", position);
        let info = products[position];
        console.log("info: ", info);
        let newITem = document.createElement("div");
        newITem.classList.add("item");
        newITem.innerHTML = `
          <div class="image">
            <img src="${info.image}" />
          </div>
          <div class="name">${info.name}</div>
          <div class="totalPrice">$${info.price * item.quantity}</div>
          <div class="quantity">
            <span class="minus" data-id="${info.id}">-</span>
            <span>${item.quantity}</span>
            <span class="plus" data-id="${info.id}">+</span>
          </div>
      `;

        listHTML.appendChild(newITem);
      });
      totalHTML.innerText = totalQuantity;
    };

    // listen for click events
    document.addEventListener("click", (event) => {
      let buttonClick = event.target;
      console.log("idDDProduct:", buttonClick.dataset.id);
      let idProduct = buttonClick.dataset.id;
      let position = cart.findIndex((value) => value.product_id == idProduct);

      let quantity = position < 0 ? 0 : cart[position].quantity;
      if (buttonClick.classList.contains("addCart")) {
        quantity++;
        setProductInCart(idProduct, quantity, position);
      } else if (buttonClick.classList.contains("plus")) {
        quantity++;
        setProductInCart(idProduct, quantity, position);
      } else if (buttonClick.classList.contains("minus")) {
        quantity--;
        setProductInCart(idProduct, quantity, position);
      }
    });
    const initApp = () => {
      if (localStorage.getItem("cart")) {
        cart = JSON.parse(localStorage.getItem("cart"));
      }
      refreshCartHTML();
    };

    initApp();
  });
};
export default cart;
