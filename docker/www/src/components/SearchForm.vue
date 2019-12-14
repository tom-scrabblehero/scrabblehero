<template>
  <div class="row">
    <div class="col-md-6 offset-md-3">
    <b-form @submit.prevent="setSearch">
    <b-form-group>
      <b-form-input v-model="input" required variant="outline-primary" type="text" placeholder="Enter letters or word" auto-focus="true"></b-form-input>
    </b-form-group>
    <b-form-group>
      <b-button block class="btn-lg" variant="primary" type="submit" value="Submit">{{ cta }}</b-button>
    </b-form-group>
    </b-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchForm",
  props: {
    prompt: String,
    cta: String
  },
  data: function() {
    return {
      input: null
    }
  },
  methods: {
    setSearch: function() {
      this.$emit('search', this.input)
    }
  }
}
</script>
