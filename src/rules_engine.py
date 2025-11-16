# src/rules_engine.py
import yaml

class RulesEngine:
    def __init__(self, rules_path):
        with open(rules_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
        self.rules = data.get('rules', [])

    def apply_rules(self, row):
        # row is a pandas Series; return a list of applied diagnoses (dict)
        for rule in self.rules:
            conds = rule.get('conditions', [])
            if self._check_conditions(conds, row):
                return {
                    'rule': rule.get('name'),
                    'severity': rule.get('severity'),
                    'cause': rule.get('cause'),
                    'message': rule.get('message'),
                    'recommended_action': rule.get('action')
                }

        # fallback automatic decision by numeric thresholds (example)
        try:
            press = float(row.get('pressao') or 0)
            temp = float(row.get('temperatura') or 0)
        except:
            press = 0.0
            temp = 0.0

        if press > 10 or temp > 80:
            return {
                'rule': 'auto_threshold',
                'severity': 'high' if press>10 or temp>90 else 'medium',
                'cause': 'Medições indicam risco',
                'message': 'Recomenda-se inspeção imediata.',
                'recommended_action': 'Isolar peça; verificar equipamento.'
            }

        return {
            'rule': 'auto_ok',
            'severity': 'low',
            'cause': 'Sem anomalias detectadas',
            'message': 'Peça dentro dos parâmetros.',
            'recommended_action': 'Liberar produção.'
        }

    def _check_conditions(self, conditions, row):
        for cond in conditions:
            field = cond.get('field')
            op = cond.get('op')
            val = cond.get('value')
            rv = row.get(field)
            if rv is None:
                return False
            try:
                # numeric compare when possible
                if op == 'equals':
                    if str(rv) != str(val):
                        return False
                elif op == 'contains':
                    if str(val) not in str(rv):
                        return False
                elif op == 'greater_than':
                    if float(rv) <= float(val):
                        return False
                elif op == 'less_than':
                    if float(rv) >= float(val):
                        return False
                else:
                    return False
            except Exception:
                return False
        return True
