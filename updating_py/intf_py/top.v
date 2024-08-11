//PART1
module fsm_drink(
    input    wire           clk         , 
    input    wire           rst_n       ,  
    input    wire   [1:0]   coin        , 
    input    wire           start_flag  , 
    input    wire           cancel      , 
    output   reg            drink_out   , 
    output   reg            charge_vld  , 
    //output   reg    [2:0]   charge_coin ,
    output   reg            working
    );

    parameter [2:0]  IDLE    = 3'b000;
    parameter [2:0]  START   = 3'b001;
    parameter [2:0]  COIN0_5 = 3'b010;
    parameter [2:0]  COIN1_0 = 3'b011;
    parameter [2:0]  COIN1_5 = 3'b100;
    parameter [2:0]  COIN2_0 = 3'b101;
    parameter [2:0]  COIN2_5 = 3'b110;
    parameter [2:0]  COIN3_0 = 3'b111;
   
    reg    [2:0]   cs;
    reg    [2:0]   ns;

    //1.CS
    always @(posedge clk or negedge rst_n)begin
        if(rst_n == 0)begin
            cs <= IDLE;
        end
        else begin
            cs <= ns;
        end
    end
endmodule

//PART2
interface top_interface();

    parameter setup_time  = 1; //1ns
    parameter holduo_time = 1; //1ns

    //input
    logic       clk         ;
    logic       rst_n       ;
    logic [1:0] coin        ;
    logic       start_flag  ;
    logic       cancel      ;

    //output
    logic       drink_out   ;
    logic       charge_vld  ;
    logic [2:0] charge_coin ;
    logic       working     ;

    clocking drv_ck(@posedge clk);
        output  clk         ;
        output  rst_n       ;
        output  coin        ;
        output  start_flag  ;
        output  cancel      ;
        input   drink_out   ;
        input   charge_vld  ;
        input   charge_coin ;
        input   working     ;
    endclocking

    clocking mon_ck(@posedge clk);
        input   clk         ;
        input   rst_n       ;
        input   coin        ;
        input   start_flag  ;
        input   cancel      ;
        input   drink_out   ;
        input   charge_vld  ;
        input   charge_coin ;
        input   working     ;
    endclocking
endinterface