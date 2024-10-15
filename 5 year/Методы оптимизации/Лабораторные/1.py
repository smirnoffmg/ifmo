import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pulp
from scipy.optimize import linprog

# Параметры задачи
num_projects: int = 5  # Количество проектов
num_sources: int = 5  # Количество источников финансирования
num_periods: int = 4  # Количество периодов

# Фиксируем seed для воспроизводимости
np.random.seed(42)


# Визуализация денежных потоков проектов и источников по периодам
def plot_cashflows(df: pd.DataFrame):
    periods = df["Период"]

    # Линии для проектов
    plt.figure(figsize=(12, 8))
    for i in range(num_projects):
        plt.plot(periods, df[f"Проект {i+1}"], label=f"Проект {i+1}", marker="o")

    # Линии для источников
    for i in range(num_sources):
        plt.plot(
            periods,
            df[f"Источник {i+1}"],
            label=f"Источник {i+1}",
            linestyle="--",
            marker="x",
        )

    # Собственные средства (только в периоде 0)
    plt.plot(
        periods,
        df["Собственные средства"],
        label="Собственные средства",
        linestyle=":",
        marker="s",
        color="black",
    )

    # Оформление графика
    plt.title("Денежные потоки по проектам и источникам финансирования")
    plt.xlabel("Периоды")
    plt.ylabel("Денежные потоки")
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()


# Функция для генерации потоков денежных средств
def generate_cash_flows(min_value: int, max_value: int, num_periods: int) -> np.ndarray:
    """
    Генерирует потоки денежных средств с хотя бы одним положительным и одним отрицательным
    значением.

    :param min_value: Минимальное значение в потоке
    :param max_value: Максимальное значение в потоке
    :param num_periods: Количество периодов
    :return: Массив сгенерированных данных
    """
    cash_flows = np.random.choice(
        np.arange(min_value, max_value + 1, 5), num_periods, replace=True
    )

    # Проверяем, есть ли хотя бы одно положительное и одно отрицательное значение
    if np.all(cash_flows >= 0) or np.all(cash_flows <= 0):
        pos_idx = (
            np.random.choice(np.where(cash_flows > 0)[0], 1)
            if np.any(cash_flows > 0)
            else np.random.choice(num_periods, 1)
        )
        neg_idx = (
            np.random.choice(np.where(cash_flows < 0)[0], 1)
            if np.any(cash_flows < 0)
            else np.random.choice(num_periods, 1)
        )
        cash_flows[pos_idx] = abs(cash_flows[pos_idx])
        cash_flows[neg_idx] = -abs(cash_flows[neg_idx])

    return cash_flows


# Проверка выполнения инвестиционного условия
def validate_investment_condition(
    projects: np.ndarray,
    sources: np.ndarray,
    own_funds: float,
) -> bool:
    """
    Проверяет условие, что сумма вложений в проекты больше или равна сумме доходов от
    всех источников финансирования, включая собственные средства.

    :param projects: Массив денежных потоков по проектам
    :param sources: Массив денежных потоков по источникам
    :param own_funds: Собственные средства
    :return: True, если условие выполняется, иначе False
    """
    total_project_investment = abs(
        projects[projects < 0].sum()
    )  # Вложения в проекты (отрицательные значения)
    total_source_income = (
        sources[sources > 0].sum() + own_funds
    )  # Доходы от источников плюс собственные средства
    return total_project_investment >= total_source_income


