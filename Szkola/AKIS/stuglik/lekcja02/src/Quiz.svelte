<script>
    import questions from '../quiz.json';
    questions.sort(() => Math.random() - 0.5);
    questions.forEach(q => q.options.sort(() => Math.random() - 0.5));
    console.log(questions);

    let currentQuestion = 0;
    let points = 0;

    function checkAnswer(selected){
        if(selected === questions[currentQuestion].answer){
            points+=1;
        }
        currentQuestion += 1;
    }
</script>

<div class="max-w-3xl mx-auto p-4">
    {#if currentQuestion < questions.length}
        <div class="bg-white shadow-md rounded p-6 mb-4">
            <h2 class="text-2xl font-bold mb-4">Question {currentQuestion + 1} of {questions.length}</h2>
            <p class="text-lg mb-4">{questions[currentQuestion].question}</p>
            <div class="space-y-2">
                {#each questions[currentQuestion].options as option}
                    <button 
                        class="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600" on:click={() => checkAnswer(option)}>
                        {option}
                    </button>
                {/each}
            </div>
        </div>
    {:else}
        <div class="bg-white shadow-md rounded p-6 text-center">
            <h2 class="text-2xl font-bold mb-4">Quiz Completed!</h2>
            <p class="text-lg">You scored {points} out of {questions.length}.</p>
            <button class="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600" on:click={()=> {currentQuestion = 0; points = 0;}}>Retake the quiz</button>
        </div>
    {/if}  
</div>
