<template>
  <div id="app" class="container">
    <Title title="Find Scrabble Words"/>
    <SearchForm prompt="Enter a word or letters" cta="Find words" v-on:setSearch="test"/>
    <SearchResult :search="search"/>
    <SearchRecommendations :search="search"/>
  </div>
</template>

<script>
import SearchForm from './components/SearchForm.vue'
import SearchResult from './components/SearchResult.vue'
import SearchRecommendations from './components/SearchRecommendations.vue'
import Title from './components/Title.vue'

export default {
  name: 'app',
  components: {
    SearchForm,
    Title,
    SearchResult,
    SearchRecommendations
  },
  data: function() {
    return {
      search: ''
    }
  },
  methods: {
    test: function(search) {
      this.search = search
    }
  }
}
</script>

<style>

</style>
