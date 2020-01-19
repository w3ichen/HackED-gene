def merge(main, secondary):
	main_list = list(main.keys())
	for key in main_list:
		main[key].extend(secondary[key])
		
