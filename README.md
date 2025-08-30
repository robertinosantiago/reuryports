# Réury Ports

**Réury Ports** é um jogo educativo desenvolvido em Python usando o **Pygame**, criado para ensinar **portas lógicas** de forma divertida e interativa.

## Sobre o jogo

O jogador deve responder corretamente a expressões lógicas que caem do topo da tela, pressionando as teclas `0` ou `1`. São usadas as portas AND, OR e NOT.

O objetivo é acertar o maior número de desafios antes que suas vidas acabem.

## Mecânicas

- Cada desafio incorreto ou que atinge o chão sem resposta **custa uma vida**.  
- Há **placar de pontos**, contabilizando acertos.  
- O jogo possui **tela inicial** com instruções e **tela de Game Over**.  
- Corações na tela representam as vidas restantes.

## Controles

- **0** → Responder com valor 0  
- **1** → Responder com valor 1  
- **ENTER** → Iniciar o jogo na tela de instruções  
- **ESC** → Reiniciar o jogo após o Game Over

## Tecnologias

- Python 3.x  
- Pygame

## Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/reuryports.git
cd reuryports
```

2. Crie e ative um ambiente virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS, para Windows use: venv\Scripts\activate
```

3. Instale o Pygame:
```bash
pip install pygame
```

4. Execute o jogo:
```bash
python main.py
```
