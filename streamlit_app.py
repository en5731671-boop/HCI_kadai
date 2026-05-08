import streamlit as st

st.set_page_config(page_title="UI改善デモ", layout="wide")

st.title("UI改善デモ：セルフレジ比較")

mode = st.radio("表示モードを選択", ["改善前（使いにくいUI）", "改善後（改善UI）"])


# -------------------------
# 改善前UI
# -------------------------
if mode == "改善前（使いにくいUI）":
    st.header("セルフレジ（改善前）")

    st.write("※どれを押せばいいか分かりにくいUI")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("商品スキャン"):
            st.error("エラー：次の操作が不明です")

        if st.button("会計"):
            st.warning("支払い方法を先に選択してください")

    with col2:
        if st.button("ポイント利用"):
            st.warning("ポイント残高が不明です")

        if st.button("クーポン入力"):
            st.error("入力形式が違います")

    with col3:
        if st.button("ヘルプ"):
            st.info("どこを押せばいいか分かりません")

    st.write("👉 問題点：情報が分散していて操作の順番が分からない")


# -------------------------
# 改善後UI
# -------------------------
else:
    st.header("セルフレジ（改善後）")

    st.write("※1ステップずつ進むガイド型UI")

    step = st.session_state.get("step", 1)

    if step == 1:
        st.subheader("① 商品をスキャンしてください")
        if st.button("スキャン完了"):
            st.session_state.step = 2
            st.rerun()

    elif step == 2:
        st.subheader("② 支払い方法を選択")
        payment = st.selectbox("支払い方法", ["現金", "クレジットカード", "QR決済"])
        if st.button("次へ"):
            st.session_state.step = 3
            st.rerun()

    elif step == 3:
        st.subheader("③ クーポン・ポイント（任意）")
        use_coupon = st.checkbox("クーポンを使う")
        use_point = st.checkbox("ポイントを使う")

        if st.button("会計へ進む"):
            st.session_state.step = 4
            st.rerun()

    elif step == 4:
        st.subheader("④ 会計完了")
        st.success("支払いが完了しました！ありがとうございました")
        if st.button("最初に戻る"):
            st.session_state.step = 1
            st.rerun()

    st.write("👉 改善点：操作が順番化され、迷わないUI")
