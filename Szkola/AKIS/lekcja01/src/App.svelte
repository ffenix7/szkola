<script lang='js'>
  import countries from './data/countries.json';
  
  function getUrl(code){
    return `https://flagicons.lipis.dev/flags/4x3/${code}.svg`;
  }
  let value;
  </script>

  <select bind:value={value}>
    <option value="" disabled selected>Wybierz kraj</option>
    {#each countries as country}
      <option value={country.code}>{country.name}</option>
    {/each}
  </select>
