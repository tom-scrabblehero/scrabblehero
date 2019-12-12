<template>
  <div class="container">
    <Title title="Two letter words" />
    <SearchRecommendations v-if="loaded" :words="words" />
  </div>
</template>


<script>
import Title from './Title.vue'
import SearchRecommendations from './SearchRecommendations.vue'


export default {
  name: 'two-letter-words',
  data: function() {
    return {
      words: null
    }
  },
  computed: {
    loaded: function() {
      return this.words != null
    }
  },
  components: {
    Title,
    SearchRecommendations
  },
  mounted: function() {
    this.$api.get(`/two-letter-words`).then(data => this.words = data.data)
  }
}
</script>
