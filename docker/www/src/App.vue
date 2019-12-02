<template>
  <div id="app" class="container">
    <Title />
    <SearchResult value="Search a word"/>
  </div>
</template>

<script>
import SearchResult from './components/SearchResult.vue'
import Title from './components/Title.vue'

export default {
  name: 'app',
  components: {
    SearchResult,
    Title
  },
  created: function() {
    console.log(process.env);
  }
}
</script>

<style>

</style>
