
import pandas as pd

def remover_duplicados(df):
    duplicados = df.duplicated().sum()
    print(f"🔁 Duplicados encontrados: {duplicados}")
    if duplicados > 0:
        df = df.drop_duplicates()
        print("✅ Duplicados removidos.")
    return df

def verificar_nulos(df):
    print("\n🔍 Verificando valores nulos:")
    nulos = df.isnull().sum()
    nulos = nulos[nulos > 0]
    if not nulos.empty:
        print(nulos)
    else:
        print("✅ Nenhum valor nulo encontrado.")
    return nulos

def verificar_valores_unicos(df, colunas, exibir_valores=True):
    print("\n🔎 Verificando valores únicos por coluna:")
    resultados = {}
    
    for col in colunas:
        print(f"\nColuna: '{col}'")
        print(f"Total de categorias distintas: {df[col].nunique()}")
        
        if exibir_valores:
            print(df[col].value_counts(dropna=False))
        
        resultados[col] = df[col].unique()
        
        if df[col].dtype == 'object':
            sugestao = df[col].str.strip().str.lower().nunique()
            if sugestao < df[col].nunique():
                print("⚠️  Possíveis inconsistências (espaços ou capitalização). Considere padronizar.")
    
    return resultados

def verificar_outliers(df, coluna='Valor', lim_inf=10, lim_sup=300):
    print(f"\n📈 Verificando outliers na coluna '{coluna}'...")
    outliers = df[(df[coluna] < lim_inf) | (df[coluna] > lim_sup)]
    print(f"Encontrados {len(outliers)} outliers fora da faixa ({lim_inf} a {lim_sup}).")
    return outliers
