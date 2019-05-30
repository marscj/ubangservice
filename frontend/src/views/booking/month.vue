<template>
  <booking-list/>
</template>

<script>
import BookingList from './components/BookingList'

export default {
  name: 'MonthBooking',
  components: { BookingList },
  data() {
    return {
      title: this.$moment().format('MMM') + ' Booking'
    }
  },
  created() {
    const route = Object.assign({}, this.$route, { title: this.title })
    this.$store.dispatch('tagsView/updateVisitedView', route)
  }
}
</script>