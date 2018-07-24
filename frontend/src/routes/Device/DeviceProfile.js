import React, { Component } from 'react';
import { connect } from 'dva';
import { Card, Badge, Table, Divider } from 'antd';
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
  }

  render() {
    const { deviceProfile, loading } = this.props;
    console.log(deviceProfile)
    const profile = deviceProfile[0]
    return (
      <PageHeaderLayout title="设备详情页">
        <Card bordered={false}>
          <DescriptionList size="large" title="基本信息" style={{ marginBottom: 32 }}>
            <Description term="设备名称">{profile.name}</Description>
            <Description term="所属用户">{profile.owner}</Description>
            <Description term="device_name">{profile.device_name}</Description>
            <Description term="device_secret">{profile.device_secret}</Description>
            <Description term="firmware_version">{profile.firmware_version}</Description>
          </DescriptionList>
          <Divider style={{ marginBottom: 32 }} />
          <DescriptionList size="large" title="状态信息" style={{ marginBottom: 32 }}>
            <Description term="设备类型">{profile.node_type}</Description>
            <Description term="IP地址">{profile.ip_address}</Description>
            <Description term="当前状态">{profile.status}</Description>
            <Description term="创建时间">{profile.gmt_create}</Description>
            <Description term="激活时间">{profile.gmt_active}</Description>
            <Description term="最后在线">{profile.gmt_online}</Description>
            <Description term="备注">无</Description>
          </DescriptionList>
          <Divider style={{ marginBottom: 32 }} />
          
        </Card>
      </PageHeaderLayout>
    );
  }
}
