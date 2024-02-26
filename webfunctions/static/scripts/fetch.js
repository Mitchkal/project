// const axios = require("axios");
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

products = fetchProducts();
// console.log(products);
