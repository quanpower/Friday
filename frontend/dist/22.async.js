(window['webpackJsonp'] = window['webpackJsonp'] || []).push([
  [22],
  {
    DJVG: function(e, t, a) {
      'use strict';
      var l = a('TqRt'),
        n = a('284h');
      Object.defineProperty(t, '__esModule', { value: !0 }), (t.default = void 0), a('Mwp2');
      var d = l(a('VXEj'));
      a('IzEo');
      var r = l(a('bx4M'));
      a('Telt');
      var u = l(a('Tckk'));
      a('qVdP');
      var f = l(a('jsC+'));
      a('5Dmo');
      var c = l(a('3S7+'));
      a('Pwec');
      var i = l(a('CtXQ'));
      a('lUTK');
      var o,
        m,
        s = l(a('BvKs')),
        p = l(a('lwsE')),
        v = l(a('W8MJ')),
        E = l(a('a1gu')),
        w = l(a('Nsbk')),
        h = l(a('7W2i')),
        g = n(a('q1tI')),
        y = (l(a('ZhIB')), a('MuoO')),
        I = l(a('hhRw')),
        b = ((o = (0, y.connect)(function(e) {
          var t = e.devices,
            a = e.loading;
          return { devices: t, loading: a.models.devices };
        })),
        o(
          (m = (function(e) {
            function t() {
              return (
                (0, p.default)(this, t),
                (0, E.default)(this, (0, w.default)(t).apply(this, arguments))
              );
            }
            return (
              (0, h.default)(t, e),
              (0, v.default)(t, [
                {
                  key: 'componentDidMount',
                  value: function() {
                    this.props.dispatch({ type: 'devices/fetchDevices' });
                  },
                },
                {
                  key: 'render',
                  value: function() {
                    var e = this.props,
                      t = e.devices.devices,
                      a = e.loading,
                      l = (e.form,
                      function(e) {
                        var t = e.status,
                          a = e.updateAt;
                        return g.default.createElement(
                          'div',
                          { className: I.default.cardInfo },
                          g.default.createElement(
                            'div',
                            null,
                            g.default.createElement('p', null, '\u5f53\u524d\u72b6\u6001'),
                            g.default.createElement('p', null, t)
                          ),
                          g.default.createElement(
                            'div',
                            null,
                            g.default.createElement('p', null, '\u66f4\u65b0\u65f6\u95f4'),
                            g.default.createElement('p', null, a)
                          )
                        );
                      }),
                      n = g.default.createElement(
                        s.default,
                        null,
                        g.default.createElement(
                          s.default.Item,
                          null,
                          g.default.createElement(
                            'a',
                            {
                              target: '_blank',
                              rel: 'noopener noreferrer',
                              href: 'http://www.alipay.com/',
                            },
                            '1st menu item'
                          )
                        ),
                        g.default.createElement(
                          s.default.Item,
                          null,
                          g.default.createElement(
                            'a',
                            {
                              target: '_blank',
                              rel: 'noopener noreferrer',
                              href: 'http://www.taobao.com/',
                            },
                            '2nd menu item'
                          )
                        ),
                        g.default.createElement(
                          s.default.Item,
                          null,
                          g.default.createElement(
                            'a',
                            {
                              target: '_blank',
                              rel: 'noopener noreferrer',
                              href: 'http://www.tmall.com/',
                            },
                            '3d menu item'
                          )
                        )
                      );
                    return g.default.createElement(
                      'div',
                      { className: I.default.filterCardList },
                      g.default.createElement(d.default, {
                        rowKey: 'id',
                        style: { marginTop: 24 },
                        grid: { gutter: 24, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 },
                        loading: a,
                        dataSource: t,
                        renderItem: function(e) {
                          return g.default.createElement(
                            d.default.Item,
                            { key: e.id },
                            g.default.createElement(
                              r.default,
                              {
                                hoverable: !0,
                                bodyStyle: { paddingBottom: 20 },
                                actions: [
                                  g.default.createElement(
                                    c.default,
                                    { title: '\u4e0b\u8f7d' },
                                    g.default.createElement(i.default, { type: 'download' })
                                  ),
                                  g.default.createElement(
                                    c.default,
                                    { title: '\u7f16\u8f91' },
                                    g.default.createElement(i.default, { type: 'edit' })
                                  ),
                                  g.default.createElement(
                                    c.default,
                                    { title: '\u5206\u4eab' },
                                    g.default.createElement(i.default, { type: 'share-alt' })
                                  ),
                                  g.default.createElement(
                                    f.default,
                                    { overlay: n },
                                    g.default.createElement(i.default, { type: 'ellipsis' })
                                  ),
                                ],
                              },
                              g.default.createElement(r.default.Meta, {
                                avatar: g.default.createElement(u.default, {
                                  size: 'small',
                                  src: e.avatar,
                                }),
                                title: e.name,
                              }),
                              g.default.createElement(
                                'div',
                                { className: I.default.cardItemContent },
                                g.default.createElement(l, {
                                  status: e.status,
                                  updateAt: e.gmt_online,
                                })
                              )
                            )
                          );
                        },
                      })
                    );
                  },
                },
              ]),
              t
            );
          })(g.PureComponent))
        ) || m);
      t.default = b;
    },
    hhRw: function(e, t, a) {
      e.exports = {
        filterCardList: 'antd-pro-pages-device-device-list-filterCardList',
        cardInfo: 'antd-pro-pages-device-device-list-cardInfo',
        wan: 'antd-pro-pages-device-device-list-wan',
      };
    },
  },
]);
