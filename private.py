class CoffeeMachine:

    WATER_LEVEL = 100

    def _start_machine(self):
        # methode protégée "_"
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("please add water")
            return False

    def __boil_water(self):
        # methode privée "__"
        return "boiling..."

    def make_coffee(self):
        if self._start_machine():
            self.WATER_LEVEL -= 20
            print(self.__boil_water())
            print("coffee is ready")


machine = CoffeeMachine()
# for i in range(0, 5):
#     machine.make_coffee()

print("Make Coffee: Public", machine.make_coffee())
print("Start Machine: Protected", machine._start_machine())


# ça marche en écrivant _MaClasse__methode_privee() question de philosophie et de responsabilité
print("Boil Water: Private", machine._CoffeeMachine__boil_water())

# erreurr si on tente directemnt
print("Boil Water: Private", machine.__boil_water())
