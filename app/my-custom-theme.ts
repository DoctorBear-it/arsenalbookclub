
import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

// #E30613
// #05346E
// #E9B419
// #977D48
// #FFFFFF
// #000000
// #CB0512
// #92050D

export const myCustomTheme: CustomThemeConfig = {
    name: 'my-custom-theme',
    properties: {
		// =~= Theme Properties =~=
		"--theme-font-family-base": `system-ui`,
		"--theme-font-family-heading": `system-ui`,
		"--theme-font-color-base": "0 0 0",
		"--theme-font-color-dark": "255 255 255",
		"--theme-rounded-base": "9999px",
		"--theme-rounded-container": "12px",
		"--theme-border-base": "1px",
		// =~= Theme On-X Colors =~=
		"--on-primary": "255 255 255",
		"--on-secondary": "255 255 255",
		"--on-tertiary": "0 0 0",
		"--on-success": "0 0 0",
		"--on-warning": "0 0 0",
		"--on-error": "255 255 255",
		"--on-surface": "255 255 255",
		// =~= Theme Colors  =~=
		// primary | #E30613 
		"--color-primary-50": "251 218 220", // #fbdadc
		"--color-primary-100": "249 205 208", // #f9cdd0
		"--color-primary-200": "248 193 196", // #f8c1c4
		"--color-primary-300": "244 155 161", // #f49ba1
		"--color-primary-400": "235 81 90", // #eb515a
		"--color-primary-500": "227 6 19", // #E30613
		"--color-primary-600": "204 5 17", // #cc0511
		"--color-primary-700": "170 5 14", // #aa050e
		"--color-primary-800": "136 4 11", // #88040b
		"--color-primary-900": "111 3 9", // #6f0309
		// secondary | #05346E 
		"--color-secondary-50": "218 225 233", // #dae1e9
		"--color-secondary-100": "205 214 226", // #cdd6e2
		"--color-secondary-200": "193 204 219", // #c1ccdb
		"--color-secondary-300": "155 174 197", // #9baec5
		"--color-secondary-400": "80 113 154", // #50719a
		"--color-secondary-500": "5 52 110", // #05346E
		"--color-secondary-600": "5 47 99", // #052f63
		"--color-secondary-700": "4 39 83", // #042753
		"--color-secondary-800": "3 31 66", // #031f42
		"--color-secondary-900": "2 25 54", // #021936
		// tertiary | #E9B419 
		"--color-tertiary-50": "252 244 221", // #fcf4dd
		"--color-tertiary-100": "251 240 209", // #fbf0d1
		"--color-tertiary-200": "250 236 198", // #faecc6
		"--color-tertiary-300": "246 225 163", // #f6e1a3
		"--color-tertiary-400": "240 203 94", // #f0cb5e
		"--color-tertiary-500": "233 180 25", // #E9B419
		"--color-tertiary-600": "210 162 23", // #d2a217
		"--color-tertiary-700": "175 135 19", // #af8713
		"--color-tertiary-800": "140 108 15", // #8c6c0f
		"--color-tertiary-900": "114 88 12", // #72580c
		// success | #977D48 
		"--color-success-50": "239 236 228", // #efece4
		"--color-success-100": "234 229 218", // #eae5da
		"--color-success-200": "229 223 209", // #e5dfd1
		"--color-success-300": "213 203 182", // #d5cbb6
		"--color-success-400": "182 164 127", // #b6a47f
		"--color-success-500": "151 125 72", // #977D48
		"--color-success-600": "136 113 65", // #887141
		"--color-success-700": "113 94 54", // #715e36
		"--color-success-800": "91 75 43", // #5b4b2b
		"--color-success-900": "74 61 35", // #4a3d23
		// warning | #FFFFFF 
		"--color-warning-50": "255 255 255", // #ffffff
		"--color-warning-100": "255 255 255", // #ffffff
		"--color-warning-200": "255 255 255", // #ffffff
		"--color-warning-300": "255 255 255", // #ffffff
		"--color-warning-400": "255 255 255", // #ffffff
		"--color-warning-500": "255 255 255", // #FFFFFF
		"--color-warning-600": "230 230 230", // #e6e6e6
		"--color-warning-700": "191 191 191", // #bfbfbf
		"--color-warning-800": "153 153 153", // #999999
		"--color-warning-900": "125 125 125", // #7d7d7d
		// error | #000000 
		"--color-error-50": "217 217 217", // #d9d9d9
		"--color-error-100": "204 204 204", // #cccccc
		"--color-error-200": "191 191 191", // #bfbfbf
		"--color-error-300": "153 153 153", // #999999
		"--color-error-400": "77 77 77", // #4d4d4d
		"--color-error-500": "0 0 0", // #000000
		"--color-error-600": "0 0 0", // #000000
		"--color-error-700": "0 0 0", // #000000
		"--color-error-800": "0 0 0", // #000000
		"--color-error-900": "0 0 0", // #000000
		// surface | #CB0512 
		"--color-surface-50": "247 218 219", // #f7dadb
		"--color-surface-100": "245 205 208", // #f5cdd0
		"--color-surface-200": "242 193 196", // #f2c1c4
		"--color-surface-300": "234 155 160", // #ea9ba0
		"--color-surface-400": "219 80 89", // #db5059
		"--color-surface-500": "203 5 18", // #CB0512
		"--color-surface-600": "183 5 16", // #b70510
		"--color-surface-700": "152 4 14", // #98040e
		"--color-surface-800": "122 3 11", // #7a030b
		"--color-surface-900": "99 2 9", // #630209
		
	}
}