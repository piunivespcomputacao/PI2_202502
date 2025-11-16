# src/app.py
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from .data_loader import DataLoader
from .rules_engine import RulesEngine
from .quality import QualityReport
import pandas as pd

def create_app():
    # project root = C:\CompressoresApp
    project_root = os.path.dirname(os.path.dirname(__file__))

    # explicit paths for templates/static (absolute paths)
    template_folder = os.path.join(project_root, "templates")
    static_folder = os.path.join(project_root, "static")

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

    data_path = os.path.join(project_root, "data", "sample_inspections.csv")
    rules_path = os.path.join(project_root, "config", "regras.yaml")

    # Loader usado por rotas de leitura
    loader = DataLoader(data_path)
    df = loader.load()
    rules_engine = RulesEngine(rules_path)
    quality = QualityReport(df)

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/analyze", methods=["POST"])
    def analyze():
        id_peca = request.form.get("id_peca", "").strip()
        if not id_peca:
            return render_template("index.html", error="Por favor, informe o número de peça.")
        row = loader.find_by_id(id_peca)
        if row is None:
            return render_template("index.html", error=f"Peça '{id_peca}' não encontrada.")
        diagnosis = rules_engine.apply_rules(row)
        piece = row.to_dict()
        return render_template("result.html", piece=piece, diagnosis=diagnosis)

    @app.route("/api/analyze", methods=["POST"])
    def api_analyze():
        data = request.get_json() or {}
        id_peca = (data.get("id_peca") or "").strip()
        if not id_peca:
            return jsonify({"error": "id_peca obrigatório"}), 400
        row = loader.find_by_id(id_peca)
        if row is None:
            return jsonify({"error": "peça não encontrada"}), 404
        diagnosis = rules_engine.apply_rules(row)
        return jsonify({"piece": row.to_dict(), "diagnosis": diagnosis})

    @app.route("/report", methods=["GET"])
    def report():
        # recarrega dados ao gerar relatório para refletir cadastros recentes
        df_latest = loader.load()
        summary = QualityReport(df_latest).summary()
        return render_template("report.html", summary=summary)

    # ---------------------------------------------------
    # ROTAS DE CADASTRO DE PEÇAS
    # ---------------------------------------------------
    @app.route("/add", methods=["GET", "POST"])
    def add_piece():
        """
        Página para cadastro de novas peças.
        Gravará a nova peça no CSV (data/sample_inspections.csv).
        """
        if request.method == "POST":
            # coletar campos
            id_peca = (request.form.get("id_peca") or "").strip()
            lote_producao = (request.form.get("lote_producao") or "").strip()
            status = (request.form.get("status") or "").strip()
            pressao = (request.form.get("pressao") or "").strip()
            temperatura = (request.form.get("temperatura") or "").strip()
            observacoes = (request.form.get("observacoes") or "").strip()

            # validações básicas
            if not id_peca:
                return render_template("add_piece.html", error="O campo ID da peça é obrigatório.")

            # carregar CSV atual
            try:
                df_current = pd.read_csv(data_path, dtype=str, keep_default_na=False)
            except FileNotFoundError:
                # criar dataframe vazio com colunas esperadas
                df_current = pd.DataFrame(columns=["id_peca","lote_producao","status","pressao","temperatura","observacoes"])

            # Verificar duplicidade de ID
            if str(id_peca) in df_current["id_peca"].astype(str).values:
                return render_template("add_piece.html", error=f"A peça com id '{id_peca}' já existe.")

            # construir nova linha (manter colunas já usadas pelo sistema)
            nova_linha = {
                "id_peca": id_peca,
                "lote_producao": lote_producao,
                "status": status,
                "pressao": pressao,
                "temperatura": temperatura,
                "observacoes": observacoes
            }

            # anexar e salvar (atenção: operação simples em CSV — considerar DB para concorrência)
            df_new = pd.concat([df_current, pd.DataFrame([nova_linha])], ignore_index=True)
            df_new.to_csv(data_path, index=False)

            # atualizar loader para leituras subsequentes na sessão
            loader.df = df_new

            return render_template("add_piece.html", success="Peça cadastrada com sucesso!")

        # GET
        return render_template("add_piece.html")

    return app

