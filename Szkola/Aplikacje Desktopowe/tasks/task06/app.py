import tkinter as tk
import pandas as pd
from tkinter import ttk

root = tk.Tk()
root.geometry("800x400")
root.title("Wykroczenia")

kierowcy = pd.read_csv("kierowcy.txt", sep=';')
rejestr = pd.read_csv("rejestr.txt", sep=';')
taryfikator = pd.read_csv("taryfikator.txt", sep=';')

tabela = ttk.Treeview(root)
columns = ('ID', 'Data', 'Kierowca', 'Nr Rej.', 'Typ Wykroczenia', 'Punkty', 'Kwota')
tabela['columns'] = columns

scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=tabela.yview)
scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=tabela.xview)

tabela.column("#0", width=0, stretch=tk.NO)
tabela.column("ID", anchor=tk.CENTER, width=40)
tabela.column("Data", anchor=tk.CENTER, width=80)
tabela.column("Kierowca", anchor=tk.CENTER, width=120)
tabela.column("Nr Rej.", anchor=tk.CENTER, width=90)
tabela.column("Typ Wykroczenia", anchor=tk.CENTER, width=170)
tabela.column("Punkty", anchor=tk.CENTER, width=60)
tabela.column("Kwota", anchor=tk.CENTER, width=80)

for col in columns:
	tabela.heading(col, text=col)

tabela.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

controls = tk.Frame(root)
controls.pack(fill=tk.X, padx=8, pady=8)

summary = tk.Frame(root)
summary.pack(fill=tk.X, padx=8, pady=(0, 8))

summary_vars = {
	'count': tk.StringVar(value='Liczba wykroczeń: 0'),
	'amount': tk.StringVar(value='Całkowita kwota mandatów: 0.00'),
	'points': tk.StringVar(value='Całkowita liczba punktów karnych: 0'),
	'most_common': tk.StringVar(value='Najczęstsze wykroczenie: - (0)'),
	'top_driver': tk.StringVar(value='Kierowca z największą łączną kwotą mandatów: - (0.00)'),
}

for key in ('count', 'amount', 'points', 'most_common', 'top_driver'):
    ttk.Label(summary, textvariable=summary_vars[key], anchor='w').pack(side=tk.LEFT, padx=(0, 16), pady=2)

def find_column(df, candidates):
	for candidate in candidates:
		if candidate in df.columns:
			return candidate
	return None

def get_first_text(row, keys):
	for key in keys:
		value = row.get(key, '')
		if pd.notna(value) and str(value).strip():
			return str(value)
	return ''

driver_first_col = 'Imie'
driver_last_col = 'Nazwisko'
driver_reg_col = 'NrRejestracyjny'
violation_col = 'Wykroczenie'

driver_options = ['Wszyscy']
if driver_first_col in kierowcy.columns and driver_last_col in kierowcy.columns:
	full_names = (
		kierowcy[driver_first_col].astype(str).str.strip()
		+ ' '
		+ kierowcy[driver_last_col].astype(str).str.strip()
	).str.strip()
	driver_options.extend(sorted(full_names[full_names != ''].unique().tolist()))

violation_options = ['Wszystkie']
if violation_col:
	violation_options.extend(sorted(taryfikator[violation_col].astype(str).unique().tolist()))

merged = rejestr.copy()

merged = merged.merge(kierowcy, on='IdOsoby', how='left')

merged = merged.merge(taryfikator, left_on='IdWykroczenia', right_on='IdWykroczenia', how='left')

selected_driver = tk.StringVar(value='Wszyscy')
selected_violation = tk.StringVar(value='Wszystkie')

tk.Label(controls, text='Kierowca:').pack(side=tk.LEFT, padx=(0, 6))
driver_combo = ttk.Combobox(controls, textvariable=selected_driver, values=driver_options, state='readonly', width=24)
driver_combo.pack(side=tk.LEFT, padx=(0, 12))

tk.Label(controls, text='Typ wykroczenia:').pack(side=tk.LEFT, padx=(0, 6))
violation_combo = ttk.Combobox(controls, textvariable=selected_violation, values=violation_options, state='readonly', width=24)
violation_combo.pack(side=tk.LEFT, padx=(0, 12))

