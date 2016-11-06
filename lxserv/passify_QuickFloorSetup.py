#Must be inside a folder called 'lxserv' somewhere in a MODO search path.

import lx, lxu.command, traceback, passify, lxifc

class cmd_setup_class(lxu.command.BasicCommand):

    _first_run = True

    def __init__(self):
        lxu.command.BasicCommand.__init__(self)

        self.dyna_Add('hide_environments_bg', lx.symbol.sTYPE_BOOLEAN)

    def arg_UIHints(self, index, hints):
        if index == 0:
            hints.Label("Hide Environments in Background Layer")

    def cmd_DialogInit(self):
        if self._first_run:
            self.attr_SetInt(0, 1)
            self.after_first_run()

    @classmethod
    def after_first_run(cls):
        cls._first_run = False

    def cmd_Flags (self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def CMD_EXE(self, msg, flags):
        hide_environments_bg = self.dyna_Bool(0) if self.dyna_IsSet(0) else True

        passify.quickFloor.build(hide_environments_bg)

        notifier = passify.Notifier()
        notifier.Notify(lx.symbol.fCMDNOTIFY_DATATYPE)

    def basic_Execute(self, msg, flags):
        try:
            self.CMD_EXE(msg, flags)
        except Exception:
            lx.out(traceback.format_exc())

    def basic_Enable(self,msg):
        return True

    def basic_ButtonName(self):
        return "Setup QuickFloor"

lx.bless(cmd_setup_class, passify.CMD_QUICKFLOOR_SETUP)