<template>
  <booking-detail :is-edit="true" />
</template>

<script>
import BookingDetail from './components/BookingDetail'

export default {
  name: 'EditForm',
  components: { BookingDetail },
  mounted() {
    console.log('#####', 'edit')
  }
}
</script>

