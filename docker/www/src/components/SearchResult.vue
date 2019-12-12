<template>
<div class="row">
	<div class="col-md-6 offset-md-3">
			<b-alert v-if="status_code == 200" :show="status_code == 200" variant="success">Congratulations! You can play <span class="font-weight-bold">{{`${this.word.id}`}}</span> in Scrabble, and it's worth <span class="font-weight-bold">{{`${this.word.score}`}} points</span>. <br><br> We also found several other similar words you can play.</b-alert>
			<b-alert v-if="status_code == 404" :show="status_code == 404" variant="danger">Unfortunately, you can not play <span class="font-weight-bold">{{`${this.$route.params.word}`}}</span> in Scrabble.<br><br> But we've found several other similar words you can try playing.</b-alert>
	</div>
</div>
</template>

<script>
export default {
	name: "SearchResult",
	props: {
		word: Object,
		status_code: Boolean
	}
}
</script>

<style>
</style>
