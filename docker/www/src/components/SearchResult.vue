<template>
<div class="row">
	<div class="col-md-6 offset-md-3">
		<h3 class="text-secondary" v-if="search">Search results</h3>
		<p v-if="search" >Searched word: {{ result.id }}</p>
		<p v-if="search">Score: {{ result.score }}</p>
	</div>
</div>
</template>

<script>
export default {
	name: "SearchResult",
	props: {
		search: String
	},
	data: function() {
		return {
			result: {}
		}
	},
	methods: {
		updateResult: async function() {
			if (this.search) {
				this.result = await this.$api.get(`/words/${this.search}`)
			}
		}
	},
	watch: {
		search: function() {
			this.updateResult()
		}
	}
}
</script>

<style>
</style>
