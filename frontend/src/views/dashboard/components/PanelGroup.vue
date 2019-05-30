<template>
  <el-row :gutter="40" class="panel-group">
    <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <router-link to="/booking/all">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-all">
            <svg-icon icon-class="order" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              All Booking
            </div>
          </div>
        </div>
      </router-link>
    </el-col>
    <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <router-link :to="{ name: 'MonthBooking', query: queryMonth, }">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-month card-panel-icon">
            <i class="el-icon-date"></i>
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              {{ this.$moment().format('MMM') }} Booking
            </div>
          </div>
        </div>
      </router-link>
    </el-col>
    <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <router-link :to="{ name: 'MyBooking', query: queryMy }">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-my">
            <svg-icon icon-class="my-order" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              My Booking
            </div>
          </div>
        </div>
      </router-link>
    </el-col>
    <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
      <router-link to="/booking/create">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-add card-panel-icon">
            <svg-icon icon-class="add" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              Add Booking
            </div>
          </div>
        </div>
      </router-link>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name:'PanelGroup',
  data() {
    return {
      queryMonth: {
        start_time: this.$moment().startOf('month').format(),
        end_time: this.$moment().endOf('month').format()
      },
      queryMy: {
        creator_by: this.$store.state.user.user.id
      },
      monthTitle: 'Booking in ' + this.$moment().format('MMM')
    }
  }
}
</script>

<style lang="scss" scoped>
.panel-group {
  margin-top: 18px;

  .card-panel-col {
    margin-bottom: 32px;
  }

  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .12);
    border-color: rgba(0, 0, 0, .12);

    &:hover {
      .card-panel-icon-wrapper {
        color: #fff;
      }

      .icon-all {
        background: #40c9c6;
      }

      .icon-month {
        background: #36a3f7;
      }

      .icon-my {
        background: #f4516c;
      }

      .icon-add {
        background: #34bfa3
      }
    }

    .icon-all {
      color: #40c9c6;
    }

    .icon-month {
      color: #36a3f7;
    }

    .icon-my {
      color: #f4516c;
    }

    .icon-add {
      color: #34bfa3
    }

    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }

    .card-panel-icon {
      float: left;
      font-size: 48px;
    }

    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 26px;
      margin-left: 0px;

      .card-panel-text {
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 16px;
        margin-bottom: 12px;
      }

      .card-panel-num {
        font-size: 20px;
      }
    }
  }
}

@media (max-width:550px) {
  .card-panel-description {
    display: none;
  }

  .card-panel-icon-wrapper {
    float: none !important;
    width: 100%;
    height: 100%;
    margin: 0 !important;

    .svg-icon {
      display: block;
      margin: 14px auto !important;
      float: none !important;
    }
  }
}
</style>
