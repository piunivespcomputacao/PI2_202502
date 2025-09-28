from django.shortcuts import render
from .models import Compressor
#from django.http import HttpResponse

# Valores de referência para o diagnóstico (pode ser calculado a partir dos dados)
VALORES_REFERENCIA = {
    'rpm_min': 480,
    'rpm_normal_min': 1650,
    'rpm_normal_max': 2000,
    'rpm_max': 2520,
    
    'motor_power_min': 1402.42,
    'motor_power_normal_min': 5906.66,
    'motor_power_normal_max': 13547.9,
    'motor_power_max': 19454.56,
    
    'outlet_pressure_bar_min': 1.0,
    'outlet_pressure_bar_normal_min': 4.44,
    'outlet_pressure_bar_normal_max': 7.88,
    'outlet_pressure_bar_max': 8.66,
    
    'air_flow_min': 95.10,
    'air_flow_normal_min': 669.49,
    'air_flow_normal_max': 1444.81,
    'air_flow_max': 1539.91,
    
    'noise_db_min': 39.88,
    'noise_db_normal_min': 47.44,
    'noise_db_normal_max': 57.98,
    'noise_db_max': 74.40,
    
    'outlet_temp_min': 76.90,
    'outlet_temp_normal_min': 94.62,
    'outlet_temp_normal_max': 141.93,
    'outlet_temp_max': 172.71,
    
    'gaccx_min': 0.54,
    'gaccx_normal_min': 0.58,
    'gaccx_normal_max': 0.60,
    'gaccx_max': 0.73,
    
    'gaccy_min': 0.27,
    'gaccy_normal_min': 0.35,
    'gaccy_normal_max': 0.35,
    'gaccy_max': 0.46,
    
    'gaccz_min': 1.73,
    'gaccz_normal_min': 3.61,
    'gaccz_normal_max': 3.92,
    'gaccz_max': 9.21,
    
    'haccx_min': 1.04,
    'haccx_normal_min': 1.08,
    'haccx_normal_max': 1.10,
    'haccx_max': 1.23,
    
    'haccy_min': 1.27,
    'haccy_normal_min': 1.35,
    'haccy_normal_max': 1.35,
    'haccy_max': 1.46,
    
    'haccz_min': 2.33,
    'haccz_normal_min': 3.34,
    'haccz_normal_max': 3.50,
    'haccz_max': 6.11
}

def home(request):
    """View para a página inicial."""
    return render(request, 'home.html') # Note que este chama um novo template: home.html


