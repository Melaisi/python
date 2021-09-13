
import TurntableGUI 
_window = None
def show():
    global _window
    if _window is None:
        controller = TurntableGUI.TurntableController()
        _window = TurntableGUI.create_window(controller)
    _window.show()
