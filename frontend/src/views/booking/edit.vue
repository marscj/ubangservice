<template>
  <booking-detail :is-edit="true" />
</template>

<script>
import BookingDetail from './components/BookingDetail'

export default {
  name: 'EditBooking',
  components: { BookingDetail }
}
</script>

