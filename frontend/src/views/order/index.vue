<template>
  <order-list :is-self="false"/>
</template>

<script>
import OrderList from './components/OrderList'

export default {
  name: 'EditForm',
  components: { OrderList }
}
</script>