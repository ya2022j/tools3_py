#! coding:utf-8



import requests
from bs4 import BeautifulSoup


# 大一些文本直接用三个双引号来处理
html_doc = """
<article class="break-word borderGray mt-20">
        <div class="jobListHeader jobListHeader-jobSearch o-h">
    <div class="o-h">
        <h4>
                        <a href="/company.php?m_id=a0C1000000sgO4l" target="_blank" class="pcIcon-after pcIcon-54-after pcIcon-blank pcIcon-forShowReview fs-18" data-_v-event-logger-key="job_search_result_click" data-_v-event-logger-parameter="company" data-_v-event-logger-multi="">
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

        </div>
                </div>
    <p class="f-l lh-high">SIer、ソフト開発、システム運用業界</p>
</div>

    <div class="pt-25 pr-25 pl-25">
        <div class="o-h p-l">
            <div class="o-h ml-5">
                <div>
                                                                                                    <p class="darkgray mr-10 fw-b d-ib">PR・広告宣伝・販促</p><ul class="d-ib"><li class="mark-grayBorder nowrap mr-5 mb-5">正社員</li><li class="mark-gold mark-small mr-5 mb-5">NEW</li><li class="d-i mb-5 ml-5 v-m"><img class="v-t" src="https://assets.vorkers.com/images/common/openwork_apply.svg" width="100" height="18" alt="OpenWork応募"></li></ul>
                    </div><h5 class="fs-20 lh-1o5 mt-5">
                    <a class="gtm_vr pcIcon-after pcIcon-54-after pcIcon-blank" href="/a0C1000000sgO4l/recruit?j=31c3850aff9c1ec2" target="_blank">
                        <span class="pcIcon-blank_border">SMB向けマーケティングマネージャー</span>
                    </a>
                </h5>
            </div>
        </div>
    </div>
    <div class="pl-25 pb-20 pr-25">
        <div class="mt-20">
                                    <div class="o-h">
                                    <div class="f-r w-280 backgroundLightGray t-c">
                                                <img src="https://image.vorkers.com/resize/643x909/recruiting/51865/job_offer/22018.jpg" class="max-h-225 max-w-280" alt="">
                    </div>
                                                    <p class="jobListJobDescription w-650">SMBセグメントは20万社強のマーケットとなっており、さらに同マーケットに対して法改正のトレンドに合わせた新しいプロダクトをローンチしています。当社が保有する大規模なハウスリストDBを活用し、ナーチャリング型のコミュニケーション戦略でマーケット攻略の実現をマネージャーとして急ピッチで目指していただきます。

【業務詳細】
・インサイドセールスやフィールドセールスを巻き込んだマーケティング戦略立案及びKPI設計・施策と予算のアロケーション
・実行オペレーションおよび組織体制の構築、マネジメント
・</p>
                                                    <table class="table-job w-650">
                                                    <tbody><tr>
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
                                    リモート可
                                </td>
                            </tr>
                                            </tbody></table>
                            </div>
        </div>
    </div>
    <div class="t-c p-r mb-20">
        <p class="jobListBody_date">12時間前</p>        <ul>
            <li class="d-i mr-20">
                                                            <a href="javascript:void(0);" data-tooltip="気になる求人をリストに入れてまとめてチェックできます" data-_vmodal-type="b" class="button button-jobBookmark jsTooltip jsLoginModalTrigger  fs-15" data-_v-event-logger-key="job_search_result_standard_click" data-_v-event-logger-parameter="bookmark_job_offer_no_login" data-_v-event-logger-multi="">
        <span class="pcIcon pcIcon-69 pcIcon-jobBookmark">気になる</span>
    </a>

            </li>
            <li class="d-i">
                                <a class="gtm_vr button button-usuallyBlue fs-16 w-250" href="/a0C1000000sgO4l/recruit?j=31c3850aff9c1ec2" target="_blank"><span class="pcIcon-after pcIcon-54-after pcIcon-blank">この求人を見る</span></a>
            </li>
        </ul>
    </div>
</article>
"""



class BS4Parse():
    def __init__(self,html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def parseOneElement(self,tagName):
        trans_list = []
        for single_tag in soup.select(tagName):
            trans_list.append("".join(single_tag.text.split()))
        tagText = " ".join(trans_list)
        return tagText

    def fetchAllText(self):
        AllText = "".join(self.soup.get_text().split())
        return AllText

b = BS4Parse(html_doc)
ret = b.fetchAllText()
print(ret)


