<template>
<div class="row">
	<div class="col-md-6 offset-md-3">
			<b-alert v-if="status_code == 200" :show="status_code == 200" variant="success">
				<p>Congratulations! You can play <span class="font-weight-bold">{{`${this.$route.params.word.toUpperCase()}`}}</span> in Scrabble, and it's worth <span class="font-weight-bold">{{`${this.word.score}`}} points</span></p>
				<p><span class="font-weight-bold">Definition</span>: {{ this.word.definition }}</p>
				<p> We also found several other similar words you can play.</p></b-alert>
			<b-alert v-if="status_code == 404" :show="status_code == 404" variant="danger">
				<p>Unfortunately, you can not play <span class="font-weight-bold">{{`${this.$route.params.word.toUpperCase()}`}}</span> in Scrabble.</p>
				<p>But we've found several other similar words you can try playing.</p>
			</b-alert>
	</div>
</div>
</template>

<script>
export default {
	name: "SearchResult",
	props: {
		word: Object,
		status_code: Number
	}
}
</script>

<style>
</style>
