<template>
  <div class="row">
    <div class="col-md-6 offset-md-3">
    <b-form @submit.prevent="setSearch">
    <b-form-group>
      <b-form-input v-model="input" type="text" :placeholder="prompt" required auto-focus="true"></b-form-input>
    </b-form-group>
    <b-form-group>
      <b-button block variant="primary" type="submit" value="Submit">{{ cta }}</b-button>
    </b-form-group>
    </b-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchResult",
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
      this.$emit("setSearch", this.input)
    }
  }
}
</script>
