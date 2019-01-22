def pl0_broken():
	return (0)


def pl1_or(ent1, ent2):
	if ent1 == 1 or ent2 == 1:
		return (1)
	else:
		return (0)


def pl2_and(ent1, ent2):
	if ent1 == 0 or ent2 == 0:
		return (0)
	else:
		return (1)



def pl3_not(ent1):
	if ent1 == 0:
		return (1)
	else:
		return (0)



def pl4_nand(ent1, ent2):
	if ent1 == 0 or ent2 == 0:
		return (1)
	else:
		return (0)


def pl5_xor(ent1, ent2):
	if (ent1 == 1  and ent2 == 0) or (ent1 == 0  and ent2 == 1):
		return (1)
	else:
		return (0)


# --- OPTATIVAS ---
def pl6_yes(ent1):
	return(ent1)


def pl7_xnor(ent1, ent2):
	if ent1 == ent2:
		return (1)
	else:
		return (0)

def pl8_nor(ent1, ent2):
	if ent1 == ent2 == 0:
		return 1
	else:
		return 0
