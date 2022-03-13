from ast import *
from type_check_Lfun import TypeCheckLfun
from utils import *

class TypeCheckLexam(TypeCheckLfun):
  def type_check_exp(self, e, env):
    match e:
      case List(es, Load()):
        ts = [self.type_check_exp(e, env) for e in es]
        elt_ty = ts[0]
        for (ty, elt) in zip(ts, es):
            self.check_type_equal(elt_ty, ty, elt)
        e.has_type = ListType(elt_ty)
        return e.has_type
      case Call(Name('len'), [tup]):
        tup_t = self.type_check_exp(tup, env)
        tup.has_type = tup_t
        match tup_t:
          case TupleType(_) | ListType(_):
            return IntType()
          case Bottom():
            return Bottom()
          case _:
            raise Exception('len expected tuple or list, not ' + repr(tup_t))
      case Call(Name('array_len'), [tup]):
        tup_t = self.type_check_exp(tup, env)
        tup.has_type = tup_t
        match tup_t:
          case ListType(_):
            return IntType()
          case _:
            raise Exception('array_len expected list, not ' + repr(tup_t))
      case Call(Name('array_load'), [tup, index]):
        tup_ty = self.type_check_exp(tup, env)
        tup.has_type = tup_ty
        index_ty = self.type_check_exp(index, env)
        self.check_type_equal(index_ty, IntType(), index)
        match tup_ty:
          case ListType(t):
            return t
          case _:
            raise Exception('array_len expected list, not ' + repr(tup_t))
      case Call(Name('array_store'), [tup, index, value]):
        tup_ty = self.type_check_exp(tup, env)
        tup.has_type = tup_ty
        index_ty = self.type_check_exp(index, env)
        value_ty = self.type_check_exp(value, env)
        self.check_type_equal(index_ty, IntType(), index)
        match tup_ty:
          case ListType(t):
            self.check_type_equal(value_ty, t, value)
            return VoidType()
          case _:
            raise Exception('array_store expected list, not ' + repr(tup_t))
      case Subscript(tup, index, Load()):
        tup_ty = self.type_check_exp(tup, env)
        tup.has_type = tup_ty
        index_ty = self.type_check_exp(index, env)
        self.check_type_equal(index_ty, IntType(), index)
        match tup_ty:
          case TupleType(ts):
            match index:
              case Constant(i):
                return ts[i]
              case _:
                raise Exception('subscript required constant integer index')
          case ListType(ty):
            return ty
          case _:
            raise Exception('subscript expected a tuple, not ' + repr(tup_ty))
      case BinOp(left, Mult() | FloorDiv() | Mod() , right):
        l = self.type_check_exp(left, env)
        self.check_type_equal(l, IntType(), left)
        r = self.type_check_exp(right, env)
        self.check_type_equal(r, IntType(), right)
        return IntType()
      case _:
        return super().type_check_exp(e, env)

  def type_check_stmts(self, ss, env):
    if len(ss) == 0:
      return VoidType()
    match ss[0]:
      case Assign([Subscript(tup, index, Store())], value):
        tup_ty = self.type_check_exp(tup, env)
        value_ty = self.type_check_exp(value, env)
        index_ty = self.type_check_exp(index, env)
        self.check_type_equal(index_ty, IntType(), index)
        tup.has_type = tup_ty
        match tup_ty:
          case ListType(ty):
            self.check_type_equal(ty, value_ty, ss[0])
          case _:
              # fall back to check for tuples
            return super().type_check_stmts(ss, env)
            #    raise Exception('type_check_stmts: expected a list, not ' \
            #                + repr(tup_t))
        return self.type_check_stmts(ss[1:], env)
      case _:
        return super().type_check_stmts(ss, env)
