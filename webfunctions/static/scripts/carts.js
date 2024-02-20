import products from "./products.js";
const cart = () => {
  $(document).ready(function () {
    const iconCart = document.querySelector(".icon-cart");
    const closeBtn = document.querySelector(".cartTab .close");
    const body = document.querySelector("body");
    // console.log(body);
    const cart = [];

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
        } else {
          cart[position].quantity = quantity;
        }
      }
      refreshCartHTML();
    };

    const refreshCartHTML = () => {
      let listHTML = document.querySelector(".listCart");
      let totalHTML = document.querySelector(".icon-cart span");

      let totalQuantity = 0;
      listHTML.innerHTML = "";
      cart.forEach((item) => {
        totalQuantity = totalQuantity + item.quantity;
        let position = products.findIndex(
          (value) => value.id == item.product_id
        );
        let info = products[position];
        let newITem = document.createElement("div");
        newITem.classList.add("item");
        newITem.innerHTML = `
          <div class="image">
            <img src="${info.image}" />
          </div>
          <div class="name">Name</div>
          <div class="totalPrice">
          $111
          </div>
          <div class="quantity">
            <span class="minus">-</div>
            <span>1</span>
            <span class="plus">+</span>
          </div>
      `;

        listHTML.appendChild(newITem);
      });
      // let position = products.findIndex(
      //   (value) => value.id == item.product_id
      // );
      // // alert(position);
      // let info = products[position];
      // let newITem = document.createElement("div");
      // newITem.classList.add("item");
      // newITem.innerHTML = `
      //     <div class="image">
      //       <img src="${info.image}" />
      //     </div>
      //     <div class="name">Name</div>
      //     <div class="totalPrice">
      //     ${info.price * item.quantity}
      //     </div>
      //     <div class="quantity">
      //       <span class="minus">-</div>
      //       <span>${item.quantity}</span>
      //       <span class="plus">+</span>
      //     </div>
      // `;
      // listHTML.appendChild(newITem);
      // });

      totalHTML.innerText = totalQuantity;
    };

    // listen for click events
    document.addEventListener("click", (event) => {
      let buttonClick = event.target;
      let idProduct = buttonClick.dataset.id;
      // alert(idProduct);
      let position = cart.findIndex((value) => value.product_id == idProduct);
      let quantity = position < 0 ? 0 : cart[position].quantity;
      if (buttonClick.classList.contains("addCart")) {
        quantity++;
        setProductInCart(idProduct, quantity, position);
      }
    });
  });
};
export default cart;
