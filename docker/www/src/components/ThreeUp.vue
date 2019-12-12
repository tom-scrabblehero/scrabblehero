<template>
  <div class="col-md-4">
  <b-card
    class="text-center"
    :title="title"
    border-variant="light"
    header-background-variant="primary">
    <b-card-text>{{ text }}</b-card-text>
    <b-button block variant="outline-primary" :href="url">{{ cta }}</b-button>
  </b-card>
  </div>
</template>


<script>
export default {
  'name': 'ThreeUp',
  'props': {
    title: String,
    text: String,
    cta: String,
    url: String
  }
}
</script>
