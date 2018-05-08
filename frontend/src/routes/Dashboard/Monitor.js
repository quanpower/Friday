import React, { PureComponent, Fragment } from 'react';
import { connect } from 'dva';
import { Row, Col, Card } from 'antd';
import numeral from 'numeral';
import { Pie, WaterWave, Gauge, TagCloud } from 'components/Charts';
import NumberInfo from 'components/NumberInfo';
import CountDown from 'components/CountDown';
import ActiveChart from 'components/ActiveChart';
import Authorized from '../../utils/Authorized';

import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';


import styles from './Monitor.less';

const { Secured } = Authorized;

const targetTime = new Date().getTime() + 3900000;

// use permission as a parameter
const havePermissionAsync = new Promise(resolve => {
  // Call resolve on behalf of passed
  setTimeout(() => resolve(), 1000);
});

@Secured(havePermissionAsync)

@connect(({ survey, loading }) => ({
  survey,
  loading: loading.models.survey,
}))

export default class Monitor extends PureComponent {
  componentDidMount() {
    this.props.dispatch({
      type: 'survey/fetchTemperatureHistory',
    });
  }

  render() {
    const { survey, loading } = this.props;
    const { data1 } = survey;

    const data = [
              {name: 'Page A', uv: 4000, pv: 2400, amt: 2400},
              {name: 'Page B', uv: 3000, pv: 1398, amt: 2210},
              {name: 'Page C', uv: 2000, pv: 9800, amt: 2290},
              {name: 'Page D', uv: 2780, pv: 3908, amt: 2000},
              {name: 'Page E', uv: 1890, pv: 4800, amt: 2181},
              {name: 'Page F', uv: 2390, pv: 3800, amt: 2500},
              {name: 'Page G', uv: 3490, pv: 4300, amt: 2100},
        ];

    return (
      <Fragment>
        <Row gutter={24}>
          <Col xl={18} lg={24} md={24} sm={24} xs={24} style={{ marginBottom: 24 }}>
            <Card title="活动实时交易情况" bordered={false}>
              <Row>
                <Col md={6} sm={12} xs={24}>
                  <NumberInfo
                    subTitle="今日交易总额"
                    suffix="元"
                    total={numeral(124543233).format('0,0')}
                  />
                </Col>
                <Col md={6} sm={12} xs={24}>
                  <NumberInfo subTitle="销售目标完成率" total="92%" />
                </Col>
                <Col md={6} sm={12} xs={24}>
                  <NumberInfo subTitle="活动剩余时间" total={<CountDown target={targetTime} />} />
                </Col>
                <Col md={6} sm={12} xs={24}>
                  <NumberInfo
                    subTitle="每秒交易总额"
                    suffix="元"
                    total={numeral(234).format('0,0')}
                  />
                </Col>
              </Row>
              <div className={styles.mapChart}>


                <LineChart width={600} height={300} data={data}
                        margin={{top: 5, right: 30, left: 20, bottom: 5}}>
                       <XAxis dataKey="name"/>
                       <YAxis/>
                       <CartesianGrid strokeDasharray="3 3"/>
                       <Tooltip/>
                       <Legend />
                       <Line type="monotone" dataKey="pv" stroke="#8884d8" activeDot={{r: 8}}/>
                       <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
                </LineChart>


              </div>
            </Card>
          </Col>
          <Col xl={6} lg={24} md={24} sm={24} xs={24}>
            <Card title="活动情况预测" style={{ marginBottom: 24 }} bordered={false}>
            
            </Card>
            <Card
              title="券核效率"
              style={{ marginBottom: 24 }}
              bodyStyle={{ textAlign: 'center' }}
              bordered={false}
            >
              <Gauge title="跳出率" height={180} percent={87} />
            </Card>
          </Col>
        </Row>

      </Fragment>
    );
  }
}
