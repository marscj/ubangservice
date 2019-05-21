<template>
  <order-list :is-self="true"/>
</template>

<script>
import OrderList from './components/OrderList'

export default {
  name: 'EditForm',
  components: { OrderList }
}
</script>