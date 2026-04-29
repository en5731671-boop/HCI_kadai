import streamlit as st

st.title("セルフレジUI改善プロジェクト")

mode = st.sidebar.selectbox("表示を選択", ["改善前UI", "改善後UI"])

# =========================
# 改善前UI
# =========================
if mode == "改善前UI":

    st.header("改善前UI（問題のある設計）")

    st.subheader("操作1")
    st.text_input("商品コード入力してください")
    st.button("OK")

    st.subheader("操作2")
    st.text_input("支払い方法コード？")
    st.button("進む？")

    st.subheader("操作3")
    st.text_input("これでいい？")
    st.button("確定")

    st.error("問題点：操作手順が不明確・説明不足・誤操作が起きやすい")

# =========================
# 改善後UI
# =========================
elif mode == "改善後UI":

    st.header("改善後UI（改善設計）")

    step = st.radio(
        "操作ステップを選択",
        ["① 商品スキャン", "② 袋選択", "③ 支払い", "④ 完了"]
    )

    if step == "① 商品スキャン":
        st.subheader("商品スキャン")
        code = st.text_input("バーコードを入力")
        if code:
            st.success("商品を追加しました")

    elif step == "② 袋選択":
        st.subheader("袋の選択")
        bag = st.selectbox("サイズを選んでください", ["不要", "小", "中", "大"])
        st.info(f"選択中：{bag}")

    elif step == "③ 支払い":
        st.subheader("支払い方法")
        pay = st.radio("方法を選択", ["現金", "クレジットカード", "QRコード"])
        st.success(f"{pay} が選択されました")

    elif step == "④ 完了":
        st.success("会計が完了しました！ありがとうございました")
