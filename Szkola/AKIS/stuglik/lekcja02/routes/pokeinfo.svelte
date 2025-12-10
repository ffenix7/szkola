<script>
  import { onMount } from 'svelte';

  let name = '';
  let pokemon = null;
  let isLoading = true;
  let error = '';
  let description = '';

  // Kolory typów
  const typeColors = {
    normal: '#A8A77A',
    fire: '#EE8130',
    water: '#6390F0',
    electric: '#F7D02C',
    grass: '#7AC74C',
    ice: '#96D9D6',
    fighting: '#C22E28',
    poison: '#A33EA1',
    ground: '#E2BF65',
    flying: '#A98FF3',
    psychic: '#F95587',
    bug: '#A6B91A',
    rock: '#B6A136',
    ghost: '#735797',
    dragon: '#6F35FC',
    dark: '#705746',
    steel: '#B7B7CE',
    fairy: '#D685AD'
  };

  // Pobierz nazwę pokemona z query stringa
  onMount(async () => {
    const params = new URLSearchParams(window.location.search);
    name = params.get('name');
    if (!name) {
      error = 'Nie podano nazwy pokemona w adresie URL (?name=...)';
      isLoading = false;
      return;
    }
    try {
      const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${name.toLowerCase()}`);
      if (!res.ok) throw new Error('Nie znaleziono pokemona');
      pokemon = await res.json();

      // Pobierz opis pokemona
      const speciesRes = await fetch(`https://pokeapi.co/api/v2/pokemon-species/${name.toLowerCase()}`);
      if (speciesRes.ok) {
        const speciesData = await speciesRes.json();
        // Szukaj polskiego opisu, jeśli nie ma to angielski
        const entryPL = speciesData.flavor_text_entries.find(e => e.language.name === 'pl');
        const entryEN = speciesData.flavor_text_entries.find(e => e.language.name === 'en');
        description = entryPL ? entryPL.flavor_text : (entryEN ? entryEN.flavor_text : 'Brak opisu.');
        // Usuń znaki nowej linii
        description = description.replace(/\f|\n/g, ' ');
      } else {
        description = 'Brak opisu.';
      }
    } catch (e) {
      error = e.message;
    } finally {
      isLoading = false;
    }
  });
</script>

{#if isLoading}
  <p>Ładowanie danych pokemona...</p>
{:else if error}
  <p style="color: red">Błąd: {error}</p>
{:else if pokemon}
  <div class="max-w-lg mx-auto my-10 bg-white/80 rounded-3xl p-8 shadow-xl border border-cyan-200 animate-fadeIn font-sans">
    <div class="relative text-center mb-6">
      <img src={pokemon.sprites.front_default} alt={pokemon.name} class="block mx-auto mb-2 max-w-xs bg-cyan-50 rounded-xl shadow-lg p-4 transition-transform duration-300 hover:scale-105" />
      <h2 class="text-3xl font-bold text-cyan-700 mb-1 tracking-wide capitalize">{pokemon.name.charAt(0).toUpperCase() + pokemon.name.slice(1)}</h2>
      <span class="absolute top-2 right-6 bg-cyan-400 text-white px-4 py-1 rounded-full text-base font-semibold shadow">#{pokemon.id}</span>
      {#if description}
        <div class="mt-4 mb-2 text-base italic text-gray-700 bg-cyan-50 rounded-xl px-4 py-3 shadow text-center whitespace-pre-line">{description}</div>
      {/if}
    </div>
    <div class="flex flex-wrap justify-center gap-2 mb-4">
      {#each pokemon.types as t}
        <span class="px-4 py-1 rounded-full font-semibold text-white shadow text-base capitalize" style="background: {typeColors[t.type.name] || '#6366f1'}">{t.type.name}</span>
      {/each}
    </div>
    <div class="flex justify-between mb-4 text-base">
      <div><b>Wzrost:</b> {pokemon.height / 10} m</div>
      <div><b>Waga:</b> {pokemon.weight / 10} kg</div>
    </div>
    <div class="mt-4">
      <b class="block mb-2 text-cyan-700">Statystyki:</b>
      <div class="space-y-2">
        {#each pokemon.stats as stat}
          <div class="flex items-center">
            <span class="w-32 font-semibold text-cyan-600 capitalize mr-2">{stat.stat.name}</span>
            <span class="flex-1 flex items-center">
              <span class="h-3 rounded bg-cyan-400 mr-2 transition-all duration-500" style="width: {Math.min(stat.base_stat, 150)}px"></span>
              <span class="font-bold text-gray-700 ml-1">{stat.base_stat}</span>
            </span>
          </div>
        {/each}
      </div>
    </div>
  </div>
{/if}
<!-- Tailwind CSS classes applied above -->