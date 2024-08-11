import matplotlib.pyplot as plt
import pandas as pd

# Создаем DataFrame с данными для диаграммы Ганта
tasks = {
    'Task': [
        'Мыть посуду', 'Пропылесосить паласы', 'Мыть столы', 'Снять шторы', 'Повесить шторы', 'Мыть окна',
        'Снять паутину с потолков', 'Закупка', 'Вызов сантехника', 'Уничтожение насекомых', 'Вызов крысолова'
    ],
    'Start': [
        9, 11, 13, 9, 12, 9, 12, 10, 9, 11, 10
    ],
    'Finish': [
        11, 13, 17, 10, 14, 17, 15, 10.5, 9.25, 11.33, 10.25
    ],
    'Resource': [
        'Член 1', 'Член 1', 'Член 1', 'Член 2', 'Член 2', 'Мойщики', 'Член 3', 'Член 3', 'Сантехник', 'Специалист', 'Крысолов'
    ]
}

df = pd.DataFrame(tasks)

# Настраиваем график
fig, ax = plt.subplots(figsize=(12, 8))

# Создаем полосы для диаграммы
for idx, row in df.iterrows():
    ax.barh(row['Resource'], row['Finish'] - row['Start'], left=row['Start'])

# Настройка осей и меток
ax.set_xlabel('Время (часы)')
ax.set_ylabel('Ресурс')
ax.set_title('Диаграмма Ганта для уборки офиса с учетом бюджета')

# Настройка меток по оси X
ax.set_xticks(range(9, 18))
ax.set_xticklabels([str(i) + ':00' for i in range(9, 18)])

# Показ диаграммы
plt.tight_layout()
plt.show()