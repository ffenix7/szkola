addEventListener('DOMContentLoaded', () => {
    let cookiesAccepted = document.cookie.split('; ').find(row => row.startsWith('cookies_accepted='));
    if(!cookiesAccepted) {
        let cookiePopUp = document.createElement('div');
        cookiePopUp.innerHTML = `
            <div style="position: fixed; bottom: 10px; left: 10px; right: 10px; background: lightgray; padding: 10px; border: 1px solid gray; z-index: 1000;">
                Dej ciastka
                <button id="accept-cookies">Accept</button>
            </div>
        `;
        document.body.appendChild(cookiePopUp);
        document.getElementById('accept-cookies').addEventListener('click', () => {
            document.body.removeChild(cookiePopUp);
            document.cookie = "cookies_accepted=true; max-age=" + Number.MAX_SAFE_INTEGER;
        });
    }

});