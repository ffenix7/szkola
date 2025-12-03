<script>
  import { onMount } from 'svelte';

  let name = '';
  let pokemon = null;
  let isLoading = true;
  let error = '';

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
  <div style="max-width: 400px; margin: 2em auto; background: #f3f4f6; border-radius: 1em; padding: 2em; box-shadow: 0 2px 8px #0001;">
    <h2 style="text-align:center">{pokemon.name.charAt(0).toUpperCase() + pokemon.name.slice(1)}</h2>
    <img src={pokemon.sprites.front_default} alt={pokemon.name} style="display:block;margin:1em auto;max-width:200px;" />
    <ul>
      <li><b>ID:</b> {pokemon.id}</li>
      <li><b>Typy:</b> {pokemon.types.map(t => t.type.name).join(', ')}</li>
      <li><b>Wzrost:</b> {pokemon.height / 10} m</li>
      <li><b>Waga:</b> {pokemon.weight / 10} kg</li>
      <li><b>Podstawowe statystyki:</b>
        <ul>
          {#each pokemon.stats as stat}
            <li>{stat.stat.name}: {stat.base_stat}</li>
          {/each}
        </ul>
      </li>
    </ul>
  </div>
{/if}