pip install ipywidgets
import numpy as np
import ipywidgets as widgets
from IPython.display import display, Markdown

def calc_credit_deposit(
    loan_amount, loan_term_months, credit_rate, deposit_rate, capitalization, tax_rate
):
    # Конвертация годовых ставок в месячные
    monthly_credit_rate = credit_rate / 12 / 100
    monthly_deposit_rate = deposit_rate / 12 / 100
    tax_multiplier = 1 - tax_rate / 100

    # Аннуитетный платёж
    if monthly_credit_rate > 0:
        annuity_payment = loan_amount * (monthly_credit_rate * (1 + monthly_credit_rate) ** loan_term_months) / ((1 + monthly_credit_rate) ** loan_term_months - 1)
    else:
        annuity_payment = loan_amount / loan_term_months

    # Доход по депозиту
    deposit_balance = loan_amount
    total_deposit_interest = 0

    for _ in range(loan_term_months):
        if capitalization:
            interest = deposit_balance * monthly_deposit_rate
            deposit_balance += interest
        else:
            interest = loan_amount * monthly_deposit_rate
        total_deposit_interest += interest

    net_interest = total_deposit_interest * tax_multiplier
    total_credit_payment = annuity_payment * loan_term_months
    profit = loan_amount + net_interest - total_credit_payment

    # Вывод
    display(Markdown(f"""
### 📈 Результаты:
- 💸 Ежемесячный платёж по кредиту: **{annuity_payment:,.2f}**
- 🏦 Доход по депозиту (после налога): **{net_interest:,.2f}**
- 📉 Общая сумма выплат по кредиту: **{total_credit_payment:,.2f}**
- 🧾 Чистая прибыль/убыток: **{profit:,.2f}**
"""))


# Виджеты
widgets.interact(
    calc_credit_deposit,
    loan_amount=widgets.IntSlider(value=1_000_000, min=100_000, max=10_000_000, step=50_000, description='Сумма кредита'),
    loan_term_months=widgets.IntSlider(value=24, min=6, max=120, step=6, description='Срок (мес)'),
    credit_rate=widgets.FloatSlider(value=14.0, min=1.0, max=30.0, step=0.1, description='Кредит % год'),
    deposit_rate=widgets.FloatSlider(value=17.0, min=1.0, max=30.0, step=0.1, description='Депозит % год'),
    capitalization=widgets.Checkbox(value=True, description='Капитализация'),
    tax_rate=widgets.FloatSlider(value=13.0, min=0.0, max=20.0, step=0.5, description='Налог %'),
);
