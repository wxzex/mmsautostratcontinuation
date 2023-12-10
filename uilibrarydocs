class Window [
	Table flags -> default location for values

	Method Section(name)
		@name -> text for the Section

	Method Toggle(name, options, callback)
		@name -> text for toggle 
		@options -> array
			location (table) -> alternate table to put value in (default = window.flags)
			flag (string) -> index for value (e.g location.farming)
		@callback -> function to call when toggle is changed

		return -> [
			Method Set(number) -> sets toggle value
		]

	Method Slider(name, options, callback)
		@name -> text for slider 
		@options -> array
			location (table) -> alternate table to put value in (default = window.flags)
			flag (string) -> index for value (e.g location.farming)
			precise (boolean) -> wether to show full number or not -- e.g 0, 1 vs 0, 0.1, 0.2, ...
			default (number) -> default slider value
			min, max (number) -> self explanatory
		@callback(value) -> function to call when slider is changed

		return -> [
			Method Set(number) -> sets slider value
		]

	Method Dropdown(name, options, callback)
		@name -> text for dropdown 
		@options -> array
			location (table) -> alternate table to put value in (default = window.flags)
			flag (string) -> index for value (e.g location.farming)
			list -> list of objects to display
		@callback(new) -> function to call when dropdown is changed

		return -> [
			Method Refresh(array) -> resets dropdown.list and sets value to first value in array
		]

	Method Button(name, callback)
		@name -> text for button 
		@callback -> function to call when button is clicked

		return -> [
			Method Fire(<void>) -> calls callback
		]

	Method Bind(name, options, callback)
		@name -> text for keybind 
		@options -> array
			location (table)  -> alternate table to put value in (default = window.flags)
			flag (string)     -> index for value (e.g location.farming)
			kbonly (bool)     -> keyboard keys only (no mouse)
			default (bool)    -> default key for bind;

		@callback(key) -> function to call when bind is changed

	Method Box(name, options, callback)
		@name -> text for box 
		@options -> array
			location (table)  -> alternate table to put value in (default = window.flags)
			flag     (string) -> index for value (e.g location.farming)
			min, max   (number) -> self explanatory
			type (string) -> if type is "number", box will only accept numbers
			
		@callback(box, new, old, enter) -> function to call when box is changed
			box -> box object;
			new -> new value;
			old -> old value;
			enter -> wether enter was pressed

		returns -> box object (Instance)

	Method SearchBox(name, options, callback)
		@name -> text for searchbox 
		@options -> array
			location (table) -> alternate table to put value in (default = window.flags)
			flag (string) -> index for value (e.g location.farming)
			list -> list of objects to search for
		@callback(new) -> function to call when dropdown is changed

		return -> [
			Method Refresh(array) -> resets dropdown.list and sets value to first value in array
		]
]
