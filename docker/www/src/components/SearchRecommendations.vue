<template>
	<div class="row">
		<div class="col-md-6 offset-md-3">
		<h3 class="text-info text-center" v-if="search">Similar words</h3>
		<b-list-group>
			<b-list-group-item
				v-for="item in result"
				:key="item.id"
				class="d-flex justify-content-between align-items-center"
				>
					{{ item.id }}
					<b-badge variant="success">{{ item.score }} points</b-badge>
			</b-list-group-item>
		</b-list-group>
		</div>
	</div>
</template>

<script>
export default {
	name: 'SearchRecommendations',
	props: {
		search: String
	},
	data: function() {
		return {
			result: []
		}
	},
	methods: {
		updateResult: async function() {
			if (this.search) {
				this.result = await this.$api.get(`/words/${this.search}/recommendations`)
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
