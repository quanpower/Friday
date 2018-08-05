import { stringify } from 'qs';
import request from '../utils/request';

export async function queryProjectNotice() {
  return request('/api/project/notice');
}

export async function queryActivities() {
  return request('/api/activities');
}

export async function queryRule(params) {
  return request(`/api/rule?${stringify(params)}`);
}

export async function removeRule(params) {
  return request('/api/rule', {
    method: 'POST',
    body: {
      ...params,
      method: 'delete',
    },
  });
}

export async function addRule(params) {
  return request('/api/rule', {
    method: 'POST',
    body: {
      ...params,
      method: 'post',
    },
  });
}

export async function fakeSubmitForm(params) {
  return request('/api/forms', {
    method: 'POST',
    body: params,
  });
}

export async function fakeChartData() {
  return request('/api/fake_chart_data');
}

export async function queryTags() {
  return request('/api/tags');
}

export async function queryBasicProfile() {
  return request('/api/profile/basic');
}

export async function queryAdvancedProfile() {
  return request('/api/profile/advanced');
}

export async function queryFakeList(params) {
  return request(`/api/fake_list?${stringify(params)}`);
}

export async function fakeAccountLogin(params) {
  return request('/api/login/account', {
    method: 'POST',
    body: params,
  });
}

export async function fakeRegister(params) {
  return request('/api/register', {
    method: 'POST',
    body: params,
  });
}

export async function queryNotices() {
  return request('/api/notices');
}


export async function queryDeviceDaqRealtime(params) {
  return request(`/api/device/daq/realtime?${stringify(params)}`);
}

export async function queryDeviceDaqAlarm(params) {
  return request(`/api/device/daq/alarm?${stringify(params)}`);
}

export async function queryDeviceDaqHistory(params) {
  return request(`/api/device/daq/history?${stringify(params)}`);
}

export async function queryDeviceDaqRecord(params) {
  return request(`/api/device/daq/record?${stringify(params)}`);
}


export async function queryProductProfile(params) {
  return request(`/api/product/profile?${stringify(params)}`);
}


export async function queryDeviceProfile(params) {
  return request(`/api/device/profile?${stringify(params)}`);
}


export async function queryProjects() {
  return request('/api/projects');
}

export async function queryProducts() {
  return request('/api/products');
}

export async function queryDevices() {
  return request('/api/devices');
}
