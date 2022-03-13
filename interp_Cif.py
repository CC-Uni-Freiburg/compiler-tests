from ast import *
from interp_Lif import InterpLif
from utils import *

class InterpCif(InterpLif):

  def interp_stmts(self, ss, env):
    if len(ss) == 0:
        return
    match ss[0]:
      case Return(value):
        return Return(self.interp_exp(value, env))
      case Goto(label):
        return Goto(label)
        # return self.interp_stmts(self.blocks[label_name(label)], env)
      case _:
        return super().interp_stmts(ss, env)
    
  def interp(self, p):
    match p:
      case CProgram(blocks):
        env = {}
        self.blocks = blocks
        r = self.interp_stmts(blocks[label_name('start')], env)
        while isinstance(r, Goto):
          r = self.interp_stmts(self.blocks[label_name(r.label)], env)
