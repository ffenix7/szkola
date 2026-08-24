const API_BASE = "https://www.thesportsdb.com/api/v1/json/123";

const leagues = [
  {
    id: "4328",
    name: "English Premier League",
    query: "English_Premier_League",
    country: "Anglia",
  },
  {
    id: "4335",
    name: "Spanish La Liga",
    query: "Spanish_La_Liga",
    country: "Hiszpania",
  },
  {
    id: "4331",
    name: "German Bundesliga",
    query: "German_Bundesliga",
    country: "Niemcy",
  },
  {
    id: "4332",
    name: "Italian Serie A",
    query: "Italian_Serie_A",
    country: "Wlochy",
  },
  {
    id: "4334",
    name: "French Ligue 1",
    query: "French_Ligue_1",
    country: "Francja",
  },
];

const leagueSelect = document.querySelector("#leagueSelect");
const leagueForm = document.querySelector("#leagueForm");
const loadButton = document.querySelector("#loadButton");
const statusText = document.querySelector("#statusText");
const leagueTitle = document.querySelector("#leagueTitle");
const leagueSubtitle = document.querySelector("#leagueSubtitle");
const hero = document.querySelector("#hero");
const teamCount = document.querySelector("#teamCount");
const nextMatch = document.querySelector("#nextMatch");
const nextMatchDate = document.querySelector("#nextMatchDate");
const lastMatch = document.querySelector("#lastMatch");
const lastMatchScore = document.querySelector("#lastMatchScore");
const standingsBody = document.querySelector("#standingsBody");
const teamsGrid = document.querySelector("#teamsGrid");
const teamCardTemplate = document.querySelector("#teamCardTemplate");

function fillLeagueSelect() {
  leagues.forEach((league) => {
    const option = document.createElement("option");
    option.value = league.id;
    option.textContent = `${league.name} (${league.country})`;
    leagueSelect.append(option);
  });
}

async function fetchJson(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Blad API: ${response.status}`);
  }

  return response.json();
}

function setLoading(isLoading) {
  loadButton.disabled = isLoading;
  loadButton.textContent = isLoading ? "Pobieranie..." : "Pobierz dane";
}

function formatDate(date, time) {
  if (!date) {
    return "Brak daty";
  }

  const cleanTime = time && time !== "00:00:00" ? `, ${time.slice(0, 5)}` : "";
  return `${date}${cleanTime}`;
}

function getEventName(event) {
  if (!event) {
    return "-";
  }

  return event.strEvent || `${event.strHomeTeam || "?"} vs ${event.strAwayTeam || "?"}`;
}

function getEventScore(event) {
  if (!event) {
    return "Brak danych.";
  }

  const homeScore = event.intHomeScore ?? "-";
  const awayScore = event.intAwayScore ?? "-";
  return `${formatDate(event.dateEvent, event.strTime)} | wynik: ${homeScore}:${awayScore}`;
}

function updateSummary(teams, nextEvents, pastEvents) {
  const nextEvent = nextEvents?.[0];
  const pastEvent = pastEvents?.[0];

  teamCount.textContent = teams.length || "-";
  nextMatch.textContent = getEventName(nextEvent);
  nextMatchDate.textContent = nextEvent ? formatDate(nextEvent.dateEvent, nextEvent.strTime) : "Brak danych.";
  lastMatch.textContent = getEventName(pastEvent);
  lastMatchScore.textContent = getEventScore(pastEvent);
}

function renderStandings(tableRows) {
  standingsBody.replaceChildren();

  if (!tableRows.length) {
    standingsBody.innerHTML = '<tr><td colspan="8">API nie zwrocilo tabeli dla tej ligi.</td></tr>';
    return;
  }

  tableRows.forEach((row, index) => {
    const tr = document.createElement("tr");
    const rank = row.intRank || row.rank || index + 1;
    const goalDiff = row.intGoalDifference ?? row.goaldifference ?? "-";

    tr.innerHTML = `
      <td>${rank}</td>
      <td>${row.strTeam || row.name || "-"}</td>
      <td>${row.intPlayed ?? row.played ?? "-"}</td>
      <td>${row.intWin ?? row.win ?? "-"}</td>
      <td>${row.intDraw ?? row.draw ?? "-"}</td>
      <td>${row.intLoss ?? row.loss ?? "-"}</td>
      <td>${goalDiff}</td>
      <td><strong>${row.intPoints ?? row.total ?? "-"}</strong></td>
    `;
    standingsBody.append(tr);
  });
}

function shorten(text, maxLength = 190) {
  if (!text) {
    return "Brak opisu w API.";
  }

  return text.length > maxLength ? `${text.slice(0, maxLength).trim()}...` : text;
}

function normalizeWebsite(url) {
  if (!url) {
    return "";
  }

  return url.startsWith("http") ? url : `https://${url}`;
}

