import React, { Component, Fragment } from 'react';
import { connect } from 'dva';

import {
  Row,
  Col,
  Icon,
  Card,
  Tooltip,
  Tabs,
  Table,
  Radio,
  DatePicker,
  Menu,
  Dropdown,
} from 'antd';

import numeral from 'numeral';

import {
  ChartCard,
  yuan,
  MiniArea,
  MiniBar,
  MiniProgress,
  Field,
  Pie,
  TimelineChart,
} from 'components/Charts';

import Trend from 'components/Trend';

import NumberInfo from 'components/NumberInfo';

import { getTimeDistance } from '../../utils/utils';
// import ReactEcharts from 'echarts-for-react';
import {Map, Marker, NavigationControl, InfoWindow} from 'react-bmap'
import styles from './Dashboard.less';


@connect(({ survey, loading }) => ({
  survey,
  loading: loading.effects['survey/fetchDeviceDaqRealtime'],
}))

export default class Dashboard extends Component {

  componentDidMount() {
    // this.props.dispatch({
    //   type: 'survey/fetchCurrentPowerData',
    //   payload: {
    //     device_id: '20180704',
    //   },
    // });
    console.log('this.props')
   

    console.log('component did mount!')
  }

  componentWillUnmount() {
    console.log('component did unmount!')
  }


  render() {
    const { survey, loading } = this.props;
    console.log('--survey,loading--')
    console.log(survey)
    console.log(loading)
    const {currentPower, deviceDaqRealtime, realtimeBars, deviceDaqHistory, historyLines } = survey;



    const devicesPieData = [
      {
        x: '北京',
        y: 1,
      },
      {
        x: '上海',
        y: 3,
      },
      {
        x: '深圳',
        y: 2,
      },
      {
        x: '杭州',
        y: 5,
      },
      
    ];


    return (
      <Fragment>
        <Row gutter={24}>

          <Col span={6} style={{ marginTop: 24 }}>
            <ChartCard
              title="产品总数"
              avatar={
                <img
                  style={{ width: 56, height: 56 }}
                  src="https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png"
                  alt="indicator"
                />
              }
              action={
                <Tooltip title="指标说明">
                  <Icon type="info-circle-o" />
                </Tooltip>
              }
              total={() => (
                <span dangerouslySetInnerHTML={{ __html: 8 }} />
              )}
              footer={
                <Field label="日均增长" value={numeral(0.1).format("0,0")} />
              }
              contentHeight={46}
            >
                <span>
                  周同比
                  <Trend flag="up" style={{ marginLeft: 8, color: "rgba(0,0,0,.85)" }}>
                    12%
                  </Trend>
                </span>
                <span style={{ marginLeft: 16 }}>
                  日环比
                  <Trend
                    flag="down"
                    style={{ marginLeft: 8, color: "rgba(0,0,0,.85)" }}
                  >
                    11%
                  </Trend>
                </span>
            </ChartCard>

          </Col>

                    <Col span={6} style={{ marginTop: 24 }}>
            <ChartCard
              title="设备总数"
              avatar={
                <img
                  style={{ width: 56, height: 56 }}
                  src="https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png"
                  alt="indicator"
                />
              }
              action={
                <Tooltip title="指标说明">
                  <Icon type="info-circle-o" />
                </Tooltip>
              }
              total={() => (
                <span dangerouslySetInnerHTML={{ __html: 8 }} />
              )}
              footer={
                <Field label="日均增长" value={numeral(3).format("0,0")} />
              }
              contentHeight={46}
            >
                <span>
                  周同比
                  <Trend flag="up" style={{ marginLeft: 8, color: "rgba(0,0,0,.85)" }}>
                    12%
                  </Trend>
                </span>
                <span style={{ marginLeft: 16 }}>
                  日环比
                  <Trend
                    flag="down"
                    style={{ marginLeft: 8, color: "rgba(0,0,0,.85)" }}
                  >
                    11%
                  </Trend>
                </span>
            </ChartCard>

          </Col>
          <Col span={6} style={{ marginTop: 24 }}>
            <ChartCard
              title="激活设备"
              avatar={
                <img
                  alt="indicator"
                  style={{ width: 56, height: 56 }}
                  src="https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png"
                />
              }
              action={
                <Tooltip title="指标说明">
                  <Icon type="info-circle-o" />
                </Tooltip>
              }
              total={() => (
                <span dangerouslySetInnerHTML={{ __html: 5 }} />
              )}
              footer={
                <Field label="日均增长" value={numeral(1).format("0,0")} />
              }
              contentHeight={46}
            >
              <span>
                  周同比
                  <Trend flag="up" style={{ marginLeft: 8, color: "rgba(0,0,0,.85)" }}>
                    26%
                  </Trend>
                </span>
                <span style={{ marginLeft: 16 }}>
                  日环比
                  <Trend
                    flag="down"
                    style={{ marginLeft: 8, color: "rgba(0,0,0,.85)" }}
                  >
                    43%
                  </Trend>
                </span>
            </ChartCard>
          </Col>
          <Col span={6} style={{ marginTop: 24 }}>
            <ChartCard
              title="当前在线"
              avatar={
                <img
                  alt="indicator"
                  style={{ width: 56, height: 56 }}
                  src="https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png"
                />
              }
              action={
                <Tooltip title="指标说明">
                  <Icon type="info-circle-o" />
                </Tooltip>
              }
              total={() => (
                <span dangerouslySetInnerHTML={{ __html: 3 }} />
              )}
              footer={
                <Field label="日均增长" value={numeral(1).format("0,0")} />
              }
              contentHeight={46}

            >
                <span>
                  周同比
                  <Trend flag="up" style={{ marginLeft: 8, color: "rgba(0,0,0,.85)" }}>
                    28%
                  </Trend>
                </span>
                <span style={{ marginLeft: 16 }}>
                  日环比
                  <Trend
                    flag="down"
                    style={{ marginLeft: 8, color: "rgba(0,0,0,.85)" }}
                  >
                    23%
                  </Trend>
                </span>
                </ChartCard>

          </Col>


        </Row>

        <Row gutter={24}>

        <Col span={18} style={{ marginTop: 24 }}>
        <Card loading={loading} bordered={false} bodyStyle={{ padding: 0 }}>
          <Map center={{lng: 115.8947652959, lat: 30.6284584424}} zoom="5">
              <Marker position={{lng: 121.2437339458, lat: 31.3436707857}} icon="loc_blue" />
              <Marker position={{lng: 120.0989329766, lat: 30.3365149757}} icon="simple_red" />
              <NavigationControl /> 
              <InfoWindow position={{lng: 121.2437339458, lat: 31.3436707857}} text="设备数:3" title="设备数:1"/>
              <InfoWindow position={{lng: 120.0989329766, lat: 30.3365149757}} text="设备数:5" title="在线数:2"/>
          </Map>
        </Card>

        </Col>

        <Col span={6} style={{ marginTop: 24 }}>

            <Pie
              title="设备分布"
              subTitle="设备分布"
              hasLegend
              total={() => (
                <span
                  dangerouslySetInnerHTML={{
                    __html: devicesPieData.reduce((pre, now) => now.y + pre, 0)
                  }}
                />
              )}
              data={devicesPieData}
              height={100}
            />,

          </Col>


        </Row>
      </Fragment>
    );
  }
}
