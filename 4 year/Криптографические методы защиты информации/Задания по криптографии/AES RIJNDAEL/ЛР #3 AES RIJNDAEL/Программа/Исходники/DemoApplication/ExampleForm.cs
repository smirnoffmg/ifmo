using System;
using System.ComponentModel;
using System.Windows.Forms;
using Rijndael;

namespace DemoApplication
{
	/// <summary>
	/// Summary description for ExampleForm.
	/// </summary>
	public class ExampleForm : System.Windows.Forms.Form
	{
		#region Поля

		private TextBox textBoxState;
		private Label label1;
		private Label label2;
		private TextBox textBoxResult;
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private Container components = null;
		private System.Windows.Forms.RadioButton radioButton1;
		private System.Windows.Forms.RadioButton radioButton2;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.TextBox textBoxKey;
		private System.Windows.Forms.Label label3;

		private Rijndael.Rijndael r;

		#endregion


		#region Конструктор

		public ExampleForm( Rijndael.Rijndael r, String text )
		{
			InitializeComponent();
			this.r = r;
			this.Text = text;
			this.textBoxState.Text = "";
			for ( int j = 0; j < this.r.BlockLength; j++ )
				this.textBoxState.Text += "00 ";
			this.textBoxResult.Text = this.textBoxState.Text;
			this.textBoxState.Width = 60 + ( ( this.r.BlockLength - 8) / 8 ) * 60;
			if ( this.Text.EndsWith( "AddRoundKey" ) )
			{
				this.textBoxKey.Text = this.textBoxState.Text;
				this.textBoxKey.Size = this.textBoxState.Size;
				this.textBoxResult.Size = this.textBoxState.Size;
				this.textBoxResult.Size = this.textBoxState.Size;
				this.textBoxKey.Left = this.textBoxState.Left + this.textBoxState.Width + 20;
				this.textBoxResult.Left = this.textBoxKey.Left + this.textBoxKey.Width + 20;
				this.label2.Left = this.textBoxResult.Left;
				this.label3.Left = this.textBoxKey.Left;
				this.label3.Visible = true;
				this.textBoxKey.Visible = true;
				this.radioButton1.Visible = false;
				this.radioButton2.Visible = false;
				this.button1.Top = this.radioButton1.Top;
				this.Height = this.radioButton2.Top + 30;
			}
			else
			{
				this.textBoxResult.Size = this.textBoxState.Size;
				this.textBoxResult.Left = this.textBoxState.Left + this.textBoxState.Width + 20;
				this.label2.Left = this.textBoxResult.Left;
			}
			this.Width = this.textBoxResult.Left + this.textBoxResult.Width + 20;
			this.button1.Width = this.textBoxResult.Left + this.textBoxResult.Width - this.textBoxState.Left;
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
				if(components != null)
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
			this.textBoxState = new System.Windows.Forms.TextBox();
			this.label1 = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.textBoxResult = new System.Windows.Forms.TextBox();
			this.radioButton1 = new System.Windows.Forms.RadioButton();
			this.radioButton2 = new System.Windows.Forms.RadioButton();
			this.button1 = new System.Windows.Forms.Button();
			this.textBoxKey = new System.Windows.Forms.TextBox();
			this.label3 = new System.Windows.Forms.Label();
			this.SuspendLayout();
			// 
			// textBoxState
			// 
			this.textBoxState.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.textBoxState.Location = new System.Drawing.Point(16, 40);
			this.textBoxState.Multiline = true;
			this.textBoxState.Name = "textBoxState";
			this.textBoxState.Size = new System.Drawing.Size(120, 80);
			this.textBoxState.TabIndex = 1;
			this.textBoxState.Text = "00 00 00 00";
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.label1.Location = new System.Drawing.Point(16, 16);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(55, 22);
			this.label1.TabIndex = 1;
			this.label1.Text = "Вход:";
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.label2.Location = new System.Drawing.Point(152, 16);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(65, 22);
			this.label2.TabIndex = 3;
			this.label2.Text = "Выход:";
			// 
			// textBoxResult
			// 
			this.textBoxResult.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.textBoxResult.Location = new System.Drawing.Point(152, 40);
			this.textBoxResult.Multiline = true;
			this.textBoxResult.Name = "textBoxResult";
			this.textBoxResult.Size = new System.Drawing.Size(128, 80);
			this.textBoxResult.TabIndex = 2;
			this.textBoxResult.Text = "";
			// 
			// radioButton1
			// 
			this.radioButton1.Checked = true;
			this.radioButton1.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.radioButton1.Location = new System.Drawing.Point(16, 136);
			this.radioButton1.Name = "radioButton1";
			this.radioButton1.Size = new System.Drawing.Size(144, 24);
			this.radioButton1.TabIndex = 4;
			this.radioButton1.TabStop = true;
			this.radioButton1.Text = "Шифрование";
			// 
			// radioButton2
			// 
			this.radioButton2.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.radioButton2.Location = new System.Drawing.Point(16, 168);
			this.radioButton2.Name = "radioButton2";
			this.radioButton2.Size = new System.Drawing.Size(144, 24);
			this.radioButton2.TabIndex = 5;
			this.radioButton2.Text = "Дешифрование";
			// 
			// button1
			// 
			this.button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
			this.button1.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.button1.Location = new System.Drawing.Point(16, 200);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(168, 24);
			this.button1.TabIndex = 0;
			this.button1.Text = "Преобразовать";
			this.button1.Click += new System.EventHandler(this.button1_Click);
			// 
			// textBoxKey
			// 
			this.textBoxKey.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.textBoxKey.Location = new System.Drawing.Point(120, 40);
			this.textBoxKey.Multiline = true;
			this.textBoxKey.Name = "textBoxKey";
			this.textBoxKey.Size = new System.Drawing.Size(120, 80);
			this.textBoxKey.TabIndex = 6;
			this.textBoxKey.Text = "00 00 00 00";
			this.textBoxKey.Visible = false;
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.label3.Location = new System.Drawing.Point(96, 16);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(55, 22);
			this.label3.TabIndex = 7;
			this.label3.Text = "Ключ:";
			this.label3.Visible = false;
			// 
			// ExampleForm
			// 
			this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
			this.ClientSize = new System.Drawing.Size(304, 232);
			this.Controls.Add(this.label3);
			this.Controls.Add(this.textBoxKey);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.radioButton2);
			this.Controls.Add(this.radioButton1);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.textBoxResult);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.textBoxState);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "ExampleForm";
			this.ShowInTaskbar = false;
			this.Text = "ExampleForm";
			this.ResumeLayout(false);

		}
		#endregion

		#endregion
		private void button1_Click(object sender, System.EventArgs e)
		{
			byte[,] state = new byte[ 4, this.r.BlockLength / 4 ];
			string[] ss = this.textBoxState.Text.Trim().Split( new char[] {' '} );
			if ( ss.Length != this.r.BlockLength )
			{
				MessageBox.Show( "Длина блока не совпадает с указанной!", "Ошибка" );
				return;
			}

			//Считываем блок
			byte[] what = new byte[ this.r.BlockLength ];
			try
			{
				for ( int i = 0; i < this.r.BlockLength; i++ )
					what[i] = Convert.ToByte( ss[i], 16 );
			}
			catch ( Exception ex )
			{
				MessageBox.Show( ex.StackTrace );
			}


			try
			{
				for ( int k = 0; k < r.BlockLength / 4; k++ )
					for ( int j = 0; j < 4; j++ )
						state[ j, k ] = Convert.ToByte( ss[j * 4 + k], 16 );
			}
			catch ( Exception ex )
			{
				MessageBox.Show( ex.StackTrace );
			}


			if ( this.Text.EndsWith( "ByteSub" ) )
			{
				if ( this.radioButton1.Checked == true )
					state = this.r.ByteSubE( state );
				else
					state = this.r.ByteSubD( state );
			}
			else if ( this.Text.EndsWith( "ShiftRow" ) )
			{
				if ( this.radioButton1.Checked == true )
					state = this.r.ShiftRowE( state );
				else
					state = this.r.ShiftRowD( state );
			}
			else if ( this.Text.EndsWith( "MixColumn" ) )
			{
				if ( this.radioButton1.Checked == true )
					state = this.r.MixColumnE( state );
				else
					state = this.r.MixColumnD( state );
			}
			else if ( this.Text.EndsWith( "AddRoundKey" ) )
			{

				byte[,] state2 = new byte[ 4, this.r.BlockLength / 4 ];
				ss = this.textBoxKey.Text.Trim().Split( new char[] {' '} );
				if ( ss.Length != this.r.BlockLength )
				{
					MessageBox.Show( "Длина блока не совпадает с указанной!", "Ошибка" );
					return;
				}


				try
				{
					for ( int k = 0; k < r.BlockLength / 4; k++ )
						for ( int j = 0; j < 4; j++ )
							state2[ j, k ] = Convert.ToByte( ss[j * 4 + k], 16 );
				}
				catch ( Exception ex )
				{
					MessageBox.Show( ex.StackTrace );
				}

				
				for ( int k = 0; k < r.BlockLength / 4; k++ )
					for ( int j = 0; j < 4; j++ )
						state[j, k] ^= state2[j, k];
			}

		
			this.textBoxResult.Text = "";
			for ( int j = 0; j < 4; j++ )
				for ( int k = 0; k < r.BlockLength / 4; k++ )
					this.textBoxResult.Text += state[ j, k ].ToString( "X2" ) + " ";
		}
	}
}