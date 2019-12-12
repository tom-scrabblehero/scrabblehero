<template>
  <div class="container">
    <Title :title="this.$route.params.word" />
    <SearchForm cta="Search other words" />
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
    }
  },
  computed: {
    loaded: function() {
      return (this.recommendations) != null && (this.word != null)
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