def analisar_compressor(request):
    resultado_analise = None # Apenas inicializa a variável

    # Tenta pegar o ID do compressor (supondo que o formulário POST é o principal)
    compressor_id = request.POST.get('compressor_id') # Funciona para POST e retorna None para GET

    # Verifica se o método é POST e se um ID foi fornecido
    if request.method == 'POST' and compressor_id:
        
        try:
            # 1. Busca o objeto Compressor no banco de dados
            compressor = Compressor.objects.get(id=compressor_id)
            
            problemas_encontrados = []
            
            # --- Lógica de regras (A sua "IA") ---
            
            # 1. Análise de RPM
            if compressor.rpm < VALORES_REFERENCIA['rpm_normal_min']:
                problemas_encontrados.append("RPM abaixo do normal. Pode indicar subalimentação ou problema no motor.")
            elif compressor.rpm > VALORES_REFERENCIA['rpm_normal_max']:
                problemas_encontrados.append("RPM acima do normal. Possível sobrecarga ou calibração incorreta.")

            # 2. Análise de Potência do Motor
            if compressor.motor_power < VALORES_REFERENCIA['motor_power_normal_min']:
                problemas_encontrados.append("Potência do motor abaixo do normal. Perda de eficiência.")
            elif compressor.motor_power > VALORES_REFERENCIA['motor_power_normal_max']:
                problemas_encontrados.append("Potência do motor acima do normal. Sobrecarga do motor.")
            
            # 3. Análise de Pressão de Saída
            if compressor.outlet_pressure_bar < VALORES_REFERENCIA['outlet_pressure_bar_normal_min']:
                problemas_encontrados.append("Pressão de saída baixa. Possível vazamento ou bloqueio no fluxo de ar.")

            # 4. Análise de Fluxo de Ar
            if compressor.air_flow < VALORES_REFERENCIA['air_flow_normal_min']:
                problemas_encontrados.append("Fluxo de ar abaixo do normal. Verifique o filtro de ar.")

            # 5. Análise de Ruído
            if compressor.noise_db > VALORES_REFERENCIA['noise_db_normal_max']:
                problemas_encontrados.append("Nível de ruído alto. Possível desgaste de rolamentos ou componentes internos.")

            # 6. Análise de Temperatura de Saída
            if compressor.outlet_temp > VALORES_REFERENCIA['outlet_temp_normal_max']:
                problemas_encontrados.append("Temperatura de saída elevada. Risco de superaquecimento.")

            # 7. Análise de Vibração (Motor - gaccx, gaccy, gaccz)
            if compressor.gaccx > VALORES_REFERENCIA['gaccx_normal_max'] or \
               compressor.gaccy > VALORES_REFERENCIA['gaccy_normal_max'] or \
               compressor.gaccz > VALORES_REFERENCIA['gaccz_normal_max']:
                problemas_encontrados.append("Vibração do motor (acelerômetro) acima do padrão. Verifique o balanceamento e alinhamento.")

            # 8. Análise de Vibração (Cilindro - haccx, haccy, haccz)
            if compressor.haccx > VALORES_REFERENCIA['haccx_normal_max'] or \
               compressor.haccy > VALORES_REFERENCIA['haccy_normal_max'] or \
               compressor.haccz > VALORES_REFERENCIA['haccz_normal_max']:
                problemas_encontrados.append("Vibração do cilindro (acelerômetro) acima do padrão. Possível desgaste interno.")

            #'dirty' foi convertido para 0.
            if compressor.exvalve == 0: 
                problemas_encontrados.append("Válvula de escape suja (Dirty/0). Afeta a eficiência do ciclo e precisa de manutenção.")

            #'unstable' foi convertido para 0.
            if compressor.acmotor == 0: 
                problemas_encontrados.append("Motor AC instável (Unstable/0). Pode indicar problemas elétricos e falha iminente.")


            # Define o status final baseado nos problemas encontrados
            if problemas_encontrados:
                status = 'REPROVADO'
                # Limita o diagnóstico a 200 caracteres, conforme o seu modelo
                diagnostico = " | ".join(problemas_encontrados)
            else:
                status = 'APROVADO'
                diagnostico = "Nenhum problema aparente. O compressor está em boas condições."

            # Salva o resultado no objeto do banco de dados
            compressor.status_qualidade = status
            compressor.diagnostico = diagnostico
            compressor.save()
           # Define a cor do status
            cor_status = 'green' if status == 'APROVADO' else 'red'

            # 4. Prepara o resultado para ser exibido no template
            resultado_analise = {
                    'id': compressor.id,
                    'status': status,
                    'diagnostico': diagnostico,
                    'cor': cor_status, # Adiciona a cor aqui
                    'detalhes_parametros': {
                    'RPM': compressor.rpm,
                    'Potência do Motor': compressor.motor_power,
                    'Pressão de Saída': compressor.outlet_pressure_bar,
                    'Fluxo de Ar': compressor.air_flow,
                    'Nível de Ruído (dB)': compressor.noise_db,
                    'Temperatura de Saída (°C)': compressor.outlet_temp,
                    'Vibração Motor X (gaccx)': compressor.gaccx,
                    'Vibração Motor Y (gaccy)': compressor.gaccy,
                    'Vibração Motor Z (gaccz)': compressor.gaccz,
                    'Vibração Cilindro X (haccx)': compressor.haccx,
                    'Vibração Cilindro Y (haccy)': compressor.haccy,
                    'Vibração Cilindro Z (haccz)': compressor.haccz,
                    'Válvula de Escape (0=Dirty)': compressor.exvalve,
                    'Motor AC (0=Unstable)': compressor.acmotor
                }
            }
            
        except Compressor.DoesNotExist:
            # Se o ID não for encontrado
            resultado_analise = {
                'status': 'Não encontrado',
                'diagnostico': f'O ID do compressor "{compressor_id}" não foi encontrado no banco de dados.'
            }
        
        except Exception as e:
            # Captura qualquer outro erro inesperado
            resultado_analise = {
                'status': 'Erro de Sistema',
                'diagnostico': f'Erro inesperado durante a análise: {e}' 
            }
    pass


    contexto = {'resultado': resultado_analise, 'valores_referencia': VALORES_REFERENCIA}
    #return HttpResponse('som som som teste teste...oi')
    return render(request, 'analise.html', contexto)