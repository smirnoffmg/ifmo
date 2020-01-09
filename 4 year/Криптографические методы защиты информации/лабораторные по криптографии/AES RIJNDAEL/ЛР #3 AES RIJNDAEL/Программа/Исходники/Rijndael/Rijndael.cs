using System;
using System.IO;
using System.Windows.Forms;

namespace Rijndael
{
	/// <summary>
	/// Реализация блочного алгоритма шифрования Rijndael
	/// </summary>
	public class Rijndael
	{
		#region Таблицы

		static byte[,] ME =
			{
				{0x02, 0x03, 0x01, 0x01},
				{0x01, 0x02, 0x03, 0x01},
				{0x01, 0x01, 0x02, 0x03},
				{0x03, 0x01, 0x01, 0x02}
			};
		static byte[,] MD =
			{
				{0x0E, 0x0B, 0x0D, 0x09},
				{0x09, 0x0E, 0x0B, 0x0D},
				{0x0D, 0x09, 0x0E, 0x0B},
				{0x0B, 0x0D, 0x09, 0x0E}
			};
		static byte[] SboxE =
			{
				0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5,
				0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
				0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0,
				0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
				0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC,
				0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
				0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A,
				0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
				0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0,
				0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
				0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B,
				0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
				0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85,
				0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
				0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5,
				0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
				0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17,
				0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
				0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88,
				0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
				0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C,
				0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
				0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9,
				0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
				0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6,
				0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
				0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E,
				0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
				0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94,
				0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
				0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68,
				0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
			};
		static byte[] SboxD =
			{
				0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38,
				0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
				0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87,
				0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
				0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D,
				0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
				0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2,
				0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
				0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16,
				0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
				0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA,
				0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
				0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A,
				0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
				0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02,
				0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
				0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA,
				0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
				0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85,
				0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
				0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89,
				0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
				0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20,
				0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
				0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31,
				0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
				0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D,
				0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
				0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0,
				0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
				0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26,
				0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
			};
		static byte[] E =
			{
				0x01, 0x03, 0x05, 0x0F, 0x11, 0x33, 0x55, 0xFF,
				0x1A, 0x2E, 0x72, 0x96, 0xA1, 0xF8, 0x13, 0x35,
				0x5F, 0xE1, 0x38, 0x48, 0xD8, 0x73, 0x95, 0xA4,
				0xF7, 0x02, 0x06, 0x0A, 0x1E, 0x22, 0x66, 0xAA,
				0xE5, 0x34, 0x5C, 0xE4, 0x37, 0x59, 0xEB, 0x26,
				0x6A, 0xBE, 0xD9, 0x70, 0x90, 0xAB, 0xE6, 0x31,
				0x53, 0xF5, 0x04, 0x0C, 0x14, 0x3C, 0x44, 0xCC,
				0x4F, 0xD1, 0x68, 0xB8, 0xD3, 0x6E, 0xB2, 0xCD,
				0x4C, 0xD4, 0x67, 0xA9, 0xE0, 0x3B, 0x4D, 0xD7,
				0x62, 0xA6, 0xF1, 0x08, 0x18, 0x28, 0x78, 0x88,
				0x83, 0x9E, 0xB9, 0xD0, 0x6B, 0xBD, 0xDC, 0x7F,
				0x81, 0x98, 0xB3, 0xCE, 0x49, 0xDB, 0x76, 0x9A,
				0xB5, 0xC4, 0x57, 0xF9, 0x10, 0x30, 0x50, 0xF0,
				0x0B, 0x1D, 0x27, 0x69, 0xBB, 0xD6, 0x61, 0xA3,
				0xFE, 0x19, 0x2B, 0x7D, 0x87, 0x92, 0xAD, 0xEC,
				0x2F, 0x71, 0x93, 0xAE, 0xE9, 0x20, 0x60, 0xA0,
				0xFB, 0x16, 0x3A, 0x4E, 0xD2, 0x6D, 0xB7, 0xC2,
				0x5D, 0xE7, 0x32, 0x56, 0xFA, 0x15, 0x3F, 0x41,
				0xC3, 0x5E, 0xE2, 0x3D, 0x47, 0xC9, 0x40, 0xC0,
				0x5B, 0xED, 0x2C, 0x74, 0x9C, 0xBF, 0xDA, 0x75,
				0x9F, 0xBA, 0xD5, 0x64, 0xAC, 0xEF, 0x2A, 0x7E,
				0x82, 0x9D, 0xBC, 0xDF, 0x7A, 0x8E, 0x89, 0x80,
				0x9B, 0xB6, 0xC1, 0x58, 0xE8, 0x23, 0x65, 0xAF,
				0xEA, 0x25, 0x6F, 0xB1, 0xC8, 0x43, 0xC5, 0x54,
				0xFC, 0x1F, 0x21, 0x63, 0xA5, 0xF4, 0x07, 0x09,
				0x1B, 0x2D, 0x77, 0x99, 0xB0, 0xCB, 0x46, 0xCA,
				0x45, 0xCF, 0x4A, 0xDE, 0x79, 0x8B, 0x86, 0x91,
				0xA8, 0xE3, 0x3E, 0x42, 0xC6, 0x51, 0xF3, 0x0E,
				0x12, 0x36, 0x5A, 0xEE, 0x29, 0x7B, 0x8D, 0x8C,
				0x8F, 0x8A, 0x85, 0x94, 0xA7, 0xF2, 0x0D, 0x17,
				0x39, 0x4B, 0xDD, 0x7C, 0x84, 0x97, 0xA2, 0xFD,
				0x1C, 0x24, 0x6C, 0xB4, 0xC7, 0x52, 0xF6, 0x01
			};
		static byte[] L =
			{
				0x00, 0x00, 0x19, 0x01, 0x32, 0x02, 0x1A, 0xC6,
				0x4B, 0xC7, 0x1B, 0x68, 0x33, 0xEE, 0xDF, 0x03,
				0x64, 0x04, 0xE0, 0x0E, 0x34, 0x8D, 0x81, 0xEF,
				0x4C, 0x71, 0x08, 0xC8, 0xF8, 0x69, 0x1C, 0xC1,
				0x7D, 0xC2, 0x1D, 0xB5, 0xF9, 0xB9, 0x27, 0x6A,
				0x4D, 0xE4, 0xA6, 0x72, 0x9A, 0xC9, 0x09, 0x78,
				0x65, 0x2F, 0x8A, 0x05, 0x21, 0x0F, 0xE1, 0x24,
				0x12, 0xF0, 0x82, 0x45, 0x35, 0x93, 0xDA, 0x8E,
				0x96, 0x8F, 0xDB, 0xBD, 0x36, 0xD0, 0xCE, 0x94,
				0x13, 0x5C, 0xD2, 0xF1, 0x40, 0x46, 0x83, 0x38,
				0x66, 0xDD, 0xFD, 0x30, 0xBF, 0x06, 0x8B, 0x62,
				0xB3, 0x25, 0xE2, 0x98, 0x22, 0x88, 0x91, 0x10,
				0x7E, 0x6E, 0x48, 0xC3, 0xA3, 0xB6, 0x1E, 0x42,
				0x3A, 0x6B, 0x28, 0x54, 0xFA, 0x85, 0x3D, 0xBA,
				0x2B, 0x79, 0x0A, 0x15, 0x9B, 0x9F, 0x5E, 0xCA,
				0x4E, 0xD4, 0xAC, 0xE5, 0xF3, 0x73, 0xA7, 0x57,
				0xAF, 0x58, 0xA8, 0x50, 0xF4, 0xEA, 0xD6, 0x74,
				0x4F, 0xAE, 0xE9, 0xD5, 0xE7, 0xE6, 0xAD, 0xE8,
				0x2C, 0xD7, 0x75, 0x7A, 0xEB, 0x16, 0x0B, 0xF5,
				0x59, 0xCB, 0x5F, 0xB0, 0x9C, 0xA9, 0x51, 0xA0,
				0x7F, 0x0C, 0xF6, 0x6F, 0x17, 0xC4, 0x49, 0xEC,
				0xD8, 0x43, 0x1F, 0x2D, 0xA4, 0x76, 0x7B, 0xB7,
				0xCC, 0xBB, 0x3E, 0x5A, 0xFB, 0x60, 0xB1, 0x86,
				0x3B, 0x52, 0xA1, 0x6C, 0xAA, 0x55, 0x29, 0x9D,
				0x97, 0xB2, 0x87, 0x90, 0x61, 0xBE, 0xDC, 0xFC,
				0xBC, 0x95, 0xCF, 0xCD, 0x37, 0x3F, 0x5B, 0xD1,
				0x53, 0x39, 0x84, 0x3C, 0x41, 0xA2, 0x6D, 0x47,
				0x14, 0x2A, 0x9E, 0x5D, 0x56, 0xF2, 0xD3, 0xAB,
				0x44, 0x11, 0x92, 0xD9, 0x23, 0x20, 0x2E, 0x89,
				0xB4, 0x7C, 0xB8, 0x26, 0x77, 0x99, 0xE3, 0xA5,
				0x67, 0x4A, 0xED, 0xDE, 0xC5, 0x31, 0xFE, 0x18,
				0x0D, 0x63, 0x8C, 0x80, 0xC0, 0xF7, 0x70, 0x07
			};

