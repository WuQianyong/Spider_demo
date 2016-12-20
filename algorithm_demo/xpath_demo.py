#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2016/12/19 10:47
# @Author  : wuqianyong
# @File    : xpath_demo.py
# @Software: PyCharm




from lxml import etree

str = """
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<!--[fe80::71fd:2e0:e9da:c179%13] staticed at 2016-12-19 10:12:05-->
<head><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta http-equiv="Content-Type" content="text/html; charset=gb2312" /><meta name="viewport" content="width=device-width" /><link rel="shortcut icon" type="image/ico" href="http://www.eastmoney.com/favicon.ico" />
    <link href="/css_001/master.css" rel="stylesheet" />
    <link rel="stylesheet" type="text/css" media="all" href="/css_001/default.css?rt=20160616" /><link rel="stylesheet" type="text/css" media="all" href="/css_001/layer2012.css?rt=20120717" />
    <script src="/js_001/ht_web.js"></script>
    <script type="text/javascript" src="http://cmsjs.eastmoney.com/channel/jquery-1.8.3.min.js?rt=20151113"></script>

    <script type="text/javascript">
        var jQuery = $.noConflict();
    </script>
    <script type="text/javascript" src="/js_001/base.js?201606021830"></script>
    <script type="text/javascript" src="/js_001/pluginNoBind.js?201606021830"></script>


    <title>
        万科A(000002)资金流向全览 _ 数据中心 _ 东方财富网</title>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
    <meta name="keywords" content="万科A，000002，资金流向,今日资金流向,实时资金流向,资金流向分析,股票资金流向,资金净流入排名,资金流向排行,主力资金流向,个股资金流向,资金净流入" />
    <meta name="description" content="东方财富网数据中心资金流向一览提供万科A(000002)主力资金流向及时数据、历史数据的流入,流出详细信息" />
    <meta name="robots" content="index, follow" />
    <meta name="googlebot" content="index, follow" />
    <meta http-equiv="refresh" content="1200" />
    <style>
        #flash-cont {
            min-height: 225px;
        }

        #flash-cont-1 {
            min-height: 250px;
        }

        #flash-cont-2 {
            min-height: 210px;
        }

        #flash-cont-3 {
            min-height: 205px;
        }

        .blockColor {
            float: left;
            width: 15px;
            height: 15px;
            margin: 5px 5px;
        }

        .content2 {
            clear: both;
        }
    </style>
    <link rel="stylesheet" href="/css_001/page_common.css?201606021831" type="text/css" />
    <base target="_blank" />
    <script>
        var page_type = "ggzjl"; //左侧导航链接标识
    </script>
<title>

</title></head>
<body>
    <!-- 微信分享img --><img id='weixin-share' src="http://wap.eastmoney.com/weixin-share.png" />
    <div class="adFrame1000">
        <script type="text/javascript">
            if (Math.random() < 0.25)
                document.write('<iframe width="1000" height="60" frameborder="0" scrolling="no" marginwidth="0" marginheight="0" src="http://same.eastmoney.com/s?z=eastmoney&c=1082&op=1"></iframe>');
            else
                document.write('<iframe width="1000" height="60" frameborder="0" scrolling="no" marginwidth="0" marginheight="0" src="http://fund.eastmoney.com/trade/hqb_hq.html?spm=100004.sbb"></iframe>');
        </script>
    </div>

    <div id="page" class="page">
        <div class="header">
            <div class="nav">
                <ul>
                    <li><a href="http://finance.eastmoney.com/">财经</a></li>
                    <li><a href="http://finance.eastmoney.com/yaowen.html">要闻</a></li>
                    <li><a href="http://stock.eastmoney.com/">股票</a></li>
                    <li><span class="red"><a href="http://stock.eastmoney.com/newstock.html">新股</a></span></li>
                    <li><a href="http://stock.eastmoney.com/gzqh.html">期指</a></li>
                    <li><a href="http://option.eastmoney.com/">期权</a></li>
                    <li><span class="red"><a href="http://quote.eastmoney.com/flash/sz300059.html">行情</a></span></li>
                    <li><a href="http://data.eastmoney.com/">数据</a></li>
                    <li><a href="http://stock.eastmoney.com/global.html">全球</a></li>
                    <li><a href="http://stock.eastmoney.com/america.html">美股</a></li>
                    <li><a href="http://hk.eastmoney.com/">港股</a></li>
                    <li><a href="http://futures.eastmoney.com/">期货</a></li>
                    <li><a href="http://forex.eastmoney.com/">外汇</a></li>
                    <li><a href="http://gold.eastmoney.com">黄金</a></li>
                    <li><a href="http://bank.eastmoney.com/">银行</a></li>
                    <li><a href="http://www.1234567.com.cn/">基金</a></li>
                    <li><a href="http://money.eastmoney.com/">理财</a></li>
                    <li><a href="http://insurance.eastmoney.com/">保险</a></li>
                    <li><a href="http://bond.eastmoney.com/">债券</a></li>
                    <li><a href="http://video.eastmoney.com/">视频</a></li>
                    <li><span class="red"><a href="http://guba.eastmoney.com/">股吧</a></span></li>
                    <li><a href="http://fund2.eastmoney.com/">基金吧</a></li>
                    <li><a href="http://blog.eastmoney.com/">博客</a></li>
                    <li><a href="http://so.eastmoney.com/">搜索</a></li>
                </ul>
            </div>
            <div class="advert">
                <script language="javascript" type="text/javascript" src="http://same.eastmoney.com/s?z=eastmoney&c=1312"></script>
            </div>
            <div class="picker">
                <div class="logo_img">
                    <a target="_blank" href="http://www.eastmoney.com">
                        <img src="/images/logo_new.gif" alt="" />
                    </a>
                    <a target="_blank" href="http://data.eastmoney.com/center/">
                        <img src="/images/data_logo.png" alt="" />
                    </a>
                </div>
                <div class="expand">
                    <span><b class="icon globle"></b><a target="_blank" href="http://kuaixun.eastmoney.com/">全球财经快讯</a></span>
                    <span><b class="icon quote"></b><a target="_blank" href="http://quote.eastmoney.com/center/">行情中心</a></span>
                    <span><b class="icon data"></b><a target="_blank" href="http://js5.eastmoney.com/tg.aspx?ID=953">Choice数据</a></span>
                </div>
                <div id="Header_tj_Bull" class="remark">
                    <div class="inp-search">
                        <div class="sim-select clearfix" id="sim-select">
                            <h3 id="h3Name">行情</h3>
                            <div class="define-select" id="define-select" style="display: none;">
                                <ul>
                                    <li class="f"><a>行情</a></li>
                                    <li><a>股吧</a></li>
                                    <li><a>博客</a></li>
                                    <li class="l"><a>资讯</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="inp-txt-wrap">
                            <div class="seach-div">
                                <form id="sofrm" method="post" onsubmit="return checkso(this);">
                                    <div class="sradio" style="display: none;">
                                        <span class="radio">
                                            <input type="radio" checked="" value="stock" id="stypeId" name="stype" onchange="return checkStock(this);" />
                                        </span>
                                    </div>
                                    <input type="text" maxlength="40" class="inp-txt" name="StockCode_bar" id="StockCode_bar" autocomplete="off" />
                                </form>

                                <input type="hidden" value="stock" id="hdRadio" name="hdRadio" />
                            </div>
                        </div>
                        <div onclick="javascript:checkso('sofrm')" class="btnNew">搜索</div>
                    </div>
                </div>
            </div>




           <div class="lableBox">
                <div class="inner"><dl class=""><dt><a href="http://data.eastmoney.com/center/" >特色</a></dt><dd><a href="http://data.eastmoney.com/stock/lhb.html" >龙虎榜单</a><a href="http://data.eastmoney.com/rzrq/sh.html" >融资融券</a><a href="http://data.eastmoney.com/gsrl/default.html" >股市日历</a><a href="http://data.eastmoney.com/dzjy/default.html" >大宗交易</a><a href="http://data.eastmoney.com/jgdy/" >机构调研</a><a href="http://data.eastmoney.com/IF/Data/Contract.html?va=IF" >期指持仓</a><a href="http://data.eastmoney.com/notices/" >公告大全</a><a href="http://data.eastmoney.com/xuangu/" >选股器</a></dd></dl><dl class=""><dt><a href="http://data.eastmoney.com/bbsj/" >财报</a></dt><dd><a href="http://data.eastmoney.com/bbsj/" >业绩报表</a><a href="http://data.eastmoney.com/bbsj/201609/yjyg.html" >最新预告</a><a href="http://data.eastmoney.com/bbsj/201606/xjfh.html" >分红送转</a></dd></dl><dl class=""><dt><a href="http://data.eastmoney.com/report/" >研报</a></dt><dd><a href="http://data.eastmoney.com/report/" >个股研报</a><a href="http://data.eastmoney.com/report/hyyb.html" >行业研报</a><a href="http://data.eastmoney.com/report/ylyc.html" >盈利预测</a></dd></dl><dl class="dlClearfix"><dt><a href="http://data.eastmoney.com/xg/" >新股</a></dt><dd><a href="http://data.eastmoney.com/xg/xg/default.html" >新股申购</a><a href="http://data.eastmoney.com/xg/xg/calendar.html" >新股日历</a><a href="http://data.eastmoney.com/xg/gh/default.html" >新股上会</a></dd></dl><dl class=""><dt><a href="http://data.eastmoney.com/zjlx/" >资金</a></dt><dd><a href="http://data.eastmoney.com/zjlx/dpzjlx.html" >大盘资金</a><a href="http://data.eastmoney.com/zjlx/detail.html" >个股资金</a><a href="http://data.eastmoney.com/bkzj/" >板块资金</a><a href="http://data.eastmoney.com/bkzj/hgt.html" >沪港通</a></dd></dl><dl class=""><dt><a href="http://fund.eastmoney.com/data/" >基金</a></dt><dd><a href="http://fund.eastmoney.com/fund.html" >基金净值</a><a href="http://fund.eastmoney.com/fundguzhi.html" >基金估值</a><a href="http://fund.eastmoney.com/data/fundranking.html" >基金排行</a></dd></dl><dl class=""><dt><a href="http://data.eastmoney.com/cjsj/cpi.html" >经济</a></dt><dd><a href="http://data.eastmoney.com/cjsj/cpi.html" >CPI</a><a href="http://data.eastmoney.com/cjsj/ppi.html" >PPI</a><a href="http://data.eastmoney.com/cjsj/pmi.html" >PMI</a><a href="http://data.eastmoney.com/cjsj/gdp.html" >GDP</a><a href="http://data.eastmoney.com/cjsj/yhll.html" >利率</a><a href="http://data.eastmoney.com/cjsj/newhouse.html" >房价</a></dd></dl></div>
            </div>
            <div class="centerbox">
                <h2><i class="icon2" style="margin-top: 1px; margin-left: 8px;"></i><a target="_blank" href="http://quote.eastmoney.com/center/">行情中心</a></h2>
                <div class="dlable">
                    <a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=654">指数</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=655">期指</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=3646">期权</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=656">个股</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=657">板块</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=658">排行</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=660">新股</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=661">基金</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=663">港股</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=665">美股</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=666">期货</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=667">外汇</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=668">黄金</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=669">自选股</a>|<a target="_blank" href="http://js1.eastmoney.com/tg.aspx?ID=670">自选基金</a>
                </div>

                <div class="search">
                    <input type="text" value="输代码、名称或拼音缩写" name="StockCode" id="StockCode" class="text" autocomplete="off" />
                    <a class="btn" href="javascript:;" onclick="toQuote();return false;">查行情</a><a class="btn" href="javascript:;" onclick="qphf.toGuBa()()">进股吧</a><a class="btn" href="javascript:;" onclick="qphf.toNews()">搜资讯</a>
                </div>
            </div>
        </div>
        <div class="main">
            <div class="vnav">
                <div class="navtop">
                </div>
                <div class="navbody">
                    <div class="qjbox">
                        <span>
                            <h2>
                                <a id="alllink">数据全景图</a><img src="/images/sjqjt.gif" class="sjqjt_img" />
                            </h2>
                        </span>
                        <div class="navview">
                            <div class="nbox"><dl class="first"><dt><a href="http://data.eastmoney.com/stock/lhb.html">特色数据</a></dt><dd><span class="left_nav_span red"><a href="http://data.eastmoney.com/stock/lhb.html">龙虎榜单</a></span><a href="http://data.eastmoney.com/rzrq/sh.html">融资融券</a><a href="http://data.eastmoney.com/stockcomment/">千股千评</a><a href="http://data.eastmoney.com/tfpxx/">停复牌信息</a><a href="http://data.eastmoney.com/xuangu/">选股器</a><a href="http://data.eastmoney.com/dzjy/default.html">大宗交易</a><a href="http://data.eastmoney.com/notices/">公告大全</a><span class="left_nav_span red"><a href="http://data.eastmoney.com/jgdy/">机构调研</a></span><a href="http://data.eastmoney.com/cjrl/default.html">财经日历</a><a href="http://data.eastmoney.com/gsrl/default.html">股市日历</a><a href="http://data.eastmoney.com/IF/Data/Contract.html?va=IF">股指期货持仓</a><a href="http://data.eastmoney.com/invest/invest/default.html">分析师指数</a><span class="left_nav_span red"><a href="http://data.eastmoney.com/executive/gdzjc.html">股东增减持</a></span><a href="http://data.eastmoney.com/executive/">高管持股</a><a href="http://data.eastmoney.com/dxf/default.html">限售解禁</a><a href="http://data.eastmoney.com/cmjzd/">股东人数</a><a href="http://data.eastmoney.com/zlsj/">主力数据</a><a href="http://data.eastmoney.com/Contract/Data/Contracttf.html?va=T">国债期货持仓</a><a href="http://quote.eastmoney.com/center/list.html#absh_0_4">AB股比价</a><a href="http://quote.eastmoney.com/center/list.html#ah_1">AH股比价</a><a href="http://data.eastmoney.com/cjsj/bankTransfer.html">交易结算资金</a><a href="http://data.eastmoney.com/cjsj/yzgptjnew.html">股票账户</a><a href="http://data.eastmoney.com/cjsj/gpjytj.html">股票统计</a><span class="left_nav_span red"><a href="http://data.eastmoney.com/other/qsjy.html">券商业绩月报</a></span></dd></dl><dl><dt><a href="http://data.eastmoney.com/zjlx/">资金流向</a></dt><dd><a href="http://data.eastmoney.com/zjlx/dpzjlx.html">大盘资金流</a><span class="left_nav_span red"><a href="http://data.eastmoney.com/zjlx/detail.html">个股资金流</a></span><a href="http://data.eastmoney.com/zjlx/list.html">主力排名</a><a href="http://data.eastmoney.com/bkzj/">板块资金</a><a href="http://data.eastmoney.com/bkzj/hy.html">行业资金流</a><a href="http://data.eastmoney.com/bkzj/gn.html">概念资金流</a><a href="http://data.eastmoney.com/bkzj/dy.html">地域资金流</a><a href="http://data.eastmoney.com/bkzj/jlr.html">资金流检测</a><span class="left_nav_span red"><a href="http://data.eastmoney.com/hsgt/index.html">沪深港通资金</a></span><a href="http://data.eastmoney.com/hsgt/top10.html">沪深港通成交榜</a></dd></dl><dl><dt><a href="http://data.eastmoney.com/xg/">新股数据</a></dt><dd><span class="left_nav_span red"><a href="http://data.eastmoney.com/xg/xg/default.html">新股申购</a></span><a href="http://data.eastmoney.com/xg/xg/calendar.html">新股日历</a><span class="left_nav_span red"><a href="http://data.eastmoney.com/xg/gh/default.html">新股上会</a></span><a href="http://data.eastmoney.com/xg/xg/sbqy.html">首发申报信息</a><a href="http://data.eastmoney.com/xg/xg/chart/zql.html">新股解析</a><a href="http://data.eastmoney.com/other/gkzf.html">增发</a><a href="http://data.eastmoney.com/zrz/pg.html">配股</a><a href="http://data.eastmoney.com/kzz/default.html">可转债</a></dd></dl><dl><dt><a href="http://data.eastmoney.com/report/">研究报告</a></dt><dd><span class="left_nav_span red"><a href="http://data.eastmoney.com/report/">个股研报</a></span><a href="http://data.eastmoney.com/report/xg.html">新股研报</a><a href="http://data.eastmoney.com/report/ylyc.html">盈利预测</a><a href="http://data.eastmoney.com/report/hyyb.html">行业研报</a><a href="http://data.eastmoney.com/report/clbg.html">策略报告</a><a href="http://data.eastmoney.com/report/qsch.html">券商晨会</a><a href="http://data.eastmoney.com/report/hgyj.html">宏观研究</a></dd></dl><dl><dt><a href="http://data.eastmoney.com/bbsj/">年报季报</a></dt><dd><span class="left_nav_span red"><a href="http://data.eastmoney.com/bbsj/201609/yjbb.html">2016三季报</a></span><a href="http://data.eastmoney.com/bbsj/">2016中报</a><a href="http://data.eastmoney.com/bbsj/201603.html">2016一季报</a><a href="http://data.eastmoney.com/bbsj/201512/yjbb.html">2015年报</a><a href="http://data.eastmoney.com/bbsj/201509/yjbb.html">2015三季报</a><span class="left_nav_span red"><a href="http://data.eastmoney.com/yjfp/">分红送配</a></span></dd></dl><dl><dt><a href="http://data.eastmoney.com/futures/sh/data.html">期货期权</a></dt><dd><a href="http://data.eastmoney.com/futures/sh/data.html">期货龙虎榜</a><a href="http://data.eastmoney.com/ifdata/kcsj.html">期货库存</a><a href="http://data.eastmoney.com/pmetal/comex/by.html">COMEX库存</a><a href="http://data.eastmoney.com/pmetal/cftc/baiyin.html">CFTC持仓</a><a href="http://data.eastmoney.com/pmetal/etf/by.html">ETF持仓</a><a href="http://data.eastmoney.com/ifdata/xhgp.html">现货与股票</a><a href="http://data.eastmoney.com/ifdata/qxhbj.html">期现货比价表</a><a href="http://data.eastmoney.com/ifdata/jcjz.html">期货价差矩阵</a><a href="http://data.eastmoney.com/tf/tf.html">可交割国债</a><a href="http://data.eastmoney.com/other/qqlhb.html">期权龙虎榜单</a><a href="http://data.eastmoney.com/other/valueAnal.html">期权价值分析</a><a href="http://data.eastmoney.com/other/riskanal.html">期权风险分析</a><a href="http://data.eastmoney.com/other/premium.html">期权折溢价</a></dd></dl><dl><dt><a href="http://data.eastmoney.com/cjsj/cpi.html">经济数据</a></dt><dd><a href="http://data.eastmoney.com/cjsj/cpi.html">CPI</a><a href="http://data.eastmoney.com/cjsj/ppi.html">PPI</a><a href="http://data.eastmoney.com/cjsj/pmi.html">PMI</a><a href="http://data.eastmoney.com/cjsj/gdp.html">GDP</a><a href="http://data.eastmoney.com/cjsj/yhll.html">中国基准利率</a><a href="http://data.eastmoney.com/cjsj/xzxd.html">新增贷款</a><a href="http://data.eastmoney.com/cjsj/ckzbj.html">存款准备金率</a><a href="http://data.eastmoney.com/cjsj/hbgyl.html">货币供应量</a><a href="http://data.eastmoney.com/cjsj/newhouse.html">房价指数</a><a href="http://data.eastmoney.com/cjsj/foreign_0_0.html">美国经济数据</a><a href="http://data.eastmoney.com/cjsj/foreign_1_0.html">德国经济数据</a><a href="http://data.eastmoney.com/cjsj/foreign_3_0.html">日本经济数据</a><a href="http://data.eastmoney.com/cjsj/foreign_4_0.html">英国经济数据</a><a href="http://data.eastmoney.com/cjsj/foreign_5_0.html">澳大利亚数据</a><a href="http://data.eastmoney.com/cjsj/foreign_7_0.html">加拿大数据</a><a href="http://data.eastmoney.com/cjsj/foreign_6_0.html">欧元区数据</a><a href="http://data.eastmoney.com/cjsj/foreign_8_0.html">香港经济数据</a><span class="left_nav_span red"><a href="http://data.eastmoney.com/cjsj/globalRate.html">全球利率</a></span></dd></dl><dl><dt><a href="http://fund.eastmoney.com/data/">基金数据</a></dt><dd><span class="left_nav_span red"><a href="http://fund.eastmoney.com/data/fundranking.html">基金排行</a></span><a href="http://fund.eastmoney.com/fundguzhi.html">净值估算</a><a href="http://fund.eastmoney.com/fund.html">基金数据</a><a href="http://fund.eastmoney.com/data/fundrating.html">基金评级</a><a href="http://fund.eastmoney.com/fbsjj_dwjz.html">封基折价</a><a href="http://fund.eastmoney.com/data/xinfund.html">新发基金</a><a href="http://fund.eastmoney.com/dingtou/syph_yndt.html">基金定投</a><a href="http://fund.eastmoney.com/data/funddaogou.html">基金导购</a><a href="http://fund.eastmoney.com/data/fundfenhong.html">基金分红</a><a href="http://fund.eastmoney.com/company/default.html">基金公司</a><a href="http://simu.eastmoney.com/data/smranklist.aspx">私募基金</a></dd></dl><dl><dt><a href="http://data.eastmoney.com/money/financial.html">理财数据</a></dt><dd><a href="http://data.eastmoney.com/money/financial.html">人民币理财</a><a href="http://data.eastmoney.com/money/FinancialProducts.aspx?area=&amp;cid=-1&amp;cname=&amp;cuir=2&amp;bt=-1&amp;sale=1&amp;tp=-1&amp;ss=1:false&amp;p=1&amp;ps=25">外币理财产品</a><a href="http://trust.eastmoney.com/product_list.aspx?type=new">集合信托产品</a><a href="http://data.eastmoney.com/money/insurance.html">保险产品库</a><a href="http://data.eastmoney.com/money/cdkll.html">银行存贷款利率</a></dd></dl></div>
                            <div class="nimg">
                                <div class="tcsj"><h3>推荐数据</h3><a href="http://data.eastmoney.com/stock/lhb.html" >龙虎榜单</a><p>剖析机构席位数据，一览主力操作！</p><a href="http://data.eastmoney.com/executive/gdzjc.html" >股东增减持</a><p>紧盯国家队的最新动向！</p><a href="http://data.eastmoney.com/bkzj/hgt.html" >沪港通资金流</a><p>实时跟踪外资操作的痕迹。</p><a href="http://data.eastmoney.com/cjsj/bankTransfer.html" >银证转账</a><p>真实的资金流入流出数据。</p><a href="http://data.eastmoney.com/xg/xg/default.html" >新股申购</a><p>独家数学模型，预测新股发行价。</p></div>
                                <div class="tcad">
                                    <p><a href="http://js5.eastmoney.com/tg.aspx?ID=953" target="_blank">数据支持：东方财富Choice数据>></a></p>
                                    <p>
                                        <a href="http://js5.eastmoney.com/tg.aspx?ID=2712" target="_blank">
                                            <img width="215" height="170" border="0" alt="" src="/images/choice.png" /></a>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <ul class="top_ul">
                        <li class="top_li"><h4><a class="top_a" target="_self" href="/center/" data-page="sjzxsy">首页</a></h4></li><li class="top_li cos"><h4><a class="top_a" target="_self" href="http://data.eastmoney.com/zjlx/" data-page="zjlx">资金流向</a></h4><ul class="mid_ul"><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/zjlx/dpzjlx.html" data-page="dpzjl">大盘资金流</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/zjlx/detail.html" data-page="ggzjl">个股资金流</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/zjlx/list.html" data-page="zlpm">主力排名</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/bkzj/" data-page="bkzj">板块资金</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/bkzj/hy.html" data-page="hyzjl">行业资金流</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/bkzj/gn.html" data-page="gnzjl">概念资金流</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/bkzj/dy.html" data-page="dyzjl">地域资金流</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/bkzj/jlr.html" data-page="zjljc">资金流监测</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/hsgt/index.html" data-page="hsgt">沪深港通资金流</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/hsgt/top10.html" data-page="sdcjg">沪深港通成交榜</a></li></ul></li><li class="top_li cos"><h4><a class="top_a" target="_self" href="http://data.eastmoney.com/stock/lhb.html" data-page="tssj">特色数据</a></h4><ul class="mid_ul"><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/stock/lhb.html" data-page="lhbd">龙虎榜单</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/rzrq/sh.html" data-page="rzrq">融资融券</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/stockcomment/" data-page="qgqp">千股千评</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/tfpxx/" data-page="tfp">停复牌信息</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/xuangu/" data-page="xgq">选股器</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/dzjy/default.html" data-page="dzjy">大宗交易</a></li><li class="mid_li cos"><h5><a class="mid_a" target="_self" href="http://data.eastmoney.com/notices/" data-page="ggdq">公告大全</a></h5><ul class="sub_ul"><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/hsa.html" data-page="ggdq_hsa">沪深A股公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/sha.html" data-page="ggdq_sha">沪市A股公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/sza.html" data-page="ggdq_sza">深主板A股公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/zxb.html" data-page="ggdq_zxb">中小板公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/cyb.html" data-page="ggdq_cyb">创业板公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/shb.html" data-page="ggdq_shb">沪市B股公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/szb.html" data-page="ggdq_szb">深市B股公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/dss.html" data-page="ggdq_dss">待上市A股公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/sb.html" data-page="ggdq_sb">三板公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/gg.html" data-page="ggdq_gg">港股公告</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/notices/mg.html" data-page="ggdq_mg">美股公告</a></li></ul></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/yjfp/" data-page="yjfp">分红送配</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/jgdy/" data-page="jgdy">机构调研</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/cjrl/default.html" data-page="cjrl">财经日历</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/gsrl/default.html" data-page="gsrl">股市日历</a></li><li class="mid_li cos"><h5><a class="mid_a" target="_self" href="http://data.eastmoney.com/IF/Data/Contract.html?va=IF" data-page="if">股指期货持仓</a></h5><ul class="sub_ul"><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/IF/Data/Contract.html?va=IF" data-page="if_IF">沪深300期指</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/IF/Data/Contract.html?va=IC" data-page="if_IC">中证500期指</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/IF/Data/Contract.html?va=IH" data-page="if_IH">上证50期指</a></li></ul></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/invest/invest/default.html" data-page="fxs">分析师指数</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/executive/gdzjc.html" data-page="gdzjc">股东增减持</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/executive/" data-page="ggcg">高管持股</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/dxf/default.html" data-page="xsjj">限售解禁</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/cmjzd/" data-page="gdrs">股东人数</a></li><li class="mid_li cos"><h5><a class="mid_a" target="_self" href="http://data.eastmoney.com/zlsj/" data-page="zlsj">主力数据</a></h5><ul class="sub_ul"><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/zlsj/jj.html" data-page="zlsj_1">基金持仓</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/zlsj/qfii.html" data-page="zlsj_2">QFII持仓</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/zlsj/sb.html" data-page="zlsj_3">社保持仓</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/zlsj/qs.html" data-page="zlsj_4">券商持仓</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/zlsj/bx.html" data-page="zlsj_5">保险持仓</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/zlsj/xt.html" data-page="zlsj_6">信托持仓</a></li></ul></li><li class="mid_li cos"><h5><a class="mid_a" target="_self" href="http://data.eastmoney.com/Contract/Data/Contracttf.html?va=T" data-page="contract">国债期货持仓</a></h5><ul class="sub_ul"><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/Contract/Data/Contracttf.html?va=T" data-page="contract_T">10年期国债</a></li><li class="sub_li"><a class="sub_a" target="_self" href="http://data.eastmoney.com/Contract/Data/Contracttf.html?va=TF" data-page="contract_TF">5年期国债</a></li></ul></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://quote.eastmoney.com/center/list.html#absh_0_4" data-page="abg">AB股比价</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://quote.eastmoney.com/center/list.html#ah_1" data-page="ahg">AH股比价</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/bankTransfer.html" data-page="jszj">交易结算资金</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/yzgptjnew.html" data-page="gpzh">股票账户</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/gpjytj.html" data-page="gptj">股票统计</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/other/qsjy.html" data-page="qsyj">券商业绩月报</a></li></ul></li><li class="top_li cos"><h4><a class="top_a" target="_blank" href="http://data.eastmoney.com/xg/" data-page="xgsj">新股数据</a></h4><ul class="mid_ul"><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/xg/xg/default.html" data-page="xgsg">新股申购</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/xg/xg/calendar.html" data-page="xgrl">新股日历</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/xg/gh/default.html" data-page="xgsh">新股上会</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/xg/xg/sbqy.html" data-page="sfsb">首发申报信息</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/xg/xg/chart/zql.html" data-page="xgjx">新股解析</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/other/gkzf.html" data-page="gkzf">增发</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/zrz/pg.html" data-page="pg">配股</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/kzz/default.html" data-page="kzz">可转债</a></li></ul></li><li class="top_li cos"><h4><a class="top_a" target="_blank" href="http://data.eastmoney.com/report/" data-page="yjbg">研究报告</a></h4><ul class="mid_ul"><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/report/" data-page="ggyb">个股研报</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/report/hyyb.html" data-page="hyyb">行业研报</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/report/ylyc.html" data-page="ylyc">盈利预测</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/report/clbg.html" data-page="clbg">策略报告</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/report/qsch.html" data-page="qsch">券商晨会</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/report/hgyj.html" data-page="hgyj">宏观研究</a></li></ul></li><li class="top_li cos"><h4><a class="top_a" target="_blank" href="http://data.eastmoney.com/bbsj/" data-page="nbjb">年报季报</a></h4><ul class="mid_ul"><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/yjfp/" data-page="yjfp">分红送配</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/bbsj/201612/yjyg.html" data-page="2016nbyg">2016年报预告</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/bbsj/201609/yjbb.html" data-page="2016sjb">2016三季报</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/bbsj/201606/yjbb.html" data-page="2015nbyjyg">2016中报</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/bbsj/201603/yjbb.html" data-page="2015nbyjyg">2016一季报</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/bbsj/201512/yjbb.html" data-page="2015sjbzxyj">2015年报</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/bbsj/201509/yjbb.html" data-page="2015sjb">2015三季报</a></li></ul></li><li class="top_li cos"><h4><a class="top_a" target="_self" href="http://data.eastmoney.com/futures/sh/data.html" data-page="qhqq">期货期权</a></h4><ul class="mid_ul"><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/futures/sh/data.html" data-page="qhlhb">期货龙虎榜</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/ifdata/kcsj.html" data-page="qhkc">期货库存</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/pmetal/comex/by.html" data-page="comexkc">COMEX库存</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/pmetal/cftc/baiyin.html" data-page="cftccc">CFTC持仓</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/pmetal/etf/by.html" data-page="etfcc">ETF持仓</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/ifdata/xhgp.html" data-page="xhygp">现货与股票</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/ifdata/qxhbj.html" data-page="qxhbjb">期现货比价表</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/ifdata/jcjz.html" data-page="qhjcjz">期货价差矩阵</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/tf/tf.html" data-page="kjggz">可交割国债</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/other/qqlhb.html" data-page="qqlhbd">期权龙虎榜单</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/other/valueAnal.html" data-page="qqjzfx">期权价值分析</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/other/riskanal.html" data-page="qqfxfx">期权风险分析</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/other/premium.html" data-page="qqzyj">期权折溢价</a></li></ul></li><li class="top_li cos"><h4><a class="top_a" target="_blank" href="http://data.eastmoney.com/cjsj/cpi.html" data-page="jjsj">经济数据</a></h4><ul class="mid_ul"><li class="mid_li cos"><h5><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/cpi.html" data-page="zgjjsj">中国经济数据</a></h5><ul class="sub_ul"><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/cpi.html" data-page="cpi">CPI</a></li><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/ppi.html" data-page="ppi">PPI</a></li><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/pmi.html" data-page="pmi">PMI</a></li><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/ckzbj.html" data-page="gdp">GDP</a></li><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/yhll.html" data-page="ll">利率调整</a></li><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/xzxd.html" data-page="xzdk">新增贷款</a></li><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/gdp.html" data-page="ckzbjl">存款准备金率</a></li><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/hbgyl.html" data-page="hbgyl">货币供应量</a></li><li class="sub_li"><a class="sub_a" target="_blank" href="http://data.eastmoney.com/cjsj/newhouse.html" data-page="fjzs">房价指数</a></li></ul></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_0_0.html" data-page="mgjjsj">美国经济数据</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_1_0.html" data-page="dgjjsj">德国经济数据</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_2_0.html" data-page="rsjjsj">瑞士经济数据</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_3_0.html" data-page="rbjjsj">日本经济数据</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_4_0.html" data-page="ygjjsj">英国经济数据</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_5_0.html" data-page="adlyjjsj">澳大利亚经济数据</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_7_0.html" data-page="jndjjsj">加拿大经济数据</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_6_0.html" data-page="oyqjjsj">欧元区经济数据</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/cjsj/foreign_8_0.html" data-page="xgjjsj">香港经济数据</a></li><li class="mid_li"><a class="mid_a" target="_self" href="http://data.eastmoney.com/cjsj/globalRate.html" data-page="qqzygjll">全球主要国家利率</a></li></ul></li><li class="top_li cos"><h4><a class="top_a" target="_blank" href="http://fund.eastmoney.com/data/" data-page="jjsj">基金数据</a></h4><ul class="mid_ul"><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/data/fundranking.html" data-page="jjph">基金排行</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/fundguzhi.html" data-page="jzgs">净值估算</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/data/fundrating.html" data-page="jjpj">基金评级</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/fbsjj_dwjz.html" data-page="fjzs">封基折价</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/data/xinfund.html" data-page="xfjj">新发基金</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/dingtou/syph_yndt.html" data-page="jjdt">基金定投</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/data/funddaogou.html" data-page="jjdg">基金导购</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/data/fundfenhong.html" data-page="jjfh">基金分红</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://fund.eastmoney.com/company/default.html" data-page="jjgs">基金公司</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://simu.eastmoney.com/data/smranklist.aspx" data-page="smjj">私募基金</a></li></ul></li><li class="top_li cos"><h4><a class="top_a" target="_blank" href="http://trust.eastmoney.com/product_list.aspx?type=new" data-page="lcsj">理财数据</a></h4><ul class="mid_ul"><li class="mid_li"><a class="mid_a" target="_blank" href="http://trust.eastmoney.com/product_list.aspx?type=new" data-page="xtcp">集合信托产品</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/money/insurance.html" data-page="bxcp">保险产品库</a></li><li class="mid_li"><a class="mid_a" target="_blank" href="http://data.eastmoney.com/money/cdkll.html" data-page="yhcdkll">银行存贷款利率</a></li></ul></li>
                    </ul>
                    <script src="/js_001/public_common_tools.js" type="text/javascript"></script>
                    <script>
                        setMenuStatus();//初始化左侧菜单
                    </script>

                </div>
            </div>
            <div class="framecontent">
                <div class="linkNav">

    <div id="Column_Navigation">
        <a href="http://www.eastmoney.com/">东方财富网</a> &gt; <a href="http://data.eastmoney.com/">数据中心</a> &gt; <a href="http://data.eastmoney.com/zjlx/">资金流向</a> &gt;
                万科A(000002)资金流向
    </div>
    <div class="ad_link"><a class="ad_link1" href="http://fundact.eastmoney.com/information/2015002_JYN/?spm=100004002.mw">买不到牛股？立即查看哪些板块正被机构盯上</a><a class="ad_link2" href="http://stattg.eastmoney.com/10149?spm=100004002.mw">10000亿资金正在建仓股票(名单)&gt;&gt;</a></div>

                </div>
                <div class="sitebody">

    <div class="maincont">
        <div class="contentBox">
            <div class="titbar">
                <b class="el"></b>
                <div class="tit">
                    <a href="http://quote.eastmoney.com/sz000002.html">
                        万科A(000002)</a>资金流向
                </div>

                <div class="search" style="float: left; padding-left: 30px;">
                    <span class="txt">个股资金流向：</span>
                    <input class="sinput" name="zjlx_bar" id="zjlx_bar" type="text">
                    <div  id="search1" class="btn" style="border: none;">
                        <img src="../images/btn_search_blue.gif" title="查询" />
                    </div>
                </div>

                <div class="help_advice" style="padding-top: 3px;">
                    [<a href="http://stock.eastmoney.com/news/1423,20110101117172217.html">帮助说明</a>]
                </div>

                <div class="tips" style="float: left; padding-left: 20px;">
                    <b class="arr_01"></b><a href="http://data.eastmoney.com/zjlx/detail.html" class="link1"
                        title="实时资金净流入排行榜">查看资金流向排名</a> <a href="http://data.eastmoney.com/zjlx/list.html"
                            class="link2" title="实时大单净流入排行榜">主力流入排名</a>
                </div>

                <script type="text/javascript">
                    var zz = new StockSuggest("zjlx_bar", {
                        text: "输代码、名称或拼音",
                        type: "ABSTOCK",
                        autoSubmit: false,
                        width: 200,
                        header: ["选项", "代码", "名称", "类型"],
                        body: [-1, 1, 4, -2],
                        callback: function (ag) {
                            var url = '/zjlx/' + ag.code + '.html';
                            window.open(url);
                        }
                    });
                    window.onload = function () {
                        zz.BindSearchClick("search1");
                    };
                    //function ggzl_search(bb) {
                    //    var s1 = document.getElementById(bb).value;
                    //    var s = escape(s1);
                    //    if (s1 == "输代码、名称或拼音" || s1 == "" || isNaN(parseInt(s1)) || s1.length != 6) {
                    //        alert("请输入所查询股票的代码！");
                    //        return false;
                    //    } else {
                    //        var url = '/zjlx/' + s1 + '.html';
                    //        window.open(url);
                    //    }
                    //}
                </script>
            </div>
            <div class="sepe">
                <div class="left">
                </div>
                <div class="right">
                </div>
            </div>
        </div>
        <div class="contentBox" style="border-top: 0; margin-top: -10px;">
            <div class="content2" id="zjlx_hqcont">
            </div>
        </div>

        <div class="s6">
        </div>
        <div class="c1">
            <div class="contentBox content1 zjlx">
                <div class="titbar shortbar">
                    <div class="tit">
                        实时资金流向图
                    </div>
                    <div class="right-tips">
                        更新时间 <span id="updateTime_0"></span>
                    </div>
                    <div class="right-tips" style="padding-right: 20px;">
                    </div>
                </div>
                <div class="content2">
                    <div>
                        <div class="flash-dw">
                            单位（万元）
                        </div>
                        <div class="jsline-cont" id="flash-cont">
                        </div>
                        <div class="flash-data-cont flash-data-cont-line">
                            <ul style="margin-left: 10px;">
                                <li class="data-type" style="width: 150px;"><span class="blockColor" style="background-color: #FE3EE1;"></span>今日主力净流入：</li>
                                <li class="data-val" style="width: 120px;"><span id="data_jlr" class=""></span>万元</li>
                                <li class="data-val">主力净比：<span id="data_jzb" class=""></span></li>
                            </ul>
                            <ul style="margin-left: 10px;">
                                <li class="data-type" style="width: 150px;"><span class="blockColor" style="background-color: #650000;"></span>今日超大单净流入：</li>
                                <li class="data-val" style="width: 120px;"><span id="data_superjlr" class=""></span>万元</li>
                                <li class="data-val">超大单净比：<span id="data_superjzb" class=""></span></li>
                            </ul>
                            <ul style="margin-left: 10px;">
                                <li class="data-type" style="width: 150px;"><span class="blockColor" style="background-color: #FF1117;"></span>今日大单净流入：</li>
                                <li class="data-val" style="width: 120px;"><span id="data_ddjlr" class=""></span>万元</li>
                                <li class="data-val">大单净比：<span id="data_ddjzb" class=""></span></li>
                            </ul>
                            <ul style="margin-left: 10px;">
                                <li class="data-type" style="width: 150px;"><span class="blockColor" style="background-color: #FFB83D;"></span>今日中单净流入：</li>
                                <li class="data-val" style="width: 120px;"><span id="data_zdjlr" class=""></span>万元</li>
                                <li class="data-val">中单净比：<span id="data_zdjzb" class=""></span></li>
                            </ul>
                            <ul style="margin-left: 10px;">
                                <li class="data-type" style="width: 150px;"><span class="blockColor" style="background-color: #94C4EE;"></span>今日小单净流入：</li>
                                <li class="data-val" style="width: 120px;"><span id="data_xdjlr" class=""></span>万元</li>
                                <li class="data-val">小单净比：<span id="data_xdjzb" class=""></span></li>
                            </ul>
                        </div>
                        <script type="text/javascript">
                            var swf_line = "http://g1.dfcfw.com/g1/201012/20101214085507.swf";
                            var swf_pie = "http://g1.dfcfw.com/g1/201104/20110412125826.swf";
                            var swf_column = "http://g1.dfcfw.com/g1/201104/20110412130313.swf";
                            var data_baseurl = "http://hqcdn.quote.eastmoney.com/";
                            var time_stamp = Math.floor((new Date().getTime()) / 60000);
                        </script>
                    </div>
                </div>
            </div>
            <div class="s6">
            </div>
            <div class="contentBox content1 second_zjlx">
                <div class="titbar shortbar">
                    <div class="tit">
                        盘后资金流向趋势
                    </div>
                    <div class="right-tips">
                        更新时间 <span id="updateTime_2"></span>&nbsp;16:05
                    </div>
                </div>
                <div class="content2">
                    <div class="flash-dw">
                        单位（万元）
                    </div>
                    <div class="jsline-cont" id="flash-cont-2">
                    </div>
                    <div class="flash-data-cont">
                        <ul style="margin-left: 10px;">
                            <li class="data-type" style="width: 120px;"><span class="blockColor" style="background-color: #FE3EE1;"></span>主力净流入</li>
                            <li class="data-type" style="width: 120px;"><span class="blockColor" style="background-color: #650000;"></span>超大单净流入</li>
                            <li class="data-type" style="width: 120px;"><span class="blockColor" style="background-color: #FF1117;"></span>大单净流入</li>
                        </ul>
                        <ul style="margin-left: 10px;">
                            <li class="data-type" style="width: 120px;"><span class="blockColor" style="background-color: #FFB83D;"></span>中单净流入</li>
                            <li class="data-type" style="width: 120px;"><span class="blockColor" style="background-color: #94C4EE;"></span>小单净流入</li>
                        </ul>
                    </div>
                    <script type="text/javascript">

                    </script>
                </div>
            </div>
        </div>
        <div class="c2">
            <div class="contentBox content1 zjlx">
                <div class="titbar shortbar">
                    <div class="tit">
                        实时成交分布图
                    </div>
                    <div class="right-tips" style="float: right;">
                        更新时间 <span id="updateTime_1"></span>
                    </div>
                </div>
                <div class="content2">
                    <div id="flash-cont-1" class="flash-cont">
                    </div>
                    <script type="text/javascript">

                    </script>
                    <div class="flash-legendrt" style="height: 120px;">
                        <table cellspacing="0" cellpadding="0">
                            <tr>
                                <th width="20%">类型
                                </th>
                                <th>流入
                                </th>
                                <th>流出
                                </th>
                            </tr>
                            <tr>
                                <td>超大单
                                </td>
                                <td>
                                    <span id="data_superlr" class="red"></span>万元
                                </td>
                                <td>
                                    <span id="data_superlc" class="green"></span>万元
                                </td>
                            </tr>
                            <tr>
                                <td>大单
                                </td>
                                <td>
                                    <span id="data_ddlr" class="red"></span>万元
                                </td>
                                <td>
                                    <span id="data_ddlc" class="green"></span>万元
                                </td>
                            </tr>
                            <tr>
                                <td>中单
                                </td>
                                <td>
                                    <span id="data_zdlr" class="red"></span>万元
                                </td>
                                <td>
                                    <span id="data_zdlc" class="green"></span>万元
                                </td>
                            </tr>
                            <tr>
                                <td>小单
                                </td>
                                <td>
                                    <span id="data_xdlr" class="red"></span>万元
                                </td>
                                <td>
                                    <span id="data_xdlc" class="green"></span>万元
                                </td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
            <div class="s6">
            </div>
            <div class="contentBox content1 second_zjlx">
                <div class="titbar shortbar">
                    <div class="tit">
                        盘后资金流向统计
                    </div>
                    <div class="right-tips">
                        更新时间 <span id="updateTime_3"></span>&nbsp;16:05
                    </div>
                </div>
                <div class="content2">
                    <div class="flash-dw" style="position: relative">
                        单位（万元）
                            <div style="position: absolute; top: 108px; left: 65px; border-top: dashed 1px #666; width: 368px">
                            </div>
                    </div>
                    <div id="flash-cont-3" class="flash-cont">
                    </div>
                    <script type='text/javascript'>
                        var so4 = new SWFObject(swf_column, 'so4', '430', '205', '8', '');
                        so4.addVariable("path", "/");
                        so4.addVariable('settings_file', encodeURIComponent('../settings/zjlx_column_plus.xml'));
                        so4.addVariable('data_file', encodeURIComponent("http://data.eastmoney.com/zjlx/graph/tj_000002.html?rt=" + time_stamp));
                        so4.write('flash-cont-3');
                    </script>
                    <div style="text-align: center; height: 25px; margin: 10px 0;">
                        <div>
                            <div style="margin-bottom: 10px;">
                                <span style="height: 15px; width: 15px; background-color: #FE3EE1;">&nbsp;&nbsp;</span>&nbsp;主力净流入
                                <span style="height: 15px; width: 15px; margin-left: 10px; background-color: #650000;">&nbsp;&nbsp;</span>&nbsp;超大单净流入
                                <span style="height: 15px; width: 15px; margin-left: 10px; background-color: #FF1117;">&nbsp;&nbsp;</span>&nbsp;大单净流入
                            </div>
                            <div>
                                <span style="height: 15px; width: 15px; background-color: #FFB83D;">&nbsp;&nbsp;</span>&nbsp;中单净流入
                                <span style="height: 15px; width: 15px; margin-left: 10px; background-color: #94C4EE;">&nbsp;&nbsp;</span>&nbsp;小单净流入
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="s6">
        </div>
        <div class="contentBox">
            <div class="titbar shortbar">
                <div class="tit">
                    万科A(000002)历史资金流向一览
                </div>

                <div class="tips" style="float: left; margin-left: 50px;">
                    <b class="arr_01"></b><a href="http://data.eastmoney.com/stockcomment/000002.html"
                        class="link1" title="点击查看万科A(000002)的控盘程度">点击查看该股控盘程度</a>
                    <a href="http://data.eastmoney.com/report/000002.html" class="link2"
                        title="点击查看万科A(000002)的最新研究报告">最新研报</a> <a href="http://data.eastmoney.com/stockcomment/000002.html"
                            class="link2" title="点击查看万科A(000002)的千股千评">千股千评</a>
                    <a href="http://data.eastmoney.com/stock/lhb,2016-12-19,000002.html"
                        class="link2" title="点击查看万科A(000002)的龙虎榜单">龙虎榜单</a>
                    <a href="http://data.eastmoney.com/bbsj/000002.html" class="link2"
                        title="点击查看万科A(000002)的最新业绩">最新业绩</a> <a href="http://data.eastmoney.com/dxf/q/000002.html"
                            class="link2" title="点击查看万科A(000002)的解禁情况一览">解禁一览</a>
                </div>
            </div>
            <div class="content2" id="content_zjlxtable">
                <table cellpadding="0" cellspacing="0" class="tab1" id="dt_1">
                    <thead class="h101">
                        <tr>
                            <th rowspan="2">日期
                            </th>
                            <th rowspan="2">收盘价
                            </th>
                            <th rowspan="2">涨跌幅
                            </th>
                            <th colspan="2">主力净流入
                            </th>
                            <th colspan="2">超大单净流入<i title="因为存在一笔大额的委托单仅成交小部分的情况，所以会导致超大单或者大单流入/流出的数额极小。">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</i>
                            </th>
                            <th colspan="2">大单净流入
                            </th>
                            <th colspan="2">中单净流入
                            </th>
                            <th colspan="2">小单净流入
                            </th>
                        </tr>
                        <tr>
                            <th>净额
                            </th>
                            <th>净占比
                            </th>
                            <th>净额
                            </th>
                            <th>净占比
                            </th>
                            <th>净额
                            </th>
                            <th>净占比
                            </th>
                            <th>净额
                            </th>
                            <th>净占比
                            </th>
                            <th>净额
                            </th>
                            <th>净占比
                            </th>
                        </tr>
                    </thead>
                    <tbody>


			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-12-16
				</td>
				<td>
					<span class='red'>22.46</span>
				</td>
				<td>
					<span class='red'>0.58%</span>
				</td>
				<td>
					<span class='green'>-5411万</span>
				</td>
				<td>
					<span class='green'>-8.19%</span>
				</td>
				<td>
					<span class='green'>-3646万</span>
				</td>
				<td>
					<span class='green'>-5.52%</span>
				</td>
				<td>
					<span class='green'>-1766万</span>
				</td>
				<td>
					<span class='green'>-2.67%</span>
				</td>
				<td>
					<span class='red'>1641万</span>
				</td>
				<td>
					<span class='red'>2.48%</span>
				</td>
				<td>
					<span class='red'>3770万</span>
				</td>
				<td>
					<span class='red'>5.71%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-12-15
				</td>
				<td>
					<span class='red'>22.33</span>
				</td>
				<td>
					<span class='red'>0.18%</span>
				</td>
				<td>
					<span class='green'>-2441万</span>
				</td>
				<td>
					<span class='green'>-3.08%</span>
				</td>
				<td>
					<span class='green'>-4148万</span>
				</td>
				<td>
					<span class='green'>-5.23%</span>
				</td>
				<td>
					<span class='red'>1707万</span>
				</td>
				<td>
					<span class='red'>2.15%</span>
				</td>
				<td>
					<span class='green'>-659万</span>
				</td>
				<td>
					<span class='green'>-0.83%</span>
				</td>
				<td>
					<span class='red'>3100万</span>
				</td>
				<td>
					<span class='red'>3.91%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-12-14
				</td>
				<td>
					<span class='green'>22.29</span>
				</td>
				<td>
					<span class='green'>-3.34%</span>
				</td>
				<td>
					<span class='green'>-1.11亿</span>
				</td>
				<td>
					<span class='green'>-11.93%</span>
				</td>
				<td>
					<span class='green'>-7567万</span>
				</td>
				<td>
					<span class='green'>-8.12%</span>
				</td>
				<td>
					<span class='green'>-3547万</span>
				</td>
				<td>
					<span class='green'>-3.81%</span>
				</td>
				<td>
					<span class='green'>-1283万</span>
				</td>
				<td>
					<span class='green'>-1.38%</span>
				</td>
				<td>
					<span class='red'>1.24亿</span>
				</td>
				<td>
					<span class='red'>13.31%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-12-13
				</td>
				<td>
					<span class='green'>23.06</span>
				</td>
				<td>
					<span class='green'>-0.86%</span>
				</td>
				<td>
					<span class='green'>-3092万</span>
				</td>
				<td>
					<span class='green'>-2.81%</span>
				</td>
				<td>
					<span class='green'>-1685万</span>
				</td>
				<td>
					<span class='green'>-1.53%</span>
				</td>
				<td>
					<span class='green'>-1407万</span>
				</td>
				<td>
					<span class='green'>-1.28%</span>
				</td>
				<td>
					<span class='green'>-130万</span>
				</td>
				<td>
					<span class='green'>-0.12%</span>
				</td>
				<td>
					<span class='red'>3222万</span>
				</td>
				<td>
					<span class='red'>2.93%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-12-12
				</td>
				<td>
					<span class='green'>23.26</span>
				</td>
				<td>
					<span class='green'>-6.25%</span>
				</td>
				<td>
					<span class='green'>-4.00亿</span>
				</td>
				<td>
					<span class='green'>-21.42%</span>
				</td>
				<td>
					<span class='green'>-3.17亿</span>
				</td>
				<td>
					<span class='green'>-16.98%</span>
				</td>
				<td>
					<span class='green'>-8286万</span>
				</td>
				<td>
					<span class='green'>-4.44%</span>
				</td>
				<td>
					<span class='red'>8665万</span>
				</td>
				<td>
					<span class='red'>4.65%</span>
				</td>
				<td>
					<span class='red'>3.13亿</span>
				</td>
				<td>
					<span class='red'>16.78%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-12-09
				</td>
				<td>
					<span class='red'>24.81</span>
				</td>
				<td>
					<span class='red'>0.28%</span>
				</td>
				<td>
					<span class='green'>-1.17亿</span>
				</td>
				<td>
					<span class='green'>-9.79%</span>
				</td>
				<td>
					<span class='green'>-2895万</span>
				</td>
				<td>
					<span class='green'>-2.43%</span>
				</td>
				<td>
					<span class='green'>-8788万</span>
				</td>
				<td>
					<span class='green'>-7.36%</span>
				</td>
				<td>
					<span class='red'>1934万</span>
				</td>
				<td>
					<span class='red'>1.62%</span>
				</td>
				<td>
					<span class='red'>9750万</span>
				</td>
				<td>
					<span class='red'>8.17%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-12-08
				</td>
				<td>
					<span class='green'>24.74</span>
				</td>
				<td>
					<span class='green'>-1.59%</span>
				</td>
				<td>
					<span class='green'>-1.92亿</span>
				</td>
				<td>
					<span class='green'>-20.34%</span>
				</td>
				<td>
					<span class='green'>-1.34亿</span>
				</td>
				<td>
					<span class='green'>-14.16%</span>
				</td>
				<td>
					<span class='green'>-5835万</span>
				</td>
				<td>
					<span class='green'>-6.18%</span>
				</td>
				<td>
					<span class='red'>5636万</span>
				</td>
				<td>
					<span class='red'>5.97%</span>
				</td>
				<td>
					<span class='red'>1.36亿</span>
				</td>
				<td>
					<span class='red'>14.37%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-12-07
				</td>
				<td>
					<span class='green'>25.14</span>
				</td>
				<td>
					<span class='green'>-0.95%</span>
				</td>
				<td>
					<span class='green'>-1.42亿</span>
				</td>
				<td>
					<span class='green'>-11.53%</span>
				</td>
				<td>
					<span class='green'>-9075万</span>
				</td>
				<td>
					<span class='green'>-7.38%</span>
				</td>
				<td>
					<span class='green'>-5107万</span>
				</td>
				<td>
					<span class='green'>-4.15%</span>
				</td>
				<td>
					<span class='red'>3004万</span>
				</td>
				<td>
					<span class='red'>2.44%</span>
				</td>
				<td>
					<span class='red'>1.12亿</span>
				</td>
				<td>
					<span class='red'>9.08%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-12-06
				</td>
				<td>
					<span class='green'>25.38</span>
				</td>
				<td>
					<span class='green'>-0.47%</span>
				</td>
				<td>
					<span class='green'>-3490万</span>
				</td>
				<td>
					<span class='green'>-3.86%</span>
				</td>
				<td>
					<span class='green'>-1142万</span>
				</td>
				<td>
					<span class='green'>-1.26%</span>
				</td>
				<td>
					<span class='green'>-2348万</span>
				</td>
				<td>
					<span class='green'>-2.60%</span>
				</td>
				<td>
					<span class='green'>-2020万</span>
				</td>
				<td>
					<span class='green'>-2.24%</span>
				</td>
				<td>
					<span class='red'>5510万</span>
				</td>
				<td>
					<span class='red'>6.10%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-12-05
				</td>
				<td>
					<span class='green'>25.50</span>
				</td>
				<td>
					<span class='green'>-3.59%</span>
				</td>
				<td>
					<span class='green'>-1.62亿</span>
				</td>
				<td>
					<span class='green'>-9.21%</span>
				</td>
				<td>
					<span class='green'>-2.11亿</span>
				</td>
				<td>
					<span class='green'>-11.99%</span>
				</td>
				<td>
					<span class='red'>4885万</span>
				</td>
				<td>
					<span class='red'>2.78%</span>
				</td>
				<td>
					<span class='red'>1331万</span>
				</td>
				<td>
					<span class='red'>0.76%</span>
				</td>
				<td>
					<span class='red'>1.49亿</span>
				</td>
				<td>
					<span class='red'>8.46%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-12-02
				</td>
				<td>
					<span class='green'>26.45</span>
				</td>
				<td>
					<span class='green'>-1.93%</span>
				</td>
				<td>
					<span class='green'>-1.46亿</span>
				</td>
				<td>
					<span class='green'>-10.65%</span>
				</td>
				<td>
					<span class='green'>-1.51亿</span>
				</td>
				<td>
					<span class='green'>-11.02%</span>
				</td>
				<td>
					<span class='red'>505万</span>
				</td>
				<td>
					<span class='red'>0.37%</span>
				</td>
				<td>
					<span class='green'>-183万</span>
				</td>
				<td>
					<span class='green'>-0.13%</span>
				</td>
				<td>
					<span class='red'>1.47亿</span>
				</td>
				<td>
					<span class='red'>10.78%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-12-01
				</td>
				<td>
					<span class='green'>26.97</span>
				</td>
				<td>
					<span class='green'>-0.04%</span>
				</td>
				<td>
					<span class='green'>-5131万</span>
				</td>
				<td>
					<span class='green'>-2.02%</span>
				</td>
				<td>
					<span class='red'>3273万</span>
				</td>
				<td>
					<span class='red'>1.29%</span>
				</td>
				<td>
					<span class='green'>-8405万</span>
				</td>
				<td>
					<span class='green'>-3.30%</span>
				</td>
				<td>
					<span class='green'>-2379万</span>
				</td>
				<td>
					<span class='green'>-0.93%</span>
				</td>
				<td>
					<span class='red'>7511万</span>
				</td>
				<td>
					<span class='red'>2.95%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-30
				</td>
				<td>
					<span class='red'>26.98</span>
				</td>
				<td>
					<span class='red'>3.13%</span>
				</td>
				<td>
					<span class='green'>-1.77亿</span>
				</td>
				<td>
					<span class='green'>-5.43%</span>
				</td>
				<td>
					<span class='green'>-5537万</span>
				</td>
				<td>
					<span class='green'>-1.70%</span>
				</td>
				<td>
					<span class='green'>-1.22亿</span>
				</td>
				<td>
					<span class='green'>-3.74%</span>
				</td>
				<td>
					<span class='red'>5758万</span>
				</td>
				<td>
					<span class='red'>1.77%</span>
				</td>
				<td>
					<span class='red'>1.20亿</span>
				</td>
				<td>
					<span class='red'>3.67%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-29
				</td>
				<td>
					<span class='green'>26.16</span>
				</td>
				<td>
					<span class='green'>-0.83%</span>
				</td>
				<td>
					<span class='green'>-3038万</span>
				</td>
				<td>
					<span class='green'>-1.48%</span>
				</td>
				<td>
					<span class='green'>-864万</span>
				</td>
				<td>
					<span class='green'>-0.42%</span>
				</td>
				<td>
					<span class='green'>-2174万</span>
				</td>
				<td>
					<span class='green'>-1.06%</span>
				</td>
				<td>
					<span class='green'>-1619万</span>
				</td>
				<td>
					<span class='green'>-0.79%</span>
				</td>
				<td>
					<span class='red'>4657万</span>
				</td>
				<td>
					<span class='red'>2.27%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-28
				</td>
				<td>
					<span class='green'>26.38</span>
				</td>
				<td>
					<span class='green'>-3.01%</span>
				</td>
				<td>
					<span class='green'>-7.73亿</span>
				</td>
				<td>
					<span class='green'>-23.22%</span>
				</td>
				<td>
					<span class='green'>-9.71亿</span>
				</td>
				<td>
					<span class='green'>-29.17%</span>
				</td>
				<td>
					<span class='red'>1.98亿</span>
				</td>
				<td>
					<span class='red'>5.95%</span>
				</td>
				<td>
					<span class='red'>3.16亿</span>
				</td>
				<td>
					<span class='red'>9.48%</span>
				</td>
				<td>
					<span class='red'>4.58亿</span>
				</td>
				<td>
					<span class='red'>13.74%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-25
				</td>
				<td>
					<span class='red'>27.20</span>
				</td>
				<td>
					<span class='red'>1.00%</span>
				</td>
				<td>
					<span class='red'>1.12亿</span>
				</td>
				<td>
					<span class='red'>6.38%</span>
				</td>
				<td>
					<span class='red'>8664万</span>
				</td>
				<td>
					<span class='red'>4.92%</span>
				</td>
				<td>
					<span class='red'>2568万</span>
				</td>
				<td>
					<span class='red'>1.46%</span>
				</td>
				<td>
					<span class='green'>-6747万</span>
				</td>
				<td>
					<span class='green'>-3.83%</span>
				</td>
				<td>
					<span class='green'>-4485万</span>
				</td>
				<td>
					<span class='green'>-2.55%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-24
				</td>
				<td>
					<span class='green'>26.93</span>
				</td>
				<td>
					<span class='green'>-1.07%</span>
				</td>
				<td>
					<span class='green'>-2420万</span>
				</td>
				<td>
					<span class='green'>-2.18%</span>
				</td>
				<td>
					<span class='green'>-413万</span>
				</td>
				<td>
					<span class='green'>-0.37%</span>
				</td>
				<td>
					<span class='green'>-2008万</span>
				</td>
				<td>
					<span class='green'>-1.81%</span>
				</td>
				<td>
					<span class='green'>-2733万</span>
				</td>
				<td>
					<span class='green'>-2.46%</span>
				</td>
				<td>
					<span class='red'>5154万</span>
				</td>
				<td>
					<span class='red'>4.65%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-23
				</td>
				<td>
					<span class='green'>27.22</span>
				</td>
				<td>
					<span class='green'>-0.29%</span>
				</td>
				<td>
					<span class='green'>-5.60亿</span>
				</td>
				<td>
					<span class='green'>-27.59%</span>
				</td>
				<td>
					<span class='green'>-5.42亿</span>
				</td>
				<td>
					<span class='green'>-26.69%</span>
				</td>
				<td>
					<span class='green'>-1840万</span>
				</td>
				<td>
					<span class='green'>-0.91%</span>
				</td>
				<td>
					<span class='red'>2.25亿</span>
				</td>
				<td>
					<span class='red'>11.08%</span>
				</td>
				<td>
					<span class='red'>3.35亿</span>
				</td>
				<td>
					<span class='red'>16.52%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-22
				</td>
				<td>
					<span class='green'>27.30</span>
				</td>
				<td>
					<span class='green'>-0.36%</span>
				</td>
				<td>
					<span class='green'>-3575万</span>
				</td>
				<td>
					<span class='green'>-2.48%</span>
				</td>
				<td>
					<span class='green'>-4500万</span>
				</td>
				<td>
					<span class='green'>-3.12%</span>
				</td>
				<td>
					<span class='red'>926万</span>
				</td>
				<td>
					<span class='red'>0.64%</span>
				</td>
				<td>
					<span class='green'>-404万</span>
				</td>
				<td>
					<span class='green'>-0.28%</span>
				</td>
				<td>
					<span class='red'>3979万</span>
				</td>
				<td>
					<span class='red'>2.76%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-21
				</td>
				<td>
					<span class='green'>27.40</span>
				</td>
				<td>
					<span class='green'>-1.15%</span>
				</td>
				<td>
					<span class='green'>-3.90亿</span>
				</td>
				<td>
					<span class='green'>-10.27%</span>
				</td>
				<td>
					<span class='green'>-4.72亿</span>
				</td>
				<td>
					<span class='green'>-12.43%</span>
				</td>
				<td>
					<span class='red'>8174万</span>
				</td>
				<td>
					<span class='red'>2.15%</span>
				</td>
				<td>
					<span class='red'>1.59亿</span>
				</td>
				<td>
					<span class='red'>4.19%</span>
				</td>
				<td>
					<span class='red'>2.31亿</span>
				</td>
				<td>
					<span class='red'>6.08%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-18
				</td>
				<td>
					<span class='red'>27.72</span>
				</td>
				<td>
					<span class='red'>2.67%</span>
				</td>
				<td>
					<span class='red'>2.60亿</span>
				</td>
				<td>
					<span class='red'>6.11%</span>
				</td>
				<td>
					<span class='red'>2.62亿</span>
				</td>
				<td>
					<span class='red'>6.15%</span>
				</td>
				<td>
					<span class='green'>-188万</span>
				</td>
				<td>
					<span class='green'>-0.04%</span>
				</td>
				<td>
					<span class='green'>-1.71亿</span>
				</td>
				<td>
					<span class='green'>-4.03%</span>
				</td>
				<td>
					<span class='green'>-8846万</span>
				</td>
				<td>
					<span class='green'>-2.08%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-17
				</td>
				<td>
					<span class='red'>27.00</span>
				</td>
				<td>
					<span class='red'>1.20%</span>
				</td>
				<td>
					<span class='red'>1.04亿</span>
				</td>
				<td>
					<span class='red'>6.51%</span>
				</td>
				<td>
					<span class='red'>5246万</span>
				</td>
				<td>
					<span class='red'>3.30%</span>
				</td>
				<td>
					<span class='red'>5118万</span>
				</td>
				<td>
					<span class='red'>3.22%</span>
				</td>
				<td>
					<span class='green'>-6372万</span>
				</td>
				<td>
					<span class='green'>-4.00%</span>
				</td>
				<td>
					<span class='green'>-3992万</span>
				</td>
				<td>
					<span class='green'>-2.51%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-16
				</td>
				<td>
					<span class='green'>26.68</span>
				</td>
				<td>
					<span class='green'>-0.97%</span>
				</td>
				<td>
					<span class='green'>-599万</span>
				</td>
				<td>
					<span class='green'>-0.27%</span>
				</td>
				<td>
					<span class='green'>-7957万</span>
				</td>
				<td>
					<span class='green'>-3.61%</span>
				</td>
				<td>
					<span class='red'>7358万</span>
				</td>
				<td>
					<span class='red'>3.34%</span>
				</td>
				<td>
					<span class='green'>-3628万</span>
				</td>
				<td>
					<span class='green'>-1.65%</span>
				</td>
				<td>
					<span class='red'>4227万</span>
				</td>
				<td>
					<span class='red'>1.92%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-15
				</td>
				<td>
					<span class='red'>26.94</span>
				</td>
				<td>
					<span class='red'>4.82%</span>
				</td>
				<td>
					<span class='red'>1.87亿</span>
				</td>
				<td>
					<span class='red'>4.73%</span>
				</td>
				<td>
					<span class='red'>4996万</span>
				</td>
				<td>
					<span class='red'>1.26%</span>
				</td>
				<td>
					<span class='red'>1.38亿</span>
				</td>
				<td>
					<span class='red'>3.47%</span>
				</td>
				<td>
					<span class='green'>-1.08亿</span>
				</td>
				<td>
					<span class='green'>-2.71%</span>
				</td>
				<td>
					<span class='green'>-7984万</span>
				</td>
				<td>
					<span class='green'>-2.01%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-14
				</td>
				<td>
					<span class='green'>25.70</span>
				</td>
				<td>
					<span class='green'>-1.12%</span>
				</td>
				<td>
					<span class='green'>-4.88亿</span>
				</td>
				<td>
					<span class='green'>-21.63%</span>
				</td>
				<td>
					<span class='green'>-4.56亿</span>
				</td>
				<td>
					<span class='green'>-20.22%</span>
				</td>
				<td>
					<span class='green'>-3176万</span>
				</td>
				<td>
					<span class='green'>-1.41%</span>
				</td>
				<td>
					<span class='red'>1.96亿</span>
				</td>
				<td>
					<span class='red'>8.69%</span>
				</td>
				<td>
					<span class='red'>2.92亿</span>
				</td>
				<td>
					<span class='red'>12.94%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-11
				</td>
				<td>
					<span class='green'>25.99</span>
				</td>
				<td>
					<span class='green'>-2.15%</span>
				</td>
				<td>
					<span class='green'>-2.27亿</span>
				</td>
				<td>
					<span class='green'>-9.10%</span>
				</td>
				<td>
					<span class='green'>-2.83亿</span>
				</td>
				<td>
					<span class='green'>-11.33%</span>
				</td>
				<td>
					<span class='red'>5555万</span>
				</td>
				<td>
					<span class='red'>2.23%</span>
				</td>
				<td>
					<span class='red'>7538万</span>
				</td>
				<td>
					<span class='red'>3.02%</span>
				</td>
				<td>
					<span class='red'>1.52亿</span>
				</td>
				<td>
					<span class='red'>6.08%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-10
				</td>
				<td>
					<span class='red'>26.56</span>
				</td>
				<td>
					<span class='red'>0.99%</span>
				</td>
				<td>
					<span class='green'>-1.20亿</span>
				</td>
				<td>
					<span class='green'>-1.82%</span>
				</td>
				<td>
					<span class='green'>-3.28亿</span>
				</td>
				<td>
					<span class='green'>-4.96%</span>
				</td>
				<td>
					<span class='red'>2.08亿</span>
				</td>
				<td>
					<span class='red'>3.14%</span>
				</td>
				<td>
					<span class='green'>-767万</span>
				</td>
				<td>
					<span class='green'>-0.12%</span>
				</td>
				<td>
					<span class='red'>1.28亿</span>
				</td>
				<td>
					<span class='red'>1.94%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-09
				</td>
				<td>
					<span class='red'>26.30</span>
				</td>
				<td>
					<span class='red'>8.59%</span>
				</td>
				<td>
					<span class='red'>24.02亿</span>
				</td>
				<td>
					<span class='red'>22.91%</span>
				</td>
				<td>
					<span class='red'>26.35亿</span>
				</td>
				<td>
					<span class='red'>25.13%</span>
				</td>
				<td>
					<span class='green'>-2.33亿</span>
				</td>
				<td>
					<span class='green'>-2.22%</span>
				</td>
				<td>
					<span class='green'>-12.90亿</span>
				</td>
				<td>
					<span class='green'>-12.31%</span>
				</td>
				<td>
					<span class='green'>-11.11亿</span>
				</td>
				<td>
					<span class='green'>-10.60%</span>
				</td>
			</tr>
			<tr class="" onmouseover="this.className='over'" onmouseout="this.className=''">

				<td>
					2016-11-08
				</td>
				<td>
					<span class='red'>24.22</span>
				</td>
				<td>
					<span class='red'>0.25%</span>
				</td>
				<td>
					<span class='green'>-7986万</span>
				</td>
				<td>
					<span class='green'>-11.35%</span>
				</td>
				<td>
					<span class='green'>-3948万</span>
				</td>
				<td>
					<span class='green'>-5.61%</span>
				</td>
				<td>
					<span class='green'>-4038万</span>
				</td>
				<td>
					<span class='green'>-5.74%</span>
				</td>
				<td>
					<span class='red'>2182万</span>
				</td>
				<td>
					<span class='red'>3.10%</span>
				</td>
				<td>
					<span class='red'>5805万</span>
				</td>
				<td>
					<span class='red'>8.25%</span>
				</td>
			</tr>
			<tr class="odd" onmouseover="this.className='over'" onmouseout="this.className='odd'">

				<td>
					2016-11-07
				</td>
				<td>
					<span class='green'>24.16</span>
				</td>
				<td>
					<span class='green'>-1.75%</span>
				</td>
				<td>
					<span class='green'>-1.27亿</span>
				</td>
				<td>
					<span class='green'>-12.53%</span>
				</td>
				<td>
					<span class='green'>-7720万</span>
				</td>
				<td>
					<span class='green'>-7.60%</span>
				</td>
				<td>
					<span class='green'>-5016万</span>
				</td>
				<td>
					<span class='green'>-4.94%</span>
				</td>
				<td>
					<span class='red'>3361万</span>
				</td>
				<td>
					<span class='red'>3.31%</span>
				</td>
				<td>
					<span class='red'>9375万</span>
				</td>
				<td>
					<span class='red'>9.23%</span>
				</td>
			</tr>
                    </tbody>
                </table>
            </div>
        </div>

    </div>

                </div>
            </div>
        </div>
        <div class="mainFrame" style="width:1000px;padding-top: 30px;">
            <div class="footer_top">
                数据来源：<a href="http://js5.eastmoney.com/tg.aspx?ID=953" style="color: #00298F;">东方财富Choice数据</a>
                <br />
            </div>
            <div class="footer" style="border-top: 0px;">
                 <div style="line-height: 20px;">
                    <b>郑重声明：</b>东方财富网发布此信息目的在于传播更多信息，与本网站立场无关。东方财富网不保证该信息（包括但不限于文字、数据及图表）全部或者部分内容的准确性、真实性、完整性、有效性、及时性、原创性等。相关信息并未经过本网站证实，不对您构成任何投资建议，据此操作，风险自担。
                </div>
                <iframe width="1000" height="314" frameborder="0" scrolling="no" marginwidth="0" marginheight="0" src="http://emres.dfcfw.com/public/footer-1000-iframe.html"></iframe>
            </div>
        </div>
    </div>

    <script src="http://emres.dfcfw.com/public/js/topnav.js" type="text/javascript"></script>
    <script src="http://hqres.eastmoney.com/EMQuote_Lib/js/qphf.js?r4900" charset="gbk" type="text/javascript"></script>
    <script src="/js_001/master.js" charset="gbk" type="text/javascript"></script>


    <script>
        window.adDataType = "data"; //共3个值：quote，data，guba不写默认表示其他频道；
        window.adSwitch = "both";//共3个值：both,left,right 不写默认both；
        window.fixedBodyWidth = 1000;//950,1000 不写默认1000







    </script>
    <script type="text/javascript" src="/js/ad.tools.v2.min.js" defer></script>
    <script type="text/javascript" src="http://cmsjs.eastmoney.com/analysis/emtj.min.js?v=20150408" defer></script>

    <!--[if IE 6]>
        <script type="text/javascript">
            jQuery(function() {
                var $ = jQuery;
                var html = '<div class="IE6_notice" style="font-size:14px;padding-top:5px;z-index:100000;width:100%;height:25px;background-color:#fbe899;">' +
	                            '您的浏览器版本太低，为了给您提供更好的浏览体验，请改用其他浏览器打开页面！' +
	                        '</div>';
                //$(html).insertBefore($(".top-nav-wrap"));
                $(html).insertBefore($("#fixMenuBar"));
                $(".IE6_notice").css("color", "red").css("font-family", "Microsoft YaHei");
                //$(".top-nav-wrap").css("top", "30px");
                $(".adFrame1000").css("padding-top", "40px");
            })
        </script>
    <![endif]-->

    <script src="http://emcharts.dfcfw.com/ec/2.2.5/emcharts.min.js" charset="utf-8"></script>
    <script type="text/javascript" src="/js_001/fn_zjlx.js?201606021830"></script>
    <script type="text/javascript">
        var _stockCode = "000002",
        _stockMarke = "2",
_stockName = "万科A";
        time_stamp = Math.floor((new Date().getTime()) / 60000);
        function ZjlxUpdate() {
            time_stamp = Math.floor((new Date().getTime()) / 60000);
            //var b = data_baseurl + "js/" + _stockCode + ".js?rt=" + Math.random();
            var b = "http://s1.dfcfw.com/js/" + _stockCode + ".js?rt=" + Math.random();
            tiny.loadJs(b, "utf-8",
            function () {
                if (!(typeof zjlx_detail == "undefined" || zjlx_detail == null)) {
                    var data = zjlx_detail.data.split(",");
                    $("updateTime_0").innerHTML = zjlx_detail.update;
                    $("updateTime_1").innerHTML = zjlx_detail.update;
                    $("data_jlr").innerHTML = data[0];
                    $("data_jlr").className = (data[0] > 0) ? "red" : ((data[0] < 0) ? "green" : "");
                    $("data_jzb").innerHTML = data[1] + "%";
                    $("data_jzb").className = (data[1] > 0) ? "red" : ((data[1] < 0) ? "green" : "");
                    $("data_superjlr").innerHTML = data[2];
                    $("data_superjlr").className = (data[2] > 0) ? "red" : ((data[2] < 0) ? "green" : "");
                    $("data_superjzb").innerHTML = data[3] + "%";
                    $("data_superjzb").className = (data[3] > 0) ? "red" : ((data[3] < 0) ? "green" : "");
                    $("data_ddjlr").innerHTML = data[4];
                    $("data_ddjlr").className = (data[4] > 0) ? "red" : ((data[4] < 0) ? "green" : "");
                    $("data_ddjzb").innerHTML = data[5] + "%";
                    $("data_ddjzb").className = (data[5] > 0) ? "red" : ((data[5] < 0) ? "green" : "");
                    $("data_zdjlr").innerHTML = data[6];
                    $("data_zdjlr").className = (data[6] > 0) ? "red" : ((data[6] < 0) ? "green" : "");
                    $("data_zdjzb").innerHTML = data[7] + "%";
                    $("data_zdjzb").className = (data[7] > 0) ? "red" : ((data[7] < 0) ? "green" : "");
                    $("data_xdjlr").innerHTML = data[8];
                    $("data_xdjlr").className = (data[8] > 0) ? "red" : ((data[8] < 0) ? "green" : "");
                    $("data_xdjzb").innerHTML = data[9] + "%";
                    $("data_xdjzb").className = (data[9] > 0) ? "red" : ((data[9] < 0) ? "green" : "");
                    $("data_superlr").innerHTML = data[12];
                    $("data_ddlr").innerHTML = data[14];
                    $("data_zdlr").innerHTML = data[16];
                    $("data_xdlr").innerHTML = data[18];
                    $("data_superlc").innerHTML = data[13];
                    $("data_ddlc").innerHTML = data[15];
                    $("data_zdlc").innerHTML = data[17];
                    $("data_xdlc").innerHTML = data[19] + "";
                }
            },
            true)
        }
        function ZjlxHqUpdate() {
            time_stamp = Math.floor((new Date().getTime()) / 60000);
            var b = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=' + _stockCode + _stockMarke + '&sty=CTBFTA&st=z&sr=&p=&ps=&cb=&js=var tab_data=({data:[(x)]})&token=70f12f2f4f091e459a279469fe49eca5';
            //var b = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=P.(x),(x)|' + _code + '|' + _code + '&sty=DCSFF|CTBF&st=z&sr=&p=&ps=&cb=&js=var tab_data=({data:[(x)]})&token=70f12f2f4f091e459a279469fe49eca5';
            tiny.loadJs(b, "utf-8", function () {
                if (!(typeof tab_data == "undefined" || tab_data == null)) {
                    var dataArr = tab_data.data;
                    if (dataArr.length == 1) {
                        //资金流
                        var _dh = dataArr[0].split(',');
                        //算和值
                        var data = [];
                        data[0] = (_dh[5] == "") ? "" : ((parseFloat(_dh[5]))).toFixed(4);//今日主力净流入
                        data[1] = (_dh[23] == "") ? "" : ((parseFloat(_dh[23]))).toFixed(2);//主力净比
                        data[2] = (_dh[9] == "") ? "" : ((parseFloat(_dh[9]))).toFixed(4);//今日超大单净流入
                        data[3] = (_dh[10] == "") ? "" : ((parseFloat(_dh[10]))).toFixed(2);//超大单净比
                        data[4] = (_dh[13] == "") ? "" : ((parseFloat(_dh[13]))).toFixed(4);//今日大单净流入
                        data[5] = (_dh[14] == "") ? "" : ((parseFloat(_dh[14]))).toFixed(2);//大单净比
                        data[6] = (_dh[17] == "") ? "" : ((parseFloat(_dh[17]))).toFixed(4);//今日中单净流入
                        data[7] = (_dh[18] == "") ? "" : ((parseFloat(_dh[18]))).toFixed(2);//中单净比
                        data[8] = (_dh[21] == "") ? "" : ((parseFloat(_dh[21]))).toFixed(4);//今日小单净流入
                        data[9] = (_dh[22] == "") ? "" : ((parseFloat(_dh[22]))).toFixed(2);//小单净比
                        data[10] = '';//
                        data[11] = '';//
                        data[12] = (_dh[7] == "") ? "" : ((parseFloat(_dh[7])) / 10000).toFixed(4);//超大单流入
                        data[13] = (_dh[8] == "") ? "" : ((parseFloat(_dh[8])) / 10000).toFixed(4);//超大单流处
                        data[14] = (_dh[11] == "") ? "" : ((parseFloat(_dh[11])) / 10000).toFixed(4);//大单流入
                        data[15] = (_dh[12] == "") ? "" : ((parseFloat(_dh[12])) / 10000).toFixed(4);//大单流出
                        data[16] = (_dh[15] == "") ? "" : ((parseFloat(_dh[15])) / 10000).toFixed(4);//中单流入
                        data[17] = (_dh[16] == "") ? "" : ((parseFloat(_dh[16])) / 10000).toFixed(4);//中单流出
                        data[18] = (_dh[19] == "") ? "" : ((parseFloat(_dh[19])) / 10000).toFixed(4);//小单流入
                        data[19] = (_dh[20] == "") ? "" : ((parseFloat(_dh[20])) / 10000).toFixed(4);//小单流出
                        $("updateTime_0").innerHTML = dateFormat(_dh[24], "HH:mm");
                        $("updateTime_1").innerHTML = dateFormat(_dh[24], "HH:mm");
                        $("data_jlr").innerHTML = data[0];
                        $("data_jlr").className = (data[0] > 0) ? "red" : ((data[0] < 0) ? "green" : "");
                        $("data_jzb").innerHTML = isNaN(data[1]) ? "0.00%" : data[1] + "%";
                        $("data_jzb").className = (data[1] > 0) ? "red" : ((data[1] < 0) ? "green" : "");
                        $("data_superjlr").innerHTML = data[2];
                        $("data_superjlr").className = (data[2] > 0) ? "red" : ((data[2] < 0) ? "green" : "");
                        $("data_superjzb").innerHTML = isNaN(data[3]) ? "0.00%" : data[3] + "%";
                        $("data_superjzb").className = (data[3] > 0) ? "red" : ((data[3] < 0) ? "green" : "");
                        $("data_ddjlr").innerHTML = data[4];
                        $("data_ddjlr").className = (data[4] > 0) ? "red" : ((data[4] < 0) ? "green" : "");
                        $("data_ddjzb").innerHTML = isNaN(data[5]) ? "0.00%" : data[5] + "%";
                        $("data_ddjzb").className = (data[5] > 0) ? "red" : ((data[5] < 0) ? "green" : "");
                        $("data_zdjlr").innerHTML = data[6];
                        $("data_zdjlr").className = (data[6] > 0) ? "red" : ((data[6] < 0) ? "green" : "");
                        $("data_zdjzb").innerHTML = isNaN(data[7]) ? "0.00%" : data[7] + "%";
                        $("data_zdjzb").className = (data[7] > 0) ? "red" : ((data[7] < 0) ? "green" : "");
                        $("data_xdjlr").innerHTML = data[8];
                        $("data_xdjlr").className = (data[8] > 0) ? "red" : ((data[8] < 0) ? "green" : "");
                        $("data_xdjzb").innerHTML = isNaN(data[9]) ? "0.00%" : data[9] + "%";
                        $("data_xdjzb").className = (data[9] > 0) ? "red" : ((data[9] < 0) ? "green" : "");
                        $("data_superlr").innerHTML = data[12];
                        $("data_ddlr").innerHTML = data[14];
                        $("data_zdlr").innerHTML = data[16];
                        $("data_xdlr").innerHTML = data[18];
                        $("data_superlc").innerHTML = data[13];
                        $("data_ddlc").innerHTML = data[15];
                        $("data_zdlc").innerHTML = data[17];
                        $("data_xdlc").innerHTML = data[19];
                    }
                }
            }, true)
        }
        function ZjlxInterval() {
            var e = new Date();
            try {
                e = Eastmoney.Time.now()
            } catch (i) { }
            var k = parseInt(tiny.dateFormat(e, "HHmm") * 1);
            var g = e.getDay();
            if (!(k <= 924 || (k >= 1145 && k <= 1259) || k >= 1515 || g > 5)) {
                try {
                    ZjlxHqUpdate();//新↑
                    var j = new Date().getTime();
                    var f = new SWFObject(swf_pie, "so30", "430", "250", "8", "");
                    f.addVariable("path", "/");
                    f.addVariable("settings_file", encodeURIComponent("../settings/zjlx_pie.xml"));
                    f.addVariable("data_file", encodeURIComponent(data_baseurl + "allXML/xml/" + _stockCode + ".xml?rt=" + j));
                    f.write("flash-cont-1")
                } catch (i) { }
            }
        }
        function ZjlInterval() {
            var e = new Date();
            try {
                e = Eastmoney.Time.now()
            } catch (i) { }
            var k = parseInt(tiny.dateFormat(e, "HHmm") * 1);
            var g = e.getDay();
            if (!(k <= 924 || (k >= 1145 && k <= 1259) || k >= 1515 || g > 5)) {
                //if(true){
                try {
                    var zljx_img = document.getElementById("zljx_img");
                    zljx_img.src = 'http://jspi.eastmoney.com/EM_CapitalFlowConvasPic/api/js?id=' + _stockCode + _stockMarke + '&type=fr&sty=S420225&jr=' + getCode();
                    var cjfb_img = document.getElementById("cjfb_img");
                    cjfb_img.src = 'http://jspi.eastmoney.com/EM_CapitalFlowConvasPic/api/js?id=' + _stockCode + _stockMarke + '&type=pie&sty=S43025090&jr=' + getCode();
                } catch (i) { }
            }
        }
        //ZjlxUpdate();//旧↓
        ZjlxHqUpdate();//新↑
        var url = "http://hqdigi2.eastmoney.com/EM_Quote2010NumericApplication/Index.aspx?Type=F&jsName=zjlx_hq&id=" + _stockCode + _stockMarke;
        var tableCache = '<table cellpadding="0" cellspacing="0" class="t2 ns2"><thead><tr><th>\u4ee3\u7801</th><th>\u540d\u79f0</th><th>\u6700\u65b0\u4ef7</th><th>\u6da8\u8dcc\u989d</th><th>\u6da8\u8dcc\u5e45</th><th>\u632f\u5e45</th><th>\u6210\u4ea4\u91cf(\u624b)</th><th>\u6210\u4ea4\u989d(\u4e07)</th><th>\u6628\u6536</th><th>\u4eca\u5f00</th><th>\u6700\u9ad8</th><th>\u6700\u4f4e</th><th>\u6362\u624b\u7387</th><th>\u91cf\u6bd4</th><th>\u5e02\u76c8\u7387</th><th>\u52a0\u81ea\u9009</th></tr></thead><tbody><tr><td><a href="http://quote.eastmoney.com/{code}.html" target="_blank">{code}</a></td><td><a href="http://quote.eastmoney.com/{code}.html" target="_blank">{name}</a></td><td>{price}</td><td>{change}</td><td>{percent}</td><td><span>{zf}</span></td><td><span>{amount}</span></td><td><span>{volume}</span></td><td>{last}</td><td>{open}</td><td>{height}</td><td>{low}</td><td><span>{hsl}</span></td><td><span>{lb}</span></td><td><span>{syl}</span></td><td><a href="http://quote.eastmoney.com/favor/infavor.aspx?code={code}" title="\u5c06{code}({name})\u52a0\u4e3a\u81ea\u9009\u80a1"><img src="../images/add.gif"></a></td></tr></tbody></table>';
        function hqUpdate() {
            var e = new Date();
            try {
                e = Eastmoney.Time.now()
            } catch (i) { }
            var k = parseInt(tiny.dateFormat(e, "HHmm") * 1);
            var g = e.getDay();
            if (!(k <= 924 || (k >= 1145 && k <= 1259) || k >= 1515 || g > 5)) {
                var b = url + "&rt=" + Math.floor((new Date().getTime()) / 30000);
                var c, d;
                var e = function (f, g, a) {
                    if (isNaN(g) || isNaN(a)) {
                        return "<span>" + f + "</span>"
                    }
                    if (parseFloat(g) > a) {
                        f = '<span class="red">' + f + "</span>"
                    } else {
                        if (parseFloat(g) < a) {
                            f = '<span class="green">' + f + "</span>"
                        } else {
                            f = "<span>" + f + "</span>"
                        }
                    }
                    return f
                };
                tiny.loadJs(b, "utf-8",
                function () {
                    if (!(typeof zjlx_hq == "undefined" || zjlx_hq == null)) {
                        c = zjlx_hq.quotation[0].split(",");
                        if (c.length < 24) {
                            c = [_stockCode, _stockCode, _stockName, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
                        }
                        d = tableCache.replace(/{code}/ig, c[1]);
                        d = d.replace(/{name}/ig, c[2]);
                        d = d.replace(/{price}/ig, e(c[5], c[10], 0));
                        d = d.replace(/{change}/ig, e(c[10], c[10], 0));
                        d = d.replace(/{percent}/ig, e(c[11], c[10], 0));
                        d = d.replace(/{zf}/ig, c[13]);
                        d = d.replace(/{amount}/ig, c[9]);
                        d = d.replace(/{volume}/ig, c[8]);
                        d = d.replace(/{last}/ig, e(c[3]));
                        d = d.replace(/{open}/ig, e(c[4], c[4], c[3]));
                        d = d.replace(/{height}/ig, e(c[6], c[6], c[3]));
                        d = d.replace(/{low}/ig, e(c[7], c[7], c[3]));
                        d = d.replace(/{hsl}/ig, c[23]);
                        d = d.replace(/{lb}/ig, c[22]);
                        d = d.replace(/{syl}/ig, (c[24] < 0 ? "--" : c[24]));
                        $("zjlx_hqcont").innerHTML = d
                    }
                },
                true)
            }
        }
        function hqInterval() {
            var e = new Date();
            try {
                e = Eastmoney.Time.now()
            } catch (g) { }
            var h = parseInt(tiny.dateFormat(e, "HHmm") * 1);
            var f = e.getDay();
            if (!(h <= 924 || (h >= 1145 && h <= 1259) || h >= 1515 || f > 5)) {
                try {
                    hqUpdate()
                } catch (g) { }
            }
        }
        setInterval(hqUpdate, 10000);
        hqUpdate();

        //新的折线图
        var chart = new EmchartsWebLine({
            container: "flash-cont",
            width: 420,
            height: 225,
            showflag: true,
            sepeNum: 6,
            font: {
                fontFamily: 'Microsoft Yahei',
                fontSize: "12",
                color: "#000"
            },
            xaxis: [""],
            series: [""]
        });
        var chartPH = new EmchartsWebLine({
            container: "flash-cont-2",
            width: 420,
            height: 210,
            showflag: true,
            sepeNum: 6,
            font: {
                fontFamily: 'Microsoft Yahei',
                fontSize: "12",
                color: "#000"
            },
            xaxis: [""],
            series: [""]
        });
        var today = new Date();
        var QuerySpan = "";
        today.setDate(today.getDate() - 42);
        QuerySpan = today.getFullYear() + "-" + (parseInt(today.getMonth()) + 1) + "-" + today.getDate();
        var ff = 0;
        var opChart = {
            draw: function (data, obj) {
                obj.options.xaxis = data.xaxis;
                obj.options.series = data.series;
                //调用绘图方法
                obj.draw(function (error) {
                    if (error == null) {
                        obj.reDraw();//使用上次的数据数据重绘
                    }
                });
            },
            dataTransfer: function (obj) {
                var value = {
                    xaxis: [],
                    series: []
                }
                var main = {
                    name: "主力净流入",
                    color: "#FE3EE1",
                    data: [],
                    suffix: '万元'
                };
                var large = {
                    name: "超大单净流入",
                    color: "#650000",
                    data: [],
                    suffix: '万元'
                };
                var big = {
                    name: "大单净流入",
                    color: "#FF1117",
                    data: [],
                    suffix: '万元'
                };
                var middle = {
                    name: "中单净流入",
                    color: "#FFB83D",
                    data: [],
                    suffix: '万元'
                };
                var small = {
                    name: "小单净流入",
                    color: "#94C4EE",
                    data: [],
                    suffix: '万元'
                };

                var xArr = obj.xa.split(",");
                for (var i = 0; i < xArr.length; i++) {
                    var time = xArr[i];
                    if (time != "") {
                        var isShow = false;
                        if (time == "09:31" || time == "10:30" || time == "11:30" || time == "14:00" || time == "15:00") {
                            isShow = true;
                        }
                        value.xaxis.push({
                            value: time,
                            showline: isShow,
                            show: isShow
                        });
                    }
                }
                var yArr = obj.ya;
                document.getElementById("flash-cont").style.backgroundImage = '';
                for (var i = 0; i < yArr.length; i++) {
                    if (i == 0 && yArr[i] == ',,,,') {
                        document.getElementById("flash-cont").style.backgroundImage = 'url(/images/panqianqingkong.jpg)';
                        document.getElementById("flash-cont").style.backgroundRepeat = 'no-repeat';
                        return false;
                    }
                    var subArray = yArr[i].split(',');
                    main.data.push(subArray[0]);
                    large.data.push(subArray[1]);
                    big.data.push(subArray[2]);
                    middle.data.push(subArray[3])
                    small.data.push(subArray[4]);
                }

                value.series.push(main);
                value.series.push(large);
                value.series.push(big);
                value.series.push(middle);
                value.series.push(small);
                this.draw(value, chart);
            },
            dataSpilt: function (data) {
                var value = {
                    xaxis: [],
                    series: []
                }
                var main = {
                    name: "主力净流入",
                    color: "#FE3EE1",
                    data: [],
                    suffix: '万元'
                };
                var large = {
                    name: "超大单净流入",
                    color: "#650000",
                    data: [],
                    suffix: '万元'
                };
                var big = {
                    name: "大单净流入",
                    color: "#FF1117",
                    data: [],
                    suffix: '万元'
                };
                var middle = {
                    name: "中单净流入",
                    color: "#FFB83D",
                    data: [],
                    suffix: '万元'
                };
                var small = {
                    name: "小单净流入",
                    color: "#94C4EE",
                    data: [],
                    suffix: '万元'
                };
                var _x = [];
                var _y = data.length;
                var xpoint = 4;
                var jg = parseInt(_y / xpoint);
                for (var i = 0; i < data.length; i++) {
                    var dataArr = data[i].split(',');
                    var isShow = false;
                    //var f = _y - (i + 1);//反序对应数
                    //console.log(f, dataArr[0], i,mo);
                    //if ((i % jg == 00) || i == _y - 1) {
                    if (_y < xpoint || i % jg == 0 || (i % jg > xpoint && i == _y - 1)) {
                        isShow = true;
                    }
                    value.xaxis.push({
                        value: dateFormat(dataArr[0], 'MM-dd'),
                        showline: isShow,
                        show: isShow
                    });
                    main.data.push(dataArr[1]);
                    large.data.push(dataArr[2]);
                    big.data.push(dataArr[3]);
                    middle.data.push(dataArr[4])
                    small.data.push(dataArr[5]);
                }
                value.series.push(main);
                value.series.push(large);
                value.series.push(big);
                value.series.push(middle);
                value.series.push(small);
                this.draw(value, chartPH);
            },
            init: function () {
                var $ = jQuery;
                var _this = this;
                $.ajax({
                    type: "get",
                    url: "http://ff.eastmoney.com/EM_CapitalFlowInterface/api/js?id=" + _stockCode + _stockMarke + "&type=ff&check=MLBMS&cb=var%20aff_data=&js={(x)}&rtntype=3",
                    dataType: "script",
                    scriptCharset: "utf-8",
                    success: function () {
                        _this.dataTransfer(aff_data);
                    }
                })
            },
            flash: function () {

                var ifm = document.createElement('img');
                ifm.id = 'zljx_img';
                ifm.src = 'http://jspi.eastmoney.com/EM_CapitalFlowConvasPic/api/js?id=' + _stockCode + _stockMarke + '&type=fr&sty=S420225&jr=' + getCode();
                document.getElementById("flash-cont").appendChild(ifm);
                var ifm_ph = document.createElement('img');
                ifm_ph.src = 'http://jspi.eastmoney.com/EM_CapitalFlowConvasPic/api/js?id=' + _stockCode + _stockMarke + '&type=hff&sty=S420210&jr=' + getCode();
                document.getElementById("flash-cont-2").appendChild(ifm_ph);
                var ifm_pi = document.createElement('img');
                ifm_pi.id = 'cjfb_img';
                ifm_pi.src = 'http://jspi.eastmoney.com/EM_CapitalFlowConvasPic/api/js?id=' + _stockCode + _stockMarke + '&type=pie&sty=S43025090&jr=' + getCode();
                document.getElementById("flash-cont-1").appendChild(ifm_pi);

            },
            panhou: function () {
                var $ = jQuery;
                var _this = this;
                $.ajax({
                    type: "get",
                    url: "http://ff.eastmoney.com/EM_CapitalFlowInterface/api/js?id=" + _stockCode + _stockMarke + "&type=hff&rtntype=2&js=(x)&check=TMLBMS&cb=var%20ph_data=&QueryStyle=1&QuerySpan=" + QuerySpan,
                    dataType: "script",
                    scriptCharset: "utf-8",
                    success: function () {
                        _this.dataSpilt(ph_data);
                    }
                })
            }
        };
        //新的饼图
        var chartPie = new EmchartsPie({
            container: "flash-cont-1",
            width: 430,
            height: 250,
            startOffset: Math.PI / 2,
            onPie: false,
            data: "",
            point: {
                x: 215,
                y: 140
            },
            radius: 90
        });
        var opChartPie = {
            draw: function (obj) {
                chartPie.options.data = obj;
                //调用绘图方法
                chartPie.reDraw();
            },
            dataTransfer: function (obj) {
                var value = [];
                if (obj == "" || obj == undefined) {
                    document.getElementById("flash-cont-1").style.backgroundImage = 'url(/images/panqianqingkong_bing.jpg)';
                    document.getElementById("flash-cont-1").style.backgroundRepeat = 'no-repeat';
                    return false;
                }
                var array = obj.replace("\"", "").split(",");
                value.push({
                    name: "小单流出",
                    color: "#77e97a",
                    value: array[20] == "" ? "0" : (parseFloat(Math.abs(array[20])) / 10000).toFixed(4),
                    showInfo: true
                });
                value.push({
                    name: "中单流出",
                    color: "#27b729",
                    value: array[16] == "" ? "0" : (parseFloat(Math.abs(array[16])) / 10000).toFixed(4),
                    showInfo: true
                });
                value.push({
                    name: "大单流出",
                    color: "#0a820a",
                    value: array[12] == "" ? "0" : (parseFloat(Math.abs(Number(array[12]))) / 10000).toFixed(4),
                    showInfo: true
                });
                value.push({
                    name: "超大单流出",
                    color: "#004800",
                    value: array[8] == "" ? "0" : (parseFloat(Math.abs(Number(array[8]))) / 10000).toFixed(4),
                    show: true,
                    showInfo: true
                });
                value.push({
                    name: "超大单流入",
                    color: "#650000",
                    value: array[7] == "" ? "0" : (parseFloat(Number(array[7])) / 10000).toFixed(4),
                    showInfo: true
                });
                value.push({
                    name: "大单流入",
                    color: "#ae0000",
                    value: array[11] == "" ? "0" : (parseFloat(Number(array[11])) / 10000).toFixed(4),
                    showInfo: true
                });
                value.push({
                    name: "中单流入",
                    color: "#f83434",
                    value: array[15] == "" ? "0" : (parseFloat(array[15]) / 10000).toFixed(4),
                    showInfo: true
                });
                value.push({
                    name: "小单流入",
                    color: "#ff8080",
                    value: array[19] == "" ? "0" : (parseFloat(array[19]) / 10000).toFixed(4),
                    showInfo: true
                });
                if (IsPanQian_pie(value)) {
                    document.getElementById("flash-cont-1").style.backgroundImage = 'url(/images/panqianqingkong_bing.jpg)';
                    document.getElementById("flash-cont-1").style.backgroundRepeat = 'no-repeat';
                    return false;
                }
                this.draw(value);
            },
            init: function () {
                var _this = this;
                var $ = jQuery;
                $.ajax({
                    type: "get",
                    url: "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=" + _stockCode + _stockMarke + "&sty=CTBF&st=z&sr=&p=&ps=&cb=var%20pie_data=&js=(x)&token=28758b27a75f62dc3065b81f7facb365",
                    dataType: "script",
                    scriptCharset: "utf-8",
                    success: function () {
                        _this.dataTransfer(pie_data);
                    }
                })
            }
        };
        function ZjlxEmIn() {
            ZjlxHqUpdate();//新↑
            opChart.init();
            opChartPie.init();
            opChart.panhou();
        }
        //var ua = navigator.userAgent.toLowerCase();
        //var app = navigator.appVersion;
        var isIE = !!window.ActiveXObject;
        var isIE6 = isIE && !window.XMLHttpRequest;
        var isIE8 = !+'\v1';
        if (isIE) {//IE的方向
            if (isIE6 || isIE8) {
                opChart.flash();
                setInterval(ZjlInterval, 60000);
            }
            else {
                ZjlxEmIn();
                setInterval(ZjlxEmIn, 60000);//新的JS记载
            }
        }
        else {
            ZjlxEmIn();
            setInterval(ZjlxEmIn, 60000);//新的JS记载
        }
        function dateFormat(dateS, part) {
            if (dateS == "-" || typeof dateS == "undefined") {
                return '-';
            }
            if (dateS.length > 10) {
                dateS = dateS.split('T')[0].replace(/-/g, "/");
            }
            var date = new Date(dateS);
            var datecopy;
            var redate = "";
            part = (part == null) ? "yyyy-MM-dd HH:mm:ss" : part;
            var y = date.getFullYear();
            var M = date.getMonth() + 1;
            var d = date.getDate();
            var H = date.getHours();
            var m = date.getMinutes();
            var s = date.getSeconds();
            var MM = (M > 9) ? M : "0" + M;
            var dd = (d > 9) ? d : "0" + d;
            var HH = (H > 9) ? H : "0" + H;
            var mm = (m > 9) ? m : "0" + m;
            var ss = (s > 9) ? s : "0" + s;
            redate = part.replace("yyyy", y).replace("MM", MM).replace("dd", dd).replace("HH", HH).replace("mm", mm).replace("ss", ss).replace("M", M).replace("d", d).replace("H", H).replace("m", m).replace("s", s);
            return redate;
        }
        function getCode(num) {
            var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            var codes = str.split('');
            num = num || 6;
            var code = "";
            for (var i = 0; i < num; i++) {
                code += codes[Math.floor(Math.random() * 52)];
            }
            return code;
        }
    </script>

</body>
</html>
    """

data = etree.HTML(str)
print(type(str))
print(data)

dataBody = data.xpath('//*[@id="dt_1"]/tbody/tr')

print(len(dataBody))
# print(len(dataBody))

import  re
for zjlx_his_one in dataBody:
    one_his=zjlx_his_one.xpath('td')
    # print(one_his[0].xpath('string(.)'))
    super_a1 = re.sub(r'[\r\n\t%]', '', one_his[7].xpath('string(.)'))
    print(super_a1)

    # print(len(one_his))