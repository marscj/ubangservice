<template >
  <div v-if="showCompany"  class="dashboard-container">
    <el-row :gutter="8">
      <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 10}" :lg="{span: 4}" :xl="{span: 4}" style="margin-bottom:30px; padding-top:10px">
        <company-panel />
      </el-col> 
      <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 14}" :lg="{span: 20}" :xl="{span: 20}" style="margin-bottom:30px;">
        <tab-view />
      </el-col>
    </el-row>
  </div>
  <div v-else style="padding: 10px 10px 10px 10px">
    <h1>
      You are not a company user
    </h1>
  </div>
</template>

<script>
import CompanyPanel from './components/CompanyPanel'
import TabView from './components/TabView'

export default {
  name: 'Dashboard',
  components: {
    CompanyPanel, TabView
  },
  data() {
    return {
      showCompany: this.$store.getters.user.company != null
    }
  },
}
</script>

<style lang="scss">
.dashboard-container {
  min-height: 100vh;
  // height: 100vh;
  width: 100%;
  padding: 16px;
  background-color: rgb(240, 242, 245);
  position: relative;
}
</style>
