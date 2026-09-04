<script>
    import { onMount } from 'svelte';

    let all_pokemons_names = [];
    let pokemon_count = 0;
    let result = [];
    let query = '';
    let isLoading = true;
    let itemsPerPage = 8;
    let currentPage = 1;
    let pokemonCache = {};

    $: displayedPokemons = (() => {
        const data = result.length > 0 ? result : all_pokemons_names;
        const startIdx = (currentPage - 1) * itemsPerPage;
        return data.slice(startIdx, startIdx + itemsPerPage);
    })();

    $: totalPages = Math.ceil((result.length > 0 ? result.length : all_pokemons_names.length) / itemsPerPage);

    async function getPokemonSprite(pokeName, pokemonId){
        if(pokemonCache[pokeName]) return pokemonCache[pokeName];
        try {
            const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokeName}`);
            const data = await response.json();
            pokemonCache[pokeName] = data.sprites.front_default;
            pokemonCache = pokemonCache; // Trigger reactivity
            return pokemonCache[pokeName];
        } catch(err) {
            console.error('Error loading sprite for', pokeName, err);
            return null;
        }
    }

    async function getPokemonCount(){
        const data = await fetch('https://pokeapi.co/api/v2/pokemon-species/');
        const json = await data.json();
        return json.count;
    }

    async function searchPokemon(){
        if (!all_pokemons_names || all_pokemons_names.length === 0) return;
        const lowerQuery = query.toLowerCase();
        result = all_pokemons_names.filter(pokeName => pokeName && pokeName.includes(lowerQuery));
        currentPage = 1;
    }

    onMount(async () => {
        try {
            pokemon_count = await getPokemonCount();
            console.log('Pokemon count:', pokemon_count);
            
            // Load from localStorage if available
            if(localStorage.getItem('all_pokemons_names')){
                const stored_names = JSON.parse(localStorage.getItem('all_pokemons_names'));
                if(Array.isArray(stored_names) && stored_names.length > 0) {
                    all_pokemons_names = [...stored_names];
                    console.log('Loaded from localStorage:', all_pokemons_names.length);
                    isLoading = false;
                    return;
                }
            }
            
            console.log('Fetching pokemon names...');
            all_pokemons_names = [];
            for(let i=0;i<pokemon_count;i++){
                const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${i+1}`);
                const data = await response.json();
                all_pokemons_names.push(data.name);
                if((i+1) % 100 === 0) console.log(`Loaded ${i+1}/${pokemon_count}`);
            }
            localStorage.setItem('all_pokemons_names', JSON.stringify(all_pokemons_names));
            all_pokemons_names = [...all_pokemons_names]; 
            console.log('Saved to localStorage:', all_pokemons_names.length);
            isLoading = false;
        } catch(err) {
            console.error('Error loading pokémons:', err);
            isLoading = false;
        }
    });
</script>

<nav class="flex flex-row gap-6 justify-center items-center bg-white text-gray-800 rounded-2xl mx-auto my-8 py-6 px-8 shadow-lg max-w-3xl border border-cyan-200">
        <div class="flex flex-col gap-1">
            <label for="pokemon_name" class="font-semibold text-base tracking-wide">Szukana fraza</label>
            <input id="pokemon_name" type="text" placeholder="search pokemon..." bind:value={query} oninput={searchPokemon} class="rounded-xl px-4 py-2 text-base bg-cyan-50 text-gray-700 shadow focus:shadow-lg focus:outline-none w-40" />
        </div>
        <div class="flex flex-col gap-1">
            <label for="count" class="font-semibold text-base tracking-wide">Ilość wyników na stronę</label>
            <input id="count" type="number" min="1" max="50" bind:value={itemsPerPage} onchange={() => currentPage = 1} class="rounded-xl px-4 py-2 text-base bg-cyan-50 text-gray-700 shadow focus:shadow-lg focus:outline-none w-32" />
        </div>
        <div class="flex flex-col gap-1">
            <label for="page" class="font-semibold text-base tracking-wide">Strona</label>
            <input id="page" type="number" min="1" max={totalPages} bind:value={currentPage} class="rounded-xl px-4 py-2 text-base bg-cyan-50 text-gray-700 shadow focus:shadow-lg focus:outline-none w-32" />
        </div>
