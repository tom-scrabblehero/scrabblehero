<template>
  <div class="container">
    <Title title="Find Scrabble Words"/>
    <SearchForm :prompt="this.$route.params.word" cta="Find words" v-on:setSearch="updateSearch"/>
    <SearchResult :search="search"/>
    <SearchRecommendations :search="search"/>
  </div>
</template>

<script>
import SearchForm from './SearchForm.vue'
import SearchResult from './SearchResult.vue'
import SearchRecommendations from './SearchRecommendations.vue'
import Title from './Title.vue'

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
    updateSearch: function(search) {
      console.log("Updated search")
      this.search = search
    }
  },
  mounted: function() {
    this.search = this.$route.params.word
  }
}
</script>

<style>

</style>
