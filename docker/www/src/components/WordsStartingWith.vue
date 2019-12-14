<template>
  <div class="container">
    <Title title="Words starting with..." />
    <SearchForm v-if="loaded" cta="Search" @search="search" />
    <SearchRecommendations v-if="loaded" :words="words" />
  </div>
</template>


<script>
import Title from './Title.vue'
import SearchRecommendations from './SearchRecommendations.vue'
import SearchForm from './SearchForm.vue'


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
    SearchRecommendations,
    SearchForm
  },
  methods: {
    update: function() {
      this.$api.get(`/words/starting-with/${this.$route.params.letters}`).then(data => this.words = data.data)
    },
    search: function(letters) {
      this.$router.push({name: 'words-starting-with', params: {'letters': letters}})
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
