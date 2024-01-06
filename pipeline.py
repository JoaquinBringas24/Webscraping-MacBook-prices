def data_processor():

    import pandas as pd
    from datetime import date
    
    df_new = pd.read_csv('C:/Users/joaco/OneDrive/Escritorio/Python/MercadoLibre/mercadolibre.csv')
    
    df_new['price'] = pd.to_numeric(df_new['price'], errors='coerce')
    
    df_new['day'] = date.today().strftime('%d/%m/%Y')
    
    df = pd.read_csv('C:/Users/joaco/OneDrive/Escritorio/Python/MercadoLibre/mercadolibre_datos.csv')
    
    df = pd.concat([df, df_new], axis=0)
    
    def generate_id(s):
        return abs(hash(s)) % (10 ** 10)
    
    df['id'] = df['title'].apply(generate_id)
    
    df = df.drop_duplicates()
    
    df.to_csv('C:/Users/joaco/OneDrive/Escritorio/Python/MercadoLibre/mercadolibre_datos.csv', index=False)
    
    

data_processor()
