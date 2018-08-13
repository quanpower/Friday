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
import { getTimeDistance } from '../../../utils/utils';
import {BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';
// import ReactEcharts from 'echarts-for-react';

import styles from './Display.less';


const Yuan = ({ children }) => (
  <span dangerouslySetInnerHTML={{ __html: yuan(children) }} /> /* eslint-disable-line react/no-danger */
);


@connect(({ survey, loading }) => ({
  survey,
  loading: loading.effects['survey/fetchDeviceDaqHistory'],
}))

export default class Analysis extends Component {

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
      type: 'survey/fetchDeviceDaqHistory',
      payload: {
        device_id: device_id,
      },
    });

    this.timer = setInterval(() => {

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


  render() {
    const { survey, loading } = this.props;
    console.log('--survey,loading--')
    console.log(survey)
    console.log(loading)
    const {currentPower, deviceDaqRealtime, deviceDaqDigital, realtimeBars, deviceDaqHistory, historyLines } = survey;


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

        <Card loading={loading} bordered={false} bodyStyle={{ padding: 0 }}>
          <div className={styles.salesCard}>

            <Row>
              <Col xl={24} lg={12} md={12} sm={24} xs={24}>
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

            </Row>
          </div>
        </Card>

      </Fragment>
    );
  }
}
