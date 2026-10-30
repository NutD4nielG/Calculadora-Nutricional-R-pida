def prot():
    kcal = gr_prot * 4
    return kcal
def cho():
    kcal = gr_cho * 4
    return kcal
def grasa():
    kcal = gr_grasa * 9
    return kcal

gr_prot = int(input("Ingrese gramos de proteína: "))
gr_cho =  int(input("Ingrese gramos de carbohidratos: "))
gr_grasa =  int(input("Ingrese gramos de grasa: "))

total_kcal = prot() + cho() + grasa()
print(f"El total de calorías de la recera es: {total_kcal}")

