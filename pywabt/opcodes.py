types = {
	'i32':			0x7f,
	'i64':		  0x7e,
	'f32':		  0x7d,
	'f64':			0x7c,
	'anyfunc':	0x70,
	'func':		  0x60,
	'void':		  0x40
}

sections = {
	'custom':   0x00,
	'type':     0x01,
	'import':   0x02,
	'function': 0x03,
	'table':    0x04,
	'memory':   0x05,
	'global':   0x06,
	'export':   0x07,
	'start':    0x08,
	'element':  0x09,
	'code':     0x0a,
	'data':     0x0b,
}

exports = {
	'function': 0x00,
	'table':    0x01,
	'memory':   0x02,
	'global':   0x03
}

instructions = {
		#control flow
		'unreachable':    0x00,
		'nop':            0x01,
		'block':          0x02,
		'loop':           0x03,
		'if':             0x04,
		'else':           0x05,
		'end':            0x0b,
		'br':             0x0c,
		'br_if':          0x0d,
		'br_table':       0x0e,
		'return':         0x0f,
		#call operators
		'call':           0x10,
		'call_indirect':  0x11,
		#parametric operators
		'drop':           0x1a,
		'select':         0x1b,
		#variable access
		'get_local':      0x20,
		'local.get':      0x20,
		'set_local':      0x21,
		'local.set':      0x21,
		'tee_local':      0x22,
    'local.tee':      0x22,
		'get_global':     0x23,
		'global.get':     0x23,
		'set_global':     0x24,
		'global.set':     0x24,
		#memory operators
		'i32.load':       0x28,
		'i64.load':       0x29,
		'f32.load':       0x2a,
		'f64.load':       0x2b,
		'i32.load8_s':    0x2c,
		'i32.load8_u':    0x2d,
		'i32.load16_s':   0x2e,
		'i32.load16_u':   0x2f,
    'i64.load8_s':    0x30,
		'i64.load8_u':    0x31,
		'i64.load16_s':   0x32,
		'i64.load16_u':   0x33,
		'i64.load32_s':   0x34,
		'i64.load32_u': 0x35,
		'i32.store': 0x36,
		'i64.store': 0x37,
		'f32.store': 0x38,
		'f64.store': 0x39,
		'i32.store8': 0x3a,
		'i32.store16': 0x3b,
		'i64.store8': 0x3c,
		'i64.store16': 0x3d,
		'i64.store32': 0x3e,
		'current_memory': 0x3f,
		'memory.current': 0x3f,
		'grow_memory': 0x40,
		'memory.grow': 0x40,
		#constants
		'i32.const': 0x41,
		'i64.const': 0x42,
		'f32.const': 0x43,
		'f64.const': 0x44,
		#comparison operators
		'i32.eqz': 0x45,
		'i32.eq': 0x46,
		'i32.ne': 0x47,
		'i32.lt_s': 0x48,
		'i32.lt_u': 0x49,
		'i32.gt_s': 0x4a,
		'i32.gt_u': 0x4b,
		'i32.le_s': 0x4c,
		'i32.le_u': 0x4d,
		'i32.ge_s': 0x4e,
		'i32.ge_u': 0x4f,
		'i64.eqz': 0x50,
		'i64.eq': 0x51,
		'i64.ne': 0x52,
		'i64.lt_s': 0x53,
		'i64.lt_u': 0x54,
		'i64.gt_s': 0x55,
		'i64.gt_u': 0x56,
		'i64.le_s': 0x57,
		'i64.le_u': 0x58,
		'i64.ge_s': 0x59,
		'i64.ge_u': 0x5a,
		'f32.eq': 0x5b,
		'f32.ne': 0x5c,
		'f32.lt': 0x5d,
		'f32.gt': 0x5e,
		'f32.le': 0x5f,
		'f32.ge': 0x60,
		'f64.eq': 0x61,
		'f64.ne': 0x62,
		'f64.lt': 0x63,
		'f64.gt': 0x64,
		'f64.le': 0x65,
		'f64.ge': 0x66,
		#numeric operators
		'i32.clz': 0x67,
		'i32.ctz': 0x68,
		'i32.popcnt': 0x69,
		'i32.add': 0x6a,
		'i32.sub': 0x6b,
		'i32.mul': 0x6c,
		'i32.div_s':0x6d,
		'i32.div_u': 0x6e,
		'i32.rem_s': 0x6f,
		'i32.rem_u': 0x70,
		'i32.and': 0x71,
		'i32.or':0x72,
		'i32.xor': 0x73,
		'i32.shl': 0x74,
		'i32.shr_s': 0x75,
		'i32.shr_u': 0x76,
		'i32.rotl': 0x77,
		'i32.rotr': 0x78,
		'i64.clz': 0x79,
		'i64.ctz': 0x7a,
		'i64.popcnt': 0x7b,
		'i64.add': 0x7c,
		'i64.sub': 0x7d,
		'i64.mul': 0x7e,
		'i64.div_s': 0x7f,
		'i64.div_u': 0x80,
		'i64.rem_s': 0x81,
		'i64.rem_u': 0x82,
		'i64.and': 0x83,
		'i64.or': 0x84,
		'i64.xor': 0x85,
		'i64.shl': 0x86,
		'i64.shr_s': 0x87,
		'i64.shr_u': 0x88,
		'i64.rotl': 0x89,
		'i64.rotr': 0x8a,
		'f32.abs': 0x8b,
		'f32.neg': 0x8c,
		'f32.ceil': 0x8d,
		'f32.floor': 0x8e,
		'f32.trunc': 0x8f,
		'f32.nearest': 0x90,
		'f32.sqrt': 0x91,
		'f32.add': 0x92,
		'f32.sub': 0x93,
		'f32.mul': 0x94,
		'f32.div': 0x95,
		'f32.min': 0x96,
		'f32.max': 0x97,
		'f32.copysign': 0x98,
		'f64.abs': 0x99,
		'f64.neg': 0x9a,
		'f64.ceil': 0x9b,
		'f64.floor': 0x9c,
		'f64.trunc': 0x9d,
		'f64.nearest': 0x9e,
		'f64.sqrt': 0x9f,
		'f64.add': 0xa0,
		'f64.sub': 0xa1,
		'f64.mul': 0xa2,
		'f64.div': 0xa3,
		'f64.min': 0xa4,
		'f64.max': 0xa5,
		'f64.copysign': 0xa6,
		#type convertions
		'i32.wrap/i64': 0xa7,
		'i32.trunc_s/f32': 0xa8,
		'i32.trunc_u/f32': 0xa9,
		'i32.trunc_s/f64': 0xaa,
		'i32.trunc_u/f64': 0xab,
		'i64.extend_s/i32': 0xac,
		'i64.extend_u/i32': 0xad,
		'i64.trunc_s/f32': 0xae,
		'i64.trunc_u/f32': 0xaf,
		'i64.trunc_s/f64': 0xb0,
		'i64.trunc_u/f64': 0xb1,
		'f32.convert_s/i32': 0xb2,
		'f32.convert_u/i32': 0xb3,
		'f32.convert_s/i64': 0xb4,
		'f32.convert_u/i64': 0xb5,
		'f32.demote/f64': 0xb6,
		'f64.convert_s/i32': 0xb7,
		'f64.convert_u/i32': 0xb8,
		'f64.convert_s/i64': 0xb9,
		'f64.convert_u/i64': 0xba,
		'f64.promote/f32': 0xbb,
		#reinterpretations
		'interpret/f32': 0xbc,
		'i64.reinterpret/f64': 0xbd,
		'f32.reinterpret/i32': 0xbe,
		'f64.reinterpret/i64': 0xbf,
}

MAGIC_HEADER = b'\0asm'
MAGIC_VERSION = bytes([0x01, 0x00, 0x00, 0x00])

_type_names = {}
for _k in types.keys():
	_type_names[types[_k]] = _k

_section_names = {}
for _k in sections.keys():
	_section_names[sections[_k]] = _k

_export_names = {}
for _k in exports.keys():
	_export_names[exports[_k]] = _k

_instr_names = {}
for _k in instructions.keys():
	_instr_names[instructions[_k]] = _k

def type_name(tc: int) -> str:
	return _type_names[tc]

def section_name(sc: int) -> str:
	return _section_names[sc]

def export_name(ec: int) -> str:
	return _export_names[ec]

def instruction_name(ic: int) -> str:
	return _instr_names[ic]