		#endregion


		#region Поля

		byte keyLength = 16;
		byte blockLength = 16;
		byte roundsNum;
		byte[] cipherKey = new byte[16] { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
		byte[] expandedKey;
		int currentAddingKeyPosition = 0;

		#endregion


		#region Проперти

		/// <summary>
		/// Ключ шифрования
		/// </summary>
		public byte[] CipherKey
		{
			get
			{
				return cipherKey;
			}
			set
			{
				if ( ( value.Length != 16 ) && ( value.Length != 24 ) && ( value.Length != 32 ) )
					throw new Exception( "Некорректная длина ключа" );
				this.keyLength = (byte)value.Length;
				this.cipherKey = value;
				this.ExpandKey();
			}
		}

		/// <summary>
		/// Расширенный ключ
		/// </summary>
		public byte[] ExpandedKey
		{
			get
			{
				return this.expandedKey;
			}
		}

		/// <summary>
		/// Длина ключа
		/// </summary>
		public byte KeyLength
		{
			get
			{
				return keyLength;
			}
			set
			{
				if ( ( value != 16 ) && ( value != 24 ) && ( value != 32 ) )
					throw new Exception( "Некорректная длина ключа" );
				if ( this.cipherKey.Length != value )
					this.cipherKey = null;
				this.keyLength = value;
				this.ExpandKey();
			}
		}

		/// <summary>
		/// Длина блока
		/// </summary>
		public byte BlockLength
		{
			get
			{
				return blockLength;
			}
			set
			{
				this.blockLength = value;
				this.ExpandKey();
			}
		}

		#endregion


		#region Расширение ключа

		#region Для расширения ключа

		private byte[] RotWord( byte[] what )
		{
			return new byte[4] { what[1], what[2], what[3], what[0] };
		}
		private byte[] SubWord( byte[] what )
		{
			return new byte[4] { SboxE[what[0]], SboxE[what[1]], SboxE[what[2]], SboxE[what[3]] };
		}
		private byte[] Rcon( byte num )
		{
			switch( num )
			{
				case 0:
					return new byte[4] {0x01, 0x00, 0x00, 0x00};
				case 1:
					return new byte[4] {0x02, 0x00, 0x00, 0x00};
				case 2:
					return new byte[4] {0x04, 0x00, 0x00, 0x00};
				case 3:
					return new byte[4] {0x08, 0x00, 0x00, 0x00};
				case 4:
					return new byte[4] {0x10, 0x00, 0x00, 0x00};
				case 5:
					return new byte[4] {0x20, 0x00, 0x00, 0x00};
				case 6:
					return new byte[4] {0x40, 0x00, 0x00, 0x00};
				case 7:
					return new byte[4] {0x80, 0x00, 0x00, 0x00};
				case 8:
					return new byte[4] {0x1B, 0x00, 0x00, 0x00};
				case 9:
					return new byte[4] {0x36, 0x00, 0x00, 0x00};
				case 10:
					return new byte[4] {0x6C, 0x00, 0x00, 0x00};
				case 11:
					return new byte[4] {0xD8, 0x00, 0x00, 0x00};
				case 12:
					return new byte[4] {0xAB, 0x00, 0x00, 0x00};
				case 13:
					return new byte[4] {0x4D, 0x00, 0x00, 0x00};
				case 14:
					return new byte[4] {0x9A, 0x00, 0x00, 0x00};
			}
			return null;
		}
		private byte[] EK( byte offset )
		{
			return new byte[4] { this.expandedKey[offset], this.expandedKey[offset + 1], this.expandedKey[offset + 2], this.expandedKey[offset + 3] };
		}
		private byte[] XOR( byte[] a, byte[] b )
		{
			return new byte[4] { (byte)( a[0] ^ b[0] ), (byte)( a[1] ^ b[1] ), (byte)( a[2] ^ b[2] ), (byte)( a[3] ^ b[3] ) };
		}

		#endregion


		private void ExpandKey()
		{
			//получаем количество раундов шифрования
			if ( ( this.blockLength == 16 ) && ( this.keyLength == 16 ) )
				this.roundsNum = 10;
			else if ( ( this.blockLength == 32 ) || ( this.keyLength == 32 ) )
				this.roundsNum = 14;
			else
				this.roundsNum = 12;

			//длина расширенного ключа
			int keyL = this.blockLength * ( this.roundsNum + 1 );
			this.expandedKey = new byte[keyL];

			this.cipherKey.CopyTo( this.expandedKey, 0 );

			switch ( this.keyLength )
			{
				case 16:
					for ( byte i = 1; i <= 10; i++ )
					{
						byte tmp = (byte)(i*4);
						XOR( XOR(  SubWord(RotWord( EK((byte)((tmp-1)*4)) ) ), Rcon((byte)((tmp/4)-1)) ), EK((byte)((tmp-4)*4)) ).CopyTo( expandedKey, tmp * 4 );
						XOR( EK((byte)((tmp+1-1)*4)), EK((byte)((tmp+1-4)*4)) ).CopyTo( this.expandedKey, (tmp+1) * 4 );
						XOR( EK((byte)((tmp+2-1)*4)), EK((byte)((tmp+2-4)*4)) ).CopyTo( this.expandedKey, (tmp+2) * 4 );
						XOR( EK((byte)((tmp+3-1)*4)), EK((byte)((tmp+3-4)*4)) ).CopyTo( this.expandedKey, (tmp+3) * 4 );
					}
					break;
				case 24:
					for ( byte i = 1; i <= 7; i++ )
					{
						byte tmp = (byte)(i*6);
						XOR( XOR( SubWord(RotWord( EK((byte)((tmp-1)*4)) ) ), Rcon((byte)((tmp/4)-1)) ), EK((byte)((tmp-4)*4)) ).CopyTo( expandedKey, tmp * 4 );
						XOR( EK((byte)((tmp+1-1)*4)), EK((byte)((tmp+1-4)*4)) ).CopyTo( this.expandedKey, (tmp+1) * 4 );
						XOR( EK((byte)((tmp+2-1)*4)), EK((byte)((tmp+2-4)*4)) ).CopyTo( this.expandedKey, (tmp+2) * 4 );
						XOR( EK((byte)((tmp+3-1)*4)), EK((byte)((tmp+3-4)*4)) ).CopyTo( this.expandedKey, (tmp+3) * 4 );
						XOR( EK((byte)((tmp+4-1)*4)), EK((byte)((tmp+4-4)*4)) ).CopyTo( this.expandedKey, (tmp+4) * 4 );
						XOR( EK((byte)((tmp+5-1)*4)), EK((byte)((tmp+5-4)*4)) ).CopyTo( this.expandedKey, (tmp+5) * 4 );
					}
					XOR( XOR( SubWord(RotWord( EK((byte)((48-1)*4)) ) ), Rcon((byte)((48/4)-1)) ), EK((byte)((48-4)*4)) ).CopyTo( expandedKey, 48 * 4 );
					XOR( EK((byte)((49-1)*4)), EK((byte)((49-4)*4)) ).CopyTo( this.expandedKey, 49 * 4 );
					XOR( EK((byte)((50-1)*4)), EK((byte)((50-4)*4)) ).CopyTo( this.expandedKey, 50 * 4 );
					XOR( EK((byte)((51-1)*4)), EK((byte)((51-4)*4)) ).CopyTo( this.expandedKey, 51 * 4 );
					break;
				case 32:
					for ( byte i = 1; i <= 6; i++ )
					{
						byte tmp = (byte)(i*8);
						XOR( XOR( SubWord(RotWord( EK((byte)((tmp-1)*4)) ) ), Rcon((byte)((tmp/4)-1)) ), EK((byte)((tmp-4)*4)) ).CopyTo( expandedKey, tmp * 4 );
						XOR( EK((byte)((tmp+1-1)*4)), EK((byte)((tmp+1-4)*4)) ).CopyTo( this.expandedKey, (tmp+1) * 4 );
						XOR( EK((byte)((tmp+2-1)*4)), EK((byte)((tmp+2-4)*4)) ).CopyTo( this.expandedKey, (tmp+2) * 4 );
						XOR( EK((byte)((tmp+3-1)*4)), EK((byte)((tmp+3-4)*4)) ).CopyTo( this.expandedKey, (tmp+3) * 4 );
						XOR( SubWord( EK((byte)((tmp+4-1)*4)) ), EK((byte)((tmp+4-4)*4)) ).CopyTo( this.expandedKey, (tmp+4) * 4 );
						XOR( EK((byte)((tmp+5-1)*4)), EK((byte)((tmp+5-4)*4)) ).CopyTo( this.expandedKey, (tmp+5) * 4 );
						XOR( EK((byte)((tmp+6-1)*4)), EK((byte)((tmp+6-4)*4)) ).CopyTo( this.expandedKey, (tmp+6) * 4 );
						XOR( EK((byte)((tmp+7-1)*4)), EK((byte)((tmp+7-4)*4)) ).CopyTo( this.expandedKey, (tmp+7) * 4 );
					}
					XOR( XOR( SubWord(RotWord( EK((byte)((56-1)*4)) ) ), Rcon((byte)((56/4)-1)) ), EK((byte)((56-4)*4)) ).CopyTo( expandedKey, 56 * 4 );
					XOR( EK((byte)((57-1)*4)), EK((byte)((57-4)*4)) ).CopyTo( this.expandedKey, 57 * 4 );
					XOR( EK((byte)((58-1)*4)), EK((byte)((58-4)*4)) ).CopyTo( this.expandedKey, 58 * 4 );
					XOR( EK((byte)((59-1)*4)), EK((byte)((59-4)*4)) ).CopyTo( this.expandedKey, 59 * 4 );
					break;
			}
		}

		#endregion


		#region Цикловое преобразования


		#region Добавление циклового ключа

		/// <summary>
		/// Добавление циклового ключа при шифровании
		/// </summary>
		/// <param name="state">Состояние</param>
		/// <returns>Результат преобразования</returns>
		public byte[,] AddRoundKeyE( byte[,] state )
		{
			byte[,] res = new byte[4, this.blockLength / 4];
			for ( int k = 0; k < state.Length / 4; k++)//по столбцам
				for ( int j = 0; j < 4; j++ )//по строкам
					res[j, k] = (byte)( state[j, k] ^ this.expandedKey[ this.currentAddingKeyPosition + j + k*4 ] );
			this.currentAddingKeyPosition += state.Length;
			return res;
		}

		/// <summary>
		/// Добавление циклового ключа при дешифровании
		/// </summary>
		/// <param name="state">Состояние</param>
		/// <returns>Результат преобразования</returns>
		public byte[,] AddRoundKeyD( byte[,] state )
		{
			byte[,] res = new byte[4, this.blockLength / 4];
			for ( int k = 0; k < state.Length / 4; k++)//по столбцам
				for ( int j = 0; j < 4; j++ )//по строкам
					res[j, k] = (byte)( state[j, k] ^ this.expandedKey[ this.currentAddingKeyPosition + j + k*4 ] );
			this.currentAddingKeyPosition -= state.Length;
			return res;
		}

		#endregion


		#region Замена байт

		/// <summary>
		/// Замена байт при шифровании
		/// </summary>
		/// <param name="state">Состояние</param>
		/// <returns>Результат преобразования</returns>
		public byte[,] ByteSubE( byte[,] state )
		{
			byte[,] result = new byte[4, state.Length / 4];
			for ( int i = 0; i < 4; i++ )
				for ( int j = 0; j < state.Length / 4; j++ )
					result[i, j] = Rijndael.SboxE[state[i, j]];
			return result;
		}

		/// <summary>
		/// Замена байт при дешифровании
		/// </summary>
		/// <param name="state">Состояние</param>
		/// <returns>Результат преобразования</returns>
		public byte[,] ByteSubD( byte[,] state )
		{
			byte[,] result = new byte[4, state.Length / 4];
			for ( int i = 0; i < 4; i++ )
				for ( int j = 0; j < state.Length / 4; j++ )
					result[i, j] = Rijndael.SboxD[state[i, j]];
			return result;
		}

		#endregion


		#region Сдвиг строк

		/// <summary>
		/// Сдвиг строк при шифровании
		/// </summary>
		/// <param name="state">Состояние</param>
		/// <returns>Результат преобразования</returns>
		public byte[,] ShiftRowE( byte[,] state )
		{
			byte c1 = 1, c2 = 0, c3 = 0;
			switch( state.Length / 4 )
			{
				case 4:
				case 6:
					c2 = 2;
					c3 = 3;
					break;
				case 8:
					c2 = 3;
					c3 = 4;
					break;
			}

			byte[,] result = new byte[4, state.Length / 4];
			//1-я строка без сдвига
			for ( int i = 0; i < state.Length / 4; i++ )
				result[0, i] = state[0, i];

			//2-я со сдвигом на с1
			for ( int i = c1; i < state.Length / 4; i++ )
				result[1, i - c1] = state[1, i];
			for ( int i = 1; i <= c1; i++ )
				result[1, state.Length / 4 - i] = state[1, c1 - i];

			//3-я со сдвигом на с2
			for ( int i = c2; i < state.Length / 4; i++ )
				result[2, i - c2] = state[2, i];
			for ( int i = 1; i <= c2; i++ )
				result[2, state.Length / 4 - i] = state[2, c2 - i];

			//4-я со сдвигом на с3
			for ( int i = c3; i < state.Length / 4; i++ )
				result[3, i - c3] = state[3, i];
			for ( int i = 1; i <= c3; i++ )
				result[3, state.Length / 4 - i] = state[3, c3 - i];

			return result;
		}

		/// <summary>
		/// Сдвиг строк при дешифровании
		/// </summary>
		/// <param name="state">Состояние</param>
		/// <returns>Результат преобразования</returns>
		public byte[,] ShiftRowD( byte[,] state )
		{
			byte c1 = 1, c2 = 0, c3 = 0;
			switch( state.Length / 4 )
			{
				case 4:
				case 6:
					c2 = 2;
					c3 = 3;
					break;
				case 8:
					c2 = 3;
					c3 = 4;
					break;
			}

			byte[,] result = new byte[4, state.Length / 4];
			//1-я строка без сдвига
			for ( int i = 0; i < state.Length / 4; i++ )
				result[0, i] = state[0, i];

			//2-я со сдвигом на с1
			for ( int i = 0; i < state.Length / 4 - c1; i++ )
				result[1, i + c1] = state[1, i];
			for ( int i = 1; i <= c1; i++ )
				result[1, c1 - i] = state[1, state.Length / 4 - i];

			//3-я со сдвигом на с2
			for ( int i = 0; i < state.Length / 4 - c2; i++ )
				result[2, i + c2] = state[2, i];
			for ( int i = 1; i <= c2; i++ )
				result[2, c2 - i] = state[2, state.Length / 4 - i];

			//4-я со сдвигом на с3
			for ( int i = 0; i < state.Length / 4 - c3; i++ )
				result[3, i + c3] = state[3, i];
			for ( int i = 1; i <= c3; i++ )
				result[3, c3 - i] = state[3, state.Length / 4 - i];

			return result;
		}

		#endregion


		#region Замешивание столбцов

		/// <summary>
		/// Замешивание столбцов при шифровании
		/// </summary>
		/// <param name="state">Состояние</param>
		/// <returns>Результат преобразования</returns>
		public byte[,] MixColumnE( byte[,] state )
		{
			byte[,] result = new byte[4, state.Length / 4];
			for ( int i = 0; i < 4; i++ )//по строкам
				for ( int j = 0; j < state.Length / 4; j++ )//по столбцам
					for ( int k = 0; k < 4; k++ )//по элементам
					{
						byte a = Rijndael.ME[i, k];
						byte b = state[k, j];
						int c = 0;
						if ( ( a != 0 ) && ( b != 0 ) )
						{
							if ( a == 0x01 )
								c = b;
							else if ( b == 0x01 )
								c = a;
							else
							{
								c = Rijndael.L[ a ] + Rijndael.L[ b ];
								if ( c > 0xff )
									c -= 0xff;
								c = Rijndael.E[ c ];
							}
						}
						result[i, j] ^= (byte)c;
					}
			return result;
		}

		/// <summary>
		/// Замешивание столбцов при дешифровании
		/// </summary>
		/// <param name="state">Состояние</param>
		/// <returns>Результат преобразования</returns>
		public byte[,] MixColumnD( byte[,] state )
		{
			byte[,] result = new byte[4, state.Length / 4];
			for ( int i = 0; i < 4; i++ )
				for ( int j = 0; j < state.Length / 4; j++ )
					for ( int k = 0; k < 4; k++ )
					{
						byte a = Rijndael.MD[i, k];
						byte b = state[k, j];
						int c = 0;
						if ( ( a != 0 ) && ( b != 0 ) )
						{
							if ( a == 0x01 )
								c = b;
							else if ( b == 0x01 )
								c = a;
							else
							{
								c = Rijndael.L[ a ] + Rijndael.L[ b ];
								if ( c > 0xff )
									c -= 0xff;
								c = Rijndael.E[ c ];
							}
						}
						result[i, j] ^= (byte)c;
					}
			return result;
		}

		#endregion


		#endregion


		#region Шифрование/дешифрование

		/// <summary>
		/// Шифрование
		/// </summary>
		/// <param name="what">Исходный текст</param>
		/// <returns>Зашифрованный текст</returns>
		public byte[] Encipher( byte[] what )
		{
			try
			{
				//пишем в начало шифруемой массива длину исходного сообщения
				MemoryStream ms = new MemoryStream();
				BinaryWriter bw = new BinaryWriter( ms );
				bw.Write( what.Length );
				bw.Write( what );
				bw.Close();
				what = ms.ToArray();

				//при необходимости дополняем нулями
				int i = what.Length - ( what.Length / this.blockLength ) * this.blockLength;
				if ( i != 0 )
				{
					byte[] tmp = new byte[ ( what.Length / this.blockLength + 1 ) * this.blockLength ];
					what.CopyTo( tmp, 0 );
					what = tmp;
				}

				byte[,] state = new byte[ 4, this.blockLength / 4 ];
				byte[] res = new byte[what.Length];
				int statesNum = statesNum = what.Length / this.blockLength;

				//шифруем
				for ( i = 0; i < statesNum; i++ )
				{
					this.currentAddingKeyPosition = 0;
					for ( int k = 0; k < this.blockLength / 4; k++ )
						for ( int j = 0; j < 4; j++ )
							state[ j, k ] = what[ i * this.blockLength + k * 4 + j ];

					state = this.AddRoundKeyE( state );
					for ( int j = 0; j < this.roundsNum - 1; j++ )
						state = this.AddRoundKeyE( this.MixColumnE( this.ShiftRowE( this.ByteSubE( state ) ) ) );
					state = this.AddRoundKeyE( this.ShiftRowE( this.ByteSubE( state ) ) );

					for ( int k = 0; k < this.blockLength / 4; k++ )
						for ( int j = 0; j < 4; j++ )
							res[ i * this.blockLength + k * 4 + j ] = state[ j, k ];
				}

				return res;
			}
			catch ( Exception e )
			{
				MessageBox.Show( e.Message, "Ошибка в процессе дешифрования" );
			}

			return null;
		}

		/// <summary>
		/// Дешифрование
		/// </summary>
		/// <param name="what">Зашифрованный текст</param>
		/// <returns>Расшифрованный текст</returns>
		public byte[] Decipher( byte[] what )
		{
			try
			{
				byte[,] state = new byte[ 4, this.blockLength / 4 ];
				byte[] res = new byte[what.Length];
				int statesNum = statesNum = what.Length / this.blockLength;

				//дефишруем
				for ( int i = 0; i < statesNum; i++ )
				{
					this.currentAddingKeyPosition = this.expandedKey.Length - this.blockLength;
					for ( int k = 0; k < this.blockLength / 4; k++ )
						for ( int j = 0; j < 4; j++ )
							state[ j, k ] = what[ i * this.blockLength + k * 4 + j ];

					state = this.AddRoundKeyD( state );
					for ( int j = 0; j < this.roundsNum - 1; j++ )
						state = this.MixColumnD( this.AddRoundKeyD( this.ByteSubD( this.ShiftRowD( state ) ) ) );
					state = this.AddRoundKeyD( this.ByteSubD( this.ShiftRowD( state ) ) );

					for ( int k = 0; k < this.blockLength / 4; k++ )
						for ( int j = 0; j < 4; j++ )
							res[ i * this.blockLength + k * 4 + j ] = state[ j, k ];
				}

				//читаем длину расшифрованного сообщения и само сообщение
				MemoryStream ms = new MemoryStream( res );
				BinaryReader br = new BinaryReader( ms );
				int len = br.ReadInt32();
				res = br.ReadBytes( len );
				br.Close();

				return res;
			}
			catch ( Exception e )
			{
				MessageBox.Show( e.Message, "Ошибка в процессе дешифрования" );
			}

			return null;
		}

		#endregion


		public override string ToString()
		{
			return base.ToString() + " : block length = " + this.blockLength + ", key length = " + this.keyLength;
		}
	}
}