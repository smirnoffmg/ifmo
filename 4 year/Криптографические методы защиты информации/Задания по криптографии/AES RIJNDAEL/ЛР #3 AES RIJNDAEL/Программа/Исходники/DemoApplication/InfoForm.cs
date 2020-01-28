using System;
using System.Drawing;
using System.ComponentModel;
using System.Windows.Forms;

namespace DemoApplication
{
	/// <summary>
	/// Summary description for InfoForm.
	/// </summary>
	public class InfoForm : System.Windows.Forms.Form
	{
		#region Поля

		private TextBox textBox;
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private Container components = null;

		#endregion

		public String info
		{
			get
			{
				return this.textBox.Text;
			}
			set
			{
				this.textBox.Text = value;
			}
		}

		#region Конструктор

		public InfoForm()
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
			this.textBox = new System.Windows.Forms.TextBox();
			this.SuspendLayout();
			// 
			// textBox
			// 
			this.textBox.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(204)));
			this.textBox.Location = new System.Drawing.Point(0, 0);
			this.textBox.Multiline = true;
			this.textBox.Name = "textBox";
			this.textBox.ReadOnly = true;
			this.textBox.ScrollBars = System.Windows.Forms.ScrollBars.Both;
			this.textBox.Size = new System.Drawing.Size(416, 300);
			this.textBox.TabIndex = 0;
			this.textBox.Text = "richTextBox1";
			// 
			// InfoForm
			// 
			this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
			this.ClientSize = new System.Drawing.Size(408, 266);
			this.Controls.Add(this.textBox);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.MinimizeBox = false;
			this.Name = "InfoForm";
			this.ShowInTaskbar = false;
			this.Text = "InfoForm";
			this.Resize += new System.EventHandler(this.InfoForm_Resize);
			this.Load += new System.EventHandler(this.InfoForm_Load);
			this.ResumeLayout(false);

		}
		#endregion


		#endregion


		private void InfoForm_Resize(object sender, System.EventArgs e)
		{
			this.textBox.Size = this.ClientSize;
		}

		private void InfoForm_Load(object sender, System.EventArgs e)
		{
			this.textBox.Size = this.ClientSize;
		}
	}
}