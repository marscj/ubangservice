<template >
  <div class="dashboard-container">
      <panel-group/>
      <el-row :gutter="8">
        <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:30px;">
          <company-panel />
        </el-col> 
        <el-col :xs="{span: 24}" :sm="{span: 24}" :md="{span: 24}" :lg="{span: 18}" :xl="{span: 18}" style="padding-right:12px;margin-bottom:30px;">
          <booking-list />
        </el-col>
        <!-- <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:30px;">
          <todo-list />
        </el-col>-->
      </el-row>
    </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import BookingList from './components/BookingList'
import CompanyPanel from './components/CompanyPanel'

export default {
  name: 'Dashboard',
  components: {
    PanelGroup, BookingList, CompanyPanel
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
