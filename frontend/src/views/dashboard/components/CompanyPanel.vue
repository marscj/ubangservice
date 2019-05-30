<template>
  <el-card class="box-card-component">
    <div slot="header" class="box-card-header">
      <img src="https://wpimg.wallstcn.com/e7d23d71-cf19-4b90-a1cc-f56af8c0903d.png">
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
        <span v-if="company.discount" >{{ company.discount.name }}</span>
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
  data() {
    return {
      company: this.$store.state.user.user.company
    }
  },
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
