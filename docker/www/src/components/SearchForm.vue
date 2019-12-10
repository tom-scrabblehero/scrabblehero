<template>
  <div class="row">
    <div class="col-md-6 offset-md-3">
    <b-form @submit.prevent="setSearch">
    <b-form-group>
      <b-form-input v-model="input" type="text" placeholder="Enter letters" required auto-focus="true"></b-form-input>
    </b-form-group>
    <b-form-group>
      <b-button block variant="primary" type="submit" value="Submit">Find words</b-button>
    </b-form-group>
    </b-form>
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
      search: null,
      input: null
    }
  },
  methods: {
    setSearch: function() {
      this.search = this.input;
      console.log(this.search);
    }
  }
}
</script>
