<template>
  <div class="container">
    <Title v-if="loaded" :title="title" />
    <SearchForm v-if="loaded" cta="Search other words" @search="search"/>
    <SearchResult v-if="loaded" :status_code="status_code" :word="word" />
    <SearchRecommendations v-if="loaded" :words="recommendations" title="Similar words"/>
  </div>
</template>

<script>
import SearchForm from './SearchForm.vue'
import Title from './Title.vue'
import SearchResult from './SearchResult.vue'
import SearchRecommendations from './SearchRecommendations.vue'

export default {
  name: 'word',
  components: {
    SearchResult,
    SearchForm,
    SearchRecommendations,
    Title
  },
  data: function() {
    return {
      word: null,
      recommendations: [],
      status_code: null
    }
  },
  methods: {
    update: function() {
      this.$api.get(`/words/${this.$route.params.word}`).then(data => {
        this.word = data.data;
        this.status_code = data.status_code;
      })
      this.$api.get(`/words/${this.$route.params.word}/recommendations`).then(data => {
        this.recommendations = data.data
      })
    },
    search: function(input) {
      this.$router.push({name: 'words', params: {'word': input}})
    }
  },
  computed: {
    loaded: function() {
      return (this.recommendations) != null && (this.word != null)
    },
    title: function() {
      if (this.status_code == 200) {
        return `"${this.$route.params.word.toUpperCase()}" is a valid scrabble word`
      } else {
        return `"${this.$route.params.word.toUpperCase()}" is not a valid scrabble word`
      }
    }
  },
  mounted: function() {
    this.update()
  },
  watch: {
    $route: function(to, from) {
      this.update()
    }
  }
}
</script>

<style>

</style>
