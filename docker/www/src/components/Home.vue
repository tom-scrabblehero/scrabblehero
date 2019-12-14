<template>
  <div class="container">
    <Title title="Find Scrabble Words"/>
    <SearchForm prompt="Enter a word or letters" cta="Find words" v-on:setSearch="test"/>
    <div class="row mt-4 text-center">
      <div class="col-md-6 offset-md-3">
        <h2 class="text-info">Improve your Scrabble and "Words With Friends" skills with our free resources and tools</h2>
      </div>
    </div>
    <div class="row mt-4">
      <ThreeUp title="Two letter words" cta="Learn more" text="All valid two letter word combinations. No need to memorize them all, just bookmark this page!" url="/two-letter-words"/>
      <ThreeUp title="Words starting with..." cta="Learn more" text="Find words that start with the letters from your hand" url="/words/starting-with/AA"/>
    </div>
  </div>
</template>

<script>
import SearchForm from './SearchForm.vue'
import Title from './Title.vue'
import ThreeUp from './ThreeUp.vue'

export default {
  name: 'app',
  components: {
    SearchForm,
    Title,
    ThreeUp
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
