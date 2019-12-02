<template>
  <div>
  <form @submit.prevent="checkValue">
  <h2 class="text-primary">{{ value }}</h2>
  <input type="text" placeholder="Search a word" ref="search" autofocus=true>
  <input type="submit" value="Submit">
  <p>{{ result }}</p>
  </form>
  </div>
</template>

<script>
export default {
  name: "SearchResult",
  props: {
    value: String
  },
  data: function() {
    return {
      result: ""
    }
  },
  methods: {
    checkValue: function() {
      var search = this.$refs.search.value
      var that = this
      fetch(`${process.env.VUE_APP_API_URL}/words/${search}`).then(function(resp) {
        resp.json().then(function() {
          var message
          if (resp.status == 200) {
            message = "is a valid word"
          } else {
            message = "is not a valid word"
          }
          that.result = `"${search}" ${message}`
        })
      })
    }
  }
}
</script>
