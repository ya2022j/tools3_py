#! coding:utf-8


import requests
from bs4 import BeautifulSoup

# 大一些文本直接用三个双引号来处理
html_doc = """



<!DOCTYPE html>
<html lang="ja">
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# article: http://ogp.me/ns/article#">
<meta charset="utf-8">
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//img.vorkers.com">
<link rel="dns-prefetch" href="//image.vorkers.com">
<link rel="dns-prefetch" href="//assets.vorkers.com">
<link rel="dns-prefetch" href="//in.treasuredata.com">
<link rel="dns-prefetch" href="//s3.amazonaws.com">
<link rel="dns-prefetch" href="//www.googletagmanager.com">
<link rel="dns-prefetch" href="//www.google-analytics.com">
<link rel="dns-prefetch" href="//www.google.co.jp">
<link rel="dns-prefetch" href="//www.google.com">
<link rel="dns-prefetch" href="//stats.g.doubleclick.net">
<link rel="icon" href="/favicon.ico?01">
<title>求人情報 - 社員クチコミならOpenWork</title>
<meta name="keywords" content="求人, 求人情報, 求人検索, 就職, 転職, 採用, クチコミ">
<meta name="description" content="求人情報です。OpenWorkの求人検索は、国内最大級の社員クチコミと合わせて求人情報を検索できます。">
<meta property="og:description" content="求人情報です。OpenWorkの求人検索は、国内最大級の社員クチコミと合わせて求人情報を検索できます。">
<meta property="og:locale" content="ja_JP">
<meta property="og:type" content="website">
<meta property="og:site_name" content="OpenWork">
<meta property="og:title" content="求人情報 - 社員クチコミならOpenWork">
<meta property="og:url" content="https://www.vorkers.com/job_search_result?n=&amp;o=&amp;z=&amp;p=&amp;remoteWork=&amp;k=Golang&amp;kt=&amp;mids=&amp;y=&amp;totalS=&amp;x=&amp;w=&amp;i=&amp;f=&amp;u=std&amp;ct=jresult">
<meta property="article:author" content="https://www.facebook.com/OpenWork.sns/">
<meta property="og:image" content="https://assets.vorkers.com/images/common/ogp.png?02">
<meta name="twitter:card" content="summary"/>
<meta name="twitter:site" content="@OpenWork_JP">
<meta name="viewport" content="width=1100">

    <link rel="stylesheet" href="https://assets.vorkers.com/assets/css_common_pc.467ebc8e.css" media="all">


            <meta name="robots" content="noindex">
        <link rel="canonical" href="https://www.vorkers.com/job_search_result?u=std">
                    <link rel="next" href="/job_search_result?kt=Golang&amp;u=std&amp;page=2">

<!--[if lt IE 9]>
<script>for(i in s="article,aside,canvas,details,datalist,figcaption,figure,footer,header,keygen,main,nav,section,summary,time".split(','))document.createElement(s[i]);</script>
<![endif]-->

<script type="text/javascript">
!function(t,e){if(void 0===e[t]){e[t]=function(){e[t].clients.push(this),this._init=[Array.prototype.slice.call(arguments)]},e[t].clients=[];for(var r=function(t){return function(){return this["_"+t]=this["_"+t]||[],this["_"+t].push(Array.prototype.slice.call(arguments)),this}},s=["addRecord","fetchGlobalID","set","trackEvent","trackPageview","trackClicks","ready"],a=0;a<s.length;a++){var c=s[a];e[t].prototype[c]=r(c)}var n=document.createElement("script");n.type="text/javascript",n.async=!0,n.src=("https:"===document.location.protocol?"https:":"http:")+"//cdn.treasuredata.com/sdk/1.9.2/td.min.js";var i=document.getElementsByTagName("script")[0];i.parentNode.insertBefore(n,i)}}("Treasure",this);
</script>

</head>
<body>
<noscript>
    <div class="backgroundGray">
        <p class="fs-16 red m-a w-1000 pt-15 pb-15">このWebサイトのすべての機能を利用するためにはJavaScriptを有効にしてください。</p>
    </div>
</noscript>
    <div id="wrapper">
                                            <div id="headTextWrapper">
                    <h1 id="headText">
                            フリーワード：Golangの求人一覧
                    </h1>
                </div>
                                        <header id="header" class="noBorder">
                            <div id="headerMain">
                    <div id="headerAction">
                                                    <p id="siteLogo">
        <a id="siteLogoLink" href="/" class="d-ib">
                            <img width="110" height="19" src="https://assets.vorkers.com/images/common/logo_header.svg?01" alt="OpenWork">

        </a>
    </p>


                                                                                                                <ul class="headerNavigation">
                                                                            <li class="headerNavigation_item headerNavigation_item-current">
                                            <a href="/job_search_result?u=std" class="searchChangeTrigger white d-b">求人を探す</a>
                                        </li>
                                        <li class="headerNavigation_item">
                                            <a href="/company_list?field=&amp;pref=&amp;src_str=&amp;sort=1" class="searchChangeTrigger white d-b">社員クチコミ・年収を探す</a>
                                        </li>
                                                                    </ul>

                                                                                            <ul id="headerPersonal">
        <li class="headerPersonal_item"><a data-_vmodal-type="m" href="javascript:void(0);" class="jsLoginModalTrigger button-header"><span class="headerPersonal_icon pcIcon pcIcon-79 pcIcon-buttonHeader-message">メッセージ</span></a></li><li class="headerPersonal_item ml-5"><a data-_vmodal-type="bj" href="javascript:void(0);" class="jsLoginModalTrigger button-header"><span class="headerPersonal_icon pcIcon pcIcon-69 pcIcon-buttonHeader-favorite">気になる</span></a></li>    </ul>

                                                                        </div>
                </div>
                                                    <div id="headerHead">
    <div id="headInner">
        <ul id="headerMenu">
                                            <li class="headerMenu_item"><a href="/recruiting?ad=com_referral_header_pc" data-_v-event-logger-key="rec_lp" data-_v-event-logger-parameter="headerText">採用ご担当者様へ</a></li>
                <li class="headerMenu_item pr-5"><a href="/admission.php" rel="nofollow">ユーザー登録（無料）</a></li>
                <li class="headerMenu_item headerMenu_item-last"><a href="/login.php" rel="nofollow">ログイン</a></li>
                    </ul>
    </div>
</div>
                            </header>

                                <main>

    <div class="o-h backgroundLightGray pt-10">
                <header id="contentsHeader" class="w-1000 center mb-15">
                            <ol id="topicPath">
                                                <li class="topicPath_item"><a class="topicPath_anchor" href="https://www.vorkers.com/">ＨＯＭＥ</a></li>

                                                <li class="topicPath_item"><a class="topicPath_anchor" href="/job_search_result?u=std">求人トップ</a></li>

                                                <li class="topicPath_item topicPath_item-last">求人情報</li>

                                    </ol>
                                        <h2 class="fs-18 fw-n mb-10 mt-50">
                                            <span class="d-ib v-t">&quot;</span><span class="truncate max-w-800 d-ib v-t">フリーワード：Golang</span><span class="d-ib v-t">&quot;</span><span class="ml-5 d-ib v-t">の求人一覧</span>
                                    </h2>
                                                            <dl class="jobCounter jsJobCountWrapper">
                        <dt class="colonListTerm jsJobCountTitle">該当求人</dt>
                        <dd class="d-i"><span class="jsJobCount ml-5 mr-5 jobCounter_number">109</span>件</dd>
                    </dl>
                    <form id="jsConditionForm" action="/job_search_result" method="GET" class="jsJobSearchCtForm">
                        <div class="box-15 mt-10 backgroundWhite">
                            <div class="o-h mt-5 pb-5 pl-5 pr-5">
                                                                                                <dl>
                                    <dt class="d-ib fs-16 fw-b w-150 v-t lh-1o5 pt-5 pb-5">
                                        <span class="pcIcon pcIcon-43 pcIcon-jobList madblack">職種</span>
                                    </dt>
                                    <dd class="d-ib">
                                        <a id="jsOccupationModalTrigger" href="javascript:void(0)"
                                           class="modalTrigger-blue pcIcon pcIcon-51 jsModalOpen">選択する</a>
                                        <div class="gray d-ib w-655 o-h">
                                            <div id="jsOccupationFamilies" class="jsFamiliesWrapper pl-5 fs-12 mt-n5 d-n">
    </div>

                                        </div>
                                        <input type="hidden" id="o" name="o" />
                                        <input type="hidden" id="z" name="z" />
                                    </dd>
                                </dl>
                                <dl class="mt-15 borderLightGray-top pt-15">
                                    <dt class="d-ib fs-16 fw-b w-150 v-t lh-1o5 pt-5 pb-5"><span
                                                class="pcIcon pcIcon-44 pcIcon-jobList madblack">勤務地</span></dt>
                                    <dd class="d-ib">
                                        <a id="jsLocationModalTrigger" href="javascript:void(0)"
                                           class="modalTrigger-blue pcIcon pcIcon-51 jsModalOpen">選択する</a>
                                        <div class="gray d-ib w-655 o-h">
                                            <div class="pl-5 fs-12 d-n" style="display: block;">
                                                <div class="jsHouse d-ib fs-13">
                                                    <ul id="jsLocationFamilies"
                                                        class="jsPrefecturesWrapper childItem childItem-location"></ul>
                                                </div>
                                            </div>

                                        </div>
                                        <input type="hidden" id="p" name="p" />
                                    </dd>
                                </dl>

                                                                <dl class="mt-15 borderLightGray-top pt-15 jsDefaultHide jsShowWhenShowCondition d-n">
                                    <dt class="d-ib fs-16 fw-b w-150 v-t lh-1o5 pt-5 pb-5"><span class="pcIcon pcIcon-89 pcIcon-jobList pcIcon-jobList-remoteWork madblack">リモートワーク</span></dt>
                                    <dd class="d-ib">
                                        <div class="selectboxWrapper-default selectboxWrapper-gray d-ib">
                                            <select id="remoteWork" name="remoteWork" class="selectbox-default selectbox-jobSearch w-210 fs-13"><option value="">指定しない</option><option value="3">リモートメイン</option><option value="2">リモート可</option></select>
                                        </div>
                                    </dd>
                                </dl>

                                                                <dl class="mt-15 borderLightGray-top pt-15 jsDefaultHide jsShowWhenShowCondition d-n">
                                    <dt class="d-ib fs-16 fw-b w-150 v-t lh-1o5 pt-10 pb-5"><span
                                                class="pcIcon pcIcon-04 pcIcon-jobList madblack">フリーワード</span></dt>
                                    <dd class="d-ib w-800 pt-5 pb-5">
                                        <div id="jsKeywordFamilies" class="jsFamiliesWrapper pb-10 o-h fs-12 mt-n10">
<div class="jsHouse d-b mr-10 fs-13 lh-high ml-n15"><ul><li class="ml-15 mr-n5 mt-10 d-ib selectedItem jsKeywordFamily"><span class="truncate max-w-650 d-ib v-m">Golang</span><a class="selectedItem-delete jsKeywordDelete jsTagItem" href="javascript:void(0)" data-_v-id="Golang">選択解除</a></li></ul></div></div>

                                        <input type="text" id="k" name="k" maxlength="100" class="textarea-blue h-32 w-450 jsJobSearchKeywordInput mr-20 fs-13 mb-5" placeholder="社名や仕事内容など" />
                                        <input type="hidden" id="kt" name="kt" value="Golang" />
                                        <input type="hidden" id="mids" name="mids" />
                                    </dd>
                                </dl>

                                <div class="mt-15 borderLightGray-top pt-15 o-h jsDefaultHide jsShowWhenShowCondition d-n">
                                                                        <dl class="f-l w-50p">
                                        <dt class="d-ib fs-16 fw-b w-150 v-t pt-5"><span
                                                    class="pcIcon pcIcon-52 pcIcon-jobList madblack">年収</span></dt>
                                        <dd class="d-ib">
                                            <div class="selectboxWrapper-default selectboxWrapper-gray d-ib">
                                                <select id="y" name="y" class="selectbox-default selectbox-jobSearch w-210 fs-13"><option value="">指定しない</option><option value="300">300万円以上</option><option value="350">350万円以上</option><option value="400">400万円以上</option><option value="450">450万円以上</option><option value="500">500万円以上</option><option value="600">600万円以上</option><option value="700">700万円以上</option><option value="800">800万円以上</option><option value="1000">1000万円以上</option></select>
                                            </div>
                                        </dd>
                                    </dl>
                                                                        <dl class="f-r w-50p">
                                        <dt class="d-ib fs-16 fw-b w-150 v-t pt-5"><span
                                                    class="pcIcon pcIcon-star10 pcIcon-jobList madblack">総合評価</span>
                                        </dt>
                                        <dd class="d-ib">
                                            <div class="selectboxWrapper-default selectboxWrapper-gray d-ib">
                                                <select id="totalS" name="totalS" class="selectbox-default selectbox-jobSearch w-210 fs-13"><option value="">指定しない</option><option value="2.5">2.5以上</option><option value="3.0">3.0以上</option><option value="3.5">3.5以上</option></select>
                                            </div>
                                        </dd>
                                    </dl>
                                </div>

                                <div class="mt-15 borderLightGray-top pt-15 o-h jsDefaultHide jsShowWhenShowCondition d-n">
                                                                        <dl class="f-l w-50p">
                                        <dt class="d-ib fs-16 fw-b w-150 v-t pt-5"><span
                                                    class="pcIcon pcIcon-57 pcIcon-jobList madblack">残業時間</span></dt>
                                        <dd class="d-ib">
                                            <div class="selectboxWrapper-default selectboxWrapper-gray d-ib">
                                                <select id="x" name="x" class="selectbox-default selectbox-jobSearch w-210 fs-13"><option value="">指定しない</option><option value="20">20時間以内</option><option value="40">40時間以内</option><option value="60">60時間以内</option><option value="80">80時間以内</option></select>
                                            </div>
                                        </dd>
                                    </dl>

                                                                        <dl class="f-r w-50p">
                                        <dt class="d-ib fs-16 fw-b w-150 v-t pt-5"><span
                                                    class="pcIcon pcIcon-56 pcIcon-jobList madblack">有休消化率</span></dt>
                                        <dd class="d-ib">
                                            <div class="selectboxWrapper-default selectboxWrapper-gray d-ib">
                                                <select id="w" name="w" class="selectbox-default selectbox-jobSearch w-210 fs-13"><option value="">指定しない</option><option value="20">20％以上</option><option value="40">40％以上</option><option value="60">60％以上</option><option value="80">80％以上</option></select>
                                            </div>
                                        </dd>
                                    </dl>
                                </div>

                                                                <dl class="mt-15 borderLightGray-top pt-15 jsDefaultHide jsShowWhenShowCondition d-n">
                                    <dt class="d-ib fs-16 fw-b w-150 v-t lh-1o5 pt-5 pb-5">
                                        <span class="pcIcon pcIcon-65 pcIcon-jobList madblack">業界</span>
                                    </dt>
                                    <dd class="d-ib">
                                        <a id="jsFieldModalTrigger" href="javascript:void(0)"
                                           class="modalTrigger-blue pcIcon pcIcon-51 jsModalOpen">選択する</a>
                                        <div class="gray d-ib w-655 o-h">
                                            <div id="jsFieldFamilies" class="jsFamiliesWrapper pl-5 fs-12 mt-n5 d-n">
    </div>

                                        </div>
                                        <input type="hidden" id="i" name="i" />
                                        <input type="hidden" id="f" name="f" />
                                    </dd>
                                </dl>
                            </div>
                        </div>
                        <div id="jsConditionSubmitBox" class="mt-20 p-r">
                            <div id="jsConditionSubmitBoxChild">
                                <div class="t-c ml-15 mr-15 p-r pb-10 pt-5">
                                    <button class="button button-usuallyGreen fs-16 fw-b w-400 button-disable jsJobSearchCtSubmit"
                                            type="submit">この条件で検索する（該当求人<span
                                                class="jsJobCount ml-5 mr-5">109</span>件
                                        <span class="ls-n13">）</span></button>
                                </div>
                            </div>
                            <div class="showOtherItem jsShowCondition jsHideWhenShowCondition">
                                <a href="javascript:void(0)" class="jsShowOtherItem">＋詳しい条件を設定する</a>
                            </div>
                        </div>
                        <div class="d-n">
                            <select id="u" name="u"><option value="total">総合評価</option><option value="satisfy">待遇の満足度</option><option value="work_life_balance">ワークライフバランス</option><option value="junior">成長できる</option><option value="senior">長く働ける</option><option value="team">チームワーク</option><option value="std" selected="selected">希望条件</option><option value="new">新着</option></select>
                        </div>
                    </form>
                                    </header>


<div class="sortTabWrapper-jobList"><ul class="sortTab-jobList fs-14"><li class="sortTab-jobList_item"><a href="/job_search_result?kt=Golang&amp;u=std&amp;page=1" class="sortTab-jobList_link sortTab-jobList_link-current">希望条件</a></li><li class="sortTab-jobList_item"><a href="/job_search_result?kt=Golang&amp;u=new&amp;page=1" class="sortTab-jobList_link">新着</a></li><li class="sortTab-jobList_item"><a href="/job_search_result?kt=Golang&amp;u=total&amp;page=1" class="sortTab-jobList_link">ランキング</a></li></ul></div>
                        </div>
            <div id="contents">                                    <div class="o-h">            <div class="mt-10 o-h">
                                                                </div>

<article class="break-word borderGray mt-20">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000qqgTo" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社モンスターラボ</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="モンスターラボのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 1x, https://image.vorkers.com/resize/105x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star7"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.72
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000qqgTo"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000qqgTo/recruit?j=4dbb63e0b10560c9"
                       target="_blank">
                        <span class="pcIcon-blank_border">サービス開発プロジェクトマネージャー</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/47620/job_offer/17927.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">…するプロジェクトに携わることができます。

◆開発環境一例
言語　　　　　　：Java, PHP, Ruby, <b>Golang</b>, JavaScript, TypeScript, HTML, CSS, Swift, Kotlin, Flutter
フレームワーク　：React, Vue.JS, Node.JS, Laravel, Ruby on Rails, Spring boot
環境　　　　　　：AWS, Azure, GCP
データベース　　：RDB, NoSQL
プロジェクト管理：JIRA,</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 490万～1000万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモートメイン
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">21日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000qqgTo/recruit?j=4dbb63e0b10560c9"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000sgO4l" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">freee株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="freeeのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/51865-94e6e349660ee65984029c0b9353d078.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/51865-94e6e349660ee65984029c0b9353d078.png 1x, https://image.vorkers.com/resize/105x-/logo/company/51865-94e6e349660ee65984029c0b9353d078.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/51865-94e6e349660ee65984029c0b9353d078.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star3"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                4.29
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000sgO4l"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000sgO4l/recruit?j=f0784f078d4bd92f"
                       target="_blank">
                        <span class="pcIcon-blank_border">シニアクレジットカード事業開発エンジニア</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/51865/job_offer/20961.jpg" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">…d」の開発に携わっていただきます。

PM・UXとチームを組み、プロダクト開発を行っていただきます（スクラム）
<b>Golang</b> / Ruby on Rails / Reactを用いてバックエンド、フロントエンド、インフラなどを問わず、広くサービス開発に携わっていただきます
グロースフェーズにあるプロダクトであり、ビジネスサイドからのフィードバックを受けながら、プロダクトマーケットフィットを目指して機能追加や改善を行っていただきます</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 500万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000sgO4l/recruit?j=f0784f078d4bd92f"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000001KAOkW" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">デロイト トーマツ サイバー合同会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="デロイト トーマツ サイバー合同会社のロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/147680-8044d31cbec6a8c2c0228ab3a983eba1.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/147680-8044d31cbec6a8c2c0228ab3a983eba1.png 1x, https://image.vorkers.com/resize/105x-/logo/company/147680-8044d31cbec6a8c2c0228ab3a983eba1.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/147680-8044d31cbec6a8c2c0228ab3a983eba1.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                4.00
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000001KAOkW"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">ITコンサルタント・システムコンサルタント</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="mark-gold mark-small mr-5 mb-5">NEW</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000001KAOkW/recruit_agent?j=5e2512e5695a496b6c"
                       target="_blank">
                        <span class="pcIcon-blank_border">Anti-Fraud Consultant Quality Assurance Platform  /Quality Cross-Validation</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">There are two major functions of quality engineering which the candidate may select:

• Platform:
o The engineer will be expected to create, track, report and execute test cases, for the platform or client dependences to maximize high SLO’s such as 9</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    別途ご案内いたします。
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモートメイン
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">3日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C1000001KAOkW/recruit_agent?j=5e2512e5695a496b6c"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000xAV2w" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">ロゴスウェア株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="ロゴスウェアのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/68992-d8439c386b118c1a7ac509f82c5683ae.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/68992-d8439c386b118c1a7ac509f82c5683ae.png 1x, https://image.vorkers.com/resize/105x-/logo/company/68992-d8439c386b118c1a7ac509f82c5683ae.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/68992-d8439c386b118c1a7ac509f82c5683ae.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star0"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                2.99
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000xAV2w"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">社内SE</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="mark-gold mark-small mr-5 mb-5">NEW</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000xAV2w/recruit_agent?j=739377134fafacdfda"
                       target="_blank">
                        <span class="pcIcon-blank_border">【Python/Go】社内SE◆経理系システムの企画開発◆</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">自社内の経理部門・営業部門で利用する業務システムの開発・構築・運用保守をご担当いただきます。経営に直結する社内のDX対応を、リーダーシップをもって推進していく人材を募集します。現在社内では顧客案件の見積り・請求を管理する自社開発のシステムが稼働しています。管理部門だけでなく、他部署のメンバーも利用するため、使いやすさに加えいかに効率よく業務を進められるかが課題になっています。

【業務内容】
■上記管理業務系システムの運用保守および機能改善
■システム化が未整備な領域の新たなシステム化（自社開発</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    別途ご案内いたします。
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    茨城県
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">2日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C1000000xAV2w/recruit_agent?j=739377134fafacdfda"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C10000015KqfW" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">GROOVE X株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="GROOVE Xのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/118308-5af65fe90a1d5d26d376e292ed03ba6f.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/118308-5af65fe90a1d5d26d376e292ed03ba6f.png 1x, https://image.vorkers.com/resize/105x-/logo/company/118308-5af65fe90a1d5d26d376e292ed03ba6f.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/118308-5af65fe90a1d5d26d376e292ed03ba6f.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star0"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.02
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C10000015KqfW"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（制御・組込み系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="mark-gold mark-small mr-5 mb-5">NEW</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C10000015KqfW/recruit_agent?j=54caa09cdeca670acb"
                       target="_blank">
                        <span class="pcIcon-blank_border">グラフィックスエンジニア（家庭用ロボット／目のレンダリング）</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">…発言語
　・目のディスプレイの描画に関係するソフトウェア: C++、Python3
　・関連するソフトウェア: <b>Golang</b>、JavaScript
・グラフィックス処理のプラットフォーム：OpenGL、EGL、X
・データベース：Redis、 BigQuery　・インフラ：GCP、Docker
・その他ツール：GitHub、Slack、CircleCI、ovice、esa</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 450万〜1000万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">3日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C10000015KqfW/recruit_agent?j=54caa09cdeca670acb"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000vBCPh" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社PKSHA Technology</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="PKSHA Technologyのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1x, https://image.vorkers.com/resize/105x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star4"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.44
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000vBCPh"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000vBCPh/recruit?j=647f15442b0fbf87"
                       target="_blank">
                        <span class="pcIcon-blank_border">エンジニアリングマネージャー【AlgorithmSolution】</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/69457/job_offer/20039.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">PKSHA Technologyは「未来のソフトウェアを形にする」をミッションに掲げています。
2012年の創業以来、ミッションの達成に向けて2000を超える企業に160以上のアルゴリズム・AI SaaSを導入し、1日930万人以上のユーザーに利用されています。

私達と一緒に、未来のソフトウエアを形にして、人とソフトウエアの共進化を進めていきたい、そのような方をお待ちしています。

【仕事内容】
PKSHA Technologyでは、多岐に渡る大手企業に、自然言語処理・画像認識・音声認識・予測</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 600万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモート可
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000vBCPh/recruit?j=647f15442b0fbf87"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000vArK5" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社ヤプリ</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="ヤプリのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/69336-85b31c4e1daecf4a4f565881ba51903d.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/69336-85b31c4e1daecf4a4f565881ba51903d.png 1x, https://image.vorkers.com/resize/105x-/logo/company/69336-85b31c4e1daecf4a4f565881ba51903d.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/69336-85b31c4e1daecf4a4f565881ba51903d.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star4"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.36
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000vArK5"></span>
        </div>
                </div>
    <p class="f-l lh-high">インターネット業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="mark-gold mark-small mr-5 mb-5">NEW</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000vArK5/recruit_agent?j=316b1e710f579355f0"
                       target="_blank">
                        <span class="pcIcon-blank_border">【リモート】サーバーサイドエンジニア／404597504</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">…びCMSの機能開発、改善を行います。

＜具体的には＞
・CMSおよびネイティブアプリ向けAPIの開発（PHP、<b>Golang</b>）
・コンテンツ管理画面（CMS）のフロントエンド実装（TypeScript,、Nuxt.js／Vue.js）
・安定的にサービスを提供できるための改善
・クライアントからの要望に応じた機能開発 ・新しい技術の検証や活用、サイトパフォーマンスのチューニング等
・サービスの品質向上や業務効率化のための提案、実施

◇◆開発環境・体制について◆◇
既存システムの技術スタックに縛</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 500万〜800万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモートメイン
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">11日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C1000000vArK5/recruit_agent?j=316b1e710f579355f0"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000lN4kl" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">GMOフィナンシャルホールディングス株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="GMOフィナンシャルホールディングスのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/19444-8a32f14071518a648b160d51c6d1ba74.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/19444-8a32f14071518a648b160d51c6d1ba74.png 1x, https://image.vorkers.com/resize/105x-/logo/company/19444-8a32f14071518a648b160d51c6d1ba74.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/19444-8a32f14071518a648b160d51c6d1ba74.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star9"></span>
    <span class="icon-star icon-star-big icon-star0"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                2.86
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000lN4kl"></span>
        </div>
                </div>
    <p class="f-l lh-high">商品取引業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000lN4kl/recruit?j=c3619383a9fd902c"
                       target="_blank">
                        <span class="pcIcon-blank_border">オープン・エントリー（バックエンドエンジニア）</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">…お待ちしております。

・技術検証、選定
・アプリケーションの設計、開発、テスト（開発エンジニア）
・Java、<b>Golang</b>を使った金融取引システムの開発
・システムのアラートや問合せ調査／障害対応

また、経験・能力に応じてプレーイングマネージャーとして以下を担当。
・ビジネス要求の分析（ビジネス部門との折衝）
・品質、運用保守等の観点も踏まえたシステム要件の取りまとめ（開発案件のマネジメント）
・業務の効率化／自動化の推進（CI/CD環境を含む開発環境の維持管理、SETによる品質維持管理）</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 500万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモート不可
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000lN4kl/recruit?j=c3619383a9fd902c"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C10000011ECFk" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">アルサーガパートナーズ株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="アルサーガパートナーズのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/77462-738a12f6e8f6db188cd50273d52824a9.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/77462-738a12f6e8f6db188cd50273d52824a9.png 1x, https://image.vorkers.com/resize/105x-/logo/company/77462-738a12f6e8f6db188cd50273d52824a9.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/77462-738a12f6e8f6db188cd50273d52824a9.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star9"></span>
    <span class="icon-star icon-star-big icon-star0"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                2.90
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C10000011ECFk"></span>
        </div>
                </div>
    <p class="f-l lh-high">インターネット業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="mark-gold mark-small mr-5 mb-5">NEW</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C10000011ECFk/recruit_agent?j=d444110b6d9a59cb26"
                       target="_blank">
                        <span class="pcIcon-blank_border">【東京】インフラエンジニア</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">…多様な案件をいただいております！
言語・フレームワーク
【 開発環境 】
◆開発言語:PHP, Elixir, <b>Golang</b>
◆フレームワーク:Laravel, Phoenix
◆DB:MySQL
◆インフラ:AWS
◆ツール:Docker,Terraform,Git
◆OS:Linux</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    別途ご案内いたします。
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモート可
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">3日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C10000011ECFk/recruit_agent?j=d444110b6d9a59cb26"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0910000000G2I3" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社ベイシア</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="ベイシアのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/7164-90a4ff2b226e92e2a8fbb6ad42846d07.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/7164-90a4ff2b226e92e2a8fbb6ad42846d07.png 1x, https://image.vorkers.com/resize/105x-/logo/company/7164-90a4ff2b226e92e2a8fbb6ad42846d07.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/7164-90a4ff2b226e92e2a8fbb6ad42846d07.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star9"></span>
    <span class="icon-star icon-star-big icon-star0"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                2.85
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0910000000G2I3"></span>
        </div>
                </div>
    <p class="f-l lh-high">小売（百貨店・専門・CVS・量販店）業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0910000000G2I3/recruit_agent?j=aa4b7067c3d7538103"
                       target="_blank">
                        <span class="pcIcon-blank_border">【リモート】アプリエンジニア（フルスタックエンジニア）／403798540</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">…装、テスト、リリースまでのすべての工程に関わって頂きます。 

環境：アプリ開発：Flutter
バックエンド：<b>Golang</b>、CMS：React＋<b>Golang</b>、クラウド：AWS 

＜同社独自の取り組み＞
デジタル人材を迎えるために、独自の人事制度（1国2制度）を導入しています。従来の就業体系（総合職）と異なる、専門職独自の年間休日の改定とジョブ型給与テーブルを設計。フルリモートワークの推奨や、オフィスを表参道に新設するなどし、エンジニアの方が働きやすい仕組みを整えています。

＜同社について＞</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 700万〜900万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    群馬県
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">15日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0910000000G2I3/recruit_agent?j=aa4b7067c3d7538103"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0910000000FrzR" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社日立ソリューションズ</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="日立ソリューションズのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/3713-7a9a7b08a387f92ec0a9961dc257cdd2.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/3713-7a9a7b08a387f92ec0a9961dc257cdd2.png 1x, https://image.vorkers.com/resize/105x-/logo/company/3713-7a9a7b08a387f92ec0a9961dc257cdd2.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/3713-7a9a7b08a387f92ec0a9961dc257cdd2.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star5"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.54
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0910000000FrzR"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0910000000FrzR/recruit_agent?j=9b37e9861793295875"
                       target="_blank">
                        <span class="pcIcon-blank_border">■【横浜】日立を代表するオープンミドルウェアの製品開発＜統合管理ソリューション部＞</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">当社は、日立グループのITセクターの中核を担う企業として、人々の社会生活や企業活動を支える最先端の技術や製品、サービスを柔軟に組み合わせたソリューションを展開しております。今回募集する部門は、日立を代表するオープンミドルウェア製品の統合管理領域の製品開発をミッションとしています。日本のDX化、デジタルシフト進み、従来型のオンプレ環境型製品が減少し、クラウドシフトが鮮明になっています。IT基盤の進化に合わせた製品開発が急務となっており、組織強化を行なうための採用を実施します。
携わっていただくミド</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 450万〜800万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    神奈川県
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">16日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0910000000FrzR/recruit_agent?j=9b37e9861793295875"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000001Nl3PQ" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">SEQSENSE株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="SEQSENSEのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/151052-3287f885841b8875d696c69f816ea134.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/151052-3287f885841b8875d696c69f816ea134.png 1x, https://image.vorkers.com/resize/105x-/logo/company/151052-3287f885841b8875d696c69f816ea134.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/151052-3287f885841b8875d696c69f816ea134.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star2"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.18
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000001Nl3PQ"></span>
        </div>
                </div>
    <p class="f-l lh-high">機械関連業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000001Nl3PQ/recruit_agent?j=003d75573e0cb885b7"
                       target="_blank">
                        <span class="pcIcon-blank_border">■【東京】バックエンドエンジニア＜社会インフラに実装する最先端の自律移動型ロボット開発＞</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">…ド開発◆Ruby on Rails、Python、PostgreSQL、Redisを利用したWebAPI開発
◆<b>Golang</b>、gRPCを利用した利用した非同期処理システムやサービス間通信システムの開発
※明治大学教授発のスタートアップ企業／世界でも最先端の技術を持つ精鋭集団／人口減少やオリンピックを背景に警備ロボットの需要急拡大中／「実社会の役に立つロボットを世の中に」という熱い社員たちの想い／ロボットと人間の共存を実現できる仕事へ／三菱地所、TIS等からも出資を受ける注目企業の中核業務</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 600万〜1000万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">16日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C1000001Nl3PQ/recruit_agent?j=003d75573e0cb885b7"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000shAEH" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社スマートドライブ</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="スマートドライブのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/52037-17dc48d02a2676713cd49044d745f591.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/52037-17dc48d02a2676713cd49044d745f591.png 1x, https://image.vorkers.com/resize/105x-/logo/company/52037-17dc48d02a2676713cd49044d745f591.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/52037-17dc48d02a2676713cd49044d745f591.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star1"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.09
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000shAEH"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000shAEH/recruit_agent?j=9122155249d853c8d7"
                       target="_blank">
                        <span class="pcIcon-blank_border">■【東京】バックエンドエンジニア＜車社会の未来を変える事業に貢献/モビリティテックベンチャー＞</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription"><b>Golang</b>、RailsによるAPIサーバーの開発・運用、各種非同期処理部分の開発・運用をメインの業務としてご担当頂きます。◆DataPlatform業務…自社／3rdparty問わず、様々なIoTデバイスから最初にデータを受け取る部分に始まり、集めたデータを正確にストアしつつ、さまざまな補正処理や解析処理のフローを実行しています。日々増加するデータを適切に処理しつづけること、また、将来を見据えた継続的なアーキテクチャのリデザイン、よりよいコスト・パフォーマンスな技術をリサーチ・選定し続けていた</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 500万〜900万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">16日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C1000000shAEH/recruit_agent?j=9122155249d853c8d7"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C3000000EoxL9" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">AZAPA株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="AZAPAのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/23072-f088691525d2871352c2954cad1f1016.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/23072-f088691525d2871352c2954cad1f1016.png 1x, https://image.vorkers.com/resize/105x-/logo/company/23072-f088691525d2871352c2954cad1f1016.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/23072-f088691525d2871352c2954cad1f1016.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star0"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                2.98
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C3000000EoxL9"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C3000000EoxL9/recruit_agent?j=823f389b0176a760cd"
                       target="_blank">
                        <span class="pcIcon-blank_border">【リモート勤務可】Web開発エンジニア</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">【業務】モビリティのUI/UXやコネクティッド領域、遠隔操作システムなどの開発【詳細】以下の何れかの業務を想定
■ディスプレイ領域（車両内外問わず）のUX／UIシステム開発。顕在化していないニーズを深掘りしながら、クライアント企業の真の課題を紐解き、最適なUX／UIを提案し、スピード感を持って実装
■モビリティ内部の情報（CANやセンサーデータ等）を取得しクラウド（主にAWS）へアップロードし、アップロードされたデータの視覚化（UX／UI）や、機械学習等を利用したデータの分析業務
■モビリティの</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 500万〜1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    愛知県
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">16日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C3000000EoxL9/recruit_agent?j=823f389b0176a760cd"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000qqgTo" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社モンスターラボ</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="モンスターラボのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 1x, https://image.vorkers.com/resize/105x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star7"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.72
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000qqgTo"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000qqgTo/recruit?j=1b604ab0bfc73d0b"
                       target="_blank">
                        <span class="pcIcon-blank_border">サービス開発ソリューションアーキテクト</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/47620/job_offer/17938.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">…X Blog

■開発環境一例 
フロントエンド：TypeScript, Javascript 
バックエンド：<b>Golang</b>, Ruby, Node.js, Java, PHP 
モバイル：Flutter, Kotlin, Swift 
フレームワーク：React, Vue.js, Node.js, Ruby on rails, Laravel, Spring boot 
パブリッククラウド：AWS, Azure, GCP 
データベース：RDB, NoSQL 
プロジェクト管理：JIRA, C</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 560万～882万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモートメイン
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">21日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000qqgTo/recruit?j=1b604ab0bfc73d0b"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000qqgTo" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社モンスターラボ</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="モンスターラボのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 1x, https://image.vorkers.com/resize/105x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star7"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.72
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000qqgTo"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">品質管理・テスティング・QA</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000qqgTo/recruit?j=88e87409074f48aa"
                       target="_blank">
                        <span class="pcIcon-blank_border">サービス開発QAリード/マネージャー</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/47620/job_offer/17940.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">…: GitHub

■開発環境一例
フロントエンド：TypeScript, Javascript
バックエンド：<b>Golang</b>, Ruby, Node.js, Java, PHP
モバイル：Flutter, Kotlin, Swift
フレームワーク：React, Vue.js, Node.js, Ruby on rails, Laravel,Spring boot
パブリッククラウド：AWS, Azure, GCP
データベース：RDB, NoSQL
デザイン：Figma, Adobe XD, </p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 600万～900万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモートメイン
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">21日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000qqgTo/recruit?j=88e87409074f48aa"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000qqgTo" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社モンスターラボ</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="モンスターラボのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 1x, https://image.vorkers.com/resize/105x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/47620-c35a54358a24441edfaeea3161e64cfa.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star7"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.72
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000qqgTo"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000qqgTo/recruit?j=80cf46313fa5a2b7"
                       target="_blank">
                        <span class="pcIcon-blank_border">サービス開発テックリード：フルスタックエンジニア</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/47620/job_offer/17951.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">…英語力は不要です)

■開発環境一例
フロントエンド：TypeScript,Javascript
バックエンド：<b>Golang</b>,Ruby,Node.js,Java,PHP
モバイル：Flutter,Kotlin,Swift
フレームワーク：React,Vue.js,Node.js,Ruby on rails,Laravel,Spring boot
パブリッククラウド：AWS, Azure, GCP
データベース　　：RDB, NoSQL
プロジェクト管理：JIRA,Confluence, Back</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 500万～900万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモートメイン
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">21日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000qqgTo/recruit?j=80cf46313fa5a2b7"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000sgO4l" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">freee株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="freeeのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/51865-94e6e349660ee65984029c0b9353d078.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/51865-94e6e349660ee65984029c0b9353d078.png 1x, https://image.vorkers.com/resize/105x-/logo/company/51865-94e6e349660ee65984029c0b9353d078.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/51865-94e6e349660ee65984029c0b9353d078.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star3"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                4.29
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000sgO4l"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000sgO4l/recruit?j=8bd9fdba2ca1fa3e"
                       target="_blank">
                        <span class="pcIcon-blank_border">クレジットカード事業開発エンジニア</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/51865/job_offer/20960.jpg" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">…d」の開発に携わっていただきます。

PM・UXとチームを組み、プロダクト開発を行っていただきます（スクラム）
<b>Golang</b> / Ruby on Rails / Reactを用いてバックエンド、フロントエンド、インフラなどを問わず、広くサービス開発に携わっていただきます
グロースフェーズにあるプロダクトであり、ビジネスサイドからのフィードバックを受けながら、プロダクトマーケットフィットを目指して機能追加や改善を行っていただきます</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 500万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000sgO4l/recruit?j=8bd9fdba2ca1fa3e"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000xAV2w" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">ロゴスウェア株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="ロゴスウェアのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/68992-d8439c386b118c1a7ac509f82c5683ae.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/68992-d8439c386b118c1a7ac509f82c5683ae.png 1x, https://image.vorkers.com/resize/105x-/logo/company/68992-d8439c386b118c1a7ac509f82c5683ae.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/68992-d8439c386b118c1a7ac509f82c5683ae.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star0"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                2.99
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000xAV2w"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">社内SE</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="mark-gold mark-small mr-5 mb-5">NEW</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000xAV2w/recruit_agent?j=fd42a8dae8e1319772"
                       target="_blank">
                        <span class="pcIcon-blank_border">バックエンドエンジニア【自社製品Libra・Platon】</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">…同社は製品ごとに使用言語が異なりますが、主に以下のような技術を使って開発を進めています。

言語：Python、<b>Golang</b>、PHP
フレームワーク：Django（Python）
DB ：MySQL、PostgreSQL
サーバー：Linux
■おすすめポイント
◆同社は自社製品であるeラーニング、デジタルライブラリ、オンラインLIVEセミナー等のソフトウェアを企画・開発、販売しています。
　あなたのアイディアが製品を創り、「企業の教育」を変えていきます。</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    別途ご案内いたします。
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    茨城県
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">2日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C1000000xAV2w/recruit_agent?j=fd42a8dae8e1319772"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C10000015KqfW" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">GROOVE X株式会社</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="GROOVE Xのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/118308-5af65fe90a1d5d26d376e292ed03ba6f.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/118308-5af65fe90a1d5d26d376e292ed03ba6f.png 1x, https://image.vorkers.com/resize/105x-/logo/company/118308-5af65fe90a1d5d26d376e292ed03ba6f.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/118308-5af65fe90a1d5d26d376e292ed03ba6f.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star0"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.02
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C10000015KqfW"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（制御・組込み系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="mark-gold mark-small mr-5 mb-5">NEW</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_agent pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C10000015KqfW/recruit_agent?j=52adfe857744174aec"
                       target="_blank">
                        <span class="pcIcon-blank_border">サウンドエンジニア（家庭用ロボット／声の生成ソフトウェア開発）</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                                    <p class="jobListJobDescription">…・開発環境】
・OS：Ubuntu(Linux)
・開発言語：C++、Python3　※関連するソフトウェア: <b>Golang</b>、 JavaScript
・データベース：Redis、BigQuery
・インフラ：GCP、Docker
・その他ツール：GitHub、Slack、CircleCI、ovice、 esa</p>
                                                    <table class="table-job">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 450万〜1000万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">3日前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_agent button button-usuallyBlue fs-16 w-250" href="/a0C10000015KqfW/recruit_agent?j=52adfe857744174aec"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000vBCPh" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社PKSHA Technology</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="PKSHA Technologyのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1x, https://image.vorkers.com/resize/105x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star4"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.44
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000vBCPh"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000vBCPh/recruit?j=b5b6f4dc86381e4d"
                       target="_blank">
                        <span class="pcIcon-blank_border">エンジニアリングマネージャー【AI SaaS】</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/69457/job_offer/20046.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">PKSHA Technologyは「未来のソフトウェアを形にする」をミッションに掲げています。
2012年の創業以来、ミッションの達成に向けて2000を超える企業に160以上のアルゴリズム・AI SaaSを導入し、1日930万人以上のユーザーに利用されています。

私達と一緒に、未来のソフトウエアを形にして、人とソフトウエアの共進化を進めていきたい、そのような方をお待ちしています。

【仕事内容】
PKSHA Technologyは、エンタープライズ企業のコールセンターに向けた自然言語処理/機械</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 600万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモート可
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000vBCPh/recruit?j=b5b6f4dc86381e4d"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000vBCPh" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社PKSHA Technology</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="PKSHA Technologyのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1x, https://image.vorkers.com/resize/105x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star4"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.44
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000vBCPh"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000vBCPh/recruit?j=f810587bf673c35b"
                       target="_blank">
                        <span class="pcIcon-blank_border">SRE【AI SaaS】</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/69457/job_offer/20048.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">PKSHA Technologyは「未来のソフトウェアを形にする」をミッションに掲げています。
2012年の創業以来、ミッションの達成に向けて2000を超える企業に160以上のアルゴリズム・AI SaaSを導入し、1日930万人以上のユーザーに利用されています。

私達と一緒に、未来のソフトウエアを形にして、人とソフトウエアの共進化を進めていきたい、そのような方をお待ちしています。

【仕事内容】
PKSHA Technologyは、エンタープライズ企業のコールセンターに向けた自然言語処理/機械</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 600万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモート可
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000vBCPh/recruit?j=f810587bf673c35b"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000vBCPh" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社PKSHA Technology</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="PKSHA Technologyのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1x, https://image.vorkers.com/resize/105x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star4"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.44
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000vBCPh"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000vBCPh/recruit?j=295727bce1f429ef"
                       target="_blank">
                        <span class="pcIcon-blank_border">ソフトウェアエンジニア【AlgorithmSolution】</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/69457/job_offer/20050.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">PKSHA Technologyは「未来のソフトウェアを形にする」をミッションに掲げています。
2012年の創業以来、ミッションの達成に向けて2000を超える企業に160以上のアルゴリズム・AI SaaSを導入し、1日930万人以上のユーザーに利用されています。

私達と一緒に、未来のソフトウエアを形にして、人とソフトウエアの共進化を進めていきたい、そのような方をお待ちしています。

【仕事内容】
多岐に渡る大手企業に、自然言語処理・画像認識・音声認識・予測・数理最適化等の領域で、機械学習・深層</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 600万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモート可
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000vBCPh/recruit?j=295727bce1f429ef"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000vBCPh" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社PKSHA Technology</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="PKSHA Technologyのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1x, https://image.vorkers.com/resize/105x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star4"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.44
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000vBCPh"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000vBCPh/recruit?j=c12cd7a1fe21350b"
                       target="_blank">
                        <span class="pcIcon-blank_border">ソフトウェアエンジニア【AI SaaS】</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/69457/job_offer/20052.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">PKSHA Technologyは「未来のソフトウェアを形にする」をミッションに掲げています。
2012年の創業以来、ミッションの達成に向けて2000を超える企業に160以上のアルゴリズム・AI SaaSを導入し、1日930万人以上のユーザーに利用されています。

私達と一緒に、未来のソフトウエアを形にして、人とソフトウエアの共進化を進めていきたい、そのような方をお待ちしています。

【仕事内容】
PKSHA Technologyは、エンタープライズ企業のコールセンターに向けた自然言語処理/機械</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 600万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモート可
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000vBCPh/recruit?j=c12cd7a1fe21350b"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>

<article class="break-word borderGray mt-50">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000vBCPh" target="_blank"
               class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18"
               data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company"
               data-_v-event-logger-multi>
                <span class="pcIcon-blank_border">株式会社PKSHA Technology</span>
            </a>
        </h4>
        <div class="jobCompanyLogoArea-header">
            <img class="companyLogoImage-space" alt="PKSHA Technologyのロゴ" src="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png" srcset="https://image.vorkers.com/resize/70x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1x, https://image.vorkers.com/resize/105x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 1.5x, https://image.vorkers.com/resize/140x-/logo/company/69457-f9214a143a7683eb45fab3d9fb60a2a5.png 2x">
        </div>
    </div>
    <div class="pt-5">
        <div class="lh-1o3 mr-5 pb-5 d-ib">
            <p class="totalEvaluation_item v-m">
                    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star10"></span>
    <span class="icon-star icon-star-big icon-star4"></span>
    <span class="icon-star icon-star-big icon-star0"></span>

            </p>
            <p class="totalEvaluation_item fs-15 fw-b v-b">
                3.44
            </p>
            <span class="jsLabelKeywordMatching p-r v-b ml-5" data-master-id="a0C1000000vBCPh"></span>
        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">システム開発（WEB・オープン系）</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000vBCPh/recruit?j=6266c3e70d03671b"
                       target="_blank">
                        <span class="pcIcon-blank_border">ソフトウェアエンジニア【MaaS】</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/69457/job_offer/20054.png" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">PKSHA Technologyは「未来のソフトウェアを形にする」をミッションに掲げています。
2012年の創業以来、ミッションの達成に向けて2000を超える企業に160以上のアルゴリズム・AI SaaSを導入し、1日930万人以上のユーザーに利用されています。

私達と一緒に、未来のソフトウエアを形にして、人とソフトウエアの共進化を進めていきたい、そのような方をお待ちしています。

【仕事内容】
MaaS領域におけるアルゴリズムの社会実装に向けてIoT機器の開発や、コンピュータビジョン技術・深</p>
                                                    <table class="table-job w-650">
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    給与
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    年収 600万～1200万円
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    勤務地
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    東京都
                                </td>
                            </tr>
                                                    <tr>
                                <th class="table-job_tableHeader pt-10 pb-10">
                                    リモートワーク
                                </th>
                                <td class="table-job_tableData pt-10 pb-10">
                                    リモート可
                                </td>
                            </tr>
                                            </table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
                <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b"
       class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key=job_search_result_standard_click data-_v-event-logger-parameter=bookmark_job_offer_no_login data-_v-event-logger-multi>
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000vBCPh/recruit?j=6266c3e70d03671b"
                   target="_blank"><span
                            class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>
            <div class="mt-50 pb-20">
            <div class="paging">
        <p class="d-ib mb-10">全109件中の1～25件</p>
    <ul class="d-ib">
                <li class="d-i">
            <ol class="d-i">
                                                            <li class="paging_item"><span class="paging_item-current">1</span></li>
                                                                                <li class="paging_item">
                            <a href="/job_search_result?kt=Golang&amp;u=std&amp;page=2" class="paging_link-item">2</a>
                        </li>
                                                                                <li class="paging_item">
                            <a href="/job_search_result?kt=Golang&amp;u=std&amp;page=3" class="paging_link-item">3</a>
                        </li>
                                                                                <li class="paging_item">
                            <a href="/job_search_result?kt=Golang&amp;u=std&amp;page=4" class="paging_link-item">4</a>
                        </li>
                                                                                <li class="paging_item">
                            <a href="/job_search_result?kt=Golang&amp;u=std&amp;page=5" class="paging_link-item">5</a>
                        </li>
                                                </ol>
        </li>
                    <li class="d-i">
                <a href="/job_search_result?kt=Golang&amp;u=std&amp;page=2" class="paging_link-more">次へ</a>
            </li>
            </ul>
</div>        </div></div>

    <div class="goTop">
    <a href="#top" class="jsGoTopLink">▲ このページのTOPへ</a>
</div>
            </div>        </main>

                <footer id="footer">
    <a class="footer_siteLogoLink" href="/">
        <img class="d-b" width="140" height="22" src="https://assets.vorkers.com/images/common/logo_with_icon.svg?01" alt="OpenWork">
    </a>
    <ul id="footerMenu">
        <li class="footerMenu_item"><a class="footerMenu_link" href="/guide">ご利用案内</a></li><!--
        --><li class="footerMenu_item"><a class="footerMenu_link" href="/policy.php">運営ポリシー</a></li><!--
        --><li class="footerMenu_item"><a class="footerMenu_link" href="https://www.openwork.co.jp/">運営会社</a></li><!--
        --><li class="footerMenu_item"><a class="footerMenu_link" href="/rule.php">利用規約</a></li><!--
        --><li class="footerMenu_item"><a class="footerMenu_link" href="/privacy.php">プライバシーポリシー</a></li><!--
        --><li class="footerMenu_item"><a class="footerMenu_link" href="/ad_info">求人掲載</a></li><!--
        --><li class="footerMenu_item"><a class="footerMenu_link" href="/contact_top.php">ヘルプ</a></li><!--
        --><li class="footerMenu_item footerMenu_item-last"><a class="footerMenu_link" href="/sitemap.php">サイトマップ</a></li>
    </ul>
    <p><small class="copyright">Copyright &copy; 2023 OpenWork Inc. All rights reserved.</small></p>
</footer>

    </div>

                        <div id="jsOccupationModal" class="d-n">
            <aside class="modalWindow-job jsModalWindow d-n" tabindex="0">
    <div class="modalWindow_detail jsModalWindowDetail"><h3 class="modalWindow_title pb-10 jsModalContentTop">職種を絞り込む</h3>
<div class="o-h borderGray jsScrollBoxContainer">
    <div class="scrollBox f-l w-360 jsScrollBox jsScrollSelectParent">
        <ul>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent scrollBox_anchor-current">
                        営業
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        管理・事務
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        経営・事業企画
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        マーケティング
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        ITエンジニア
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        機械・電気・電子・半導体（技術職）
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        化学・繊維・食品（技術職）
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        建築・土木・設備（技術職）
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        メディカル（専門職）
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        金融（専門職）
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        不動産（専門職）
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        コンサルタント・専門職
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        クリエイティブ
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                            <li>
                    <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                        サービス・小売・運輸・その他
                        <span class="scrollBox_mark d-n jsSelectCount"></span>
                    </a>
                </li>
                    </ul>
    </div>
    <div class="scrollBox borderGray-left jsScrollBox jsScrollChildrenArea">
                    <div class=" jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-550" 
                        data-_v-parent-id="550" 
                        data-_v-parent-name="営業">
                        営業 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-567" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="567" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="法人営業">法人営業
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-568" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="568" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="個人営業">個人営業
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-565" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="565" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="カウンターセールス・内勤営業">カウンターセールス・内勤営業
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-554" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="554" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="代理店営業">代理店営業
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-555" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="555" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="海外営業">海外営業
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-569" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="569" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="カスタマーサクセス">カスタマーサクセス
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-556" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="556" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="営業企画・営業管理職">営業企画・営業管理職
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-553" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="553" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="MR・医療関連営業">MR・医療関連営業
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-566" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="566" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="その他（営業）">その他（営業）
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-500" 
                        data-_v-parent-id="500" 
                        data-_v-parent-name="管理・事務">
                        管理・事務 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-501" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="501" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="総務">総務
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-502" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="502" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="人事・労務">人事・労務
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-503" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="503" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="法務">法務
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-504" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="504" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="内部監査">内部監査
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-505" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="505" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="特許・知的財産">特許・知的財産
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-507" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="507" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="経理・会計・財務">経理・会計・財務
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-508" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="508" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="IR">IR
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-509" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="509" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="広報">広報
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-514" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="514" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="資材購買・調達">資材購買・調達
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-511" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="511" 
                                data-_v-child-sort="9" 
                                data-_v-child-name="物流">物流
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-510" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="510" 
                                data-_v-child-sort="10" 
                                data-_v-child-name="国際業務・貿易事務">国際業務・貿易事務
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-512" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="512" 
                                data-_v-child-sort="11" 
                                data-_v-child-name="秘書">秘書
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-513" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="513" 
                                data-_v-child-sort="12" 
                                data-_v-child-name="一般事務・営業事務">一般事務・営業事務
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-515" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="515" 
                                data-_v-child-sort="13" 
                                data-_v-child-name="医療事務">医療事務
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-516" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="516" 
                                data-_v-child-sort="14" 
                                data-_v-child-name="受付">受付
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-400" 
                        data-_v-parent-id="400" 
                        data-_v-parent-name="経営・事業企画">
                        経営・事業企画 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-401" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="401" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="経営者・CEO・COO">経営者・CEO・COO
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-402" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="402" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="経営企画・戦略">経営企画・戦略
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-403" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="403" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="事業企画・統括">事業企画・統括
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-408" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="408" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="新規事業企画・事業開発">新規事業企画・事業開発
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-406" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="406" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="CIO・CTO">CIO・CTO
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-407" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="407" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="CFO・コントローラー">CFO・コントローラー
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-450" 
                        data-_v-parent-id="450" 
                        data-_v-parent-name="マーケティング">
                        マーケティング すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-454" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="454" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="プロダクトマーケティング・商品企画">プロダクトマーケティング・商品企画
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-451" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="451" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="PR・広告宣伝・販促">PR・広告宣伝・販促
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-452" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="452" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="マーケティングリサーチ">マーケティングリサーチ
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-456" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="456" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="Webマーケティング">Webマーケティング
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-457" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="457" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="バイヤー・マーチャンダイザー">バイヤー・マーチャンダイザー
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-1" 
                        data-_v-parent-id="1" 
                        data-_v-parent-name="ITエンジニア">
                        ITエンジニア すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-34" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="34" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="プロジェクトマネージャー">プロジェクトマネージャー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-11" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="11" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="ITコンサルタント・システムコンサルタント">ITコンサルタント・システムコンサルタント
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-19" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="19" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="システム開発（WEB・オープン系）">システム開発（WEB・オープン系）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-35" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="35" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="システム開発（汎用系）">システム開発（汎用系）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-21" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="21" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="システム開発（制御・組込み系）">システム開発（制御・組込み系）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-36" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="36" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="モバイルアプリエンジニア">モバイルアプリエンジニア
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-23" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="23" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="サーバー設計・構築">サーバー設計・構築
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-24" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="24" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="ネットワーク設計・構築">ネットワーク設計・構築
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-30" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="30" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="セキュリティ設計・構築">セキュリティ設計・構築
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-31" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="31" 
                                data-_v-child-sort="9" 
                                data-_v-child-name="通信インフラ設計・構築">通信インフラ設計・構築
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-26" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="26" 
                                data-_v-child-sort="10" 
                                data-_v-child-name="プリセールス・セールスエンジニア">プリセールス・セールスエンジニア
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-32" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="32" 
                                data-_v-child-sort="11" 
                                data-_v-child-name="品質管理・テスティング・QA">品質管理・テスティング・QA
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-28" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="28" 
                                data-_v-child-sort="12" 
                                data-_v-child-name="テクニカルサポート・運用・保守">テクニカルサポート・運用・保守
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-27" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="27" 
                                data-_v-child-sort="13" 
                                data-_v-child-name="社内SE">社内SE
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-33" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="33" 
                                data-_v-child-sort="14" 
                                data-_v-child-name="データアナリスト・データサイエンティスト">データアナリスト・データサイエンティスト
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-50" 
                        data-_v-parent-id="50" 
                        data-_v-parent-name="機械・電気・電子・半導体（技術職）">
                        機械・電気・電子・半導体（技術職） すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-51" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="51" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="研究開発・企画">研究開発・企画
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-102" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="102" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="製品開発・設計">製品開発・設計
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-52" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="52" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="回路・電機・電機制御設計">回路・電機・電機制御設計
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-110" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="110" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="光学設計">光学設計
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-53" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="53" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="半導体・記録媒体・液晶プロセスエンジニア">半導体・記録媒体・液晶プロセスエンジニア
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-59" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="59" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="パターン・レイアウト設計">パターン・レイアウト設計
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-60" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="60" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="評価・解析・検証">評価・解析・検証
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-54" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="54" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="生産技術・製造技術・エンジニアリング">生産技術・製造技術・エンジニアリング
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-55" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="55" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="生産管理・品質管理・品質保証">生産管理・品質管理・品質保証
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-56" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="56" 
                                data-_v-child-sort="9" 
                                data-_v-child-name="セールス・サポートエンジニア">セールス・サポートエンジニア
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-150" 
                        data-_v-parent-id="150" 
                        data-_v-parent-name="化学・繊維・食品（技術職）">
                        化学・繊維・食品（技術職） すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-151" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="151" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="研究・開発">研究・開発
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-152" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="152" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="生産技術・製造技術・エンジニアリング">生産技術・製造技術・エンジニアリング
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-153" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="153" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="生産管理・品質管理・品質保証">生産管理・品質管理・品質保証
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-154" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="154" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="セールス・サポートエンジニア">セールス・サポートエンジニア
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-200" 
                        data-_v-parent-id="200" 
                        data-_v-parent-name="建築・土木・設備（技術職）">
                        建築・土木・設備（技術職） すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-201" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="201" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="設計・測量・積算（建築）">設計・測量・積算（建築）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-202" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="202" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="施工管理（建築）">施工管理（建築）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-203" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="203" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="保守・メンテナンス（建築）">保守・メンテナンス（建築）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-204" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="204" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="設計・測量・積算（土木）">設計・測量・積算（土木）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-205" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="205" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="施工管理（土木）">施工管理（土木）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-206" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="206" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="保守・メンテナンス（土木）">保守・メンテナンス（土木）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-207" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="207" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="設計・測量・積算（設備）">設計・測量・積算（設備）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-208" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="208" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="施工管理（設備）">施工管理（設備）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-209" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="209" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="保守・メンテナンス（設備）">保守・メンテナンス（設備）
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-250" 
                        data-_v-parent-id="250" 
                        data-_v-parent-name="メディカル（専門職）">
                        メディカル（専門職） すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-251" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="251" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="研究・開発（医薬品）">研究・開発（医薬品）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-252" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="252" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="臨床開発・学術・薬事（医療機器）">臨床開発・学術・薬事（医療機器）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-253" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="253" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="臨床開発・治験（医薬品）">臨床開発・治験（医薬品）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-254" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="254" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="製剤・薬事・学術">製剤・薬事・学術
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-256" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="256" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="生産管理・品質管理・品質保証（医薬品）">生産管理・品質管理・品質保証（医薬品）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-257" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="257" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="セールス・サポートエンジニア（医療機器）">セールス・サポートエンジニア（医療機器）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-258" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="258" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="医師">医師
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-259" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="259" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="薬剤師">薬剤師
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-260" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="260" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="看護師">看護師
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-261" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="261" 
                                data-_v-child-sort="9" 
                                data-_v-child-name="その他メディカル系">その他メディカル系
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-300" 
                        data-_v-parent-id="300" 
                        data-_v-parent-name="金融（専門職）">
                        金融（専門職） すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-304" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="304" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="プライベートバンカー">プライベートバンカー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-305" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="305" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="ファンドマネージャー・ディーラー・トレーダー">ファンドマネージャー・ディーラー・トレーダー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-306" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="306" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="投資研究・アナリスト・エコノミスト・ストラテジスト">投資研究・アナリスト・エコノミスト・ストラテジスト
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-307" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="307" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="M&amp;A・投資銀行部門">M&amp;A・投資銀行部門
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-310" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="310" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="アクチュアリー・クオンツ・金融工学">アクチュアリー・クオンツ・金融工学
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-311" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="311" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="リスク管理・与信管理・債権管理">リスク管理・与信管理・債権管理
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-312" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="312" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="コンプライアンス・内部監査">コンプライアンス・内部監査
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-313" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="313" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="金融事務・バックオフィス">金融事務・バックオフィス
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-320" 
                        data-_v-parent-id="320" 
                        data-_v-parent-name="不動産（専門職）">
                        不動産（専門職） すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-321" 
                                data-_v-parent-index="10" 
                                data-_v-child-id="321" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="アセットマネジメント・プロパティマネジメント">アセットマネジメント・プロパティマネジメント
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-322" 
                                data-_v-parent-index="10" 
                                data-_v-child-id="322" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="鑑定・デューデリジェンス">鑑定・デューデリジェンス
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-323" 
                                data-_v-parent-index="10" 
                                data-_v-child-id="323" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="開発（用地仕入・企画）">開発（用地仕入・企画）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-324" 
                                data-_v-parent-index="10" 
                                data-_v-child-id="324" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="マンション管理・ビル管理">マンション管理・ビル管理
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-350" 
                        data-_v-parent-id="350" 
                        data-_v-parent-name="コンサルタント・専門職">
                        コンサルタント・専門職 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-351" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="351" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="経営・戦略・業務コンサルタント">経営・戦略・業務コンサルタント
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-352" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="352" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="財務・会計コンサルタント">財務・会計コンサルタント
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-353" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="353" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="組織・人事コンサルタント">組織・人事コンサルタント
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-355" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="355" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="物流・SCMコンサルタント">物流・SCMコンサルタント
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-361" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="361" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="生産管理・品質管理コンサルタント">生産管理・品質管理コンサルタント
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-358" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="358" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="弁護士・弁理士">弁護士・弁理士
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-359" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="359" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="会計士・税理士">会計士・税理士
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-362" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="362" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="司法書士・行政書士・社会保険労務士">司法書士・行政書士・社会保険労務士
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-360" 
                                data-_v-parent-index="11" 
                                data-_v-child-id="360" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="その他（専門職系）">その他（専門職系）
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-600" 
                        data-_v-parent-id="600" 
                        data-_v-parent-name="クリエイティブ">
                        クリエイティブ すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-601" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="601" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="ディレクター（WEB）">ディレクター（WEB）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-615" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="615" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="ディレクター（ゲーム）">ディレクター（ゲーム）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-602" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="602" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="ディレクター（その他）">ディレクター（その他）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-603" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="603" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="デザイナー（WEB）">デザイナー（WEB）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-604" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="604" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="デザイナー（アパレル・ファッション）">デザイナー（アパレル・ファッション）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-607" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="607" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="Webコーディング">Webコーディング
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-608" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="608" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="プロダクト・工業デザイナー">プロダクト・工業デザイナー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-609" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="609" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="グラフィック・CGデザイナー">グラフィック・CGデザイナー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-610" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="610" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="DTPオペレーター">DTPオペレーター
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-612" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="612" 
                                data-_v-child-sort="9" 
                                data-_v-child-name="映像クリエーター">映像クリエーター
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-613" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="613" 
                                data-_v-child-sort="10" 
                                data-_v-child-name="サウンドクリエーター">サウンドクリエーター
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-611" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="611" 
                                data-_v-child-sort="11" 
                                data-_v-child-name="編集・ライター">編集・ライター
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-614" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="614" 
                                data-_v-child-sort="12" 
                                data-_v-child-name="芸能関連">芸能関連
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-606" 
                                data-_v-parent-index="12" 
                                data-_v-child-id="606" 
                                data-_v-child-sort="13" 
                                data-_v-child-name="その他（クリエイティブ系）">その他（クリエイティブ系）
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea p-10">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-o-650" 
                        data-_v-parent-id="650" 
                        data-_v-parent-name="サービス・小売・運輸・その他">
                        サービス・小売・運輸・その他 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-654" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="654" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="店長・店舗開発・スーパーバイザー">店長・店舗開発・スーパーバイザー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-651" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="651" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="販売">販売
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-652" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="652" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="カスタマーサポート・コールセンター運営・管理">カスタマーサポート・コールセンター運営・管理
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-655" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="655" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="教師・講師・インストラクター">教師・講師・インストラクター
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-671" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="671" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="警察官・消防士・自衛官">警察官・消防士・自衛官
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-672" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="672" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="行政事務・サービス職">行政事務・サービス職
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-656" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="656" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="介護・福祉">介護・福祉
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-663" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="663" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="ウェディングプランナー">ウェディングプランナー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-664" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="664" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="ホテル・レジャー施設運営">ホテル・レジャー施設運営
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-667" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="667" 
                                data-_v-child-sort="9" 
                                data-_v-child-name="コーディネーター・仲介（人材・ブライダルなど）">コーディネーター・仲介（人材・ブライダルなど）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-670" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="670" 
                                data-_v-child-sort="10" 
                                data-_v-child-name="翻訳・通訳">翻訳・通訳
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-658" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="658" 
                                data-_v-child-sort="11" 
                                data-_v-child-name="パイロット">パイロット
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-657" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="657" 
                                data-_v-child-sort="12" 
                                data-_v-child-name="キャビンアテンダント">キャビンアテンダント
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-659" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="659" 
                                data-_v-child-sort="13" 
                                data-_v-child-name="運転手・セールスドライバー">運転手・セールスドライバー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-661" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="661" 
                                data-_v-child-sort="14" 
                                data-_v-child-name="調理師・パティシエ・キッチンスタッフ">調理師・パティシエ・キッチンスタッフ
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-666" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="666" 
                                data-_v-child-sort="15" 
                                data-_v-child-name="飲食ホールスタッフ">飲食ホールスタッフ
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-662" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="662" 
                                data-_v-child-sort="16" 
                                data-_v-child-name="エステティシャン・ネイリスト・美容師">エステティシャン・ネイリスト・美容師
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-665" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="665" 
                                data-_v-child-sort="17" 
                                data-_v-child-name="整体士・マッサージ">整体士・マッサージ
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-668" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="668" 
                                data-_v-child-sort="18" 
                                data-_v-child-name="警備員">警備員
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-675" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="675" 
                                data-_v-child-sort="19" 
                                data-_v-child-name="学芸員・司書">学芸員・司書
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-674" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="674" 
                                data-_v-child-sort="20" 
                                data-_v-child-name="水産・農林・酪農・農園">水産・農林・酪農・農園
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-673" 
                                data-_v-parent-index="13" 
                                data-_v-child-id="673" 
                                data-_v-child-sort="21" 
                                data-_v-child-name="その他">その他
                            </label>
                        </li>
                                    </ul>
            </div>
            </div>
</div>
<div class="t-c pt-30 jsModalContentBottom p-r">
    <dl class="modalWindow_counter">
        <dt class="colonListTerm">該当求人</dt>
        <dd class="d-i"><span class="fw-b jsJobCount">109</span>件</dd>
    </dl>
    <button class="button button-usuallyBlue fs-20 w-280 jsCloseButton">職種を決定する</button>
</div>

</div>
</aside>
<a href="javascript:void(0)" class="modalWindowClose-large jsModalWindowCloseButton jsModalWindowClose d-n">×</a><div class="modalWindowBackground jsModalWindowBackground d-n"></div><div class="modalWindowWrapper-large jsModalWindowWrapper d-n"></div>        </div>
        <div id="jsLocationModal" class="d-n">
            <aside class="modalWindow-job jsModalWindow d-n" tabindex="0">
    <div class="modalWindow_detail jsModalWindowDetail"><h3 class="modalWindow_title pb-10 jsModalContentTop">勤務地を絞り込む</h3>
<div class="o-h borderGray jsScrollBoxContainer">
    <div class="scrollBox jsScrollBox jsScrollChildrenArea">
        <div class="p-10 jsPrefecturesArea">
            <ul class="pt-10 o-h">
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-1"
                           data-_v-prefecture-id="1"
                           data-_v-prefecture-name="北海道">
                        北海道
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-2"
                           data-_v-prefecture-id="2"
                           data-_v-prefecture-name="青森県">
                        青森県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-3"
                           data-_v-prefecture-id="3"
                           data-_v-prefecture-name="岩手県">
                        岩手県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-4"
                           data-_v-prefecture-id="4"
                           data-_v-prefecture-name="宮城県">
                        宮城県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-5"
                           data-_v-prefecture-id="5"
                           data-_v-prefecture-name="秋田県">
                        秋田県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-6"
                           data-_v-prefecture-id="6"
                           data-_v-prefecture-name="山形県">
                        山形県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-7"
                           data-_v-prefecture-id="7"
                           data-_v-prefecture-name="福島県">
                        福島県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-8"
                           data-_v-prefecture-id="8"
                           data-_v-prefecture-name="茨城県">
                        茨城県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-9"
                           data-_v-prefecture-id="9"
                           data-_v-prefecture-name="栃木県">
                        栃木県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-10"
                           data-_v-prefecture-id="10"
                           data-_v-prefecture-name="群馬県">
                        群馬県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-11"
                           data-_v-prefecture-id="11"
                           data-_v-prefecture-name="埼玉県">
                        埼玉県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-12"
                           data-_v-prefecture-id="12"
                           data-_v-prefecture-name="千葉県">
                        千葉県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-13"
                           data-_v-prefecture-id="13"
                           data-_v-prefecture-name="東京都">
                        東京都
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-14"
                           data-_v-prefecture-id="14"
                           data-_v-prefecture-name="神奈川県">
                        神奈川県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-15"
                           data-_v-prefecture-id="15"
                           data-_v-prefecture-name="新潟県">
                        新潟県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-16"
                           data-_v-prefecture-id="16"
                           data-_v-prefecture-name="富山県">
                        富山県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-17"
                           data-_v-prefecture-id="17"
                           data-_v-prefecture-name="石川県">
                        石川県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-18"
                           data-_v-prefecture-id="18"
                           data-_v-prefecture-name="福井県">
                        福井県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-19"
                           data-_v-prefecture-id="19"
                           data-_v-prefecture-name="山梨県">
                        山梨県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-20"
                           data-_v-prefecture-id="20"
                           data-_v-prefecture-name="長野県">
                        長野県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-21"
                           data-_v-prefecture-id="21"
                           data-_v-prefecture-name="岐阜県">
                        岐阜県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-22"
                           data-_v-prefecture-id="22"
                           data-_v-prefecture-name="静岡県">
                        静岡県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-23"
                           data-_v-prefecture-id="23"
                           data-_v-prefecture-name="愛知県">
                        愛知県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-24"
                           data-_v-prefecture-id="24"
                           data-_v-prefecture-name="三重県">
                        三重県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-25"
                           data-_v-prefecture-id="25"
                           data-_v-prefecture-name="滋賀県">
                        滋賀県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-26"
                           data-_v-prefecture-id="26"
                           data-_v-prefecture-name="京都府">
                        京都府
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-27"
                           data-_v-prefecture-id="27"
                           data-_v-prefecture-name="大阪府">
                        大阪府
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-28"
                           data-_v-prefecture-id="28"
                           data-_v-prefecture-name="兵庫県">
                        兵庫県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-29"
                           data-_v-prefecture-id="29"
                           data-_v-prefecture-name="奈良県">
                        奈良県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-30"
                           data-_v-prefecture-id="30"
                           data-_v-prefecture-name="和歌山県">
                        和歌山県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-31"
                           data-_v-prefecture-id="31"
                           data-_v-prefecture-name="鳥取県">
                        鳥取県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-32"
                           data-_v-prefecture-id="32"
                           data-_v-prefecture-name="島根県">
                        島根県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-33"
                           data-_v-prefecture-id="33"
                           data-_v-prefecture-name="岡山県">
                        岡山県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-34"
                           data-_v-prefecture-id="34"
                           data-_v-prefecture-name="広島県">
                        広島県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-35"
                           data-_v-prefecture-id="35"
                           data-_v-prefecture-name="山口県">
                        山口県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-36"
                           data-_v-prefecture-id="36"
                           data-_v-prefecture-name="徳島県">
                        徳島県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-37"
                           data-_v-prefecture-id="37"
                           data-_v-prefecture-name="香川県">
                        香川県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-38"
                           data-_v-prefecture-id="38"
                           data-_v-prefecture-name="愛媛県">
                        愛媛県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-39"
                           data-_v-prefecture-id="39"
                           data-_v-prefecture-name="高知県">
                        高知県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-40"
                           data-_v-prefecture-id="40"
                           data-_v-prefecture-name="福岡県">
                        福岡県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-41"
                           data-_v-prefecture-id="41"
                           data-_v-prefecture-name="佐賀県">
                        佐賀県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-42"
                           data-_v-prefecture-id="42"
                           data-_v-prefecture-name="長崎県">
                        長崎県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-43"
                           data-_v-prefecture-id="43"
                           data-_v-prefecture-name="熊本県">
                        熊本県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-44"
                           data-_v-prefecture-id="44"
                           data-_v-prefecture-name="大分県">
                        大分県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-45"
                           data-_v-prefecture-id="45"
                           data-_v-prefecture-name="宮崎県">
                        宮崎県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-46"
                           data-_v-prefecture-id="46"
                           data-_v-prefecture-name="鹿児島県">
                        鹿児島県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-47"
                           data-_v-prefecture-id="47"
                           data-_v-prefecture-name="沖縄県">
                        沖縄県
                    </label>
                </li>
                            <li class="w-20p f-l jsChildrenListItem">
                    <label class="scrollBox_item">
                        <input type="checkbox" class="jsPrefecture"
                           id="prefecture-99"
                           data-_v-prefecture-id="99"
                           data-_v-prefecture-name="海外">
                        海外
                    </label>
                </li>
                        </ul>
        </div>
    </div>
</div>

<div class="t-c pt-30 jsModalContentBottom p-r">
    <dl class="modalWindow_counter">
        <dt class="colonListTerm">該当求人</dt>
        <dd class="d-i"><span class="fw-b jsJobCount">109</span>件</dd>
    </dl>
    <button class="button button-usuallyBlue fs-20 w-280 jsCloseButton">勤務地を決定する</button>
</div>

</div>
</aside>
<a href="javascript:void(0)" class="modalWindowClose-large jsModalWindowCloseButton jsModalWindowClose d-n">×</a><div class="modalWindowBackground jsModalWindowBackground d-n"></div><div class="modalWindowWrapper-large jsModalWindowWrapper d-n"></div>        </div>
        <div id="jsFieldModal" class="d-n">
        <aside class="modalWindow-job jsModalWindow d-n" tabindex="0">
    <div class="modalWindow_detail jsModalWindowDetail"><h3 class="modalWindow_title pb-10 jsModalContentTop">業界を絞り込む</h3>
<div class="o-h borderGray jsScrollBoxContainer">
    <div class="scrollBox f-l w-360 jsScrollBox jsScrollSelectParent">
        <ul>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent scrollBox_anchor-current">
                    金融
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    コンサルティング・専門事務所
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    IT・通信・インターネット
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    メーカー・商社
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    メディカル
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    マスコミ・広告関連
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    サービス、小売、外食
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    生活インフラ、運輸、不動産、建設
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    行政機関、社団法人、非営利団体
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                    <li>
                <a href="javascript:void(0)" class="scrollBox_anchor jsSelectParent ">
                    その他
                    <span class="scrollBox_mark d-n jsSelectCount"></span>
                </a>
            </li>
                </ul>
    </div>
    <div class="scrollBox borderGray-left jsScrollBox p-10 jsScrollChildrenArea">
                    <div class=" jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0001" 
                        data-_v-parent-id="0001" 
                        data-_v-parent-name="金融">
                        金融 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0002" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="0002" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="銀行（都市・信託・政府系）、信金">銀行（都市・信託・政府系）、信金
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0001" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="0001" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="証券会社、投資ファンド、投資関連">証券会社、投資ファンド、投資関連
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0007" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="0007" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="生命保険、損害保険">生命保険、損害保険
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0005" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="0005" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="投信投資顧問">投信投資顧問
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0009" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="0009" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="クレジット、信販、リース">クレジット、信販、リース
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0010" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="0010" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="商品取引">商品取引
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0012" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="0012" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="消費者金融、事業者金融">消費者金融、事業者金融
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0014" 
                                data-_v-parent-index="0" 
                                data-_v-child-id="0014" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="その他金融関連">その他金融関連
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0002" 
                        data-_v-parent-id="0002" 
                        data-_v-parent-name="コンサルティング・専門事務所">
                        コンサルティング・専門事務所 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0015" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="0015" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="コンサルティング、シンクタンク">コンサルティング、シンクタンク
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0020" 
                                data-_v-parent-index="1" 
                                data-_v-child-id="0020" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="監査法人、税理士法人、法律事務所">監査法人、税理士法人、法律事務所
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0003" 
                        data-_v-parent-id="0003" 
                        data-_v-parent-name="IT・通信・インターネット">
                        IT・通信・インターネット すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0023" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="0023" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="SIer、ソフト開発、システム運用">SIer、ソフト開発、システム運用
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0025" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="0025" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="インターネット">インターネット
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0026" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="0026" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="通信、ISP、データセンター">通信、ISP、データセンター
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0090" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="0090" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="制御システム、組込みソフトウェア">制御システム、組込みソフトウェア
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0028" 
                                data-_v-parent-index="2" 
                                data-_v-child-id="0028" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="その他ＩＴ・通信関連">その他ＩＴ・通信関連
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0009" 
                        data-_v-parent-id="0009" 
                        data-_v-parent-name="メーカー・商社">
                        メーカー・商社 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0045" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0045" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="総合商社">総合商社
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0054" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0054" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="総合電機、家電、AV機器">総合電機、家電、AV機器
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0056" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0056" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="自動車、自動車部品、輸送機器">自動車、自動車部品、輸送機器
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0053" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0053" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="コンピュータ、通信機器、OA機器関連">コンピュータ、通信機器、OA機器関連
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0049" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0049" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="半導体、電子、精密機器">半導体、電子、精密機器
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0055" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0055" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="重電、産業用電気機器、プラント関連">重電、産業用電気機器、プラント関連
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0063" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0063" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="鉄鋼、非鉄金属">鉄鋼、非鉄金属
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0051" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0051" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="機械関連">機械関連
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0058" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0058" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="化学、石油、ガラス、セラミック">化学、石油、ガラス、セラミック
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0065" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0065" 
                                data-_v-child-sort="9" 
                                data-_v-child-name="食品、飲料">食品、飲料
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0060" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0060" 
                                data-_v-child-sort="10" 
                                data-_v-child-name="日用品、化粧品">日用品、化粧品
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0064" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0064" 
                                data-_v-child-sort="11" 
                                data-_v-child-name="ファッション、アパレル、繊維">ファッション、アパレル、繊維
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0062" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0062" 
                                data-_v-child-sort="12" 
                                data-_v-child-name="インテリア、雑貨、文具、スポーツ">インテリア、雑貨、文具、スポーツ
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0061" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0061" 
                                data-_v-child-sort="13" 
                                data-_v-child-name="印刷、紙・パルプ、書籍、パネル">印刷、紙・パルプ、書籍、パネル
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0059" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0059" 
                                data-_v-child-sort="14" 
                                data-_v-child-name="住宅設備、建材、エクステリア">住宅設備、建材、エクステリア
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0052" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0052" 
                                data-_v-child-sort="15" 
                                data-_v-child-name="ゲーム関連、玩具">ゲーム関連、玩具
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0066" 
                                data-_v-parent-index="3" 
                                data-_v-child-id="0066" 
                                data-_v-child-sort="16" 
                                data-_v-child-name="その他メーカー・商社">その他メーカー・商社
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0005" 
                        data-_v-parent-id="0005" 
                        data-_v-parent-name="メディカル">
                        メディカル すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0032" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="0032" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="医薬品、医療機器">医薬品、医療機器
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0035" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="0035" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="治験、臨床試験、医薬営業受託">治験、臨床試験、医薬営業受託
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0036" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="0036" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="調剤薬局">調剤薬局
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0038" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="0038" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="バイオ関連">バイオ関連
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0037" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="0037" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="病院、医療機関">病院、医療機関
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0039" 
                                data-_v-parent-index="4" 
                                data-_v-child-id="0039" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="その他医療・医薬サービス">その他医療・医薬サービス
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0004" 
                        data-_v-parent-id="0004" 
                        data-_v-parent-name="マスコミ・広告関連">
                        マスコミ・広告関連 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0029" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="0029" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="放送、出版、新聞、映像、音響">放送、出版、新聞、映像、音響
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0030" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="0030" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="広告代理店、PR、SP、デザイン">広告代理店、PR、SP、デザイン
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0031" 
                                data-_v-parent-index="5" 
                                data-_v-child-id="0031" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="その他マスコミ関連">その他マスコミ関連
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0010" 
                        data-_v-parent-id="0010" 
                        data-_v-parent-name="サービス、小売、外食">
                        サービス、小売、外食 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0067" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0067" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="小売（百貨店・専門・CVS・量販店）">小売（百貨店・専門・CVS・量販店）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0089" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0089" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="通信販売">通信販売
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-1015" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="1015" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="物品レンタル">物品レンタル
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0068" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0068" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="フードサービス、飲食">フードサービス、飲食
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0069" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0069" 
                                data-_v-child-sort="4" 
                                data-_v-child-name="旅行、ホテル、旅館、レジャー">旅行、ホテル、旅館、レジャー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-1014" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="1014" 
                                data-_v-child-sort="5" 
                                data-_v-child-name="冠婚葬祭">冠婚葬祭
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0070" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0070" 
                                data-_v-child-sort="6" 
                                data-_v-child-name="人材サービス">人材サービス
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-1013" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="1013" 
                                data-_v-child-sort="7" 
                                data-_v-child-name="コールセンター、業務請負">コールセンター、業務請負
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0021" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0021" 
                                data-_v-child-sort="8" 
                                data-_v-child-name="情報サービス、リサーチ">情報サービス、リサーチ
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0078" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0078" 
                                data-_v-child-sort="9" 
                                data-_v-child-name="教育、研修サービス">教育、研修サービス
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0071" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0071" 
                                data-_v-child-sort="10" 
                                data-_v-child-name="警備、メンテナンス">警備、メンテナンス
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0072" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0072" 
                                data-_v-child-sort="11" 
                                data-_v-child-name="介護、福祉関連サービス">介護、福祉関連サービス
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0074" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0074" 
                                data-_v-child-sort="12" 
                                data-_v-child-name="美容、エステ、リラクゼーション">美容、エステ、リラクゼーション
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-1012" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="1012" 
                                data-_v-child-sort="13" 
                                data-_v-child-name="環境サービス">環境サービス
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0079" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0079" 
                                data-_v-child-sort="14" 
                                data-_v-child-name="受託製造（設計・開発・加工）">受託製造（設計・開発・加工）
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0080" 
                                data-_v-parent-index="6" 
                                data-_v-child-id="0080" 
                                data-_v-child-sort="15" 
                                data-_v-child-name="その他小売、外食、レジャー、サービス">その他小売、外食、レジャー、サービス
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0006" 
                        data-_v-parent-id="0006" 
                        data-_v-parent-name="生活インフラ、運輸、不動産、建設">
                        生活インフラ、運輸、不動産、建設 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0040" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="0040" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="電力、ガス、エネルギー">電力、ガス、エネルギー
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0041" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="0041" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="航空、鉄道、運輸、倉庫">航空、鉄道、運輸、倉庫
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0083" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="0083" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="不動産関連、住宅">不動産関連、住宅
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0081" 
                                data-_v-parent-index="7" 
                                data-_v-child-id="0081" 
                                data-_v-child-sort="3" 
                                data-_v-child-name="建築、土木、設備工事">建築、土木、設備工事
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0007" 
                        data-_v-parent-id="0007" 
                        data-_v-parent-name="行政機関、社団法人、非営利団体">
                        行政機関、社団法人、非営利団体 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0044" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="0044" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="官公庁">官公庁
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-1010" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="1010" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="独立行政、社団、財団、学校法人">独立行政、社団、財団、学校法人
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-1011" 
                                data-_v-parent-index="8" 
                                data-_v-child-id="1011" 
                                data-_v-child-sort="2" 
                                data-_v-child-name="非政府組織(NGO)、非営利団体(NPO)">非政府組織(NGO)、非営利団体(NPO)
                            </label>
                        </li>
                                    </ul>
            </div>
                    <div class="d-n jsChildrenArea">
                <div class="borderGray-bottom-dotted pb-10">
                    <label class="scrollBox_item fw-b">
                        <input type="checkbox" class="jsCheckParent" 
                        id="parent-f-0012" 
                        data-_v-parent-id="0012" 
                        data-_v-parent-name="その他">
                        その他 すべて
                    </label>
                </div>
                <ul class="pt-10">
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0086" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="0086" 
                                data-_v-child-sort="0" 
                                data-_v-child-name="農業、林業、水産、畜産">農業、林業、水産、畜産
                            </label>
                        </li>
                                            <li class="jsChildrenListItem">
                            <label class="scrollBox_item">
                                <input type="checkbox" class="jsCheckChild" 
                                id="child-0087" 
                                data-_v-parent-index="9" 
                                data-_v-child-id="0087" 
                                data-_v-child-sort="1" 
                                data-_v-child-name="鉱業">鉱業
                            </label>
                        </li>
                                    </ul>
            </div>
            </div>
</div>
<div class="t-c pt-30 jsModalContentBottom p-r">
    <dl class="modalWindow_counter">
        <dt class="colonListTerm">該当求人</dt>
        <dd class="d-i"><span class="fw-b jsJobCount">109</span>件</dd>
    </dl>
    <button class="button button-usuallyBlue fs-20 w-280 jsCloseButton">業界を決定する</button>
</div>

</div>
</aside>
<a href="javascript:void(0)" class="modalWindowClose-large jsModalWindowCloseButton jsModalWindowClose d-n">×</a><div class="modalWindowBackground jsModalWindowBackground d-n"></div><div class="modalWindowWrapper-large jsModalWindowWrapper d-n"></div>    </div>
        <input class="d-n" id="jsIsBackForwardForJobSearch">
        <div class="dialog jsModalBookmarkOfJobOffer" id="jsModalBookmarkOfJobOfferResultMessage"><p class="dialogMessage"></p></div>


        <div class="d-n" id="jsNewGraduateJobSearchModal">
        <aside class="modalWindow jsModalWindow d-n" tabindex="0">
    <div class="modalWindow_detail jsModalWindowDetail">    <div id="jsNewGraduateJobSearchModalVue"></div>
</div>
</aside>
<a href="javascript:void(0)" class="modalWindowCloseButton jsModalWindowCloseButton jsModalWindowClose d-n">×</a><div class="modalWindowBackground jsModalWindowBackground d-n"></div><div class="modalWindowWrapper jsModalWindowWrapper d-n"></div>
    </div>


        <script src="https://assets.vorkers.com/assets/4689.e71e3e28.js"></script><script src="https://assets.vorkers.com/assets/5074.ce6b1b5b.js"></script><script src="https://assets.vorkers.com/assets/2252.5f78b359.js"></script><script src="https://assets.vorkers.com/assets/9892.36565870.js"></script><script src="https://assets.vorkers.com/assets/web-com-common_pc-entry.js.1dca036f.js"></script>
<script src="https://assets.vorkers.com/assets/vue.a6d2a516.js"></script><script src="https://assets.vorkers.com/assets/3670.27288580.js"></script><script src="https://assets.vorkers.com/assets/com-pc-entry.js.a4047f40.js"></script>
    <script>
!function() {
    'use strict';

    var writeKey = '6488/a6c7f3b05230c6f924c1687da6998e76e3f817a8';
    var database = 'vorkers_production';
    var userDevice = 'pc';
    var uid = null;
    var route = 'job_list';
    var vcid = '2ebbbcc5-987d-4740-906f-a7bcf41c2ba9';
    var isProd = true;

    var td = new Treasure({
        host: 'in.treasuredata.com',
        writeKey: writeKey,
        database: database
    });
    _v.ErrorLogger.setup(td, userDevice, uid, route, vcid);
    var errorLogger = _v.ErrorLogger.getInstance();

    if (!window.addEventListener) {
        return; // サポートされてないブラウザではエラーリスナーを登録しない
    }
    window.addEventListener('error', function (event) {
        if (isProd) {
            event.preventDefault(); // コンソールにエラーを表示しない
        }
        errorLogger.logEvent(event);
    }, false); // useCapture https://developer.mozilla.org/ja/docs/Web/API/EventTarget/addEventListener
}();
</script>    <script>
$(function(){
    'use strict';
    _v.search_form = _v.search_form || {};

    var fieldCode;
    var $keywordSearchInput = $('.jsKeywordSearchInput');
    var eventLogger = _v.EventLogger.getNewInstance();
    var displayTimeStamp = new Date().getTime();

    const ULM2841_TEST_NAME = 'ulm2841Test';
    const isUlm2841TestTarget = $keywordSearchInput.hasClass('ulm2841TestTargetInput');
    const isUlm2841TestPatternB = $keywordSearchInput.hasClass('w-350');

    const conversionTracker = new _v.ab.ConversionTracker(ULM2841_TEST_NAME, '/ab/track_conversion');
    const displayTracker = new _v.ab.ConversionTracker(ULM2841_TEST_NAME, '/ab/track_display');

    $keywordSearchInput.on('focus', function() {
        fieldCode = $(this).closest('form').find('.jsField').val();
        eventLogger.logEvent('searchSuggestFocus', displayTimeStamp, null, false);
    });

    /**
     * クリック、タップ、キーボードで選択されたオートコンプリートの候補をここに格納
     * {
     * isHeading: bool,
     * label: string,
     * path: string,
     * value: string
     * }
     * @type object
     */
    var autocompleteSelectedItem;

    $keywordSearchInput.vsearchautocomplete({
        source: function(request, response){
            $.ajax({
                url: 'https://www.vorkers.com/search/suggest',
                type: 'GET',
                dataType: 'json',
                data: {src_str: request.term, field:fieldCode},
                success: function(data) {
                    response(data);
                }
            });
        },
        select: function(event, ui){
            autocompleteSelectedItem = ui.item;
            if (ui.item.isHeading) {
                return false;             }
                        $(event.target).val(ui.item.value);
                        eventLogger.logEvent('searchSuggestClick', displayTimeStamp + '_' + ui.item.eventParameter, ui.item.path);
            location.href = ui.item.path;
        },
        focus: function(event, ui) {
            if (ui.item.isHeading) {
                                $(this).val('');
                return false;
            }
        },
        minLength: 0,
        isUlm2841TestTarget: isUlm2841TestTarget,
        isUlm2841TestPatternB: isUlm2841TestPatternB,
        ulm2841TestName: ULM2841_TEST_NAME,
        displayTracker: displayTracker,
        conversionTracker: conversionTracker,
    }).on('focus.vSearchForm', function() {         $(this).vsearchautocomplete("search", "");
    });

        function overrideCloseIfInstance(instance) {
        if (!instance) {
            return;
        }
        var originalClose = instance.close;         instance.close = function(e) {                         if (e.type === 'menuselect' && autocompleteSelectedItem.isHeading) {
                return false;
            }
                        originalClose.apply(this, arguments);         };
    }

    var instance = $keywordSearchInput.data('vorkersVsearchautocomplete');
    overrideCloseIfInstance(instance);

        $('.ui-menu').on('touchmove', function(event) {
        event.preventDefault();
    });

        $('.jsKeywordSearchInput').on('keyup', function(e){
        _v.search_form.changeKeywordIcon(e.currentTarget);
    });
        $('.jsKeywordSearchInput').on('blur', function(e){
        _v.search_form.changeKeywordIcon(e.currentTarget);
    });
        $('.jsClearSearchKeyword').on('click', function() {
        $(this).prevAll('input')
                .val('')
                .trigger('blur');
    });
        function showKeywordClearIcon(e) {
        $(e).nextAll('.jsClearSearchKeyword').show();
    }
        function hideKeywordClearIcon(e) {
        $(e).nextAll('.jsClearSearchKeyword').hide();
    }
        $keywordSearchInput.on('keydown.vSearchForm', function(e) {
        if ($keywordSearchInput.val() !== '') {             return;
        }

        var key = e.keyCode;
        if (key !== 38 && key !== 40) {             return;
        }

        var $uiMenuItem = $('.ui-menu-item');
        var $uiStateFocus = $('.ui-state-focus');
                if (key === 38) {
            if ($uiMenuItem.get(0) === $uiStateFocus.get(0)) {
                var $lastUiMenuItem = $uiMenuItem.eq(-1);
                $lastUiMenuItem.trigger('mouseover');
                $keywordSearchInput.val($lastUiMenuItem.text());
            }
            return;
        }
                if (key === 40) {
            if ($uiMenuItem.get(0) === $uiStateFocus.get(0)) {
                var $firstUiMenuItem = $uiMenuItem.eq(1);
                $firstUiMenuItem.trigger('mouseover');
                $keywordSearchInput.val($firstUiMenuItem.text());
            }
        }

    });
        _v.search_form.changeKeywordIcon = function(e) {
        var keyword = $(e).val();
        if (keyword === '') {
            hideKeywordClearIcon(e);
        } else if (keyword === '社名で検索する') {
            hideKeywordClearIcon(e);
        } else {
            showKeywordClearIcon(e);
        }
    };

    $('.jsKeywordSearchForm').on('submit', function() {
        var srcStr = $(this).find('input[name="src_str"]').val();
        var keyword = srcStr ? srcStr : 'nodata';
        eventLogger.logEvent('searchSuggestSubmit', displayTimeStamp + '_' + 'keyword:' + keyword);

        // 初回のdisplayログ送信後であれば検索時にログを送信
        if (isUlm2841TestTarget && $keywordSearchInput.vsearchautocomplete('option', 'hasTrackedFirstDisplay')) {
            conversionTracker.track(ULM2841_TEST_NAME, 'search', false, false)
        }
    });
});
</script>
<script>
$(function(){
        $('.jsSearchCtSubmit').one('click', function() {
                var ctPath;
                    ctPath = 'com';                 if (ctPath && $('.jsKeywordSearchInput').val().replace(/\s+|　/g,'').length !== 0) {
            $('.jsKeywordSearchForm').append('<input type="hidden" name="ct" value="' + ctPath + '">');
        }
    });
});
</script>    <script>
function recordOutboundLink(link, category, action) {
  try {
    var pageTracker=_gat._getTracker("UA-4148420-1");
    pageTracker._trackEvent(category, action);
    setTimeout('document.location = "' + link.href + '"', 100)
  }catch(err){}
}
</script>


<script>
!function() {
    'use strict';

    var eventLogger = new _v.EventLogger('/log_event');
    eventLogger.registerClickEvent();
}();
</script>
<input id="jsDataJobSearchList" type="hidden" data-_v-jsdata="{&quot;keywordMatchingResults&quot;:[]}">

<script src="https://assets.vorkers.com/assets/9503.696b6e4a.js"></script><script src="https://assets.vorkers.com/assets/com-jobSearch-pc-list-entry.ts.46dae57a.js"></script>

<script src="https://assets.vorkers.com/assets/372.6f7d4274.js"></script><script src="https://assets.vorkers.com/assets/web-jui-result-entry.js.4f585d1c.js"></script>
<script>
!function() {
    'use strict';

        $('.autoHeight').autoHeight({ 
        column:2
    });

        var jobKeywordAutoComplete = _v.jui.JobKeywordAutoComplete;
    var keywordAutoComplete = new jobKeywordAutoComplete();
    keywordAutoComplete.init(
            $('.jsJobSearchKeywordInput'),
            $('#jsConditionForm'),
            null,
            'https://www.vorkers.com/job_search/api/suggestKeyword'
    );

        var modalManager = _v.jui.JobSearchModalManager;
    var occupationModalMgr = new modalManager();
    var locationModalMgr = new _v.jui.PrefectureCheckboxModalManager();
    var fieldModalMgr = new modalManager();
    var hqModalManager = new _v.jui.JobSearchPrefModalManager();

        var conditionFormManager = new _v.jui.result.ConditionFormManager();

    conditionFormManager.occupationModalMgr = occupationModalMgr;
    conditionFormManager.locationModalMgr = locationModalMgr;
    conditionFormManager.fieldModalMgr = fieldModalMgr;
    conditionFormManager.hqModalManager = hqModalManager;

        conditionFormManager.familyHtml = '<div class="jsHouse d-ib mr-15 fs-13 mt-10 lh-high"><h3 class="d-ib">NAME</h3><ul class="childItem childItem-jobList">CHILDREN</ul></div>';
    conditionFormManager.childHtml = '<li class="ml-15 mr-n5 mt-10 d-ib selectedItem">NAME<a href="javascript:void(0)" class="selectedItem-delete jsChildDelete" data-_v-id="ID" data-_v-method="METHOD">選択解除</a></li>';
    conditionFormManager.prefectureListItemHtml = '<li class="mr-10 d-ib selectedItem mb-10">NAME<a href="javascript:void(0)" class="selectedItem-delete jsPrefectureDelete" data-_v-id="ID">選択解除</a></li>';

    $(function() {
                conditionFormManager.init();

                        var occupationParentId = 'o';
        var occupationChildId = 'z';
        occupationModalMgr.init(
            $('#jsOccupationModal'),
            $('#jsOccupationModalTrigger'),
            $('#' + occupationParentId),
            $('#' + occupationChildId),
            40,
            function(selectionStore) {
                conditionFormManager.occupationalModalCallback(selectionStore);
            }
        );

                var prefectureId = 'p';
        locationModalMgr.init(
            $('#jsLocationModal'),
            $('#jsLocationModalTrigger'),
            $('#' + prefectureId),
            100,
            function(selectionStore) {
                conditionFormManager.locationModalCallback(selectionStore);
            }
        );
        locationModalMgr.runCallback();


                var industryId = 'i';
        var fieldId = 'f';
        fieldModalMgr.init(
            $('#jsFieldModal'),
            $('#jsFieldModalTrigger'),
            $('#' + industryId),
            $('#' + fieldId),
            20,
            function(selectionStore) {
                conditionFormManager.fieldModalCallback(selectionStore);
            }
        );

                var maxNextRankingJobs = 10;
        $('.jsShowNextRankingJob').on('click', function() {
            var $this = $(this);
            var $job = $this.closest('.jsRankingJob');
            var $hiddenJobs = $job.find('.jsRankingJobs').find('.jsHiddenRankingJob:hidden');
            if ($hiddenJobs.length <= maxNextRankingJobs) {                 $hiddenJobs.removeClass('d-n');
                $this.remove();
                return;
            }
            for (var i = 0; i < maxNextRankingJobs; i++) {                 $hiddenJobs.eq(i).removeClass('d-n');
            }
            var $remainingHiddenJobs = $hiddenJobs.filter(':hidden');             if ($remainingHiddenJobs.length < maxNextRankingJobs) {                 $this.find('.jsNextJobsCount').text($remainingHiddenJobs.length);
            }
        });

                var jobCountUrl = "https://www.vorkers.com/job_search/api/rankingCount";
        var jobCountFetcher = new _v.jui.JobCountFetcher();
        jobCountFetcher.init(jobCountUrl, $('#jsConditionForm'), 'jsJobCount');

                var $isReload = $('#jsIsBackForwardForJobSearch');
        if ($isReload.val()) {
                        occupationModalMgr.runCallback();
            locationModalMgr.runCallback();
            fieldModalMgr.runCallback();
            jobCountFetcher.updateJobCount();
                        $('.jsShowScoreSelectbox:checked').trigger('change');
        } else {
                        $isReload.val(1);
        }

        $('.jsShowCondition').on('click', function() {
            $('.jsDefaultHide').show();
            $(this).hide();
        });
        $('.jsShowCondition').on('click', function() {
            $('.jsHideWhenShowCondition').hide();
            $('.jsShowWhenShowCondition').show();
            $('.jsJobCountWrapper').addClass('mt-10');
            $('.jsJobCountTitle').text('この条件の求人数');
        });
    });
}();
</script>
<script>
$(function(){
        $('.jsJobSearchCtSubmit').one('click', function() {
                var ctPath = 'jresult';
        if ($('.jsJobSearchKeywordInput').val().replace(/\s+|　/g,'').length !== 0) {
            $('.jsJobSearchCtForm').append('<input type="hidden" name="ct" value="' + ctPath + '">');
        }
    });
});
</script><script>
    $(function(){
        'use strict';
        var bookmarkOfJobOfferActionFacade = new _v.bookmark.BookmarkOfJobOfferActionFacade();
        $('.jsAddBookmarkOfJobOffer').on('click.vBookmarkOfJobOfferActionFacade', function() {
            var $this = $(this);
            var jobId = $this.data('_v-job-id');
            var jobService = $this.data('_v-job-service');
            bookmarkOfJobOfferActionFacade.addBookmarkOfJobOffer(jobId, jobService);
        });
        $('.jsDeleteBookmarkOfJobOffer').on('click.vBookmarkOfJobOfferActionFacade', function() {
            var $this = $(this);
            var jobId = $this.data('_v-job-id');
            var jobService = $this.data('_v-job-service');
            bookmarkOfJobOfferActionFacade.deleteBookmarkOfJobOffer(jobId, jobService);
        });
        $('.jsBookmarkOfJobOfferIfNotLogin').on('click.vBookmarkOfJobOfferActionFacade', function() {
            bookmarkOfJobOfferActionFacade.openModalOrFlash('#jsModalBookmarkOfJobOfferIfNotLogin');
        });
    });
</script>
<script>
!function(module) {
    'use strict';
    // モジュールのエクスポート
    _v.util.registerNameSpace('_v.bookmark');
    _v.bookmark.BookmarkOfJobOfferActionFacade = module();
}(function() {
    'use strict';
    var EVENT_LOG_API_URL = '/log_event';

    var BookmarkOfJobOfferActionFacade = function() {
        this.isInRequest = false;
    };

        BookmarkOfJobOfferActionFacade.prototype.deleteBookmarkOfJobOffer = function(jobId, jobService, $modal, $countDisplayElement) {
        var _this = this;
        if (this.isInRequest) {
            return;
        }
        _this.isInRequest = true;
        var isSuccessDelete = false;
        var elementIds;
        $.ajax({
            type: 'POST',
            url: '/bookmark_job_offer/delete',
            dataType: 'json',
            data: {job_id: jobId, job_service: jobService, output: 'json'},
            success: function(res) {
                if ($modal) {
                    $modal.dialog('close');
                    $modal.remove();
                }
                isSuccessDelete = res.data.isSuccessDelete;
                elementIds = res.data.deletedJobs;
                _this._previewBookmark(res.data.bookmarkPreviews);
                _this._controlDialog(res.data.message);
            },
            error: function() {
                                if ($modal || !$countDisplayElement) {
                    alert('ネットワークに接続されていません。接続後にリトライしてください。');
                }
            },
            complete: function() {
                _this.isInRequest = false;
                var deleteCount = 0;
                if (isSuccessDelete) {
                                        deleteCount = BookmarkOfJobOfferActionFacade._removeJobElements(elementIds);
                }
                                if (isSuccessDelete && $countDisplayElement) {
                    _this._changeCount($countDisplayElement, deleteCount);
                }
                                if (!$modal && !$countDisplayElement) {
                    var $bookmarkButton = $('.js' + jobService + jobId);
                    $bookmarkButton
                            .addClass('jsAddBookmarkOfJobOffer')
                            .removeClass('jsDeleteBookmarkOfJobOffer')
                            .off('click')
                            .on('click', function() {
                                var $this = $(this);
                                var jobId = $this.data('_v-job-id');
                                var jobService = $this.data('_v-job-service');
                                _this.addBookmarkOfJobOffer(jobId, jobService);
                            })
                            .data('_v-event-logger-parameter', 'bookmark_job_offer_add')
                            .addClass('jsTooltip')
                            .attr('data-tooltip', '')
                            .data('tooltip', '気になる求人をリストに入れてまとめてチェックできます')
                            .removeClass('button-current')
                            .find('.jsBookmarkButtonSpan')
                                .removeClass('pcIcon-25')
                                .addClass('pcIcon-69')
                                .text('気になる');
                                        _v.util.initializeTooltip();
                    (new _v.EventLogger(EVENT_LOG_API_URL)).registerClickEvent();
                }
            }
        });
    };

        BookmarkOfJobOfferActionFacade.prototype.deleteAllBookmarkOfJobOffer = function($modal, $countDisplayElement, $deleteAllElement) {
        var _this = this;
        if (_this.isInRequest) {
            return;
        }
        _this.isInRequest = true;
        var isSuccessDelete = false;
        var elementIds;
        $.ajax({
            url: '/bookmark_job_offer/delete_all',
            type: 'POST',
            dataType: 'json',
            data: {output: 'json'},
            success: function(res) {
                $modal.dialog('close');
                $modal.remove();
                isSuccessDelete = res.data.isSuccessDelete;
                elementIds = res.data.deletedJobs;
            },
            error: function() {
                alert('ネットワークに接続されていません。接続後にリトライしてください。');
            },
            complete: function() {
                _this.isInRequest = false;
                if (!isSuccessDelete) {
                                        return;
                }
                                var deleteCount = BookmarkOfJobOfferActionFacade._removeJobElements(elementIds);
                                if ($countDisplayElement) {
                    _this._changeCount($countDisplayElement, deleteCount);
                }
                if ($deleteAllElement) {
                    $deleteAllElement.remove();
                }
            }
        });
    };
        BookmarkOfJobOfferActionFacade.prototype.addBookmarkOfJobOffer = function(jobId, jobService) {
        var _this = this;
        if (_this.isInRequest) {
            return;
        }
        _this.isInRequest = true;
        var shouldChangeButton = false;
        $.ajax({
            type: 'POST',
            url: '/bookmark_job_offer/add',
            data: {job_id: jobId, job_service: jobService, output: 'json'},
            dataType: 'json',
            async: true,
            cache: false,
            success: function(res) {
                _this._controlDialog(res.data.message);
                shouldChangeButton = res.data.shouldChangeButton;
                _this._previewBookmark(res.data.bookmarkPreviews);
            },
            error: function(res) {
            },
            complete: function() {
                _this.isInRequest = false;
                if (!shouldChangeButton) {
                    return;
                }
                                var $bookmarkButton = $('.js' + jobService + jobId);
                                    $bookmarkButton
                        .removeClass('jsAddBookmarkOfJobOffer')
                        .addClass('jsDeleteBookmarkOfJobOffer')
                        .off('click')
                        .on('click', function() {
                            var $this = $(this);
                            var jobId = $this.data('_v-job-id');
                            var jobService = $this.data('_v-job-service');
                            _this.deleteBookmarkOfJobOffer(jobId, jobService);
                        })
                        .data('_v-event-logger-parameter', 'bookmark_job_offer_delete')
                        .removeClass('jsTooltip')
                        .removeAttr('data-tooltip')
                        .removeData('tooltip')
                        .addClass('button-current')
                        .find('.jsBookmarkButtonSpan')
                            .removeClass('pcIcon-69')
                            .addClass('pcIcon-25')
                            .text('気になる済');
                                                if ($bookmarkButton.tooltip('instance')) {
                    $bookmarkButton.tooltip('destroy');
                }
                _v.util.initializeTooltip();
                (new _v.EventLogger(EVENT_LOG_API_URL)).registerClickEvent();
            }
        });
    };

        BookmarkOfJobOfferActionFacade.prototype._controlDialog = function(message) {
        var $dialog = $('#jsModalBookmarkOfJobOfferResultMessage');
        $dialog.hide();
        $dialog.children('.dialogMessage').text(message);
        if ($dialog) {
            $dialog.fadeIn(400).delay(750).fadeOut(400);
        }
    };

        BookmarkOfJobOfferActionFacade.prototype._changeCount = function($countDisplayElement, deleteCount) {
        if (!deleteCount) {
            return;
        }
        var count = $countDisplayElement.data('_v-bookmark-count') - deleteCount;
        if (count >= 0) {
            $countDisplayElement.text('該当件数：' + count + '件');
            $countDisplayElement.data('_v-bookmark-count', count);
        } else {
            $countDisplayElement.remove();
        }
    };

        BookmarkOfJobOfferActionFacade._removeJobElements = function(elementIds) {
        if (!elementIds) {
            return 0;
        }
        var removeCount = 0;
        for (var key in elementIds) {
            var elementId = elementIds[key];
            var $element = $('#' + elementId);
            if (!$element.length) {
                continue;
            }
            $element.fadeOut(400).queue(function() {
                $element.remove();
            });
            ++removeCount;
        }

        return removeCount;
    };

        BookmarkOfJobOfferActionFacade.prototype._previewBookmark = function(bookmarkPreviews) {
        if (!_v.bookmark.bookmarkPreview) {
            return;
        }
        _v.bookmark.bookmarkPreview.setBookmarkPreviews(bookmarkPreviews);
    };

    return BookmarkOfJobOfferActionFacade;
});
</script>

    <script type="application/ld+json">
    {
        "@context": "http://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
                            {
    "@type": "ListItem",
    "position": 1,
    "item": {
        "@id": "https://www.vorkers.com/",
        "name": "ＨＯＭＥ"
    }
}
,                            {
    "@type": "ListItem",
    "position": 2,
    "item": {
        "@id": "/job_search_result?u=std",
        "name": "求人トップ"
    }
}
,                            {
    "@type": "ListItem",
    "position": 3,
    "item": {
        "@id": "https://www.vorkers.com/job_search_result",
        "name": "求人情報"
    }
}
                    ]
    }
</script>

    <script>
    $(function(){
                if (!_v || !_v.ab || !_v.ab.ConversionTracker) {
                        return;
        }
        var apiUrl = '/ab/track_conversion';
        var abTests = [];
                    abTests.push('mission80Test');
                    abTests.push('mlopsRelease');
                    abTests.push('mktg43TestHtmlPC');
                    abTests.push('mktg43TestStylePC');
                    abTests.push('rec3581Test');
                    abTests.push('rec3712TestHtml');
                    abTests.push('daily1155Test');
                    abTests.push('mktg101Test');
                    abTests.push('rec3882TestHtml');
                    abTests.push('mktg104TestHtmlSP');
                    abTests.push('mktg104TestHtmlPC');
                    abTests.push('mktg114TestHtmlTopPC');
                    abTests.push('mktg114TestHtmlMiddlePC');
                    abTests.push('mktg114TestHtmlBottomPC');
                    abTests.push('mktg114TestStylePC');
                    abTests.push('mktg114TestHtmlMiddleSP');
                    abTests.push('mktg114TestHtmlBottomSP');
                    abTests.push('mktg114TestHtmlTopSP');
                    abTests.push('mktg114TestStyleSP');
                    abTests.push('daily1318Test');
                    abTests.push('mktg115TestStylePC');
                    abTests.push('mktg115TestHtmlTopPC');
                    abTests.push('mktg115TestHtmlMiddlePC');
                    abTests.push('mktg115TestHtmlBottomPC');
                    abTests.push('mktg115TestStyleSP');
                    abTests.push('mktg115TestHtmlTopSP');
                    abTests.push('mktg115TestHtmlMiddleSP');
                    abTests.push('mktg115TestHtmlBottomSP');
                    abTests.push('recmktg25TestHtml');
                    abTests.push('recmktg25TestStyle');
                    abTests.push('ulm1419Test');
                    abTests.push('daily1549TestHtml');
                    abTests.push('ulm1524Test');
                    abTests.push('ulm1511Test');
                    abTests.push('adpr26TestHtml');
                    abTests.push('adpr25TestHtml');
                    abTests.push('adpr38TestHtml');
                    abTests.push('daily1582TestHtml');
                    abTests.push('ulm1784Test');
                    abTests.push('ulm1987Test');
                    abTests.push('daily2160Test');
                    abTests.push('adpr215TestJobHead');
                    abTests.push('adpr215TestJobFoot');
                    abTests.push('ulm2238Test');
                    abTests.push('ulm2239Test');
                    abTests.push('ulm2362Test');
                    abTests.push('ulm2470Test');
                    abTests.push('ulm2508Test');
                    abTests.push('ulm2379Test');
                    abTests.push('adpr330Test');
                    abTests.push('daily2551PatternBTest');
                    abTests.push('daily2551PatternATest');
                    abTests.push('ulm2600Test');
                    abTests.push('ulm2646Test');
                    abTests.push('daily2688Test_2');
                    abTests.push('daily2688Test_1');
                    abTests.push('ulm2655Test');
                    abTests.push('daily2621Test');
                    abTests.push('ulm2705Test');
                    abTests.push('daily2732Test');
                    abTests.push('daily2787Test');
                    abTests.push('ulm2841Test');
                    abTests.push('keywordMatchingFeatureFlag');
                    abTests.push('keywordMatchingClosedReleaseFlag');
                    abTests.push('ulm2855Test');
                    abTests.push('daily2967Test');
                var conversionTracker = new _v.ab.ConversionTracker(abTests, apiUrl);
        conversionTracker.registListener();
    });
</script>

<script type="text/javascript">
    var td = new Treasure({
        host: 'in.treasuredata.com',
        writeKey: '6488/a6c7f3b05230c6f924c1687da6998e76e3f817a8',
        database: 'vorkers_production'
    });
            td.set('pageviews', {
            user_device: 'pc'
        });
        td.trackPageview('pageviews');
    </script>

<script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
        'route'   : 'job_list',
        'data_16' : '|mission80Test,mission80PatternG|mlopsRelease,ml_ops_company_recommend_7_pattern_1|mktg43TestHtmlPC,mktg43TestHtmlPC|mktg43TestStylePC,mktg43TestStylePC|rec3581Test,rec3581PatternA|rec3712TestHtml,rec3712TestHtml|daily1155Test,daily1155PatternA|mktg101Test,mktg101PatternA|rec3882TestHtml,rec3882TestHtml|mktg104TestHtmlSP,mktg107TestHtmlSP_0203|mktg104TestHtmlPC,mktg107TestHtmlPC_0203|mktg114TestHtmlTopPC,fix0304|mktg114TestHtmlMiddlePC,fix0304|mktg114TestHtmlBottomPC,fix0304|mktg114TestStylePC,fix0304|mktg114TestHtmlMiddleSP,fix0304|mktg114TestHtmlBottomSP,fix0304|mktg114TestHtmlTopSP,fix0304|mktg114TestStyleSP,fix0304|daily1318Test,daily1318PatternB|mktg115TestStylePC,test_0520|mktg115TestHtmlTopPC,test_0519|mktg115TestHtmlMiddlePC,test_0520|mktg115TestHtmlBottomPC,test_0325|mktg115TestStyleSP,test_0520|mktg115TestHtmlTopSP,test_0519|mktg115TestHtmlMiddleSP,test_0519|mktg115TestHtmlBottomSP,test_0325|recmktg25TestHtml,recmktg25TestHtml_0520|recmktg25TestStyle,recmktg25TestStyle_0520|ulm1419Test,ulm1419PatternB|daily1549TestHtml,daily1549TestHtml|ulm1524Test,ulm1524PatternA|ulm1511Test,ulm1511PatternB|adpr26TestHtml,adpr26TestHtml|adpr25TestHtml,adpr25TestHtml|adpr38TestHtml,adpr38TestHtml|daily1582TestHtml,daily1582TestHtml|ulm1784Test,ulm1784PatternB|ulm1987Test,ulm1987PatternB|daily2160Test,daily2160PatternB|adpr215TestJobHead,adpr215_0203|adpr215TestJobFoot,adpr215_0203|ulm2238Test,ulm2238PatternB|ulm2239Test,ulm2239PatternB|ulm2362Test,ulm2362PatternB|ulm2470Test,ulm2470PatternB|ulm2508Test,ulm2508PatternB|ulm2379Test,ulm2379PatternB|adpr330Test,adpr330|daily2551PatternBTest,daily2551PatternB|daily2551PatternATest,daily2551PatternA|ulm2600Test,ulm2600PatternB|ulm2646Test,ulm2646PatternB|daily2688Test_2,daily2688PatternA|daily2688Test_1,daily2688PatternA|ulm2655Test,ulm2655PatternB|daily2621Test,daily2621PatternB|ulm2705Test,ulm2705PatternB|daily2732Test,daily2732PatternB|daily2787Test,daily2787PatternB|ulm2841Test,ulm2841PatternB|keywordMatchingFeatureFlag,enabled|keywordMatchingClosedReleaseFlag,isClosedRelease|ulm2855Test,ulm2855PatternB|daily2967Test,daily2967PatternB|',
        'data_24' : '0',
        'event'   : 'allpage_ready',
                    'data_60' : '',
            });
</script>








<!-- Google Tag Manager -->
<noscript>
    <iframe src="//www.googletagmanager.com/ns.html?id=GTM-M4SF4C" height="0" width="0" style="display:none;visibility:hidden"></iframe>
</noscript>
<script>
!(function(w,d,s,l,i) {
    w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});
    var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
    j.async = true;
    j.src = '//www.googletagmanager.com/gtm.js?id=' + i + dl;
    f.parentNode.insertBefore(j, f);
})(window,document,'script','dataLayer','GTM-M4SF4C');
</script>
<!-- End Google Tag Manager -->
</body>
</html>

"""


