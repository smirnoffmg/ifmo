using System;
using System.ComponentModel;
using System.IO;
using System.Text;
using System.Windows.Forms;
//using Rijndael;

namespace DemoApplication
{
	/// <summary>
	/// Summary description for Form1.
	/// </summary>
	public class MainForm : System.Windows.Forms.Form
	{
		#region Поля

		private TextBox textBoxCipherKey;
		private Label label1;
		private ComboBox comboBoxKeyLength;
		private Label label2;
		private Label label3;
		private ComboBox comboBoxBlockLength;
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private Container components = null;
		private Label label4;
		private Label label5;
		private TextBox textBoxOut;
		private TextBox textBoxIn;
		private Button buttonEncipher;
		private Button buttonDecipher;
		private Button buttonExpandedKey;
		private Button buttonOpenIn;
		private Button buttonOpenOut;
		private System.Windows.Forms.MainMenu mainMenu1;
		private System.Windows.Forms.MenuItem menuItem1;
		private System.Windows.Forms.MenuItem menuItem2;
		private System.Windows.Forms.MenuItem menuItem3;
		private System.Windows.Forms.MenuItem menuItem4;
		private System.Windows.Forms.GroupBox groupBox1;
		private System.Windows.Forms.Button buttonByteSub;
		private System.Windows.Forms.Button buttonShiftRow;
		private System.Windows.Forms.Button buttonMixColumn;
		private System.Windows.Forms.Button buttonAddRoundKey;
		private System.Windows.Forms.GroupBox groupBox2;
		private System.Windows.Forms.GroupBox groupBox3;

		Rijndael.Rijndael r = new Rijndael.Rijndael();

		#endregion


		#region Конструктор

		public MainForm()
		{
			InitializeComponent();
		}

		#endregion


