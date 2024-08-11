//=================================================================
//Copyright (C) 2024 MOMOTA Micro-electronics. All rights reserved.
// 
// File Name   :reg_model.sv
// Creater     :Dan
// Create Date :2024-05-16 21:39:52
// Modification History:
// 
// Description:
// 
//=================================================================

`ifndef REG_MODEL_SV
`define REG_MODEL_SV

class REG0 extends uvm_reg;
    rand uvm_reg_field p0_l;
    rand uvm_reg_field p0_h;

    virtual function void build();
        p0_l = uvm_reg_field::type_id::create("p0_l");
        p0_h = uvm_reg_field::type_id::create("p0_h");
        //parameter:this,size,lsb_pos,access,1,reset value,1,1,0)
        p0_l.configure(this,8,0,"RW",1,4'hff,1,1,0);
        p0_h.configure(this,8,0,"RW",1,4'hff,1,1,0);
    endfunction

    `uvm_object_utils(REG0)

    function new (string name = "REG0");
        //parameter:name,bus_size(data),UVM_NO_COVERAGE
        super.new(name,8,UVM_NO_COVERAGE);
    endfunction:new
endclass:REG0

class REG1 extends uvm_reg;
    rand uvm_reg_field p1_l;
    rand uvm_reg_field p1_h;

    virtual function void build();
        p1_l = uvm_reg_field::type_id::create("p1_l");
        p1_h = uvm_reg_field::type_id::create("p1_h");
        //parameter:this,size,lsb_pos,access,1,reset value,1,1,0)
        p1_l.configure(this,8,0,"RW",1,4'hff,1,1,0);
        p1_h.configure(this,8,0,"RW",1,4'hff,1,1,0);
    endfunction

    `uvm_object_utils(REG1)

    function new (string name = "REG1");
        //parameter:name,bus_size(data),UVM_NO_COVERAGE
        super.new(name,8,UVM_NO_COVERAGE);
    endfunction:new
endclass:REG1

/*
 *...
 */

class reg_model extends uvm_reg_block;
    rand REG0 reg0;
    rand REG1 reg1;

    virtual function void build();
        default_map = create_map("default_map",0,1,UVM_LITTLE_ENDIAN,0);

        reg0 = REG0::type_id::create("reg0", ,get_full_name());
        reg0.configure(this,null,"");
        reg0.build();
        //parameter:filed_name,lsb_pos,size
        reg0.add_hdl_path_slice.("p0_l",0,4);
        reg0.add_hdl_path_slice.("p0_h",4,4);
        //parameter:reg_ins_name,reg_addr,reg_access
        //offset_addr
        default_map.add_reg(reg0,'h00,"RW");

        reg1 = REG1::type_id::create("reg1", ,get_full_name());
        reg1.configure(this,null,"");
        reg1.build();
        reg1.add_hdl_path_slice.("p1_l",0,4);
        reg1.add_hdl_path_slice.("p1_h",4,4);
        default_map.add_reg(reg1,'h01,"RW");
    endfunction

    `uvm_object_utils(reg_model)

    function new (string name = "reg_model");
        super.new(name,UVM_NO_COVERAGE);
    endfunction:new
endclass:reg_model

class sys extends uvm_reg_block;
    //actual_addr = base_addr + offset_addr;
    rand reg_model model;

    virtual function void build();
        default_map = create_map("default_map",0,1,UVM_LITTLE_ENDIAN,0);

        model = model::type_id::create("model");
        model.configure(this,"");
        model.build();
        model.lock_model();
        //base_addr
        default_map.add_submap(model.default_map,8'h0);
    endfunction

    `uvm_object_utils(sys)

    function new (string name = "sys");
        super.new(name,UVM_NO_COVERAGE);
    endfunction:new
endclass:sys

`endif 