def refresh_table(_):
	for item in tabela.get_children():
		tabela.delete(item)

	filtered = merged.copy()

	if selected_driver.get() != 'Wszyscy' and driver_first_col in filtered.columns and driver_last_col in filtered.columns:
		full_names = (
			filtered[driver_first_col].fillna('').astype(str).str.strip()
			+ ' '
			+ filtered[driver_last_col].fillna('').astype(str).str.strip()
		).str.strip()
		filtered = filtered[full_names == selected_driver.get()]

	if selected_violation.get() != 'Wszystkie' and violation_col:
		filtered = filtered[filtered[violation_col].astype(str) == selected_violation.get()]

	count = len(filtered)
	points_col = find_column(filtered, ['Punkty'])
	points_total = int(pd.to_numeric(filtered[points_col], errors='coerce').fillna(0).sum()) if points_col else 0
	amount_col = find_column(filtered, ['Kwota'])
	amount_total = float(pd.to_numeric(filtered[amount_col], errors='coerce').fillna(0).sum()) if amount_col else 0.0

	violation_name_col = find_column(filtered, ['Wykroczenie'])
	if violation_name_col and not filtered.empty:
		violations = filtered[violation_name_col].astype(str).replace('nan', '').str.strip()
		violations = violations[violations != '']
		if not violations.empty:
			vc = violations.value_counts()
			top_violation = vc.idxmax()
			top_violation_count = int(vc.max())
		else:
			top_violation = '-'
			top_violation_count = 0
	else:
		top_violation = '-'
		top_violation_count = 0

	if driver_first_col in filtered.columns and driver_last_col in filtered.columns and not filtered.empty:
		full_names = (
			filtered[driver_first_col].astype(str).str.strip()
			+ ' '
			+ filtered[driver_last_col].astype(str).str.strip()
		).str.strip()
		total_by_driver = filtered.copy()
		total_by_driver['_driver_name'] = full_names
		total_by_driver['_amount'] = pd.to_numeric(total_by_driver[amount_col], errors='coerce').fillna(0) if amount_col else 0
		driver_totals = total_by_driver.groupby('_driver_name')['_amount'].sum()
		if not driver_totals.empty:
			top_driver = driver_totals.idxmax()
			top_driver_amount = float(driver_totals.max())
		else:
			top_driver = '-'
			top_driver_amount = 0.0
	else:
		top_driver = '-'
		top_driver_amount = 0.0

	summary_vars['count'].set(f'Liczba wykroczeń: {count}')
	summary_vars['amount'].set(f'Całkowita kwota mandatów: {amount_total:.2f}')
	summary_vars['points'].set(f'Całkowita liczba punktów karnych: {points_total}')
	summary_vars['most_common'].set(f'Najczęstsze wykroczenie: {top_violation} ({top_violation_count})')
	summary_vars['top_driver'].set(f'Kierowca z największą łączną kwotą mandatów: {top_driver} ({top_driver_amount:.2f})')

	for _, row in filtered.iterrows():
		amount = row.get('Kwota', 0)
		try:
			amount_text = f"{float(amount):.2f}"
		except ValueError:
			amount_text = "0.00"
		tabela.insert(
			'',
			tk.END,
			values=(
				row.get('IdZdarzenia'),
				row.get('Data', row.get('data', '')),
				f"{row.get(driver_first_col, '')} {row.get(driver_last_col, '')}".strip(),
				row.get(driver_reg_col),
				row.get('Wykroczenie'),
				row.get('Punkty'),
				amount_text,
			),
		)

def reset_filters():
	selected_driver.set("Wszyscy")
	selected_violation.set("Wszystkie")
	refresh_table(0)

driver_combo.bind('<<ComboboxSelected>>', refresh_table)
violation_combo.bind('<<ComboboxSelected>>', refresh_table)

tk.Button(controls, text='Resetuj', command=reset_filters).pack(side=tk.LEFT)

refresh_table(0)

scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


root.mainloop()
