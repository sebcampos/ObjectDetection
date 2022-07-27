# /home/mrrobot/.pyenv/versions/ObjectDetection/lib64/python3.8/site-packages/bluetooth

"""
bit 3 (0x08) is used for broadcasting video

GATT server is the bluetooth server

GAP or generic access profile define how devices discover and connections are created / taken down
	Four roles of bluetooth LE devices defined by GAP
	- peripheral
	- central       ---- could be this one
	- broadcaster

ATT the attribute protocal allows a connected GATT client to communicate with the GAT server and vice versa
	(PDUs) are the ATT protocol's data units

"""


from pandas import DataFrame 

AVRCP_SPEC = DataFrame({
	"Value": ["Bit 0 (0x01)", "Bit 1 (0x02)", "Bit 2 (0x04)", "Bit 3 (0x08)", "Bit 4-7"],
	"Parameter Description": ["Audio", "Video", "Boradcaseting Audio", "Broadcasting Video", "Reserved"]
})


GATT_OPERATIONS_CHARACTERISTICS_EXAMPLE = DataFrame({
	"Characteristic": ["READ", "WRITE WITHOUT RESPONSE", "NOTIFY", "WRITABLE AUXILIARIES", "EXTENDED PROPERTIES", "WRITE", "SIGNED WRITE", "INDICATE", "BROADCAST", "RELIABLE WRITE"],
	"Value": ["MANDATORY", "EXCLUDED", "MANDATORY", "EXCLUDED", "EXCLUDED", "EXCLUDED", "EXLUDED", "EXLUDED","EXLUDED", "EXLUDED"]	
})
