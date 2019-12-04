<template>
  <div class="row">
    <div class="col-md-6 offset-md-3">
    <b-form @submit.prevent="checkValue">
    <b-form-group>
      <b-form-input v-model="form.search" type="text" placeholder="Enter a word" required auto-focus="true"></b-form-input>
    </b-form-group>
    <b-form-group>
      <b-button block variant="primary" type="submit" value="Submit">Check word</b-button>
    </b-form-group>
    </b-form>
    <b-alert :show="result.show" :variant="result.variant">{{ result.value }}</b-alert>
    </div>
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
      form: {
        search: ""
      },
      result: {
        value: "",
        show: false,
        variant: "info"
      }
    }
  },
  methods: {
    checkValue: function(e) {
      var that = this
      fetch(`${process.env.VUE_APP_API_URL}/words/${this.form.search}`).then(function(resp) {
        resp.json().then(function(data) {
          var message
          if (resp.status == 200) {
            message = `is a valid word worth ${data.score} points`
            that.result.variant = "success"
          } else {
            message = "is not a valid word"
            that.result.variant = "danger"
          }
          that.result.value = `${that.form.search} ${message}`
          that.result.show = true
        })
      })
    }
  }
}
</script>
