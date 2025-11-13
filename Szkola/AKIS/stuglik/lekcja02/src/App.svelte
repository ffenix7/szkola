<script lang='js'>
  import Header from '../routes/Header.svelte';
  import Countries from '../routes/Countries.svelte';
  import Colorpicker from '../routes/Colorpicker.svelte';
  import Quiz from '../routes/Quiz.svelte';
  import Quiz2 from '../routes/Quiz2.svelte';
  import Jokes from '../routes/Jokes.svelte';
  import NotFound from '../routes/NotFound.svelte';
  import Index from '../routes/Index.svelte';
  import { Router, Link, Route } from "svelte-routing";
  export let url = "";
  
  function getUrl(code){
    return `https://flagicons.lipis.dev/flags/4x3/${code.toLowerCase()}.svg`;
  }
  let value = 'PL';
  </script>

  <Header />

 <Router url="{url}">

    <Route path="/"><Index /></Route>
    <Route path="/countries"><Countries /></Route>
    <Route path="/colorpicker"><Colorpicker /></Route>
    <Route path="/jokes"><Jokes /></Route>
    <Route path="/quiz"><Quiz /></Route>
    <Route path="/quiz2"><Quiz2 /></Route>
    <Route path="/*"><NotFound /></Route>

</Router>