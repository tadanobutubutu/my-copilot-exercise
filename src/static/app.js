const apiBase = "/activities";

async function fetchActivities() {
    const response = await fetch(apiBase);
    const activities = await response.json();
    renderActivities(activities);
}

function renderActivities(activities) {
    const container = document.getElementById("activities-container");
    container.innerHTML = "";
    for (const [name, data] of Object.entries(activities)) {
        const card = document.createElement("div");
        card.className = "activity-card";
        card.innerHTML = `
            <h3>${name}</h3>
            <p>${data.description}</p>
            <p><strong>Participants:</strong></p>
            <ul class="participant-list">
                ${data.participants.map(p => `<li>${p} <button class="unregister-btn" onclick="unregister('${name}', '${p}')">X</button></li>`).join("")}
            </ul>
            <button onclick="signup('${name}')">Sign Up</button>
        `;
        container.appendChild(card);
    }
}

async function unregister(activityName, email) {
    await fetch(`/activities/${activityName}/unregister?email=${email}`, { method: 'POST' });
    await fetchActivities();
}

async function signup(activityName) {
    const email = prompt("Enter your email:");
    if (email) {
        await fetch(`/activities/${activityName}/signup?email=${email}`, { method: 'POST' });
        await fetchActivities();
    }
}

fetchActivities();
