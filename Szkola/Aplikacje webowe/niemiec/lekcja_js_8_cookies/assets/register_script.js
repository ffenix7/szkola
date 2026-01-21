import { countryList } from './countries.js';

addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const countryInput = document.querySelector('input[name="country"]');

    countryInput.addEventListener('input',async function e(e) {
        // if(e.target.value.length <2) {
        //     return;
        // }
        const resp = await fetch('/country-search/' + encodeURIComponent(e.target.value.trim())); 
        const countries = await resp.json();
        console.log(countries);

        const countriesDiv = document.getElementById('countries');
        countriesDiv.innerHTML = '';

        const trimmed = e.target.value.trim();
        if (countries.length === 0 && trimmed.length > 0) {
                countryInput.style.border = '2px solid red';
                error.style.color = 'red'
                error.textContent = 'No such country!';
        }
        else{
            const match = countries.find(c => c.toLowerCase() === trimmed.toLowerCase());
            if (match) {
                countryInput.style.border = '2px solid green';
                error.textContent = '';
            } else {
                countryInput.style.border = '1px solid black';
                error.textContent = '';
            }
        }

        for (let i=0; i<countries.length; i++) {
            const country = countries[i];
            const button = document.createElement('div');
            
            button.textContent = country;
            button.onclick = function() {
                countryInput.value = country;
                countriesDiv.innerHTML = '';
                countryInput.style.border = '2px solid green';
                error.textContent = '';
            }
            button.style.border = '1px solid black';
            button.style.padding = '5px';
            button.style.margin = '5px';
            button.style.cursor = 'pointer';
            button.style.width = 'fit-content';
            button.style.backgroundColor = '#f0f0f0';
            button.style.borderRadius = '5px';
            countriesDiv.appendChild(button);
        }
    })

    const emailInput = document.querySelector('input[name="email"]');
    const error = document.getElementById('email-error');

    emailInput.addEventListener('input', async function e(e) {
        const value = e.target.value;
        if (value.includes('@') && value.includes('.')) {
            emailInput.style.border = '2px solid green';
            const resp = await fetch('/check-user/' + encodeURIComponent(e.target.value.trim()));
            const data = await resp.json();
            
            emailInput.style.border = '2px solid green';
            error.textContent = '';
            if (data.exists) {
                emailInput.style.border = '2px solid red';
                error.style.color = 'red'
                error.textContent = 'Email is already registered';
            }
        } else {
            emailInput.style.border = '2px solid red';
        }
    });

    const password1 = document.querySelector('input[name="password1"]');
    const password2 = document.querySelector('input[name="password2"]');

    if(password1 && password2) {
        password2.addEventListener('input', (e) => {
            if (password1.value === password2.value) {
                password2.style.border = '2px solid green';
            } else {
                password2.style.border = '2px solid red';
            }
        });
    }

        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            if (password1 && password2 && password1.value !== password2.value) {
                alert('Passwords do not match');
                return;
            }

            if (!emailInput.value.includes('@') || !emailInput.value.includes('.')) {
                alert('Please enter a valid email address');
                return;
            }

            if (countryInput.value.trim().length < 2) {
                alert('Please enter a valid country name');
                return;
            }

            if(countryList.indexOf(countryInput.value.trim()) === -1) {
                alert('Please select a country from the list');
                return;
            }

            try {
                const resp = await fetch('/check-user/' + encodeURIComponent(emailInput.value.trim()));
                const data = await resp.json();
                if (data.exists) {
                    const error = document.getElementById('email-error');
                    if (error) error.textContent = 'Email is already registered';
                    emailInput.style.border = '2px solid red';
                    alert('Email is already registered');
                    return;
                }
            } catch (err) {
                console.error(err);
                alert('Could not verify email. Please try again.');
                return;
            }

            form.submit();
        });
});

console.log(document.cookie);