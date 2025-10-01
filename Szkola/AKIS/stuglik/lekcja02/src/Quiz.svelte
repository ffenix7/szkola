<script>
    import questions from '../quiz.json';
    console.log(questions);
</script>

<div class="max-w-3xl mx-auto p-4">
    {#each questions as item}
        <div class="mb-6 p-4 rounded-lg shadow-md bg-white border border-gray-200">
            <h2 class="text-xl font-semibold mb-3">{item.question}</h2>
            <ul class="space-y-2">
                {#each item.options as option, i}
                    <button class="border-b-2 border-r-2 border-black w-full flex flex-row text-black hover:bg-gray-100 transition ease-in-out duration-200 m-2">
                        <span class="p-2 bg-gray-200">{i + 1}</span>
                        <span class="p-2">{option}</span>
                    </button>
                {/each}
            </ul>
        </div>
    {/each}
</div>
