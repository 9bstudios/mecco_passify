#Must be inside a folder called 'lxserv' somewhere in a MODO search path.

import lx, lxu.command, traceback, passify, lxifc

class cmd_add_to_layer(lxu.command.BasicCommand):

    def __init__(self):
        lxu.command.BasicCommand.__init__(self)

    def cmd_Flags (self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def CMD_EXE(self, msg, flags):
        if passify.fetch_by_tag(passify.QUICKFLOOR_PGRP) == None:

            # passify.debug("No QuickFloor pass group found. Creating.", True)
            lx.eval(passify.CMD_QUICKFLOOR_SETUP)

        passify.quickFloor.add_selected()

        notifier = passify.Notifier()
        notifier.Notify(lx.symbol.fCMDNOTIFY_DATATYPE)

    def basic_Execute(self, msg, flags):
        try:
            self.CMD_EXE(msg, flags)
        except Exception:
            lx.out(traceback.format_exc())

    def basic_Enable(self,msg):
        return True

lx.bless(cmd_add_to_layer, passify.CMD_QUICKFLOOR_ADD_ITEMS)
