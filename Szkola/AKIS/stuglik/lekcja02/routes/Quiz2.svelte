<script>
import { onMount } from 'svelte';

    async function getPokemonData(id){
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
        return response.json();
    }

    async function getPokemonCount(){
        const data = await fetch('https://pokeapi.co/api/v2/pokemon-species/');
        const json = await data.json();
        return json.count;
    }

    async function getRandomPokemon(){
        const count = await getPokemonCount();
        const randomId = Math.floor(Math.random() * count) + 1; 
        const pokemonData = await getPokemonData(randomId);
        let data = {
            name: pokemonData.name,
            sprite: pokemonData.sprites.front_default
        };
        return data;
    }

    async function generateQuestions(){
        const num_questions = 5;
        let qs = [];
        for(let i=0;i<num_questions;i++){
            const pokemon = await getRandomPokemon();
            const option1 = await getRandomPokemon();
            const option2 = await getRandomPokemon();
            const option3 = await getRandomPokemon();
            qs.push({
                question: `What is the name of this Pokémon?`,
                sprite: pokemon.sprite,
                options: [pokemon.name, option1.name, option2.name, option3.name],
                answer: pokemon.name
            });
            qs[i].options.sort(() => Math.random() - 0.5);
            console.log('Generated question', qs[i]);
        }
        return qs;
    }

    onMount(async () => {
        try {
            const count = await getPokemonCount();
            console.log('pokemon count', count);

            const pokemon = await getRandomPokemon();
            console.log('random pokemon data', pokemon);
        } catch (err) {
            console.error('failed to get pokemon count', err);
        }
    });

    let questions = [];
    let currentQuestion = 0;
    let points = 0;
    let selectedOption = null;
    let showAnswer = false;
    let questionsLoaded = false;
    let quizFinished = false;
    let results_history = [];

    onMount(async () => {
        questions = await generateQuestions();
        questionsLoaded = true;
        results_history = JSON.parse(localStorage.getItem('results_history') || '[]');
    });

    function checkAnswer(selected) {
        if (showAnswer) return; // blokada wielokrotnego klikania
        selectedOption = selected;
        showAnswer = true;
        if (selected === questions[currentQuestion].answer) {
            points += 1;
        }
    }

    function nextQuestion() {
        if (questionsLoaded && currentQuestion < questions.length - 1) {
            currentQuestion += 1;
            selectedOption = null;
            showAnswer = false;
        } else {
            quizFinished = true;
            showAnswer = false;
            setHighscore();
        }
    }

    function setHighscore() {
        let highscore = localStorage.getItem('highscore') || 0;
        let name = prompt("Podaj swój nick:");
        if (points > +highscore) {
            localStorage.setItem('highscore', points.toString());
        }
        results_history = JSON.parse(localStorage.getItem('results_history') || '[]');
        results_history.push({ date: new Date().toISOString(), score: points, name: name });
        localStorage.setItem('results_history', JSON.stringify(results_history));
        results_history = [...results_history];
    }
</script>

<div class="max-w-3xl mx-auto p-4 min-h-screen bg-gradient-to-br from-blue-100 to-purple-100">
    {#if !quizFinished}
        {#if questionsLoaded && questions.length > 0 && questions[currentQuestion]}
            <div class="bg-white shadow-lg rounded-xl p-8 mb-6 flex flex-col items-center">
                <h2 class="text-2xl font-bold mb-4 text-blue-700">Pytanie {currentQuestion + 1} z {questions.length}</h2>
                <img src="{questions[currentQuestion].sprite}" alt="Pokémon sprite" class="mb-4 w-32 h-32 object-contain drop-shadow-lg transition-all duration-300 {selectedOption ? 'brightness-100' : 'brightness-0'}" />
                <p class="text-lg mb-4 text-gray-700">{questions[currentQuestion].question}</p>
                <div class="space-y-2 w-full">
                    {#each questions[currentQuestion].options as option}
                        <button
                            class="w-full py-2 px-4 rounded-lg border border-blue-300 font-semibold shadow-sm transition-colors duration-200
                            bg-blue-500 text-white hover:bg-blue-600
                            {showAnswer && option === questions[currentQuestion].answer ? 'bg-green-500 border-green-600 text-white' : ''}
                            {showAnswer && selectedOption === option && option !== questions[currentQuestion].answer ? 'bg-red-500 border-red-600 text-white' : ''}"
                            disabled={showAnswer}
                            onclick={() => checkAnswer(option)}>
                            {option}
                        </button>
                    {/each}
                </div>
                    {#if showAnswer}
                        <button class="mt-4 w-full bg-gray-700 text-white py-2 px-4 rounded-lg font-semibold hover:bg-gray-800 transition-colors duration-200" onclick={nextQuestion}>Następne pytanie</button>
                {/if}
            </div>
        {/if}
    {:else}
        <div class="bg-white shadow-lg rounded-xl p-8 text-center max-w-lg mx-auto mt-8">
            <h2 class="text-2xl font-bold mb-4 text-green-700">Quiz ukończony!</h2>
            <p class="text-lg mb-6 text-gray-700">Twój wynik: <span class="font-bold text-green-600">{points}</span> z <span class="font-bold">{questions.length}</span>.</p>
            <button class="w-full bg-green-500 text-white py-2 px-4 rounded-lg font-semibold hover:bg-green-600 transition-colors duration-200 mb-6" onclick={async ()=> {
                questions = await generateQuestions();
                currentQuestion = 0;
                points = 0;
                selectedOption = null;
                showAnswer = false;
                quizFinished = false;
            }}>Spróbuj ponownie</button>
        </div>
        <div class="overflow-x-auto mt-8">
            <table class="min-w-full bg-white rounded-xl shadow-md">
                <thead>
                    <tr>
                        <th colspan="4" class="text-center py-3 text-lg font-semibold text-blue-700 bg-blue-100 rounded-t-xl">Najlepsze wyniki:</th>
                    </tr>
                    <tr class="bg-blue-50 text-blue-800">
                        <th class="py-2 px-4">Lp.</th>
                        <th class="py-2 px-4">Nick</th>
                        <th class="py-2 px-4">Wynik</th>
                        <th class="py-2 px-4">Data</th>
                    </tr>
                </thead>
                <tbody>
                    {#each results_history as result, idx}
                    <tr class="even:bg-gray-50 hover:bg-blue-50 transition-colors">
                        <td class="py-2 px-4 text-center">{idx + 1}</td>
                        <td class="py-2 px-4 text-center">{result.name}</td>
                        <td class="py-2 px-4 text-center">{result.score} pkt</td>
                        <td class="py-2 px-4 text-center">{new Date(result.date).toLocaleString()}</td>
                    </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    {/if}
</div>
