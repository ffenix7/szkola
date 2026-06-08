const selectKolor = document.querySelector('select');
const imgSamochod = document.getElementById('prawe-zdjecie');
const felgi = document.getElementsByName('felgi');
const doposazenie = document.getElementsByName('doposażenie');

document.querySelectorAll('input').forEach(element => element.onchange = obliczWycene);
document.querySelector('select').onchange = obliczWycene; 

function obliczWycene(){
    let cena = 75000;
    let wycena = document.getElementById('wycena');
    wycena.innerHTML = ' ';

    if(selectKolor.value !== "szary"){
        wycena.innerHTML += "<br>Lakier: 9000zł";
        cena += 9000;
    }

    if(felgi[1].checked){
        wycena.innerHTML += '<br>Felgi aluminiowe: 7000zł';
        cena += 7000;
    }

    if(doposazenie[0].checked){
        wycena.innerHTML += "<br>Czujniki parkowania: 6500zł";
        cena += 6500;
    }

    if(doposazenie[1].checked){
        wycena.innerHTML += "<br>Climatronic: 8500zł";
        cena += 8500;
    }

    if(doposazenie[2].checked){
        wycena.innerHTML += "<br>Nawigacja: 5000zł";
        cena += 5000;
    }
    wycena.innerHTML += "<hr><b>RAZEM: </b>" + cena + "zł"

}

const mapaKolorow = {
	czerwony: 'czerwony.png',
	niebieski: 'niebieski.png',
	zielony: 'zielony.png',
	szary: 'szary.png',
	zolty: 'zolty.png'
};

selectKolor.addEventListener('change', function(){
    const wybranyKolor = selectKolor.value;
    if (mapaKolorow[wybranyKolor]) {
        imgSamochod.src = mapaKolorow[wybranyKolor];
    }
    obliczWycene();
});

