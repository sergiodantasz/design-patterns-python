from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('O carro de luxo está buscando o cliente.')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('O carro popular está buscando o cliente.')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('A moto de luxo está buscando o cliente.')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('A moto popular está buscando o cliente.')


class VeiculoFactory:
    @staticmethod
    def pegar_veiculo(tipo: str) -> Veiculo:
        if tipo == 'carro_luxo':
            return CarroLuxo()
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        if tipo == 'moto_popular':
            return MotoPopular()
        assert 0, 'O veículo não existe.'


if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis = ('carro_luxo', 'carro_popular', 'moto_luxo', 'moto_popular')
    for _ in range(10):
        carro = VeiculoFactory.pegar_veiculo(choice(veiculos_disponiveis))
        carro.buscar_cliente()
