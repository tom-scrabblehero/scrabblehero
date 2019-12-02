<template>
  <div id="app">
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
