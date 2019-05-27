<template>
  <booking-detail :is-edit="false" />
</template>

<script>
import BookingDetail from './components/BookingDetail'

export default {
  name: 'CreateForm',
  components: { BookingDetail },
  mounted() {
    console.log('#####', 'create')
  }
}
</script>

