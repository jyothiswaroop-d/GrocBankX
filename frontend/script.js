const backendURL = "http://127.0.0.1:5000";

function pay() {
  const amount = document.getElementById("amount").value;
  const items = document.getElementById("items").value;

  fetch(`${backendURL}/check-fraud`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      amount: amount,
      items: items
    })
  })
  .then(res => res.json())
  .then(data => {
    if (data.status === "SUSPICIOUS") {
      alert("⚠ Suspicious transaction detected. Please verify.");
      openCamera();
    } else {
      alert("✅ Payment Successful. Groceries booked!");
    }
  });
}

function openCamera() {
  document.getElementById("cameraBox").style.display = "block";

  navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
      document.getElementById("video").srcObject = stream;
    });
}

function capture() {
  const video = document.getElementById("video");
  const canvas = document.createElement("canvas");

  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0);

  canvas.toBlob(blob => {
    const formData = new FormData();
    formData.append("image", blob);

    fetch(`${backendURL}/verify-face`, {
      method: "POST",
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      if (data.status === "APPROVED") {
        alert("✅ Identity verified. Payment Successful!");
      } else {
        alert("❌ Face not matched. Payment Blocked!");
      }
    });
  }, "image/jpeg");
}
