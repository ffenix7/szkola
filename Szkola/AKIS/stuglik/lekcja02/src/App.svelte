<script lang='js'>
  import Header from '../routes/Header.svelte';
  import Countries from '../routes/Countries.svelte';
  import Colorpicker from '../routes/Colorpicker.svelte';
  import Quiz from './Quiz.svelte';
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
    <Route path="/quiz"><Quiz /></Route>
    <Route path="/*"><NotFound /></Route>
</Router>