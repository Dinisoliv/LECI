library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity DisplayDemo is
	port (SW   : in std_logic_vector(3 downto 0); 
        KEY   : in std_logic_vector(0 downto 0);
        HEX0  : out std_logic_vector(6 downto 0);
        LEDR  : out std_logic_vector(6 downto 0); 
        LEDG  : out std_logic_vector(3 downto 0));
end DisplayDemo;

architecture Behavioral of DisplayDemo is
	signal s_decOut_n : std_logic_vector(6 downto 0);
begin
	bin_7_seg_decider : entity work.Bin7SegDecoder(Behavioral)
		port map(binInput  => SW,
					enable    => KEY(0),
					decOut_n  => s_decOut_n);
					
	HEX0 <= s_decOut_n;
	LEDR <= s_decOut_n;
	LEDG <= SW;
end Behavioral;