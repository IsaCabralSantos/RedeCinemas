# Sistema de Rede de Cinemas

## Sobre o Projeto

Este projeto implementa um sistema de gestao para uma rede de cinemas. O sistema permite gerenciar cinemas, filmes, sessoes e gerar relatorios de publico.

## Estrutura de Diretorios

```
atvd06-05/
├── app.py                 
├── database.py            
├── models/              
│   ├── cinema.py
│   ├── filme.py
│   └── sessao.py
├── controllers/       
│   ├── cinema_controller.py
│   ├── filme_controller.py
│   └── sessao_controller.py
├── services/            
│   ├── cinema_service.py
│   ├── filme_service.py
│   └── sessao_service.py
├── repository/           
│   ├── cinema_repository.py
│   ├── filme_repository.py
│   └── sessao_repository.py
├── views/                 
│   ├── cinema_view.py
│   ├── filme_view.py
│   └── sessao_view.py
├── docs/               
│   ├── RF.md             
│   └── RN.md            
│
└── cinema.db            
```

## Funcionalidades

### Gerenciar Cinemas
- Cadastrar novos cinemas
- Listar cinemas cadastrados
- Atualizar informacoes
- Excluir cinemas

### Gerenciar Filmes
- Cadastrar novos filmes
- Listar filmes disponiveis
- Atualizar informacoes
- Excluir filmes

### Gerenciar Sessoes
- Cadastrar sessoes
- Listar sessoes por cinema/filme
- Registrar publico das sessoes
- Atualizar sessoes
- Excluir sessoes

### Relatorios
- Publico por sessao
- Publico total por filme
- Publico total por cinema
- Ocupacao percentual por sessao

**Desenvolvido para a disciplina de Engenharia de Software** 

*Data: 06-05-2026* 
