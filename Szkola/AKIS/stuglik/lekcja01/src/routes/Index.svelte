<script>
    let title = "Welcome to AKIS Lesson 01";
</script>

<main>
    <h1>{title}</h1>
    <p>This is the index page for your Svelte project.</p>
    <nav>
        <ul>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/lessons">Lessons</a></li>
        </ul>
    </nav>
</main>

<style>
    main {
        max-width: 600px;
        margin: 2rem auto;
        padding: 2rem;
        border-radius: 8px;
        background: #f9f9f9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        text-align: center;
    }
    nav ul {
        list-style: none;
        padding: 0;
    }
    nav li {
        display: inline-block;
        margin: 0 1rem;
    }
    nav a {
        text-decoration: none;
        color: #0070f3;
        font-weight: bold;
    }
    nav a:hover {
        text-decoration: underline;
    }
</style>