def writeinto_txtfile(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        f.write(data)
        f.write("\n")


class BS4Parse():
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def parseOneElement(self, tagName):
        trans_list = []
        for single_tag in self.soup.select(tagName):
            trans_list.append(" ".join(single_tag.text.split()))
        tagText = " ".join(trans_list)
        return tagText, trans_list
    def parseClassAttribute(self,outsidetag,classAttribute):
        trans_list = []
        ret = self.soup.findAll(name=outsidetag, attrs={"class":classAttribute})

        for item in ret:
            trans_list.append("".join(item.text))
        tagText = " ".join(trans_list)
        return tagText, trans_list


    def parseIDAttribute(self,DAttribute):
        trans_list = []
        ret = self.soup.findAll(id=DAttribute)

        for item in ret:
            trans_list.append("".join(item.text))
        tagText = " ".join(trans_list)
        return tagText, trans_list


    def fetchAllText(self):
        AllText = "".join(self.soup.get_text().split())
        return AllText


# Truncating strings for readable output
def truncate_string_for_readed(text):
    ret_list = []

    len_text = len(text)
    base_text_num = 88
    integer, remainder = divmod(len_text, base_text_num)
    # 整数,处理
    ret_list.append(text[0:base_text_num])
    for item in range(1, integer):
        ret_list.append(text[base_text_num * item:base_text_num * (item + 1)])
    # 余数处理 - ok
    ret_list.append(text[integer * base_text_num:])

    return ret_list


def for_count_and_read(countfile, readfile, text):
    # for count
    writeinto_txtfile(countfile, text)

    # for read

    ret_list = truncate_string_for_readed(text)
    for item in ret_list:
        writeinto_txtfile(readfile, item)
        writeinto_txtfile(readfile, "\t")


def writeinto_htmlfile(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        f.write(data)
        f.write("\n")


html_head = """
<html>

<head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width,initial-scale=1.0">

            <style type="text/css">
                        .todo[data-v-ee48fd14] {
                                    margin: 8px auto;
                                    padding: 12px 8px;
                                    text-align: left;
                                    -webkit-box-shadow: 0px 0px 2px #847070;
                                    box-shadow: 0px 0px 2px #847070;
                                    border-radius: 4px;
                                    display: -webkit-box;
                                    display: -ms-flexbox;
                                    display: flex;
                                    font-size: medium;
                                    width: 888px;
                                    -webkit-box-align: center;
                                    color: #495057;
                                    -ms-flex-align: center;
                                    align-items: center;
                                    background-color: #ffff;
                        }

                        body {
                                    background-color: #94d3a2;
                        }
            </style>
</head>

<body>

            <div data-v-fae5bece="">
"""
html_body = '<div data-v-ee48fd14="" data-v-fae5bece="" class="todo">{0}</div>'
html_footer = """
            </div>
</body>

</html>
"""
if __name__ == "__main__":
    infoID = 0
    soup = BeautifulSoup(html_doc, 'html.parser')
    # ret = soup.findAll(name="a", attrs={"class" :"searchChangeTrigger white d-b"})
    # print(ret)
    b = BS4Parse(html_doc)
    ret,_ = b.parseIDAttribute("footerMenu")


    # for item in ret:
    #     print(item)
    #     infoID += 1
    #     f_text = str(infoID) + ". " + item
    #     writeinto_htmlfile("test.html", html_head)
    #     writeinto_htmlfile("test.html", html_body.format(f_text))
    #     writeinto_htmlfile("test.html", html_footer)
    #
    #     for_count_and_read("count.tsv", "read.tsv", f_text)
