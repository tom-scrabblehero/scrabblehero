<template>
  <div id="app" class="container">
    <SearchResult value="Search a word"/>
  </div>
</template>

<script>
import SearchResult from './components/SearchResult.vue'

export default {
  name: 'app',
  components: {
    SearchResult
  },
  created: function() {
    console.log(process.env);
  }
}
</script>

<style>

</style>
