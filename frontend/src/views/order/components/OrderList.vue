<template>
  <div class="app-container">
    <h1 v-if="isSelf">
      My Order
    </h1>
    <h1 v-else>
      Order List
    </h1>
  </div>
</template>

<script>
export default {
  props: {
    isSelf: {
      type: Boolean,
      default: false
    }
  }
}
</script>