		#region Pregenerated

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );
		}

		#region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.textBoxCipherKey = new System.Windows.Forms.TextBox();
			this.label1 = new System.Windows.Forms.Label();
			this.buttonExpandedKey = new System.Windows.Forms.Button();
			this.comboBoxKeyLength = new System.Windows.Forms.ComboBox();
			this.label2 = new System.Windows.Forms.Label();
			this.label3 = new System.Windows.Forms.Label();
			this.comboBoxBlockLength = new System.Windows.Forms.ComboBox();
			this.textBoxIn = new System.Windows.Forms.TextBox();
			this.label4 = new System.Windows.Forms.Label();
			this.buttonOpenIn = new System.Windows.Forms.Button();
			this.buttonOpenOut = new System.Windows.Forms.Button();
			this.label5 = new System.Windows.Forms.Label();
			this.textBoxOut = new System.Windows.Forms.TextBox();
			this.buttonEncipher = new System.Windows.Forms.Button();
			this.buttonDecipher = new System.Windows.Forms.Button();
			this.mainMenu1 = new System.Windows.Forms.MainMenu();
			this.menuItem1 = new System.Windows.Forms.MenuItem();
			this.menuItem2 = new System.Windows.Forms.MenuItem();
			this.menuItem3 = new System.Windows.Forms.MenuItem();
			this.menuItem4 = new System.Windows.Forms.MenuItem();
			this.groupBox1 = new System.Windows.Forms.GroupBox();
			this.buttonByteSub = new System.Windows.Forms.Button();
			this.buttonShiftRow = new System.Windows.Forms.Button();
			this.buttonMixColumn = new System.Windows.Forms.Button();
			this.buttonAddRoundKey = new System.Windows.Forms.Button();
			this.groupBox2 = new System.Windows.Forms.GroupBox();
			this.groupBox3 = new System.Windows.Forms.GroupBox();
			this.groupBox1.SuspendLayout();
			this.groupBox2.SuspendLayout();
			this.groupBox3.SuspendLayout();
			this.SuspendLayout();
			// 
			// textBoxCipherKey
			// 
			this.textBoxCipherKey.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.textBoxCipherKey.Location = new System.Drawing.Point(152, 56);
			this.textBoxCipherKey.Multiline = true;
			this.textBoxCipherKey.Name = "textBoxCipherKey";
			this.textBoxCipherKey.Size = new System.Drawing.Size(392, 25);
			this.textBoxCipherKey.TabIndex = 3;
			this.textBoxCipherKey.Text = "00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f";
			// 
			// label1
			// 
			this.label1.BackColor = System.Drawing.Color.Transparent;
			this.label1.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.label1.Location = new System.Drawing.Point(8, 56);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(136, 24);
			this.label1.TabIndex = 4;
			this.label1.Text = "Ключ шифрования:";
			// 
			// buttonExpandedKey
			// 
			this.buttonExpandedKey.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonExpandedKey.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonExpandedKey.Location = new System.Drawing.Point(552, 56);
			this.buttonExpandedKey.Name = "buttonExpandedKey";
			this.buttonExpandedKey.Size = new System.Drawing.Size(104, 24);
			this.buttonExpandedKey.TabIndex = 5;
			this.buttonExpandedKey.Text = "Расширенный";
			this.buttonExpandedKey.Click += new System.EventHandler(this.buttonExpandedKey_Click);
			// 
			// comboBoxKeyLength
			// 
			this.comboBoxKeyLength.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxKeyLength.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.comboBoxKeyLength.Items.AddRange(new object[] {
																   "16",
																   "24",
																   "32"});
			this.comboBoxKeyLength.Location = new System.Drawing.Point(152, 16);
			this.comboBoxKeyLength.Name = "comboBoxKeyLength";
			this.comboBoxKeyLength.Size = new System.Drawing.Size(88, 24);
			this.comboBoxKeyLength.TabIndex = 1;
			this.comboBoxKeyLength.SelectedIndexChanged += new System.EventHandler(this.comboBoxKeyLength_SelectedIndexChanged);
			// 
			// label2
			// 
			this.label2.BackColor = System.Drawing.Color.Transparent;
			this.label2.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.label2.Location = new System.Drawing.Point(8, 16);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(104, 24);
			this.label2.TabIndex = 7;
			this.label2.Text = "Длина ключа:";
			// 
			// label3
			// 
			this.label3.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.label3.Location = new System.Drawing.Point(336, 16);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(104, 24);
			this.label3.TabIndex = 9;
			this.label3.Text = "Длина блока:";
			// 
			// comboBoxBlockLength
			// 
			this.comboBoxBlockLength.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxBlockLength.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.comboBoxBlockLength.Items.AddRange(new object[] {
																	 "16",
																	 "24",
																	 "32"});
			this.comboBoxBlockLength.Location = new System.Drawing.Point(456, 16);
			this.comboBoxBlockLength.Name = "comboBoxBlockLength";
			this.comboBoxBlockLength.Size = new System.Drawing.Size(88, 24);
			this.comboBoxBlockLength.TabIndex = 2;
			// 
			// textBoxIn
			// 
			this.textBoxIn.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.textBoxIn.Location = new System.Drawing.Point(152, 24);
			this.textBoxIn.Name = "textBoxIn";
			this.textBoxIn.ReadOnly = true;
			this.textBoxIn.Size = new System.Drawing.Size(392, 22);
			this.textBoxIn.TabIndex = 10;
			this.textBoxIn.Text = "";
			// 
			// label4
			// 
			this.label4.BackColor = System.Drawing.Color.Transparent;
			this.label4.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.label4.Location = new System.Drawing.Point(8, 24);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(128, 24);
			this.label4.TabIndex = 11;
			this.label4.Text = "Входной файл:";
			// 
			// buttonOpenIn
			// 
			this.buttonOpenIn.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonOpenIn.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonOpenIn.Location = new System.Drawing.Point(552, 24);
			this.buttonOpenIn.Name = "buttonOpenIn";
			this.buttonOpenIn.Size = new System.Drawing.Size(104, 25);
			this.buttonOpenIn.TabIndex = 13;
			this.buttonOpenIn.Text = "Открыть";
			this.buttonOpenIn.Click += new System.EventHandler(this.buttonOpenIn_Click);
			// 
			// buttonOpenOut
			// 
			this.buttonOpenOut.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonOpenOut.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonOpenOut.Location = new System.Drawing.Point(552, 64);
			this.buttonOpenOut.Name = "buttonOpenOut";
			this.buttonOpenOut.Size = new System.Drawing.Size(104, 25);
			this.buttonOpenOut.TabIndex = 17;
			this.buttonOpenOut.Text = "Открыть";
			this.buttonOpenOut.Click += new System.EventHandler(this.buttonOpenOut_Click);
			// 
			// label5
			// 
			this.label5.BackColor = System.Drawing.Color.Transparent;
			this.label5.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.label5.Location = new System.Drawing.Point(8, 64);
			this.label5.Name = "label5";
			this.label5.Size = new System.Drawing.Size(128, 24);
			this.label5.TabIndex = 15;
			this.label5.Text = "Выходной файл:";
			// 
			// textBoxOut
			// 
			this.textBoxOut.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.textBoxOut.Location = new System.Drawing.Point(152, 64);
			this.textBoxOut.Name = "textBoxOut";
			this.textBoxOut.ReadOnly = true;
			this.textBoxOut.Size = new System.Drawing.Size(392, 22);
			this.textBoxOut.TabIndex = 14;
			this.textBoxOut.Text = "";
			// 
			// buttonEncipher
			// 
			this.buttonEncipher.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonEncipher.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonEncipher.Location = new System.Drawing.Point(152, 96);
			this.buttonEncipher.Name = "buttonEncipher";
			this.buttonEncipher.Size = new System.Drawing.Size(112, 24);
			this.buttonEncipher.TabIndex = 22;
			this.buttonEncipher.Text = "Зашифровать";
			this.buttonEncipher.Click += new System.EventHandler(this.buttonEncipher_Click);
			// 
			// buttonDecipher
			// 
			this.buttonDecipher.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonDecipher.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonDecipher.Location = new System.Drawing.Point(432, 96);
			this.buttonDecipher.Name = "buttonDecipher";
			this.buttonDecipher.Size = new System.Drawing.Size(112, 24);
			this.buttonDecipher.TabIndex = 23;
			this.buttonDecipher.Text = "Расшифровать";
			this.buttonDecipher.Click += new System.EventHandler(this.buttonDecipher_Click);
			// 
			// mainMenu1
			// 
			this.mainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
																					  this.menuItem1,
																					  this.menuItem3});
			// 
			// menuItem1
			// 
			this.menuItem1.Index = 0;
			this.menuItem1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
																					  this.menuItem2});
			this.menuItem1.Text = "Файл";
			// 
			// menuItem2
			// 
			this.menuItem2.Index = 0;
			this.menuItem2.Text = "Выход";
			this.menuItem2.Click += new System.EventHandler(this.menuItem2_Click);
			// 
			// menuItem3
			// 
			this.menuItem3.Index = 1;
			this.menuItem3.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
																					  this.menuItem4});
			this.menuItem3.Text = "Помощь";
			// 
			// menuItem4
			// 
			this.menuItem4.Index = 0;
			this.menuItem4.Text = "О программе";
			this.menuItem4.Click += new System.EventHandler(this.menuItem4_Click);
			// 
			// groupBox1
			// 
			this.groupBox1.Controls.Add(this.buttonByteSub);
			this.groupBox1.Controls.Add(this.buttonShiftRow);
			this.groupBox1.Controls.Add(this.buttonMixColumn);
			this.groupBox1.Controls.Add(this.buttonAddRoundKey);
			this.groupBox1.Location = new System.Drawing.Point(680, 8);
			this.groupBox1.Name = "groupBox1";
			this.groupBox1.Size = new System.Drawing.Size(136, 240);
			this.groupBox1.TabIndex = 24;
			this.groupBox1.TabStop = false;
			this.groupBox1.Text = "Преобразования";
			// 
			// buttonByteSub
			// 
			this.buttonByteSub.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonByteSub.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonByteSub.Location = new System.Drawing.Point(16, 32);
			this.buttonByteSub.Name = "buttonByteSub";
			this.buttonByteSub.Size = new System.Drawing.Size(104, 24);
			this.buttonByteSub.TabIndex = 6;
			this.buttonByteSub.Text = "ByteSub";
			this.buttonByteSub.Click += new System.EventHandler(this.buttonByteSub_Click);
			// 
			// buttonShiftRow
			// 
			this.buttonShiftRow.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonShiftRow.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonShiftRow.Location = new System.Drawing.Point(16, 88);
			this.buttonShiftRow.Name = "buttonShiftRow";
			this.buttonShiftRow.Size = new System.Drawing.Size(104, 24);
			this.buttonShiftRow.TabIndex = 6;
			this.buttonShiftRow.Text = "ShiftRow";
			this.buttonShiftRow.Click += new System.EventHandler(this.buttonShiftRow_Click);
			// 
			// buttonMixColumn
			// 
			this.buttonMixColumn.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonMixColumn.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonMixColumn.Location = new System.Drawing.Point(16, 144);
			this.buttonMixColumn.Name = "buttonMixColumn";
			this.buttonMixColumn.Size = new System.Drawing.Size(104, 24);
			this.buttonMixColumn.TabIndex = 6;
			this.buttonMixColumn.Text = "MixColumn";
			this.buttonMixColumn.Click += new System.EventHandler(this.buttonMixColumn_Click);
			// 
			// buttonAddRoundKey
			// 
			this.buttonAddRoundKey.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.buttonAddRoundKey.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.buttonAddRoundKey.Location = new System.Drawing.Point(16, 200);
			this.buttonAddRoundKey.Name = "buttonAddRoundKey";
			this.buttonAddRoundKey.Size = new System.Drawing.Size(104, 24);
			this.buttonAddRoundKey.TabIndex = 6;
			this.buttonAddRoundKey.Text = "AddRoundKey";
			this.buttonAddRoundKey.Click += new System.EventHandler(this.buttonAddRoundKey_Click);
			// 
			// groupBox2
			// 
			this.groupBox2.Controls.Add(this.textBoxCipherKey);
			this.groupBox2.Controls.Add(this.label1);
			this.groupBox2.Controls.Add(this.buttonExpandedKey);
			this.groupBox2.Controls.Add(this.comboBoxKeyLength);
			this.groupBox2.Controls.Add(this.label2);
			this.groupBox2.Controls.Add(this.label3);
			this.groupBox2.Controls.Add(this.comboBoxBlockLength);
			this.groupBox2.Location = new System.Drawing.Point(8, 8);
			this.groupBox2.Name = "groupBox2";
			this.groupBox2.Size = new System.Drawing.Size(664, 112);
			this.groupBox2.TabIndex = 0;
			this.groupBox2.TabStop = false;
			this.groupBox2.Text = "Параметры";
			// 
			// groupBox3
			// 
			this.groupBox3.Controls.Add(this.textBoxIn);
			this.groupBox3.Controls.Add(this.label4);
			this.groupBox3.Controls.Add(this.buttonOpenIn);
			this.groupBox3.Controls.Add(this.buttonOpenOut);
			this.groupBox3.Controls.Add(this.label5);
			this.groupBox3.Controls.Add(this.textBoxOut);
			this.groupBox3.Controls.Add(this.buttonEncipher);
			this.groupBox3.Controls.Add(this.buttonDecipher);
			this.groupBox3.Location = new System.Drawing.Point(8, 120);
			this.groupBox3.Name = "groupBox3";
			this.groupBox3.Size = new System.Drawing.Size(664, 128);
			this.groupBox3.TabIndex = 26;
			this.groupBox3.TabStop = false;
			this.groupBox3.Text = "Действия с файлами";
			// 
			// MainForm
			// 
			this.AutoScaleBaseSize = new System.Drawing.Size(8, 15);
			this.ClientSize = new System.Drawing.Size(826, 259);
			this.Controls.Add(this.groupBox3);
			this.Controls.Add(this.groupBox2);
			this.Controls.Add(this.groupBox1);
			this.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
			this.MaximizeBox = false;
			this.Menu = this.mainMenu1;
			this.MinimizeBox = false;
			this.Name = "MainForm";
			this.Text = "Демонстрация алгоритма шифрования Rijndael";
			this.Load += new System.EventHandler(this.Form1_Load);
			this.groupBox1.ResumeLayout(false);
			this.groupBox2.ResumeLayout(false);
			this.groupBox3.ResumeLayout(false);
			this.ResumeLayout(false);

		}
		#endregion


		#endregion


		#region <<<---Main--->>>

		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main() 
		{
			Application.Run(new MainForm());
		}

		#endregion


		#region Хэндлеры

		private void Form1_Load(object sender, EventArgs e)
		{
			this.comboBoxKeyLength.SelectedIndex = 0;
			this.comboBoxBlockLength.SelectedIndex = 0;
		}


		private void comboBoxKeyLength_SelectedIndexChanged(object sender, EventArgs e)
		{
			if ( this.comboBoxKeyLength.SelectedIndex == 0 )
				this.textBoxCipherKey.Height = 24;
			else
				this.textBoxCipherKey.Height = 48;
			this.textBoxCipherKey.MaxLength = ( 16 + 8 * this.comboBoxKeyLength.SelectedIndex ) * 2 + 16 + 8 * this.comboBoxKeyLength.SelectedIndex - 1;
			if ( this.textBoxCipherKey.Text.Length > this.textBoxCipherKey.MaxLength )
				this.textBoxCipherKey.Text = this.textBoxCipherKey.Text.Substring( 0, this.textBoxCipherKey.MaxLength );
		}

		#endregion


		#region Получение ключа

		private bool GetKeyFromTextBox()
		{
			String[] ss = this.textBoxCipherKey.Text.Split( new char[] {' '} );
			if ( ss.Length.ToString() != this.comboBoxKeyLength.Text )
			{
				MessageBox.Show( "Длина ключа не совпадает с указанной!", "Ошибка" );
				return false;
			}

			//Считываем ключ
			byte[] key = new byte[ ss.Length ];
			try
			{
				for ( int i = 0; i < ss.Length; i++ )
					key[i] = Convert.ToByte( ss[i], 16 );
			}
			catch ( Exception e )
			{
				MessageBox.Show( e.Message, "Ошибка преобразования" );
				return false;
			}
			this.r.CipherKey = key;
			return true;
		}

		#endregion


		#region Просмотр расширенного ключа

		private void buttonExpandedKey_Click(object sender, EventArgs e)
		{
			if ( this.GetKeyFromTextBox() == true )
			{
				//Показываем расширенный
				String expKey = "";
				foreach ( byte b in this.r.ExpandedKey )
					expKey += b.ToString( "X2" ) + " ";
				InfoForm form = new InfoForm();
				form.Text = "Расширенный ключ";
				form.info = expKey.Trim();
				form.ShowDialog();
			}
		}

		#endregion


		#region Выбор входного файла

		private bool SelectInput()
		{
			OpenFileDialog dialog = new OpenFileDialog();
			dialog.Title = "Выберите файл для шифрования";
			if ( dialog.ShowDialog() == DialogResult.OK )
			{
				this.textBoxIn.Text = dialog.FileName;
				return true;
			}
			else
				return false;
		}

		#endregion


		#region Выбор выходного


		private bool SelectOutput()
		{
			SaveFileDialog dialog = new SaveFileDialog();
			dialog.Title = "Выберите файл для записи зашифрованной информации";
			if ( dialog.ShowDialog() == DialogResult.OK )
			{
				this.textBoxOut.Text = dialog.FileName;
				return true;
			}
			else
				return false;
		}

		#endregion


		#region Отображение файлов

		private void buttonOpenIn_Click(object sender, EventArgs e)
		{
			OpenAndShowFile( this.textBoxIn.Text, "Входной файл ");
		}

		private void buttonOpenOut_Click(object sender, EventArgs e)
		{
			OpenAndShowFile( this.textBoxOut.Text, "Выходной файл ");
		}

		private void OpenAndShowFile( String filename, String title )
		{
			if ( File.Exists( filename ) == false )
				return;
			FileStream fs = new FileStream( filename, FileMode.Open );
			byte[] data = new byte[ fs.Length ];
			try
			{
				fs.Read( data, 0, Convert.ToInt32( fs.Length ) );
			}
				catch ( Exception e )
			{
				MessageBox.Show( e.StackTrace );
			}
			fs.Close();
	
			StringBuilder sb = new StringBuilder();
			foreach ( byte b in data )
				sb.Append( b.ToString( "X2" ) + " " );
			InfoForm form = new InfoForm();
			form.Text = title + filename;
			form.info = sb.ToString().Trim();
			form.ShowDialog();
		}

		#endregion


		#region Шифрование

		private void buttonEncipher_Click(object sender, EventArgs e)
		{
			this.textBoxIn.Text = "";
			this.textBoxOut.Text = "";
			if ( File.Exists( this.textBoxIn.Text ) == false )
				if ( this.SelectInput() == false )
					return;
			if ( File.Exists( this.textBoxOut.Text ) == false )
				if ( this.SelectOutput() == false )
					return;

			//ставим размеры блока
			this.r.BlockLength = (byte)( 16 + this.comboBoxBlockLength.SelectedIndex * 8 );

			//устанавливаем ключ
			if ( this.GetKeyFromTextBox() == false )
				return;

			//считываем данные
			FileStream fileStreamIn = new FileStream( this.textBoxIn.Text, FileMode.Open );
			byte[] data = new byte[ fileStreamIn.Length ];
			try
			{
				fileStreamIn.Read( data, 0, Convert.ToInt32( fileStreamIn.Length ) );
			}
			catch ( Exception ex )
			{
				MessageBox.Show( ex.StackTrace );
			}

			fileStreamIn.Close();

			//шифруем
			data = r.Encipher( data );

			//записываем данные
			FileStream fileStreamOut = new FileStream( this.textBoxOut.Text, FileMode.Create );
			fileStreamOut.Write( data, 0, data.Length );
			fileStreamOut.Close();
		}

		#endregion


		#region Дешифрование

		private void buttonDecipher_Click(object sender, EventArgs e)
		{
			this.textBoxIn.Text = "";
			this.textBoxOut.Text = "";
			if ( File.Exists( this.textBoxIn.Text ) == false )
				if ( this.SelectInput() == false )
					return;
			if ( File.Exists( this.textBoxOut.Text ) == false )
				if ( this.SelectOutput() == false )
					return;

			//ставим размеры ключа и блока
			this.r.BlockLength = (byte)( 16 + this.comboBoxBlockLength.SelectedIndex * 8 );

			//устанавливаем ключ
			if ( this.GetKeyFromTextBox() == false )
				return;


			//считываем данные
			FileStream fileStreamIn = new FileStream( this.textBoxIn.Text, FileMode.Open );
			byte[] data = new byte[ fileStreamIn.Length ];
			try
			{
				fileStreamIn.Read( data, 0, Convert.ToInt32( fileStreamIn.Length ) );
			}
			catch ( Exception ex )
			{
				MessageBox.Show( ex.StackTrace );
			}

			fileStreamIn.Close();

			//шифруем
			data = r.Decipher( data );

			//записываем данные
			if ( data != null )
			{
				FileStream fileStreamOut = new FileStream( this.textBoxOut.Text, FileMode.Create );
				fileStreamOut.Write( data, 0, data.Length );
				fileStreamOut.Close();
			}
		}

		#endregion


		#region Меню

		private void menuItem2_Click(object sender, EventArgs e)
		{
			this.Close();
		}

		private void menuItem4_Click(object sender, EventArgs e)
		{
			MessageBox.Show( "Программа демонстрации алгоритма шифрования Rijndael.\n© Смирнов Виктор 2005г", "О программе RijndaelDemo" );
		}

		#endregion


		#region Примеры трансформаций

		private void buttonByteSub_Click(object sender, EventArgs e)
		{
			this.ShowExampleTransformation("Преобразование ByteSub");
		}

		private void buttonShiftRow_Click(object sender, EventArgs e)
		{
			this.ShowExampleTransformation("Преобразование ShiftRow");
		}

		private void buttonMixColumn_Click(object sender, EventArgs e)
		{
			this.ShowExampleTransformation("Преобразование MixColumn");
		}

		private void buttonAddRoundKey_Click(object sender, EventArgs e)
		{
			this.ShowExampleTransformation("Преобразование AddRoundKey");
		}

		public void ShowExampleTransformation( string text )
		{
			//устанавливаем ключ
			if ( this.GetKeyFromTextBox() == false )
				return;
	
			//ставим размеры ключа и блока
			this.r.KeyLength = (byte)( 16 + this.comboBoxKeyLength.SelectedIndex * 8 );
			this.r.BlockLength = (byte)( 16 + this.comboBoxBlockLength.SelectedIndex * 8 );

			ExampleForm form = new ExampleForm( this.r, text );
			form.ShowDialog();
		}

		#endregion
	}
}