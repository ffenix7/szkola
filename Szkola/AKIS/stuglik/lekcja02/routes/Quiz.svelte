<script>
    import defaultQuestions from '../quiz.json';
    let questions = [...defaultQuestions];
    questions.sort(() => Math.random() - 0.5);
    questions.forEach(q => q.options.sort(() => Math.random() - 0.5));
    let currentQuestion = 0;
    let points = 0;
    let selectedOption = null;
    let showAnswer = false;

    function checkAnswer(selected) {
        if (showAnswer) return; // blokada wielokrotnego klikania
        selectedOption = selected;
        showAnswer = true;
        if (selected === questions[currentQuestion].answer) {
            points += 1;
        }
    }

    function nextQuestion() {
        currentQuestion += 1;
        selectedOption = null;
        showAnswer = false;
    }

    function handleFileChange(event) {
        const file = event.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const text = typeof e.target.result === 'string' ? e.target.result : String(e.target.result);
                const data = JSON.parse(text);
                if (Array.isArray(data) && data.length > 0 && data[0].question && data[0].options && data[0].answer) {
                    questions = [...data];
                    questions.sort(() => Math.random() - 0.5);
                    questions.forEach(q => q.options.sort(() => Math.random() - 0.5));
                    currentQuestion = 0;
                    points = 0;
                } else {
                    alert('Nieprawidłowy format pliku!');
                }
            } catch (err) {
                alert('Błąd podczas wczytywania pliku!');
            }
        };
        reader.readAsText(file);
    }
</script>

<div class="max-w-3xl mx-auto p-4">
    <input type="file" accept="application/json" onchange={handleFileChange}>
    {#if currentQuestion < questions.length}
        <div class="bg-white shadow-md rounded p-6 mb-4">
            <h2 class="text-2xl font-bold mb-4">Question {currentQuestion + 1} of {questions.length}</h2>
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
                <button class="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600" onclick={()=> {currentQuestion = 0; points = 0; selectedOption = null; showAnswer = false;}}>Retake the quiz</button>
        </div>
    {/if}
</div>
