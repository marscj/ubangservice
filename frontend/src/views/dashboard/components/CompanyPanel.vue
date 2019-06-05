<template>
  <el-card class="box-card-component">
    <div slot="header" class="box-card-header">
      <img src="http://www.luxos.com/cn/media/k2/items/cache/5d9bd784bfd234610bf8ba15e7ad6a4e_XL.jpg">
    </div>
    <div style="position:relative;">
      <div style="padding-top:5px;" class="progress-item">
        <span style="font-size:18px;">{{ company.name }}</span>
      </div>
      <div style="padding-top:15px;" class="progress-item">
        <span>Phone:</span> 
        <span>{{ company.phone }}</span> 
      </div>
      <div style="padding-top:15px;" class="progress-item">
        <span>Tel:</span> 
        <span>{{ company.tel }}</span> 
      </div>
      <div style="padding-top:15px;" class="progress-item">
        <span>Email:</span> 
        <span>{{ company.email }}</span> 
      </div>
      <div style="padding-top:15px;" class="progress-item">
        <span>Address:</span> 
        <span>{{ company.address }}</span> 
      </div>
      <div style="padding-top:15px;" class="progress-item">
        <span>Discount:</span> 
        <span v-if="company.discount" >{{ discount }}</span>
        <span v-else>None</span>
      </div>
    </div>
  </el-card>
</template>

<script>

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        success: 'success',
        pending: 'danger'
      }
      return statusMap[status]
    }
  },
  computed: {
    discount: {
      get() {
        if(this.company && this.company.discount) {
          return this.company.discount * 100 + '% for free'
        }
      }
    }
  },
  data() {
    return {
      company: this.$store.getters.user.company
    }
  }
}
</script>

<style lang="scss" >
.box-card-component{
  .el-card__header {
    padding: 0px!important;
  }
}
</style>
<style lang="scss" scoped>
.box-card-component {
  .box-card-header {
    position: relative;
    height: 220px;
    img {
      width: 100%;
      height: 100%;
      transition: all 0.2s linear;
      &:hover {
        transform: scale(1.1, 1.1);
        filter: contrast(130%);
      }
    }
  }
  .progress-item {
    margin-bottom: 10px;
    font-size: 14px;
  }
  @media only screen and (max-width: 1510px){
    .mallki-text{
      display: none;
    }
  }
}
</style>
