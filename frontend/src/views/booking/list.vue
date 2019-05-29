<template>
  <booking-list :is-self="false"/>
</template>

<script>
import BookingList from './components/BookingList'

export default {
  name: 'EditForm',
  components: { BookingList }
}
</script>