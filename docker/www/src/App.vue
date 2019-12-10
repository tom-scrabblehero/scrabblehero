<template>
  <div id="app" class="container">
    <Title />
    <SearchForm value="Search a word"/>
    <SearchResult search="" />
  </div>
</template>

<script>
import SearchForm from './components/SearchForm.vue'
import SearchResult from './components/SearchResult.vue'
import Title from './components/Title.vue'

export default {
  name: 'app',
  components: {
    SearchForm,
    Title,
    SearchResult
  },
  created: function() {
    console.log(process.env);
  }
}
</script>

<style>

</style>