</nav>

<div class="min-h-screen overflow-y-auto bg-gradient-to-br from-cyan-50 to-cyan-100 pb-8">
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6 w-full max-w-6xl mx-auto my-8 bg-white/80 rounded-3xl p-8 shadow-xl border border-cyan-200">
        {#if isLoading}
            <div class="col-span-full text-center py-8 text-lg text-cyan-700 font-semibold">
                <p>Ładowanie pokemonów...</p>
            </div>
        {:else}
            {#each displayedPokemons as pokemon, idx}
            <a href={`/pokeinfo?id=${(currentPage - 1) * itemsPerPage + idx + 1}`} class="block">
                <div class="flex flex-col items-center justify-center bg-white rounded-xl shadow border border-cyan-100 p-5 hover:scale-105 hover:shadow-2xl transition-transform duration-200">
                    {#await getPokemonSprite(pokemon, (currentPage - 1) * itemsPerPage + idx + 1)}
                        <div class="w-24 h-24 flex items-center justify-center text-3xl text-cyan-400">⏳</div>
                    {:then spriteUrl}
                        {#if spriteUrl}
                            <img src={spriteUrl} alt={pokemon} class="w-24 h-24 object-contain mb-2 bg-cyan-50 rounded-lg shadow" />
                        {:else}
                            <div class="w-24 h-24 flex items-center justify-center text-3xl text-red-400">❌</div>
                        {/if}
                    {/await}
                    <h3 class="mt-2 text-lg font-bold text-cyan-700 tracking-wide capitalize">{pokemon}</h3>
                </div>
            </a>
            {/each}
        {/if}
    </div>

    {#if !isLoading && totalPages > 1}
        <div class="flex flex-wrap justify-center items-center gap-3 mt-8">
            <button style="cursor: pointer;" class="select-none px-4 py-2 text-base bg-cyan-400 text-white rounded-lg font-semibold transition disabled:opacity-50" onclick={() => currentPage = Math.max(1, currentPage - 1)} disabled={currentPage === 1}>
                ← Poprzednia
            </button>
            {#if currentPage > 2}
                <button style="cursor: pointer;" class="select-none px-3 py-2 text-base bg-cyan-100 text-cyan-700 rounded-lg transition" onclick={() => currentPage = 1}>1</button>
                {#if currentPage > 3}
                    <span class="select-none px-2 text-xl">⋯</span>
                {/if}
            {/if}
            {#if currentPage > 1}
                <button style="cursor: pointer;" class="select-none px-3 py-2 text-base bg-cyan-100 text-cyan-700 rounded-lg transition" onclick={() => currentPage = currentPage - 1}>{currentPage - 1}</button>
            {/if}
            <button style="cursor: pointer;" class="select-none px-4 py-2 text-base bg-cyan-400 text-white rounded-lg font-bold cursor-default shadow disabled" disabled>
                {currentPage}
            </button>
            {#if currentPage < totalPages}
                <button style="cursor: pointer;" class="select-none px-3 py-2 text-base bg-cyan-100 text-cyan-700 rounded-lg transition" onclick={() => currentPage = currentPage + 1}>{currentPage + 1}</button>
            {/if}
            {#if currentPage < totalPages - 1}
                {#if currentPage < totalPages - 2}
                    <span class="select-none px-2 text-xl">⋯</span>
                {/if}
                <button style="cursor: pointer;" class="select-none px-3 py-2 text-base bg-cyan-100 text-cyan-700 rounded-lg transition" onclick={() => currentPage = totalPages}>{totalPages}</button>
            {/if}
            <button style="cursor: pointer;" class="select-none px-4 py-2 text-base bg-cyan-400 text-white rounded-lg font-semibold transition disabled:opacity-50" onclick={() => currentPage = Math.min(totalPages, currentPage + 1)} disabled={currentPage === totalPages}>
                Następna →
            </button>
        </div>
    {/if}
</div>