<template>
  <div class="row">
    <div class="col-md-12">
      <h1 class="text-light text-center">{{ title }}</h1>
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
