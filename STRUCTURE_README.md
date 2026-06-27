# Customer Intelligence Suite — Project Scaffold

yeh structure aap ke diye gaye template (US Visa MLOps pattern)
ka **exact adaptation** hai — multi-tier project ke liye.

## Kya Same Rakha Gaya (Aap Ke Template Se)
- `components/` pattern: `data_ingestion → data_validation → data_transformation → model_trainer → model_evaluation → model_pusher`
- `configuration/`, `constants/`, `entity/`, `exception/`, `logger/`, `utils/` — sab **SHARED** rakhe gaye (ek hi jagah, sab tiers use karenge)
- `pipeline/` (training_pipeline.py + prediction_pipeline.py)
- Root level: `app.py`, `demo.py`, `setup.py`, `requirements.txt`, `Dockerfile`, `.dockerignore`, `config/model.yaml`, `config/schema.yaml`

## Kya Naya Add Hua (Multi-Tier Ke Liye)
Aap ke template mein **ek hi pipeline** thi. Hamare project mein **5 tiers**
hain, isliye har tier ka apna `components/` folder hai:

```
customer_intelligence_suite/
├── tier1_clv/components/              ← Regression (CLV)
├── tier2_churn/components/             ← Classification (Churn)
├── tier3_segmentation/components/      ← Clustering (Segmentation)
├── tier4_demand_forecast/components/   ← Time Series (Demand)
├── tier5_recommendation/components/    ← Similarity-based (Recommendation)
│
├── configuration/   ← SHARED (sab tiers use karenge)
├── constants/        ← SHARED
├── entity/           ← SHARED
├── exception/        ← SHARED
├── logger/           ← SHARED
├── utils/            ← SHARED
└── pipeline/          ← SHARED (orchestrates all tiers)
```

Plus ek `app/` folder Flask routes ke liye (har tier ka apna route file —
`clv_routes.py`, `churn_routes.py`, etc.)

## Har File Mein Docstring Hai

Har `.py` file **khali nahi hai** — usme ek docstring likha hai jo batata hai:
1. File ka role/maqsad kya hai
2. Us file mein kya function/class banana hoga (rough structure, code nahi)
3. ke liye context (kyun yeh step zaroori hai)

**Important:** Yeh docstrings sirf GUIDANCE hain — aap khud actual code
likhenge. Jab atke, mujhe specific file/error dikhayen, hum discuss karenge.

## Kahan Se Shuru Karein

1. `customer_intelligence_suite/logger/__init__.py` — pehle yeh likhein (sabse simple, sab jagah use hoga)
2. `customer_intelligence_suite/exception/__init__.py` — phir yeh
3. `customer_intelligence_suite/constants/__init__.py` — already kuch starter constants diye hain, apne hisab se add karein
4. `customer_intelligence_suite/tier1_clv/components/data_ingestion.py` — Phase 0/1 yahan se shuru

## Reference Script

`PROJECT_SCAFFOLD_SCRIPT.py` wahi script hai jisne yeh structure banaya —
agar kabhi koi file accidentally delete ho jaye, isko dobara run kar dein,
sirf MISSING files banayega (jo already maujood hain unko touch nahi karega
— exactly aap ke original template ki tarah).
