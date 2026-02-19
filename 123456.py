import streamlit as st  #引用streamlit库，起别名st，streanlit可以不用管前端框架
import random           #引用随机数库
from datetime import datetime#引用时间库，获取当前时间


st.set_page_config(page_title="马年幸运签",page_icon="123456.png")#网页的标题


st.title("农历马年幸运数字生成器")#网页里面呈现的主标题
st.caption("用Python快速生成你的新年幸运数字")#标题下的小字注释


name = st.text_input("请输入你的名字", placeholder="例如：小明")#st.text:创建文本框；input(里面是提示文字)；placeholder是占位符，就相当于是默认写在上面的东西，输入后就被输入的东西；输入的内容赋值给name


if st.button("生成我的马年幸运数字", type="primary"):#st.button创建了一个按钮，返回的是真或者假（在判断时0表示假，其他为真）。
    if name: # 检查用户是否在输入框中输入了名字，输入了就为真，执行
        lucky_number= random.sample(range(1, 10), 3)# 从1到9（包含1，不包含10）的数字范围中，随机、不重复地抽取3个数字(利用range和random库)，组成一个列表，赋值给变量lucky_number
        st.balloons() 
        st.success(f"**{name}，你好！**")# 显示成功提示框，里面有用户输入的名字（f-string格式化字符串），**表示加粗
        st.markdown(f"### 你的丙午马年幸运数字是：")#Markdown 语法显示一个三级标题
        cols = st.columns(3)# 创建3个等宽的列
        for i, num in enumerate(lucky_number):# 遍历幸运数字列表，i是索引（0/1/2），num是对应的数字
            with cols[i]: # 把每个数字卡片放入对应的列中


                # 用markdown和HTML自定义数字卡片样式(只有美化作用，设置渐变背景、圆角等)
                st.markdown(f"""
                <div style='
                    background: linear-gradient(135deg, #FFD700, #FFA500);
                    border-radius: 15px;
                    padding: 30px 10px;
                    text-align: center;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                '>
                <h1 style='font-size: 48px; margin: 0; color: #8B0000;'>{num}</h1>
                </div>
                """, unsafe_allow_html=True)
        



        # 显示一个蓝色的信息框，内容是新年签文，解释每个数字的寓意。签文中动态填入当前的农历年份和三个幸运数字
        st.info(f"""
        **新年签文**
        这三个数字将伴随你在{datetime.now().year}丙午马年：
        1.  **{lucky_number[0]}** 代表 **锐意进取**
        2.  **{lucky_number[1]}** 代表 **稳如泰山**
        3.  **{lucky_number[2]}** 代表 **好运连连**
        """)
        

        total = sum(lucky_number)# 根据总和大小给出不同的建议，sum函数直接使用求和并赋值给变量total
        if total > 15:#若和大于15
            st.markdown(f"**建议**：数字之和较大（{total}），马年宜主动出击，开拓新领域！")
        else:#若不大于15
            st.markdown(f"**建议**：数字之和适中（{total}），马年宜稳扎稳打，深耕现有优势！")
    else:# 接最上面的判断（if name），如果用户未输入名字（name为空），显示警告提示
        st.warning("请输入你的名字再试哦~")

st.divider()#水平分割线

