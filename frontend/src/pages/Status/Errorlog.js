import React, { Fragment } from 'react';
import { formatMessage, FormattedMessage } from 'umi/locale';
import { Button, Row, Col, Icon, Steps, Card } from 'antd';
import PageHeaderWrapper from '@/components/PageHeaderWrapper';

export default () => (
  <PageHeaderWrapper>
    <iframe
      style={{ border: 0, width: '100%', height: 630 }}
      src="http://127.0.0.1:5000/conf2d/errorlog"
    />
  </PageHeaderWrapper>
);
