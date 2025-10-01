<script lang='js'>
  import countries from '../data/countries.json';
  import Header from '../routes/Header.svelte';
  
  function getUrl(code){
    return `https://flagicons.lipis.dev/flags/4x3/${code.toLowerCase()}.svg`;
  }
  let value = 'PL';
  </script>
    <!--  <Header /> -->


  <div class="flex flex-row justify-center items-center mt-20 bg-gray-200 p-10 shadow-lg">
    <h1>Wybierz kraj:</h1>
    <select bind:value={value}>
      {#each countries as {name,code}}
        <option value={code}>{name}</option>
      {/each}
    </select>

      <img src={getUrl(value)} alt="Flaga" class="w-48" />
  </div>