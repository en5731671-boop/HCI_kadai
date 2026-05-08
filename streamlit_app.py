import streamlit as st

st.set_page_config(page_title="セルフレジUI比較", layout="wide")

# -----------------------------
# 初期化
# -----------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "bad"

if "page" not in st.session_state:
    st.session_state.page = "home"

if "cart" not in st.session_state:
    st.session_state.cart = []


PRODUCTS = [
    ("おにぎり", 140),
    ("サンドイッチ", 320),
    ("お茶", 120),
    ("カップ麺", 230),
]


def go(page):
    st.session_state.page = page
    st.rerun()


# -----------------------------
# モード切替
# -----------------------------
st.sidebar.title("UI切替")
mode = st.sidebar.radio("表示", ["改善前UI（悪い設計）", "改善後UI（良い設計）"])

st.session_state.mode = "bad" if "改善前" in mode else "good"

if st.sidebar.button("リセット"):
    st.session_state.page = "home"
    st.session_state.cart = []
    st.rerun()


# =====================================================
# ■ 改善前UI（悪い設計：混乱型）
# =====================================================
if st.session_state.mode == "bad":

    st.title("セルフレジ（改善前UI）")

    st.write("※全部が同じ画面にあり、操作順が分かりにくい")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("商品（バラバラ操作）")
        for name, price in PRODUCTS:
            if st.button(f"{name} ¥{price}"):
                st.session_state.cart.append((name, price))

    with col2:
        st.subheader("操作メニュー（多すぎ）")
        st.button("ポイントカード読み取り")
        st.button("クーポン入力")
        st.button("レシート設定")
        st.button("支払い")
        st.button("ヘルプ")

    st.markdown("---")
    st.subheader("カート")
    for item in st.session_state.cart:
        st.write(f"{item[0]} - ¥{item[1]}")

    st.write(f"合計：¥{sum(p for _, p in st.session_state.cart)}")


# =====================================================
# ■ 改善後UI（良い設計：画面遷移型）
# =====================================================
else:

    st.title("セルフレジ（改善後UI）")

    # -----------------------------
    # ホーム
    # -----------------------------
    if st.session_state.page == "home":
        st.write("ようこそ。スキャンを開始してください。")

        if st.button("開始"):
            go("scan")

    # -----------------------------
    # スキャン
    # -----------------------------
    elif st.session_state.page == "scan":

        st.subheader("スキャン画面")

        for name, price in PRODUCTS:
            if st.button(f"＋ {name} ¥{price}"):
                st.session_state.cart.append((name, price))

        if st.button("カートへ進む"):
            go("cart")

        if st.button("戻る"):
            go("home")

    # -----------------------------
    # カート
    # -----------------------------
    elif st.session_state.page == "cart":

        st.subheader("カート確認")

        for name, price in st.session_state.cart:
            st.write(f"{name} - ¥{price}")

        st.write(f"合計：¥{sum(p for _, p in st.session_state.cart)}")

        if st.button("支払いへ"):
            go("pay")

        if st.button("スキャンに戻る"):
            go("scan")

    # -----------------------------
    # 支払い
    # -----------------------------
    elif st.session_state.page == "pay":

        st.subheader("支払い")

        st.write(f"合計金額：¥{sum(p for _, p in st.session_state.cart)}")

        method = st.radio("支払い方法", ["現金", "カード", "QR決済"])

        if st.button("支払い確定"):
            st.session_state.cart = []
            go("done")

        if st.button("戻る"):
            go("cart")

    # -----------------------------
    # 完了
    # -----------------------------
    elif st.session_state.page == "done":

        st.success("支払い完了")

        if st.button("最初へ"):
            go("home")
