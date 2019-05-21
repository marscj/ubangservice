<template>
  <booking-list :is-self="true"/>
</template>

<script>
import BookingList from './components/BookingList'

export default {
  name: 'EditForm',
  components: { BookingList }
}
</script>

