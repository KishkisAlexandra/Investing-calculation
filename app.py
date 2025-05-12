import streamlit as st

st.title("📈 Инвестиционный калькулятор: Кредит → Депозит")

loan_amount = st.slider("Сумма кредита (₽)", 100_000, 10_000_000, 1_000_000, step=100_000)
loan_term = st.slider("Срок кредита (мес)", 6, 120, 24, step=6)
credit_rate = st.slider("Ставка по кредиту (%)", 1.0, 30.0, 14.0, step=0.1)
deposit_rate = st.slider("Ставка по депозиту (%)", 1.0, 30.0, 17.0, step=0.1)
capitalization = st.checkbox("Капитализация процентов на депозите", value=True)
tax_rate = st.slider("Налог на доход (%)", 0.0, 20.0, 13.0, step=0.5)

monthly_credit_rate = credit_rate / 12 / 100
monthly_deposit_rate = deposit_rate / 12 / 100
tax_multiplier = 1 - tax_rate / 100

if monthly_credit_rate > 0:
    annuity = loan_amount * (monthly_credit_rate * (1 + monthly_credit_rate) ** loan_term) / ((1 + monthly_credit_rate) ** loan_term - 1)
else:
    annuity = loan_amount / loan_term

deposit_balance = loan_amount
total_deposit_interest = 0

for _ in range(loan_term):
    if capitalization:
        interest = deposit_balance * monthly_deposit_rate
        deposit_balance += interest
    else:
        interest = loan_amount * monthly_deposit_rate
    total_deposit_interest += interest

net_interest = total_deposit_interest * tax_multiplier
total_credit_paid = annuity * loan_term
profit = loan_amount + net_interest - total_credit_paid

st.subheader("📊 Результаты:")
st.write(f"💸 Ежемесячный платёж по кредиту: **{annuity:,.2f} ₽**")
st.write(f"🏦 Доход по депозиту (после налога): **{net_interest:,.2f} ₽**")
st.write(f"📉 Общая сумма выплат по кредиту: **{total_credit_paid:,.2f} ₽**")
st.write(f"🧾 Чистая прибыль/убыток: **{profit:,.2f} ₽**")