def generate_df() -> pd.DataFrame:

    projects = np.zeros((num_projects, num_periods))
    sources = np.zeros((num_sources, num_periods))
    own_funds = np.random.randint(50, 100)

    # Генерируем проекты и источники поэтапно
    for i in range(num_projects):
        while True:
            project_cash_flows = generate_cash_flows(-200, 200, num_periods)
            if (
                project_cash_flows.sum()
                > abs(project_cash_flows[project_cash_flows < 0].sum()) * 1.1
            ):
                projects[i, :] = project_cash_flows
                break

    # Для источников и собственных средств будем следить за выполнением условия "полузакрытости"
    while True:
        for i in range(num_sources):
            while True:
                source_cash_flows = generate_cash_flows(-150, 150, num_periods)
                if (
                    source_cash_flows.sum() < 0
                    and abs(source_cash_flows[source_cash_flows > 0].sum())
                    >= abs(source_cash_flows.sum()) * 1.15
                ):
                    sources[i, :] = source_cash_flows
                    break

        # Проверка инвестиционного условия с учетом собственных средств в периоде 0
        if validate_investment_condition(projects, sources, own_funds):
            break

    columns = (
        ["Период"]
        + [f"Проект {i+1}" for i in range(num_projects)]
        + [f"Источник {i+1}" for i in range(num_sources)]
        + ["Собственные средства"]
    )
    data = np.hstack([np.arange(num_periods).reshape(-1, 1), projects.T, sources.T])

    # Добавляем собственные средства в период 0
    data_with_own_funds = np.column_stack([data, [own_funds] + [0] * (num_periods - 1)])

    # Создаем DataFrame для отображения данных
    return pd.DataFrame(data_with_own_funds, columns=columns)


def find_profit_w_pulp(df: pd.DataFrame):
    # Создаем задачу линейного программирования для максимизации прибыли
    prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

    # Переменные для проектов (доля вложений)
    x_vars = [
        pulp.LpVariable(f"x{i+1}", lowBound=0, upBound=1) for i in range(num_projects)
    ]

    # Переменные для источников финансирования (доля использования)
    y_vars = [
        pulp.LpVariable(f"y{j+1}", lowBound=0, upBound=1) for j in range(num_sources)
    ]

    # Целевая функция: максимизация чистой прибыли
    profit_from_projects = pulp.lpSum(
        [x_vars[i] * df[f"Проект {i+1}"].sum() for i in range(num_projects)]
    )
    cost_from_sources = pulp.lpSum(
        [y_vars[j] * df[f"Источник {j+1}"].sum() for j in range(num_sources)]
    )
    own_funds = df["Собственные средства"].iloc[0]

    # Задаем целевую функцию: максимизация чистой прибыли
    prob += profit_from_projects - cost_from_sources, "Чистая прибыль"

    # Ограничение: вложения >= доходов от источников финансирования + собственные средства
    prob += (
        profit_from_projects >= cost_from_sources + own_funds,
        "Ограничение на финансирование",
    )

    # Решаем задачу
    prob.solve()

    # Результаты
    print(f"Статус решения: {pulp.LpStatus[prob.status]}")
    for v in prob.variables():
        print(f"{v.name} = {v.varValue}")

    print(f"Максимальная чистая прибыль: {pulp.value(prob.objective)}")


def find_profit_w_scipy(df: pd.DataFrame):
    # Получаем суммы денежных потоков по проектам и источникам
    project_sums = np.array([df[f"Проект {i+1}"].sum() for i in range(num_projects)])
    source_sums = np.array([df[f"Источник {j+1}"].sum() for j in range(num_sources)])
    own_funds = df["Собственные средства"].iloc[0]

    # Коэффициенты для целевой функции
    # Мы минимизируем отрицательную чистую прибыль, поэтому используем -project_sums для минимизации
    c = np.concatenate([-project_sums, source_sums])

    # Матрица ограничений (включая собственные средства)
    A_eq = np.concatenate([project_sums, -source_sums]).reshape(1, -1)
    b_eq = np.array([own_funds])

    # Границы для переменных (от 0 до 1)
    x_bounds = [(0, 1) for _ in range(num_projects + num_sources)]

    # Решаем задачу с помощью линейного программирования (метод 'highs')
    result_scipy = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method="highs")

    # Выводим результаты
    if result_scipy.success:
        print(f"Максимальная чистая прибыль (SciPy): {-result_scipy.fun}")
        for i in range(num_projects):
            print(f"Проект {i+1}: {result_scipy.x[i]} (доля вложений)")
        for j in range(num_sources):
            print(
                f"Источник {j+1}: {result_scipy.x[num_projects + j]} (доля использования)"
            )
    else:
        print("Решение не найдено.")


def main():
    df = generate_df()
    # df.to_csv("gen.csv")
    plot_cashflows(df)
    # find_profit_w_pulp(df)
    # find_profit_w_scipy(df)


if __name__ == "__main__":
    main()
