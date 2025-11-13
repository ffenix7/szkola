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
                image: pokemon.sprite.style.,
                options: [pokemon.name, option1.name, option2.name, option3.name],
                answer: pokemon.name
            });
            qs[i].options.sort(() => Math.random() - 0.5);
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

    onMount(async () => {
        questions = await generateQuestions();
        questionsLoaded = true;
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
        if (questionsLoaded && currentQuestion < questions.length) {
            currentQuestion += 1;
            selectedOption = null;
        }
        showAnswer = false;
    }
</script>

<div class="max-w-3xl mx-auto p-4">
    {#if currentQuestion < questions.length}
        <div class="bg-white shadow-md rounded p-6 mb-4">
            <h2 class="text-2xl font-bold mb-4">Question {currentQuestion + 1} of {questions.length}</h2>
            <img src="{questions[currentQuestion].image}" alt="Pokémon sprite" class="mb-4 w-32 h-32 object-contain">
            <p class="text-lg mb-4">{questions[currentQuestion].question}</p>
            <div class="space-y-2">
                {#each questions[currentQuestion].options as option}
                    <button
                        class="w-full py-2 px-4 rounded bg-blue-500 text-white
                        {showAnswer && option === questions[currentQuestion].answer ? 'bg-green-500 text-white' : ''}
                        {showAnswer && selectedOption === option && option !== questions[currentQuestion].answer ? 'bg-red-500 text-white' : ''}"
                        disabled={showAnswer}
                        onclick={() => checkAnswer(option)}>
                        {option}
                    </button>
                {/each}
            </div>
                {#if showAnswer}
                    <button class="mt-4 w-full bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600" onclick={nextQuestion}>Następne pytanie</button>
            {/if}
        </div>
    {:else}
        <div class="bg-white shadow-md rounded p-6 text-center">
            <h2 class="text-2xl font-bold mb-4">Quiz Completed!</h2>
            <p class="text-lg">You scored {points} out of {questions.length}.</p>
                <button class="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600" onclick={async ()=> {questions = await generateQuestions();currentQuestion = 0; points = 0; selectedOption = null; showAnswer = false;}}>Retake the quiz</button>
        </div>
    {/if}
</div>
