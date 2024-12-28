import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import json
import os
import sys
from pathlib import Path
import uuid
import random
import importlib.util
import subprocess

# Add parent directory to Python path
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Import all available modules
def import_module(file_path):
    try:
        spec = importlib.util.spec_from_file_location("module", file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    except Exception as e:
        print(f"Error importing {file_path}: {e}")
    return None

# Load all available modules
MODULES = {
    'Crypto & Finance': {
        'MEV Disruptor': 'mev_disruptor.py',
        'Multi Chain Manager': 'multi_chain_manager.py',
        'Quantum Network': 'quantum_network.py',
        'Wallet Manager': 'wallet_manager.py',
        'Sniper Bot': 'sniper_bot.py',
        'AI Memecoin Sniper': 'ai_memecoin_sniper.py',
        'DeFi Manager': 'defi_manager.py',
        'Payment Manager': 'payment_manager.py',
        'Revenue Streams': 'revenue_streams.py'
    },
    'Empire & Business': {
        'Empire Builder': 'empire_builder.py',
        'Empire Expander': 'empire_expander.py',
        'Mega Expander': 'mega_expander.py',
        'Universal Domination': 'universal_domination.py',
        'Resource Manager': 'resource_manager.py',
        'Business Intelligence': 'business_intelligence.py',
        'Market Intelligence': 'market_intelligence.py',
        'Process Automator': 'process_automator.py',
        'Competitive Intelligence': 'competitive_intelligence.py',
        'Unified Wealth System': 'unified_wealth_system.py'
    },
    'Growth & Scaling': {
        'Smart Scaling': 'smart_scaling_system.py',
        'Hyper Scaler': 'hyper_scaler.py',
        'Cost Optimizer': 'cost_optimizer.py',
        'Budget Optimizer': 'budget_optimizer.py',
        'Infrastructure Manager': 'infrastructure_manager.py',
        'Cloud Manager': 'cloud_manager.py',
        'VPS Setup': 'vps_setup.py'
    },
    'Marketing & Content': {
        'Marketing Automation': 'marketing_automation.py',
        'YouTube Finder': 'youtube_opportunity_finder.py',
        'SaaS Factory': 'saas_factory.py',
        'Content Factory': 'content_factory.py',
        'Campaign Manager': 'campaign_manager.py',
        'Social Media Manager': 'social_media_manager.py',
        'Lead Generation': 'lead_gen.py',
        'Affiliate Manager': 'affiliate_manager.py'
    },
    'Ecommerce & Retail': {
        'Ecommerce Manager': 'ecommerce_manager.py',
        'Market Analyzer': 'market_analyzer.py',
        'Offer Manager': 'offer_manager.py',
        'Bookmark Analyzer': 'bookmark_analyzer.py'
    },
    'Metaverse & NFT': {
        'Metaverse Manager': 'metaverse_manager.py',
        'NFT Manager': 'nft_manager.py'
    },
    'System & Security': {
        'System Monitor': 'system_monitor.py',
        'Task Manager': 'task_manager.py',
        'Resource Utilizer': 'resource_utilizer.py',
        'Agent Orchestrator': 'agent_orchestrator.py',
        'Security Manager': 'security_manager.py'
    }
}

class ModuleController:
    def __init__(self):
        self.modules = {}
        self.load_modules()
        
    def load_modules(self):
        base_path = "c:/Users/p8tty/Downloads/agency-swarm-0.2.0/autonomous_growth"
        for category, modules in MODULES.items():
            self.modules[category] = {}
            for name, filename in modules.items():
                module_path = os.path.join(base_path, filename)
                if os.path.exists(module_path):
                    module = import_module(module_path)
                    if module:
                        self.modules[category][name] = module
                        
    def get_module(self, category, name):
        return self.modules.get(category, {}).get(name)
        
    def execute_module(self, category, name, *args, **kwargs):
        module = self.get_module(category, name)
        if module and hasattr(module, 'main'):
            try:
                return module.main(*args, **kwargs)
            except Exception as e:
                return f"Error executing {name}: {e}"
        return f"Module {name} not found or has no main function"

class Agent:
    def __init__(self, name, agent_type, specialization, power_level=1):
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = agent_type
        self.specialization = specialization
        self.power_level = power_level
        self.experience = 0
        self.missions_completed = 0
        self.status = "Ready"
        self.current_task = None
        self.achievements = []
        self.skills = self._init_skills()
        
    def _init_skills(self):
        base_skills = {
            'business': {
                'market_analysis': 70,
                'trading': 65,
                'negotiation': 60,
                'strategy': 75
            },
            'content': {
                'creation': 70,
                'distribution': 65,
                'analytics': 60,
                'engagement': 75
            },
            'tech': {
                'development': 70,
                'optimization': 65,
                'security': 60,
                'innovation': 75
            },
            'divine': {
                'influence': 70,
                'manifestation': 65,
                'protection': 60,
                'ascension': 75
            }
        }
        return base_skills.get(self.type.lower(), {})
        
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100 * self.power_level:
            self.power_level += 1
            self.experience = 0
            for skill in self.skills:
                self.skills[skill] = min(99, self.skills[skill] + 5)
            return True
        return False
        
    def complete_mission(self, difficulty):
        self.missions_completed += 1
        exp_gain = difficulty * random.randint(10, 20)
        leveled_up = self.gain_experience(exp_gain)
        return leveled_up

def init_session_state():
    """Initialize session state variables"""
    if 'market_data' not in st.session_state:
        st.session_state.market_data = None
    if 'empire_status' not in st.session_state:
        st.session_state.empire_status = None
    if 'system_metrics' not in st.session_state:
        st.session_state.system_metrics = None
    if 'agent_counts' not in st.session_state:
        st.session_state.agent_counts = {
            'business': 1000,
            'content': 500,
            'tech': 300,
            'divine': 200
        }
    if 'performance' not in st.session_state:
        st.session_state.performance = {
            'efficiency': 85,
            'success_rate': 90,
            'resource_usage': 75
        }
    if 'autonomous_mode' not in st.session_state:
        st.session_state.autonomous_mode = True
    if 'last_update' not in st.session_state:
        st.session_state.last_update = datetime.now()
    if 'agent_responses' not in st.session_state:
        st.session_state.agent_responses = []
    if 'selected_agents' not in st.session_state:
        st.session_state.selected_agents = []
    if 'agents' not in st.session_state:
        st.session_state.agents = {
            'business': [
                Agent("Business Agent 1", "Business", "Trading", 1),
                Agent("Business Agent 2", "Business", "Market Analysis", 1),
                Agent("Business Agent 3", "Business", "Strategy", 1),
                Agent("Business Agent 4", "Business", "Negotiation", 1),
                Agent("Business Agent 5", "Business", "Investment", 1)
            ],
            'content': [
                Agent("Content Agent 1", "Content", "Video Production", 1),
                Agent("Content Agent 2", "Content", "Blog Writing", 1),
                Agent("Content Agent 3", "Content", "Social Media", 1),
                Agent("Content Agent 4", "Content", "SEO", 1),
                Agent("Content Agent 5", "Content", "Community", 1)
            ],
            'tech': [
                Agent("Tech Agent 1", "Tech", "AI Development", 1),
                Agent("Tech Agent 2", "Tech", "Blockchain", 1),
                Agent("Tech Agent 3", "Tech", "Security", 1),
                Agent("Tech Agent 4", "Tech", "Infrastructure", 1),
                Agent("Tech Agent 5", "Tech", "Mobile", 1)
            ],
            'divine': [
                Agent("Divine Agent 1", "Divine", "Protection", 1),
                Agent("Divine Agent 2", "Divine", "Manifestation", 1),
                Agent("Divine Agent 3", "Divine", "Influence", 1),
                Agent("Divine Agent 4", "Divine", "Ascension", 1),
                Agent("Divine Agent 5", "Divine", "Balance", 1)
            ]
        }
    if 'missions' not in st.session_state:
        st.session_state.missions = []
    if 'achievements' not in st.session_state:
        st.session_state.achievements = []
    if 'agent_teams' not in st.session_state:
        st.session_state.agent_teams = {}
    if 'module_controller' not in st.session_state:
        st.session_state.module_controller = ModuleController()

def simulate_agent_response(command, agents):
    """Simulate agent responses to commands with enhanced intelligence"""
    responses = []
    command_lower = command.lower()
    
    # Special commands that trigger achievements
    achievement_commands = {
        "masterful analysis": "Awarded 'Master Analyst' achievement",
        "perfect execution": "Awarded 'Perfect Executor' achievement",
        "divine intervention": "Awarded 'Divine Mastery' achievement",
        "market domination": "Awarded 'Market Dominator' achievement"
    }
    
    # Check for achievement commands
    for ach_command, achievement in achievement_commands.items():
        if ach_command in command_lower:
            st.session_state.achievements.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {achievement}")
    
    # Mission difficulty based on command complexity
    difficulty = 1 + len(command.split()) / 5
    
    for agent in agents:
        # Simulate mission completion and experience gain
        leveled_up = agent.complete_mission(difficulty)
        
        # Generate response based on agent type and specialization
        base_response = f"{agent.name} (Level {agent.power_level}, {agent.specialization}): "
        
        if "analyze" in command_lower:
            if agent.type == "Business":
                response = f"Market analysis complete. Found {agent.power_level + 2} high-profit opportunities in {agent.specialization}."
            elif agent.type == "Content":
                response = f"Content gap analysis finished. Identified {agent.power_level + 3} trending topics in {agent.specialization}."
            elif agent.type == "Tech":
                response = f"Technical analysis done. System optimization potential: {agent.power_level * 5}%"
            elif agent.type == "Divine":
                response = f"Divine analysis completed. Detected {agent.power_level + 4} major market inefficiencies."
                
        elif "optimize" in command_lower:
            if agent.type == "Business":
                response = f"Optimizing {agent.specialization}. ROI improved by {agent.power_level * 3}%"
            elif agent.type == "Content":
                response = f"{agent.specialization} optimized. Reach increased by {agent.power_level * 5}%"
            elif agent.type == "Tech":
                response = f"System optimization complete. Performance up by {agent.power_level * 4}%"
            elif agent.type == "Divine":
                response = f"Divine optimization finished. Influence expanded by {agent.power_level * 6}%"
                
        elif "deploy" in command_lower:
            if agent.type == "Business":
                response = f"Deploying new {agent.specialization} systems. Coverage: +{agent.power_level * 2} markets"
            elif agent.type == "Content":
                response = f"Launching {agent.specialization} campaign. Target: {agent.power_level}M views"
            elif agent.type == "Tech":
                response = f"Deploying {agent.specialization} updates. New features: {agent.power_level * 2}"
            elif agent.type == "Divine":
                response = f"Initiating {agent.specialization} intervention. Impact: {['Local', 'Regional', 'Global', 'Universal'][min(3, agent.power_level-1)]}"
                
        else:
            response = f"Processing command: {command}. Using {agent.specialization} expertise."
        
        # Add level up notification if applicable
        if leveled_up:
            response += f" [LEVEL UP! Now level {agent.power_level}]"
            
        responses.append(base_response + response)
        
    return responses

def update_autonomous_systems():
    """Simulate autonomous system updates"""
    if st.session_state.autonomous_mode:
        current_time = datetime.now()
        time_diff = (current_time - st.session_state.last_update).total_seconds()
        
        if time_diff >= 5:  # Update every 5 seconds
            # Simulate autonomous growth
            for key in st.session_state.agent_counts:
                growth = int(st.session_state.agent_counts[key] * 0.01)  # 1% growth
                st.session_state.agent_counts[key] += growth
            
            # Simulate performance improvements
            for key in st.session_state.performance:
                if st.session_state.performance[key] < 99:
                    st.session_state.performance[key] = min(99, st.session_state.performance[key] + 0.1)
            
            st.session_state.last_update = current_time

def get_empire_status():
    """Get status of all empire components"""
    update_autonomous_systems()
    
    return {
        'Crypto Empire': {
            'status': '🟢 Active',
            'revenue': f"${2.5 + sum(st.session_state.agent_counts.values()) / 1000:.1f}M",
            'growth': '+15%',
            'components': {
                'MEV Bots': f"Running ({st.session_state.agent_counts['business']} active)",
                'Flash Loans': 'Active',
                'Arbitrage': 'Hunting',
                'Token Factory': 'Producing'
            }
        },
        'Content Empire': {
            'status': '🟢 Scaling',
            'revenue': f"${1.8 + sum(st.session_state.agent_counts.values()) / 2000:.1f}M",
            'growth': '+25%',
            'components': {
                'YouTube': f"{st.session_state.agent_counts['content']} channels",
                'Blogs': '1000 sites',
                'Social': '5000 accounts',
                'NFTs': 'Minting'
            }
        },
        'Tech Empire': {
            'status': '🟢 Expanding',
            'revenue': f"${3.2 + sum(st.session_state.agent_counts.values()) / 1500:.1f}M",
            'growth': '+18%',
            'components': {
                'SaaS': f"{st.session_state.agent_counts['tech']} products",
                'AI Services': 'Operating',
                'Web3': 'Building',
                'Mobile Apps': 'Deploying'
            }
        },
        'Divine Empire': {
            'status': '🟢 Omnipresent',
            'revenue': f"${5.5 + sum(st.session_state.agent_counts.values()) / 800:.1f}M",
            'growth': '+30%',
            'components': {
                'Guardian': 'Protecting',
                'Angels': f"{st.session_state.agent_counts['divine']} serving",
                'Snipers': 'Hunting',
                'Orchestrator': 'Conducting'
            }
        }
    }

def get_system_metrics():
    """Get overall system performance metrics"""
    total_agents = sum(st.session_state.agent_counts.values())
    total_revenue = sum([2.5, 1.8, 3.2, 5.5]) + total_agents / 500
    
    return {
        'Total Revenue': {
            'value': f'${total_revenue:.1f}M',
            'change': '+22%',
            'trend': 'exponential'
        },
        'Active Agents': {
            'value': str(total_agents),
            'change': f"+{int(total_agents * 0.01)}",
            'trend': 'growing'
        },
        'Market Dominance': {
            'value': f"{min(99, 85 + total_agents / 10000):.1f}%",
            'change': '+5%',
            'trend': 'increasing'
        },
        'System Health': {
            'value': f"{sum(st.session_state.performance.values()) / len(st.session_state.performance):.1f}%",
            'change': '+2%',
            'trend': 'stable'
        }
    }

def create_revenue_chart():
    """Create revenue chart for all empires"""
    empires = ['Crypto', 'Content', 'Tech', 'Divine']
    revenues = [2.5, 1.8, 3.2, 5.5]
    growth = [15, 25, 18, 30]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Revenue ($M)',
        x=empires,
        y=revenues,
        text=[f'${x}M' for x in revenues],
        textposition='auto',
    ))
    fig.add_trace(go.Scatter(
        name='Growth (%)',
        x=empires,
        y=growth,
        text=[f'+{x}%' for x in growth],
        mode='lines+markers+text',
        textposition='top center',
        yaxis='y2'
    ))
    
    fig.update_layout(
        title='Empire Performance',
        yaxis=dict(title='Revenue ($M)'),
        yaxis2=dict(title='Growth (%)', overlaying='y', side='right'),
        barmode='group'
    )
    return fig

