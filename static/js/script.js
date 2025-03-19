document.getElementById("getFortuneBtn").addEventListener("click", function () {
  fetch("/fortune")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("fortuneText").innerText = data.fortune;
    })
    .catch((error) => console.error("Error fetching fortune:", error));
});
