<template >
  <div class="dashboard-container">
      <el-row :gutter="8">
        <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 10}" :lg="{span: 5}" :xl="{span: 5}" style="margin-bottom:30px; padding-top:10px">
          <company-panel />
        </el-col> 
        <el-col :xs="{span: 24}" :sm="{span: 24}" :md="{span: 24}" :lg="{span: 19}" :xl="{span: 19}" style="margin-bottom:30px;">
          <tab-view />
        </el-col>
      </el-row>
    </div>
</template>

<script>
import CompanyPanel from './components/CompanyPanel'
import TabView from './components/TabView'

export default {
  name: 'Dashboard',
  components: {
    CompanyPanel, TabView
  }
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