def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title="Empire Control Center",
        page_icon="🏛️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    init_session_state()

    # Title and description
    st.title("🏛️ Empire Control Center")
    st.markdown("""
    Welcome to your empire's control center. Monitor and manage all autonomous operations from this dashboard.
    """)

    # Sidebar
    st.sidebar.title("Control Panel")
    
    # Autonomous Mode Toggle
    autonomous_mode = st.sidebar.toggle("Autonomous Mode", value=st.session_state.autonomous_mode)
    if autonomous_mode != st.session_state.autonomous_mode:
        st.session_state.autonomous_mode = autonomous_mode
    
    # Team Management
    st.sidebar.subheader("Team Management")
    team_name = st.sidebar.text_input("Team Name")
    if team_name and st.sidebar.button("Create Team"):
        if team_name not in st.session_state.agent_teams:
            st.session_state.agent_teams[team_name] = []
            st.sidebar.success(f"Team '{team_name}' created!")
    
    if st.session_state.agent_teams:
        selected_team = st.sidebar.selectbox("Select Team", list(st.session_state.agent_teams.keys()))
        if selected_team:
            team_agents = st.session_state.agent_teams[selected_team]
            st.sidebar.write(f"Team Members ({len(team_agents)}):")
            for agent in team_agents:
                st.sidebar.write(f"- {agent.name} ({agent.specialization})")

    # System Metrics
    st.subheader("System Overview")
    metrics = get_system_metrics()
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Revenue", 
                 metrics['Total Revenue']['value'],
                 metrics['Total Revenue']['change'],
                 help="Combined revenue across all empires")
    
    with col2:
        st.metric("Active Agents",
                 metrics['Active Agents']['value'],
                 metrics['Active Agents']['change'],
                 help="Total number of autonomous agents operating")
    
    with col3:
        st.metric("Market Dominance",
                 metrics['Market Dominance']['value'],
                 metrics['Market Dominance']['change'],
                 help="Overall market presence and influence")
    
    with col4:
        st.metric("System Health",
                 metrics['System Health']['value'],
                 metrics['System Health']['change'],
                 help="Overall system performance and stability")

    # Empire Status
    st.subheader("Empire Status")
    empire_status = get_empire_status()
    
    for empire_name, empire_data in empire_status.items():
        with st.expander(f"{empire_name} ({empire_data['status']})"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Revenue", empire_data['revenue'], empire_data['growth'])
            
            with col2:
                components = empire_data['components']
                st.write("Components:")
                for component, status in components.items():
                    st.write(f"- {component}: {status}")
            
            with col3:
                if empire_name == "Crypto Empire":
                    st.button("Optimize MEV", key=f"optimize_{empire_name}")
                elif empire_name == "Content Empire":
                    st.button("Scale Content", key=f"scale_{empire_name}")
                elif empire_name == "Tech Empire":
                    st.button("Deploy Updates", key=f"deploy_{empire_name}")
                elif empire_name == "Divine Empire":
                    st.button("Divine Intervention", key=f"divine_{empire_name}")

    # Agent Communication
    st.subheader("Agent Communication")
    
    # Agent Selection
    col1, col2 = st.columns(2)
    with col1:
        agent_type = st.selectbox("Select Agent Type", ['Business', 'Content', 'Tech', 'Divine'])
        agents = st.session_state.agents[agent_type.lower()]
        selected_agents = st.multiselect("Select Agents", agents, 
                                       format_func=lambda x: f"{x.name} (Level {x.power_level}, {x.specialization})")
    
    with col2:
        if st.session_state.agent_teams:
            st.write("Teams:")
            for team_name, team_agents in st.session_state.agent_teams.items():
                if st.button(f"Select {team_name}"):
                    selected_agents = team_agents

    # Command Interface
    command = st.text_input("Enter Command")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Send Command") and selected_agents:
            responses = simulate_agent_response(command, selected_agents)
            st.session_state.agent_responses.extend(responses)
    
    with col2:
        if selected_agents:
            if st.button("Add to Team"):
                team_name = st.text_input("Enter team name")
                if team_name:
                    if team_name not in st.session_state.agent_teams:
                        st.session_state.agent_teams[team_name] = []
                    st.session_state.agent_teams[team_name].extend(selected_agents)
                    st.success(f"Added agents to team '{team_name}'")
    
    # Agent Responses and Achievements
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Agent Responses")
        for response in st.session_state.agent_responses:
            st.write(response)
        if st.session_state.agent_responses and st.button("Clear Responses"):
            st.session_state.agent_responses = []
    
    with col2:
        st.subheader("Achievements")
        for achievement in st.session_state.achievements:
            st.success(achievement)

    # Agent Stats
    if selected_agents:
        st.subheader("Agent Statistics")
        for agent in selected_agents:
            with st.expander(f"{agent.name} Stats"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"Type: {agent.type}")
                    st.write(f"Specialization: {agent.specialization}")
                    st.write(f"Level: {agent.power_level}")
                    st.write(f"Experience: {agent.experience}/{100 * agent.power_level}")
                    st.write(f"Missions Completed: {agent.missions_completed}")
                with col2:
                    st.write("Skills:")
                    for skill, value in agent.skills.items():
                        st.write(f"- {skill.replace('_', ' ').title()}: {value}%")

    # Performance Metrics
    st.subheader("Performance Metrics")
    performance_data = pd.DataFrame({
        'Metric': ['Efficiency', 'Success Rate', 'Resource Usage'],
        'Value': [
            st.session_state.performance['efficiency'],
            st.session_state.performance['success_rate'],
            st.session_state.performance['resource_usage']
        ]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=performance_data['Metric'],
        y=performance_data['Value'],
        marker_color=['#1f77b4', '#2ca02c', '#ff7f0e']
    ))
    fig.update_layout(
        title='System Performance',
        yaxis_title='Percentage',
        showlegend=False,
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

    # Module Controller
    st.subheader("Module Controller")
    module_controller = st.session_state.module_controller
    categories = list(module_controller.modules.keys())
    selected_category = st.selectbox("Select Category", categories)
    if selected_category:
        modules = list(module_controller.modules[selected_category].keys())
        selected_module = st.selectbox("Select Module", modules)
        if selected_module:
            if st.button("Execute Module"):
                result = module_controller.execute_module(selected_category, selected_module)
                st.write(result)

if __name__ == "__main__":
    main()
