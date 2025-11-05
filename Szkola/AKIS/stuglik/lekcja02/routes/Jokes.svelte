<script>
    import { onMount } from 'svelte';
    let joke = null;
    let categoriesPromise;
    let selectedCategory = '';

    async function fetchJokes() {
        const res = await fetch('https://api.chucknorris.io/jokes/random');
        joke = await res.json();
        console.log(joke)
    }

    async function fetchJokeByCategory(category) {
        if (!category) return;
        const res = await fetch(`https://api.chucknorris.io/jokes/random?category=${category}`);
        joke = await res.json();
        console.log(joke)
    }

    async function get_categories(){
        const res = await fetch('https://api.chucknorris.io/jokes/categories');
        const data = await res.json();
        console.log(data)
        return data;
    }
    
    onMount(() => {
        fetchJokes();
        categoriesPromise = get_categories();
    })
</script>

<main class="flex flex-row items-center justify-center gap-10">
    <select bind:value={selectedCategory} on:change={() => fetchJokeByCategory(selectedCategory)}>
        <option selected disabled value="Select a category"> Select a category</option>
        {#await categoriesPromise}
            <option>Loading...</option>
        {:then categories}
            {#each categories as category}
                <option value={category}>{category}</option>
            {/each}
        {/await}
    </select>

    {#if joke}
        <img src="{joke.icon_url}" alt="Joke icon">
        <p>{joke.value}</p>
    {/if}
</main>
