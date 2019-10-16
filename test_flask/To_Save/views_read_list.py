# -*- coding: utf-8 -*-
from app.crud import crud
from flask import render_template
from app.orm import ORM
from app.models import Employee, Hobby
from app.crud.views_common import page
from pyecharts import Pie, Funnel, Bar, WordCloud
from sqlalchemy import func
from app.params import *


# 職位統計 餅狀圖
def pie_html(title, key, val):
    pie = Pie(title, title_pos="center", width="100%", height=300)
    pie.add(
        "",
        key,
        val,
        is_random=True,
        radius=[30, 75],
        rosetype="area",
        is_legend_show=False,
        is_label_show=True
    )
    return pie.render_embed()

# 學歷統計 漏斗圖
def funnel_html(title, key, val):
    funnel = Funnel(
        title,
        title_pos="center",
        width="100%",
        height=300
    )
    funnel.add(
        "",
        key,
        val,
        is_label_show=True,
        label_pos="outside",
        legend_orient="vertical",
        legend_pos="left"
    )
    return funnel.render_embed()


# 愛好統計 詞雲
def wordcloud_html(title, key, val):
    wordcloud = WordCloud(
        title,
        title_pos="center",
        width="100%",
        height=300
    )
    wordcloud.add(
        "",
        key,
        val,
        word_size_range=[20, 100]
    )
    return wordcloud.render_embed()

# 性別統計 柱狀圖
def bar_html(title, key, val):
    bar = Bar(title, title_pos="center", width="100%", height=300)
    bar.add("", key, val, mark_line=["min", "max"])
    return bar.render_embed()


@crud.route("/", methods=("GET", "POST"))
@crud.route("/read/list/", methods=("GET", "POST"))
def read_list():
    data = dict(
        title="員工列表"
    )
    arr = None
    session = ORM.db()
    try:
        model = session.query(Employee).order_by(Employee.id.desc())
        arr = page(model)
        # 按照職位分組統計查詢
        
        job = session.query(Employee.job, func.count(
            Employee.id)).group_by(Employee.job).all()
        job_dict = {
            v[0]: v[1]
            for v in job
        }
        data['job_pie'] = pie_html(
            "職位統計",
            job_list,
            [job_dict.get(k + 1, 0) for k, v in enumerate(job_list)]
        )
        # 按照學歷分組統計查詢
        edu = session.query(Employee.edu, func.count(Employee.id)).group_by(Employee.edu).all()
        edu_dict = {
            v[0]: v[1]
            for v in edu
        }
        data["edu_funnel"] = funnel_html(
            "學歷統計",
            edu_list,
            [edu_dict.get(k + 1, 0) for k, v in enumerate(edu_list)]
        )
        # 按照性別分組統計查詢
        sex = session.query(Employee.sex, func.count(Employee.id)).group_by(Employee.sex).all()
        sex_dict = {
            v[0]: v[1]
            for v in sex
        }
        data["sex_bar"] = bar_html(
            "性別統計",
            sex_list,
            [sex_dict.get(k + 1, 0) for k, v in enumerate(sex_list)]
        )
        # 按照愛好分組統計查詢
        hobby = session.query(Hobby.hobby_key, func.count(Hobby.id)).group_by(Hobby.hobby_key).all()
        hobby_dict = {
            v[0]: v[1]
            for v in hobby
        }
        data['hobby_wc'] = wordcloud_html(
            "愛好詞雲",
            hobby_list,
            [hobby_dict.get(k + 1, 0) for k, v in enumerate(hobby_list)]
        )
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    data["arr"] = arr
    return render_template("read_list.html", data=data)

"""       # 按照学历分组统计查询
        edu = session.query(Employee.edu, func.count(
            Employee.id)).group_by(Employee.edu).all()
        edu_dict = {
            v[0]: v[1]
            for v in edu
        }
        data["edu_funnel"] = funnel_html(
            "學歷統計",
            edu_list,
            [edu_dict.get(k + 1, 0) for k, v in enumerate(edu_list)]
        )
        # 按照性别分组统计查询
        sex = session.query(Employee.sex, func.count(
            Employee.id)).group_by(Employee.sex).all()
        sex_dict = {
            v[0]: v[1]
            for v in sex
        }
        data["sex_bar"] = bar_html(
            "性別統計",
            sex_list,
            [sex_dict.get(k + 1, 0) for k, v in enumerate(sex_list)]
        )
        # 按爱好分组查询统计
        hobby = session.query(Hobby.hobby_key, func.count(
            Hobby.id)).group_by(Hobby.hobby_key).all()
        hobby_dict = {
            v[0]: v[1]
            for v in hobby
        }
        data['hobby_wc'] = wordcloud_html(
            "愛好詞雲",
            hobby_list,
            [hobby_dict.get(k + 1, 0) for k, v in enumerate(hobby_list)]
        )
"""