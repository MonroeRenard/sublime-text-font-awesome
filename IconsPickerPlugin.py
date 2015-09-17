import sublime, sublime_plugin

s = sublime.load_settings("IconsList.sublime-settings")
icons = s.get("icons")

class iconboxCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_quick_panel(icons, self.onsel)
	def onsel(self, id):
		lalkaid = id
		self.window.active_view().run_command("selecticon", {"lalkaid":lalkaid} )
		
class selecticonCommand(sublime_plugin.TextCommand):
	def run(self, edit, lalkaid):
		if lalkaid != -1:
			needed = icons[int(lalkaid)]
			html = needed[1]
			pos = self.view.sel()[0]
			self.view.insert(edit, pos.a, html )



	
