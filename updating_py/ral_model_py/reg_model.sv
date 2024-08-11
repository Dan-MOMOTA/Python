// Version 
// SFR excel name : reg.xlsx
// SFR excel time : Mon Apr  1 00:02:57 2024
// Genrate date   : 2024/4/6/0h/47min/45s
// Function       : for sfr test 
// Creator        : Dan 
 
`ifndef REG_MODEL_SV 
`define REG_MODEL_SV 
class trim_00 extends uvm_reg;
	rand uvm_reg_field trim_vx;
	rand uvm_reg_field trim_ib;
	rand uvm_reg_field trim_cco;
	rand uvm_reg_field trim_ntc;
	rand uvm_reg_field trim_bgr;

	`uvm_object_utils(trim_00)

	function new(string name = "trim_00");
		super.new(name, 32, build_coverage(UVM_NO_COVERAGE));
	endfunction:new

	virtual function void build();
		this.trim_vx = uvm_reg_field::type_id::create("trim_vx", ,get_full_name());
		this.trim_vx.configure(this,9,23,"RW",1,6'b100000,1,1,0);
		this.add_hdl_path_slice(.name("trim_vx"),.offset(23),.size(9));

		this.trim_ib = uvm_reg_field::type_id::create("trim_ib", ,get_full_name());
		this.trim_ib.configure(this,5,17,"RW",1,5'b01111,1,1,0);
		this.add_hdl_path_slice(.name("trim_ib"),.offset(17),.size(5));

		this.trim_cco = uvm_reg_field::type_id::create("trim_cco", ,get_full_name());
		this.trim_cco.configure(this,5,12,"RW",1,5'b10000,1,1,0);
		this.add_hdl_path_slice(.name("trim_cco"),.offset(12),.size(5));

		this.trim_ntc = uvm_reg_field::type_id::create("trim_ntc", ,get_full_name());
		this.trim_ntc.configure(this,6,6,"RW",1,6'b100000,1,1,0);
		this.add_hdl_path_slice(.name("trim_ntc"),.offset(6),.size(6));

		this.trim_bgr = uvm_reg_field::type_id::create("trim_bgr", ,get_full_name());
		this.trim_bgr.configure(this,6,0,"RW",1,6'b100000,1,1,0);
		this.add_hdl_path_slice(.name("trim_bgr"),.offset(0),.size(6));

	endfunction:build
endclass:trim_00

class trim_01 extends uvm_reg;
	rand uvm_reg_field trim_adc_offset_ch0;
	rand uvm_reg_field trim_adc_offset_ch1;
	rand uvm_reg_field trim_adc_offset_ch2;
	rand uvm_reg_field trim_adc_offset_ch3;

	`uvm_object_utils(trim_01)

	function new(string name = "trim_01");
		super.new(name, 32, build_coverage(UVM_NO_COVERAGE));
	endfunction:new

	virtual function void build();
		this.trim_adc_offset_ch0 = uvm_reg_field::type_id::create("trim_adc_offset_ch0", ,get_full_name());
		this.trim_adc_offset_ch0.configure(this,8,24,"RW",1,8'b0,1,1,0);
		this.add_hdl_path_slice(.name("trim_adc_offset_ch0"),.offset(24),.size(8));

		this.trim_adc_offset_ch1 = uvm_reg_field::type_id::create("trim_adc_offset_ch1", ,get_full_name());
		this.trim_adc_offset_ch1.configure(this,8,16,"RW",1,8'b0,1,1,0);
		this.add_hdl_path_slice(.name("trim_adc_offset_ch1"),.offset(16),.size(8));

		this.trim_adc_offset_ch2 = uvm_reg_field::type_id::create("trim_adc_offset_ch2", ,get_full_name());
		this.trim_adc_offset_ch2.configure(this,8,8,"RW",1,8'b0,1,1,0);
		this.add_hdl_path_slice(.name("trim_adc_offset_ch2"),.offset(8),.size(8));

		this.trim_adc_offset_ch3 = uvm_reg_field::type_id::create("trim_adc_offset_ch3", ,get_full_name());
		this.trim_adc_offset_ch3.configure(this,8,0,"RW",1,8'b0,1,1,0);
		this.add_hdl_path_slice(.name("trim_adc_offset_ch3"),.offset(0),.size(8));

	endfunction:build
endclass:trim_01

class reg_model extends uvm_reg_block;
	 rand trim_00 trim_00_ins;
	 rand trim_01 trim_01_ins;

	virtual function void build();
		default_map = create_map("default_map",0,4,UVM_LITTLE_ENDIAN,0);

		trim_00_ins = trim_00::type_id::create("trim_00_ins", ,get_full_name());
		trim_00_ins.configure(this,null,"");
		trim_00_ins.build();
		default_map.add_reg(trim_00_ins,'h00,"RW");

		trim_01_ins = trim_01::type_id::create("trim_01_ins", ,get_full_name());
		trim_01_ins.configure(this,null,"");
		trim_01_ins.build();
		default_map.add_reg(trim_01_ins,'h04,"RW");

	endfunction

	`uvm_object_utils(reg_model)

	function new(input string name = "reg_moedl");
		super.new(name,UVM_NO_COVERAGE);
	endfunction

endclass
`endif