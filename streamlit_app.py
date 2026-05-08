import streamlit as st
import random

st.set_page_config(page_title="セルフレジUI比較", layout="wide")

# -----------------------------
# ダミー商品
# -----------------------------
PRODUCTS = [
    {"name": "おにぎり（鮭）", "price": 140},
    {"name": "おにぎり（ツナマヨ）", "price": 150},
    {"name": "ペットボトルお茶", "price": 120},
    {"name": "カップラーメン", "price": 230},
    {"name": "サンドイッチ", "price": 320},
    {"name": "チョコレート", "price": 180},
]

if "cart" not in st.session_state:
    st.session_state.cart = []

if "step" not in st.session_state:
    st.session_state.step = "select"

def cart_total():
    return sum(item["price"] for item in st.session_state.cart)


st.title("コンビニセルフレジUI改善デモ（リアル版）")

mode = st.radio("表示モード", ["改善前UI（混乱する実機風）", "改善後UI（設計改善版）"])


# =====================================================
# 改善前UI（リアルに“ごちゃついた実機風”）
# =====================================================
if mode == "改善前UI（混乱する実機風）":
    st.subheader("セルフレジ画面（旧型）")

    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        st.markdown("### 商品一覧（スクロール）")
        for p in PRODUCTS:
            if st.button(f"{p['name']} ¥{p['price']}"):
                st.session_state.cart.append(p)

    with col2:
        st.markdown("### 操作メニュー（多すぎる問題）")
        if st.button("ポイントカード読み取り"):
            st.warning("カード未検出")
        if st.button("クーポン読取"):
            st.error("読み取り失敗")
        if st.button("支払いへ進む"):
            st.info("支払い方法未選択です")
        if st.button("レシート設定"):
            st.write("設定画面（複雑）")
        if st.button("ヘルプ"):
            st.write("説明が長すぎて読まれない")

    with col3:
        st.markdown("### カート")
        if st.session_state.cart:
            for i, item in enumerate(st.session_state.cart):
                st.write(f"{item['name']} - ¥{item['price']}")
        else:
            st.write("空")

        st.markdown(f"**合計：¥{cart_total()}**")

        if st.button("会計（未整理状態）"):
            st.error("エラー：手順が不明確")


    st.info("問題点：情報が同時に出すぎて“どこを見ればいいか分からない”")


# =====================================================
# 改善後UI（実在レジに寄せた設計）
# =====================================================
else:
    st.subheader("セルフレジ画面（改善版）")

    col1, col2 = st.columns([3, 2])

    # -------------------------
    # 左：商品スキャンエリア
    # -------------------------
    with col1:
        st.markdown("## スキャン（商品登録）")

        st.caption("商品をタップするとスキャンされます")

        for p in PRODUCTS:
            if st.button(f"＋ {p['name']}（¥{p['price']}）"):
                st.session_state.cart.append(p)

        st.markdown("---")

        st.markdown("### カート内容")
        if st.session_state.cart:
            for i, item in enumerate(st.session_state.cart):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.write(f"{item['name']}")
                with c2:
                    st.write(f"¥{item['price']}")
        else:
            st.write("商品がまだありません")


    # -------------------------
    # 右：決済エリア（固定UI風）
    # -------------------------
    with col2:
        st.markdown("## 決済パネル")

        st.metric("合計金額", f"¥{cart_total()}")

        st.markdown("### 支払い方法")
        pay = st.radio("", ["現金", "クレジットカード", "QR決済"], index=0)

        st.markdown("### オプション")
        coupon = st.checkbox("クーポン使用")
        point = st.checkbox("ポイント使用")

        st.markdown("---")

        if st.button("▶ 支払い確定"):
            if len(st.session_state.cart) == 0:
                st.error("商品がありません")
            else:
                st.success("支払い完了（実機イメージ）")
                st.session_state.cart = []

        if st.button("リセット"):
            st.session_state.cart = []

    st.info("改善点：①導線を左→右に固定 ②操作を決済に集約 ③情報密度を整理")