function renderTeams(teams) {
  teamsGrid.replaceChildren();

  if (!teams.length) {
    teamsGrid.innerHTML = "<p>API nie zwrocilo listy druzyn.</p>";
    return;
  }

  teams.forEach((team) => {
    const card = teamCardTemplate.content.cloneNode(true);
    const badge = card.querySelector(".team-badge");
    const title = card.querySelector("h3");
    const meta = card.querySelector(".team-meta");
    const description = card.querySelector(".team-description");
    const link = card.querySelector(".team-link");

    badge.src = team.strBadge || "";
    badge.alt = `Herb klubu ${team.strTeam}`;
    title.textContent = team.strTeam || "Nieznana druzyna";
    meta.textContent = `${team.strStadium || "Nieznany stadion"} | ${team.strLocation || team.strCountry || "Brak lokalizacji"}`;
    description.textContent = shorten(team.strDescriptionEN);

    const website = normalizeWebsite(team.strWebsite);
    if (website) {
      link.href = website;
    } else {
      link.classList.add("hidden");
    }

    teamsGrid.append(card);
  });
}

function updateHero(league, teams) {
  leagueTitle.textContent = league.name;
  leagueSubtitle.textContent = `${league.country}: tabela, mecze i kluby pobrane z TheSportsDB.`;

  const teamWithFanart = teams.find((team) => team.strFanart1);
  if (teamWithFanart) {
    hero.style.backgroundImage = `linear-gradient(90deg, rgba(10, 18, 13, 0.88), rgba(10, 18, 13, 0.36)), url("${teamWithFanart.strFanart1}")`;
  }
}

async function loadLeague(leagueId) {
  const league = leagues.find((item) => item.id === leagueId) || leagues[0];

  setLoading(true);
  statusText.textContent = `Pobieranie danych: ${league.name}...`;
  standingsBody.innerHTML = '<tr><td colspan="8">Ladowanie tabeli...</td></tr>';
  teamsGrid.replaceChildren();

  try {
    const [teamsData, tableData, nextData, pastData] = await Promise.all([
      fetchJson(`${API_BASE}/search_all_teams.php?l=${encodeURIComponent(league.query)}`),
      fetchJson(`${API_BASE}/lookuptable.php?l=${league.id}`),
      fetchJson(`${API_BASE}/eventsnextleague.php?id=${league.id}`),
      fetchJson(`${API_BASE}/eventspastleague.php?id=${league.id}`),
    ]);

    const teams = teamsData.teams || [];
    const tableRows = tableData.table || [];
    const nextEvents = nextData.events || [];
    const pastEvents = pastData.events || [];

    updateHero(league, teams);
    updateSummary(teams, nextEvents, pastEvents);
    renderStandings(tableRows);
    renderTeams(teams);
    statusText.textContent = `Gotowe. Dane pobrano z publicznego API TheSportsDB.`;
  } catch (error) {
    statusText.textContent = "Nie udalo sie pobrac danych. Sprawdz polaczenie z internetem albo limit API.";
    standingsBody.innerHTML = '<tr><td colspan="8">Wystapil blad podczas pobierania danych.</td></tr>';
    teamsGrid.innerHTML = `<p>${error.message}</p>`;
  } finally {
    setLoading(false);
  }
}

leagueForm.addEventListener("submit", (event) => {
  event.preventDefault();
  loadLeague(leagueSelect.value);
});

fillLeagueSelect();
loadLeague(leagues[0].id);
