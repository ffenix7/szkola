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
            const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId}`);
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
            
            // Załaduj z cache
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

<style>
     .pokemons-container {
        display: flex;
        flex-wrap: wrap;
        gap: 1.5rem;
        justify-content: center;
        align-items: center;
        width: 80%;
        margin: 2rem auto;
        background-color: antiquewhite;
        border-radius: 10px;
        padding: 2em;
    }
    .pokemon-card {
        text-align: center;
        background-color: rgba(59, 130, 246, 0.4);
        border-radius: 10px;
    }

    .pokemon-card:hover {
        background-color: rgba(59, 130, 246, 0.6);
        transition: .5s;
    }
</style>

<nav>
    <label for="pokemon_name">Szukana fraza</label>
    <input id="pokemon_name" type="text" placeholder="search pokemon..." bind:value={query} oninput={searchPokemon} />

    <label for="count">Ilość wyników na stronę</label>
    <input id="count" type="number" min="1" max="50" bind:value={itemsPerPage} onchange={() => currentPage = 1} />

    <label for="page">Strona</label>
    <input id="page" type="number" min="1" max={totalPages} bind:value={currentPage} />
</nav>

<div class="container">
    <div class="pokemons-container">
        {#if isLoading}
            <div style="text-align: center; padding: 2rem;">
                <p>Ładowanie pokemonów...</p>
            </div>
        {:else}
            {#each displayedPokemons as pokemon, idx}
            <a href={`/pokeinfo?name=${pokemon}`}> 
                <div class="pokemon-card">
                    {#await getPokemonSprite(pokemon, (currentPage - 1) * itemsPerPage + idx + 1)}
                        <div style="width: 96px; height: 96px; display: flex; align-items: center; justify-content: center;">
                            ⏳
                        </div>
                    {:then spriteUrl}
                        {#if spriteUrl}
                            <img src={spriteUrl} alt={pokemon} />
                        {:else}
                            <div style="width: 96px; height: 96px; display: flex; align-items: center; justify-content: center;">
                                ❌
                            </div>
                        {/if}
                    {/await}
                    <h3>{pokemon}</h3>
                </div>
            </a>
            {/each}
        {/if}
    </div>
    

    {#if !isLoading && totalPages > 1}
        <div style="display: flex; justify-content: center; align-items: center; gap: 0.75rem; margin-top: 2rem; flex-wrap: wrap;">
            <button style="user-select: none; padding: 0.75rem 1.25rem; font-size: 1rem; background-color: #3b82f6; color: white; border: none; border-radius: 0.5rem; cursor: pointer; font-weight: 600; transition: all 0.2s;" onclick={() => currentPage = Math.max(1, currentPage - 1)} disabled={currentPage === 1}>
                ← Poprzednia
            </button>
            
            {#if currentPage > 2}
                <button style="user-select: none; padding: 0.75rem 1rem; font-size: 1rem; background-color: #e5e7eb; color: #1f2937; border: none; border-radius: 0.5rem; cursor: pointer; transition: all 0.2s;" onclick={() => currentPage = 1}>1</button>
                {#if currentPage > 3}
                    <span style="user-select: none; padding: 0 0.5rem; font-size: 1.25rem;">⋯</span>
                {/if}
            {/if}
            
            {#if currentPage > 1}
                <button style="user-select: none; padding: 0.75rem 1rem; font-size: 1rem; background-color: #e5e7eb; color: #1f2937; border: none; border-radius: 0.5rem; cursor: pointer; transition: all 0.2s;" onclick={() => currentPage = currentPage - 1}>{currentPage - 1}</button>
            {/if}
            
            <button style="user-select: none; padding: 0.75rem 1.25rem; font-size: 1rem; background-color: #3b82f6; color: white; border: none; border-radius: 0.5rem; font-weight: bold; cursor: default; box-shadow: 0 0 0 2px #dbeafe;" disabled>
                {currentPage}
            </button>
            
            {#if currentPage < totalPages}
                <button style="user-select: none; padding: 0.75rem 1rem; font-size: 1rem; background-color: #e5e7eb; color: #1f2937; border: none; border-radius: 0.5rem; cursor: pointer; transition: all 0.2s;" onclick={() => currentPage = currentPage + 1}>{currentPage + 1}</button>
            {/if}
            
            {#if currentPage < totalPages - 1}
                {#if currentPage < totalPages - 2}
                    <span style="user-select: none; padding: 0 0.5rem; font-size: 1.25rem;">⋯</span>
                {/if}
                <button style="user-select: none; padding: 0.75rem 1rem; font-size: 1rem; background-color: #e5e7eb; color: #1f2937; border: none; border-radius: 0.5rem; cursor: pointer; transition: all 0.2s;" onclick={() => currentPage = totalPages}>{totalPages}</button>
            {/if}
            
            <button style="user-select: none; padding: 0.75rem 1.25rem; font-size: 1rem; background-color: #3b82f6; color: white; border: none; border-radius: 0.5rem; cursor: pointer; font-weight: 600; transition: all 0.2s;" onclick={() => currentPage = Math.min(totalPages, currentPage + 1)} disabled={currentPage === totalPages}>
                Następna →
            </button>
        </div>
    {/if}
</div>