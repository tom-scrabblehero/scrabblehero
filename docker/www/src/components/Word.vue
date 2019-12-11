<template>
  <div class="container">
    <Title :title="this.title" />
    <SearchForm :prompt="this.$route.params.word" cta="Search other words" v-on:setSearch="updateSearch"/>
    <SearchResult :search="search" v-on:loadSearch="updateTitle"/>
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
      search: '',
      title: `Checking if "${this.$route.params.word}" is valid...`
    }
  },
  methods: {
    updateSearch: function(search) {
      this.search = search
    },
    updateTitle: function(result) {
      if (result.id) {
        this.title = `"${this.$route.params.word}" is a valid scrabble word`
      } else {
        this.title = `"${this.$route.params.word}" is not a valid scrabble word`
      }
    }
  },
  mounted: function() {
    this.search = this.$route.params.word
  }
}
</script>

<style>

</style>
