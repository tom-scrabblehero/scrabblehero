<template>
  <div class="row">
    <div class="col-md-12">
      <h1 class="mt-4 mb-4 text-primary text-center">{{ title }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "Title",
  props: {
    title: String
  }
}
</script>
