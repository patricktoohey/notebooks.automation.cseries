import mouse

supervisor_information = mouse.point(mouse.left, 281)
supervisor_setup = mouse.point(mouse.left, 506)
supervisor_system = mouse.point(mouse.submenu, 382)
supervisor_motor = mouse.point(mouse.subsubmenu, 318)

def LoginSupervisor():
    mouse.Login()
    mouse.Login_Password()
    mouse.Keyboard_3()
    mouse.Keyboard_OK()
    mouse.Login_OK()

def InformationSupervisor():
    mouse.Menu()
    mouse.moveClick(supervisor_information)

def SetupSupervisor(loginFirst=False):
    if (loginFirst):
        LoginSupervisor()
    mouse.Menu()
    mouse.moveClick(supervisor_setup)

def SystemSupervisor(loginFirst=False):
    SetupSupervisor(loginFirst=loginFirst)
    mouse.moveClick(supervisor_system)

def MotorSupervisor(loginFirst=False):
    SystemSupervisor(loginFirst=loginFirst)
    mouse.moveClick(supervisor_motor)