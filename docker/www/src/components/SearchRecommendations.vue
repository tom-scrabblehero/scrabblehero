<template>
	<div class="row">
		<div class="col-md-6 offset-md-3">
		<h3 class="text-info text-center">{{ title }}</h3>
		<b-list-group>
			<b-list-group-item
				v-for="word in words"
				:key="word.id"
				class="d-flex justify-content-between align-items-center"
				>
					{{ word.id }}
					<b-badge variant="success">{{ word.score }} points</b-badge>
			</b-list-group-item>
		</b-list-group>
		</div>
	</div>
</template>

<script>
export default {
	name: 'SearchRecommendations',
	props: {
		words: Array,
		title: String
	}
}
</script>

<style>
</style>
