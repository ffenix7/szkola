<script>
    let r,g,b;
</script>

<h2 class="text-2xl font-bold text-center pt-20">Color picker</h2>

<div class="flex flex-col items-center pt-10">
    <main class="flex flex-row ">
        <div style="width:500px; height:250px; background-color: rgb({r},{g},{b})"></div>
        <div class="flex flex-col gap-4 ml-4 justify-center">
            <div>R: {r}<input class="accent-black" type="range" min="0" max="255" bind:value={r} /></div>
            <div>G: {g}<input class="accent-black" type="range" min="0" max="255" bind:value={g} /></div>
            <div>B: {b}<input class="accent-black" type="range" min="0" max="255" bind:value={b} /></div>
        </div>
    </main>
</div>
