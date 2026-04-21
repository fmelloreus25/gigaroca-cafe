import { useState } from 'react'
import './index.css'
// Importando os ícones profissionais que acabamos de instalar
import { 
  LayoutDashboard, 
  ShoppingCart, 
  Package, 
  ArrowLeftRight, 
  DollarSign, 
  Store 
} from 'lucide-react'

function App() {
  // O React guarda aqui qual é a tela que está aberta no momento. O padrão é 'painel'
  const [telaAtiva, setTelaAtiva] = useState('painel')

  // Essa função renderiza o conteúdo da tela dependendo do que estiver selecionado
  const renderizarConteudo = () => {
    switch (telaAtiva) {
      case 'painel':
        return <div className="cartao-placeholder"><h2>📊 Visão Geral</h2><p>Gráficos de faturamento e vendas do dia aparecerão aqui.</p></div>
      case 'pdv':
        return <div className="cartao-placeholder"><h2>🛒 Frente de Caixa (PDV)</h2><p>Interface rápida para registrar vendas no balcão.</p></div>
      case 'produtos':
        return <div className="cartao-placeholder"><h2>🧀 Catálogo de Produtos</h2><p>Lista de produtos, preços e botão de Novo Produto.</p></div>
      case 'estoque':
        return <div className="cartao-placeholder"><h2>📦 Controle de Estoque</h2><p>Entradas, saídas e transferências entre Lojas.</p></div>
      case 'financeiro':
        return <div className="cartao-placeholder"><h2>💰 Financeiro</h2><p>Contas a pagar, receber e relatórios de lucro.</p></div>
      case 'lojas':
        return <div className="cartao-placeholder"><h2>🏪 Lojas & Permissões</h2><p>Gestão de filiais e acessos de usuários (Gerente/Vendedor).</p></div>
      default:
        return null
    }
  }

  // Nome do título que vai aparecer no cabeçalho branco lá em cima
  const titulos = {
    painel: "Painel Geral",
    pdv: "Registrar Venda (PDV)",
    produtos: "Gestão de Produtos",
    estoque: "Movimentações de Estoque",
    financeiro: "Controle Financeiro",
    lojas: "Lojas e Permissões"
  }

  return (
    <div className="layout-mestre">
      
      {/* --- BARRA LATERAL (SIDEBAR) --- */}
      <aside className="sidebar">
        <div className="sidebar-logo">
          ☕ GigaRoça
        </div>
        
        <nav className="sidebar-menu">
          <div className={`menu-item ${telaAtiva === 'painel' ? 'ativo' : ''}`} onClick={() => setTelaAtiva('painel')}>
            <LayoutDashboard size={20} /> Painel Geral
          </div>
          
          <div className={`menu-item ${telaAtiva === 'pdv' ? 'ativo' : ''}`} onClick={() => setTelaAtiva('pdv')}>
            <ShoppingCart size={20} /> Registrar Venda
          </div>
          
          <div className={`menu-item ${telaAtiva === 'produtos' ? 'ativo' : ''}`} onClick={() => setTelaAtiva('produtos')}>
            <Package size={20} /> Cadastrar Produtos
          </div>
          
          <div className={`menu-item ${telaAtiva === 'estoque' ? 'ativo' : ''}`} onClick={() => setTelaAtiva('estoque')}>
            <ArrowLeftRight size={20} /> Estoque & Transf.
          </div>
          
          <div className={`menu-item ${telaAtiva === 'financeiro' ? 'ativo' : ''}`} onClick={() => setTelaAtiva('financeiro')}>
            <DollarSign size={20} /> Financeiro
          </div>
          
          <div className={`menu-item ${telaAtiva === 'lojas' ? 'ativo' : ''}`} onClick={() => setTelaAtiva('lojas')}>
            <Store size={20} /> Lojas e Equipe
          </div>
        </nav>
      </aside>

      {/* --- ÁREA DE CONTEÚDO (DIREITA) --- */}
      <main className="area-conteudo">
        <header className="cabecalho-pagina">
          <h1>{titulos[telaAtiva]}</h1>
        </header>
        
        <section className="conteudo-dinamico">
          {/* A mágica acontece aqui: o conteúdo muda conforme o clique */}
          {renderizarConteudo()}
        </section>
      </main>

    </div>
  )
}

export default App