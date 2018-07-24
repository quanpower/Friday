import React, { Component, Fragment } from 'react';
import { connect } from 'dva';
import {
  Row,
  Col,
  Icon,
  Card,
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
import {BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';
import ReactEcharts from 'echarts-for-react';

import styles from './Analysis.less';

const { TabPane } = Tabs;
const { RangePicker } = DatePicker;

const rankingListData = [];
for (let i = 0; i < 10; i += 1) {
  rankingListData.push({
    title: `${i} 通道`,
    total: 323234,
  });
}

const Yuan = ({ children }) => (
  <span dangerouslySetInnerHTML={{ __html: yuan(children) }} /> /* eslint-disable-line react/no-danger */
);




@connect(({ survey, loading }) => ({
  survey,
  loading: loading.effects['survey/fetchDeviceDaqRealtime'],
}))

export default class Analysis extends Component {
  state = {
    salesType: 'all',
    currentTabKey: '',
    rangePickerValue: getTimeDistance('year'),
  };

  componentDidMount() {
    // this.props.dispatch({
    //   type: 'survey/fetchCurrentPowerData',
    //   payload: {
    //     device_id: '20180704',
    //   },
    // });
    console.log('this.props')
    console.log(this.props);
    const device_id = this.props.match.params.device_id;

    console.log(device_id);

    this.props.dispatch({
      type: 'survey/fetchDeviceDaqRealtime',
      payload: {
        device_id: device_id,
      },
    });

    this.props.dispatch({
      type: 'survey/fetchDeviceDaqHistory',
      payload: {
        device_id: device_id,
      },
    });

    this.timer = setInterval(() => {

      this.props.dispatch({
        type: 'survey/fetchDeviceDaqRealtime',
        payload: {
          device_id: device_id,
        },
      });

      this.props.dispatch({
        type: 'survey/fetchDeviceDaqHistory',
        payload: {
          device_id: device_id,
        },
      });

    }, 10000);

    console.log('component did mount!')
  }

  componentWillUnmount() {
    const { dispatch } = this.props;
    dispatch({
      type: 'survey/clear',
    });
  }

  handleChangeSalesType = e => {
    this.setState({
      salesType: e.target.value,
    });
  };

  handleTabChange = key => {
    this.setState({
      currentTabKey: key,
    });
  };


  handleRangePickerChange = rangePickerValue => {
    this.setState({
      rangePickerValue,
    });

    this.props.dispatch({
      type: 'survey/fetchDeviceDaqHistory',
    });
  };

  selectDate = type => {
    this.setState({
      rangePickerValue: getTimeDistance(type),
    });

    this.props.dispatch({
      type: 'survey/fetchDeviceDaqHistory',
    });
  };

  isActive(type) {
    const { rangePickerValue } = this.state;
    const value = getTimeDistance(type);
    if (!rangePickerValue[0] || !rangePickerValue[1]) {
      return;
    }
    if (
      rangePickerValue[0].isSame(value[0], 'day') &&
      rangePickerValue[1].isSame(value[1], 'day')
    ) {
      return styles.currentDate;
    }
  }

  render() {
    const { rangePickerValue, salesType, currentTabKey } = this.state;
    const { survey, loading } = this.props;
    console.log('--survey,loading--')
    console.log(survey)
    console.log(loading)
    const {currentPower, deviceDaqRealtime, realtimeBars, deviceDaqHistory, historyLines } = survey;


    const salesExtra = (
      <div className={styles.salesExtraWrap}>
        <div className={styles.salesExtra}>
          <a className={this.isActive('today')} onClick={() => this.selectDate('today')}>
            今日
          </a>
          <a className={this.isActive('week')} onClick={() => this.selectDate('week')}>
            本周
          </a>
          <a className={this.isActive('month')} onClick={() => this.selectDate('month')}>
            本月
          </a>
          <a className={this.isActive('year')} onClick={() => this.selectDate('year')}>
            全年
          </a>
        </div>
        <RangePicker
          value={rangePickerValue}
          onChange={this.handleRangePickerChange}
          style={{ width: 256 }}
        />
      </div>
    );


    const topColResponsiveProps = {
      xs: 24,
      sm: 12,
      md: 12,
      lg: 12,
      xl: 6,
      style: { marginBottom: 24 },
    };



    return (
      <Fragment>
        <Row gutter={24}>
          {console.log('currentPower:', currentPower)}

          {currentPower.map((item, i) => (
            <Col {...topColResponsiveProps}>
              <ChartCard
                bordered={item.bordered}
                title={item.title}
                action={
                  <Tooltip title={item.tooltip_title}>
                    <Icon type="info-circle-o" />
                  </Tooltip>
                }
                total={item.voltage}
                footer={<Field label={item.footer_label} value={item.footer_value} />}
                contentHeight={item.contentHeight}
              >
                <MiniArea color={item.mini_area_color} data={item.mini_area_data} />
              </ChartCard>
            </Col>
            )
          )}
        </Row>


        <Card loading={loading} bordered={false} bodyStyle={{ padding: 0 }}>
          <div className={styles.salesCard}>
            <Tabs tabBarExtraContent={salesExtra} size="large" tabBarStyle={{ marginBottom: 24 }}>
              <TabPane tab="实时温度" key="sales">
                <Row>
                  <Col xl={16} lg={12} md={12} sm={24} xs={24}>
                    <div className={styles.salesBar}>
                          {console.log('deviceDaqRealtime:', deviceDaqRealtime)}
                          {console.log('realtimeBars:', realtimeBars)}

                          <BarChart width={600} height={300} data={deviceDaqRealtime}
                                margin={{top: 5, right: 30, left: 20, bottom: 5}}>
                           <CartesianGrid strokeDasharray="3 3"/>
                           <XAxis dataKey="name"/>
                           <YAxis/>
                           <Tooltip/>
                           <Legend />

                          {realtimeBars.map((item, i) => (
                            <Bar dataKey={item.dataKey} fill={item.fill} />
                          ))}

                          </BarChart>
                    </div>
                  </Col>
                  <Col xl={8} lg={12} md={12} sm={24} xs={24}>
                    <div className={styles.salesRank}>
                      <h4 className={styles.rankingTitle}>实时温度</h4>
                      <ul className={styles.rankingList}>
                        {rankingListData.map((item, i) => (
                          <li key={item.title}>
                            <span className={i < 3 ? styles.active : ''}>{i + 1}</span>
                            <span>{item.title}</span>
                            <span>{numeral(item.total).format('0,0')}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </Col>
                </Row>
              </TabPane>

              <TabPane tab="历史温度" key="views">
                <Row>
                  <Col xl={16} lg={12} md={12} sm={24} xs={24}>
                    <div className={styles.salesBar}>
                      <LineChart width={600} height={300} data={deviceDaqHistory}
                              margin={{top: 5, right: 30, left: 20, bottom: 5}}>
                         <XAxis dataKey="time"/>
                         <YAxis/>
                         <CartesianGrid strokeDasharray="3 3"/>
                         <Tooltip/>
                         <Legend />

                          {historyLines.map((item, i) => (
                            <Line type={item.type} dataKey={item.dataKey} stroke={item.stroke} />
                          ))}

                      </LineChart>
                    </div>
                  </Col>
                  <Col xl={8} lg={12} md={12} sm={24} xs={24}>
                    <div className={styles.salesRank}>
                      <h4 className={styles.rankingTitle}>历史温度</h4>
                      <ul className={styles.rankingList}>
                        {rankingListData.map((item, i) => (
                          <li key={item.title}>
                            <span className={i < 3 ? styles.active : ''}>{i + 1}</span>
                            <span>{item.title}</span>
                            <span>{numeral(item.total).format('0,0')}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </Col>
                </Row>
              </TabPane>

            </Tabs>
          </div>
        </Card>

      </Fragment>
    );
  }
}
