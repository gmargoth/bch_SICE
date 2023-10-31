# bch_SICE
Descarga automatizada de importaciones, exportaciones y balanza cambiaría del Sistema Información de Comercio Exterior de Honduras (SICE) .  https://sisee.bch.hn/SICE/Login.aspx?ReturnUrl=%2fSICE%2f

Por ejemplo:
```python
username, password = "YOUR_USERNAME", "YOUR_PASSWORD"
driver = login_SICE(username, password)

serie = "Importaciones" # Importaciones, Exportaciones, BalanzaCambiaria
year = True
month = True
country = True
downaload_SICE_query(driver, serie, year, month, country)
```

La función `login_SICE()` toma los parámetros `username` y `password` estos se definen en base al usuario y contraseña creada en el portal del [SISEE](https://sisee.bch.hn/SICE/Login.aspx?ReturnUrl=%2fSICE%2f). Entonces primero se inicia sesion. Despues la funcion `downaload_SICE_query` toma los parametros `driver` que es el inicio de sesion, `serie` que define que datos se solicita a la base estos pueden ser: Importaciones, Exportaciones o BalanzaCambiaria, `year`, `month`, `country` pueden ser True o False, y esto define si se muestran o no como en cabezado en la tabulación. 
