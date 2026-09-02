import abc

class Temperature(abc.ABC):
    def __init__(self, value: float):
        self.value = value

    @abc.abstractmethod
    def to_celsius(self) -> 'Celsius':
        pass

    @abc.abstractmethod
    def to_fahrenheit(self) -> 'Fahrenheit':
        pass

    @abc.abstractmethod
    def to_kelvin(self) -> 'Kelvin':
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"


class Celsius(Temperature):
    def to_celsius(self) -> 'Celsius':
        return self

    def to_fahrenheit(self) -> 'Fahrenheit':
        return Fahrenheit((self.value * 9/5) + 32)

    def to_kelvin(self) -> 'Kelvin':
        return Kelvin(self.value + 273.15)


class Fahrenheit(Temperature):
    def to_celsius(self) -> 'Celsius':
        return Celsius((self.value - 32) * 5/9)

    def to_fahrenheit(self) -> 'Fahrenheit':
        return self

    def to_kelvin(self) -> 'Kelvin':
        return Kelvin((self.value - 32) * 5/9 + 273.15)


class Kelvin(Temperature):
    def to_celsius(self) -> 'Celsius':
        return Celsius(self.value - 273.15)

    def to_fahrenheit(self) -> 'Fahrenheit':
        return Fahrenheit((self.value - 273.15) * 9/5 + 32)

    def to_kelvin(self) -> 'Kelvin':
        return self
# Exercise 2: Quantum Realm
# This implementation handles measurements, quantum disturbance updates, object representations, and quantum entanglement between particles.

import random

class QuantumParticle:
    def __init__(self, x: int = None, y: float = None, p: float = None):
        self.x = x if x is not None else random.randint(1, 10000)
        self.y = y if y is not None else random.uniform(0, 1)
        self.p = p if p in (0.5, -0.5) else random.choice([0.5, -0.5])
        self.entangled_particle = None

    def _disturbance(self):
        self.x = random.randint(1, 10000)
        self.y = random.uniform(0, 1)
        print("Quantum Interferences!!")

    def position(self) -> int:
        self._disturbance()
        return self.x

    def momentum(self) -> float:
        self._disturbance()
        return self.y

    def spin(self) -> float:
        self._disturbance()
        if self.entangled_particle:
            # Setting the entangled particle's spin to the opposite value
            self.entangled_particle.p = -self.p
        return self.p

    def entangle(self, other: 'QuantumParticle'):
        if not isinstance(other, QuantumParticle):
            raise TypeError("A quantum particle can only be entangled to another QuantumParticle.")
        
        self.entangled_particle = other
        other.entangled_particle = self
        print("Spooky Action at a Distance !!")

    def __repr__(self):
        entangled_status = f", entangled=True" if self.entangled_particle else ""
        return f"QuantumParticle(x={self.x}, y={self.y:.4f}, spin={self.p}{entangled_status})"