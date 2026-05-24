// Finalized app.js (Simulating Copilot output)
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
            <p><strong>Schedule:</strong> ${data.schedule}</p>
            <div class="participants">
                <h4>Participants:</h4>
                <ul>
                    ${data.participants.map(p => `<li>${p} <button onclick="unregister('${name}', '${p}')">Unregister</button></li>`).join("")}
                </ul>
            </div>
            <button onclick="signup('${name}')">Sign Up</button>
        `;
        container.appendChild(card);
    }
}

async function unregister(activityName, email) {
    console.log(`Unregistering ${email} from ${activityName}`);
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
