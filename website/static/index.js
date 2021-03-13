function deleteStock(stockId) {
  fetch("/delete-stock", {
    method: "POST",
    body: JSON.stringify({ stockId: stockId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
