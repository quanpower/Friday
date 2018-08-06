import React, { Component } from 'react';
import { connect } from 'dva';
import { Card, Badge, Table, List, Divider } from 'antd';
import DescriptionList from 'components/DescriptionList';
import PageHeaderLayout from '../../layouts/PageHeaderLayout';
import styles from './DeviceProfile.less';

const { Description } = DescriptionList;


@connect(({ devices, loading }) => ({
  devices,
  loading: loading.effects['devices/fetchDeviceProfile'],
}))

export default class DeviceProfile extends Component {
  componentDidMount() {
    const { dispatch } = this.props;
    dispatch({
      type: 'devices/fetchDeviceProfile',
      payload: {
          device_id: 1,
        },
    });

    this.timer = setInterval(() => {
    dispatch({
      type: 'devices/fetchDeviceProfile',
      payload: {
          device_id: 1,
        },
    });

    }, 10000);

  }

  render() {
    const { deviceProfile, loading } = this.props.devices;
    console.log(deviceProfile)
    return (
      <PageHeaderLayout title="设备详情页">

        <List
          rowKey="id"
          style={{ marginTop: 24 }}
          grid={{ gutter: 24, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 }}
          loading={loading}
          dataSource={deviceProfile}
          renderItem={item => (
            <List.Item key={item.id}>
              <Card bordered={false}>
                <DescriptionList size="large" title="基本信息" style={{ marginBottom: 32 }}>
                  <Description term="设备名称">{item.name}</Description>
                  <Description term="所属用户">{item.owner}</Description>
                  <Description term="device_name">{item.device_name}</Description>
                  <Description term="device_secret">{item.device_secret}</Description>
                  <Description term="firmware_version">{item.firmware_version}</Description>
                </DescriptionList>
                <Divider style={{ marginBottom: 32 }} />
                <DescriptionList size="large" title="状态信息" style={{ marginBottom: 32 }}>
                  <Description term="设备类型">{item.node_type}</Description>
                  <Description term="IP地址">{item.ip_address}</Description>
                  <Description term="当前状态">{item.status}</Description>
                  <Description term="创建时间">{item.gmt_create}</Description>
                  <Description term="激活时间">{item.gmt_active}</Description>
                  <Description term="最后在线">{item.gmt_online}</Description>
                  <Description term="备注">无</Description>
                </DescriptionList>
                <Divider style={{ marginBottom: 32 }} />
                
              </Card>

            </List.Item>
          )}
        />

      </PageHeaderLayout>
    );
  }
}
