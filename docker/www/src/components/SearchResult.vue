<template>
<div class="row">
	<div class="col-md-6 offset-md-3">
			<b-alert :show="valid === true" variant="success">Congratulations! You can play <span class="font-weight-bold">{{`${this.search}`}}</span> in Scrabble, and it's worth <span class="font-weight-bold">{{`${this.result.score}`}} points</span>. <br><br> We also found several other similar words you can play.</b-alert>
			<b-alert :show="valid === false" variant="danger">Unfortunately, you can not play <span class="font-weight-bold">{{`${this.search}`}}</span> in Scrabble.<br><br> But we've found several other similar words you can try playing.</b-alert>
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
			result: {},
			valid: null,
			message: null
		}
	},
	methods: {
		updateResult: async function() {
			if (this.search) {
				this.result = await this.$api.get(`/words/${this.search}`)
				this.$emit("loadSearch", this.result)
				this.valid = this.result.id == null ? false : true
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
