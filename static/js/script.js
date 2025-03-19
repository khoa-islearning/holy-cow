// let pre = "";

document.getElementById("getFortuneBtn").addEventListener("click", function () {
  fetch("/fortune")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("fortuneText").innerText = data.fortune;
      // pre = data.raw;

      // hide response cow
      // document.getElementById("responseText").style.display = "none";
      // document.getElementById("getResponseBtn").style.display = "inherit";
    })
    .catch((error) => console.error("Error fetching fortune:", error));
});

// document
//   .getElementById("getResponseBtn")
//   .addEventListener("click", function () {
//     fetch("/response", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({
//         msg: pre,
//       }),
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         document.getElementById("responseText").innerText = data.response;
//         document.getElementById("responseText").style.display = "inherit";
//       })
//       .catch((error) => console.error("Error fetching response:", error));
//   });
