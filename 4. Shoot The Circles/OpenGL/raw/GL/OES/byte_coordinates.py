'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_OES_byte_coordinates'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_OES_byte_coordinates',error_checker=_errors._error_checker)
GL_BYTE=_C('GL_BYTE',0x1400)
@_f
@_p.types(None,_cs.GLenum,_cs.GLbyte)
def glMultiTexCoord1bOES(texture,s):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLbyteArray)
def glMultiTexCoord1bvOES(texture,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLbyte,_cs.GLbyte)
def glMultiTexCoord2bOES(texture,s,t):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLbyteArray)
def glMultiTexCoord2bvOES(texture,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glMultiTexCoord3bOES(texture,s,t,r):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLbyteArray)
def glMultiTexCoord3bvOES(texture,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glMultiTexCoord4bOES(texture,s,t,r,q):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLbyteArray)
def glMultiTexCoord4bvOES(texture,coords):pass
@_f
@_p.types(None,_cs.GLbyte)
def glTexCoord1bOES(s):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glTexCoord1bvOES(coords):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte)
def glTexCoord2bOES(s,t):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glTexCoord2bvOES(coords):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glTexCoord3bOES(s,t,r):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glTexCoord3bvOES(coords):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glTexCoord4bOES(s,t,r,q):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glTexCoord4bvOES(coords):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte)
def glVertex2bOES(x,y):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glVertex2bvOES(coords):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glVertex3bOES(x,y,z):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glVertex3bvOES(coords):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glVertex4bOES(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glVertex4bvOES(coords):pass
