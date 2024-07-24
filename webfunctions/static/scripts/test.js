$(document).ready(function () {
  //   const app = $("#app");
  const app = document.getElementById("app");

  //   const temporaryContent = $("#temporaryContent");
  const temporaryContent = document.getElementById("temporaryContent");
  console.log("hello");

  const loadTemplate = () => {
    fetch("http://localhost:5000/template")
      .then((response) => response.text())
      .then((htmlContent) => {
        app.innerHTML = htmlContent;
        const contentTab = document.getElementById("contentTab");
        // $("#contentTab").html(temporaryContent.html());
        contentTab.innerHTML = temporaryContent.innerHTML;
        temporaryContent.innerHTML = "";
      })
      .catch((error) => {
        console.error("Error fetching template: ", error);
      });
  };

  loadTemplate();
});
