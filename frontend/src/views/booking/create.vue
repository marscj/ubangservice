<template>
  <booking-detail :is-edit="false" />
</template>

<script>
import BookingDetail from './components/BookingDetail'

export default {
  name: 'CreateBooking',
  components: { BookingDetail }
}
</script>

