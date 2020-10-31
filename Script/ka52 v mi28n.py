rhs_ammo_spall:
	"caliber": 10,
	"deflecting": 90,
	"deflectiondirdistribution": 1,
	"deflectionslowdown": 2,
	"hit": 20,
	"indirecthit": 0,
	"indirecthitrange": 0.15,
	"penetrationdirdistribution": 1,
	"typicalspeed": 50,
	#""initspeed"" = 200
	# penetration = 30mm RHA


Rhs_mag_b13l_s13b:
	"airfriction": 0.09,
	"fusedistance": 50,
	"hit": 470,
	"indirecthit": 240,
	"indirecthitrange": 10,
	"initspeed": 44,
	"maxspeed": 590, #doesn't really mean maximum speed
	"thrust": 1060,
	"thrusttime": 0.6,
	"timetolive": 15,
	rhs_ammo_s8_penetrator:
		#(5 spall (ATGMs usually produce 30))
		"submunitionconetype": ["randomcenter",5],
		"caliber": 26.6667,
		"hit": 290,
		"typicalspeed": 1000,
		# penetration = 400.0005mm RHA

rhs_mag_9M120M_Mi28_8x:
	"airfriction": -2e-005,
	"explosive": 1,
	"fusedistance": 100,
	"hit": 350,
	"indirecthit": 26,
	"indirecthitrange": 4.6,
	"maneuvrability": 13,
	"maxcontrolrange": 8000,
	"maxspeed": 550,
	"missilemanualcontrolcone": 50,
	"rhs_ballisticmode": 0,
	"rhs_guidemode": "RADIO",
	"rhs_saclos": 2,
	"sideairfriction": 0.3,
	"thrust": 172,
	"thrusttime": 3.5,
	"timetolive": 25,
	"tracklead": 0,
	"trackoversteer": 1,
	"typicalspeed": 115,
	rhs_ammo_9m120m_penetrator:
		"hit": 290,
		"caliber": 63.3333,
		"typicalspeed": 1000,
		# penetration = 949.9995mm RHA


rhs_mag_apu6_9m127m_ka52:
	"airfriction": 0.075,
	"cmimmunity": 0.9,
	"explosive": 1,
	"fusedistance": 100,
	"hit": 240,
	"indirecthit": 86,
	"indirecthitrange": 9.6,
	"maneuvrability": 16,
	"maxcontrolrange": 10000,
	"maxspeed": 600,
	"missilemanualcontrolcone": 50,
	"rhs_ballisticmode": 0,
	"rhs_guidemode": "BEAMRIDER",
	"rhs_saclos": 2,
	"sideairfriction": 0.3,
	"thrust": 342,
	"thrusttime": 3,
	"timetolive": 25,
	"tracklead": 1,
	"trackoversteer": 1,
	"typicalspeed": 115,
	rhs_ammo_9m127_penetrator:
		"hit": 290,
		"caliber": 70,
        "typicalspeed": 1000,
		# penetration = 1050mm rha

rhs_mag_b8v20a_ka52_s8kom:
	"airfriction": 0.09,
	"fusedistance": 50,
	"hit": 400,
	"indirecthit": 60,
	"indirecthitrange": 15,
	"maxspeed": 590,
	"thrust": 1060,
	"thrusttime": 0.69,
    "timetolive": 15,
	rhs_ammo_s8_penetrator:
		#(5 spall (ATGMs usually produce 30))
		"submunitionconetype": ["randomcenter",5],
		"caliber": 26.6667,
		"hit": 290,
		"typicalspeed": 1000,
		# penetration = 400.0005mm RHA