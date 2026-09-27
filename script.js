// Visitor counter — this will call API Gateway endpoint once we build the backend
// (Steps 5 & 6 of the Cloud Resume Challenge: Lambda + DynamoDB + API Gateway)

const API_ENDPOINT = "https://qp4d54zz9f.execute-api.us-east-1.amazonaws.com/count";

async function loadVisitorCount() {
  const counterEl = document.getElementById("counter");
  try {
    const response = await fetch(API_ENDPOINT);
    const data = await response.json();
    counterEl.textContent = data.count;
  } catch (err) {
    // Falls back gracefully until the backend is deployed
    counterEl.textContent = "—";
    console.log("Visitor counter not connected yet:", err);
  }
}

loadVisitorCount();
