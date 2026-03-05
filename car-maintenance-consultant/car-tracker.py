# 1. BASE DE DATOS Y CONFIGURACIÓN INICIAL
autos_compatibles = {
    "Ford": ["Fiesta", "Focus", "Ranger", "Ka"],
    "Volkswagen": ["Gol", "Vento", "Amarok", "Polo"],
    "Toyota": ["Corolla", "Hilux", "Etios"]
}

precios_base = {
    "aceite": 135000,
    "correa": 310000,
    "filtro_aire": 30000,
    "bujias": 55000,
    "pastillas": 75000,
    "filtro_nafta": 45000,
    "filtro_diesel": 65000  # Agregamos el costo específico de Diesel
}

inversion_total = 0
fallas_detectadas = []

print("--- Bienvenido al Car Maintenance Tracker & Buyer Consultant ---")

while True:
    marca = input("\nIngrese la marca del auto (o 'salir' para terminar): ").strip().capitalize()
    if marca == "Salir":
        exit()

    if marca in autos_compatibles:
        modelo = input(f"Ingrese el modelo de {marca}: ").strip().capitalize()
        if modelo in autos_compatibles[marca]:
             print(f"✅ El auto {marca} {modelo} es compatible.")
             break
        else:
            print(f"❌ El modelo {modelo} no es compatible.")
    else:
        print(f"❌ La marca {marca} no es compatible.")

# 3. SECCIÓN DE SEGUIMIENTO (TRACKER)

# Cambio de aceite
print("\n--- Sección: Aceite ---")
kilometraje = int(input("Ingrese el kilometraje actual del vehiculo: ")) 
ultimo_cambio_aceite = int(input("¿A qué kilometraje marcaba el tablero en el último cambio?: "))
uso_aceite = kilometraje - ultimo_cambio_aceite

if uso_aceite >= 10000:
    costo = precios_base["aceite"]
    print(f"⚠️ Recomendable cambio de aceite. Costo: ${costo:,}")
    inversion_total += costo
    fallas_detectadas.append("Cambio de aceite y filtros")
else:    
    print(f"✅ Aceite OK. Te quedan {10000 - uso_aceite} km.")

# Correa de distribucion 
print("\n--- Sección: Distribución ---")
años_correa = int(input("¿Hace cuántos años se cambió la correa?: "))
km_correa = int(input("¿Hace cuántos km se cambió la correa?: "))

if años_correa >= 5 or km_correa >= 60000:
    costo = precios_base["correa"]
    print(f"⚠️ Recomendable cambio de correa. Costo: ${costo:,}")
    inversion_total += costo
    fallas_detectadas.append("Kit de distribución")
else:    
    print("✅ La correa está en buen estado.")

# Filtro de aire
print("\n--- Sección: Filtro de Aire ---")
km_filtro_aire = int(input("¿Hace cuántos km tiene el filtro de aire?: "))

if km_filtro_aire >= 15000:
    costo = precios_base["filtro_aire"]
    print(f"⚠️ Recomendable cambio de filtro de aire. Costo: ${costo:,}")
    inversion_total += costo
    fallas_detectadas.append("Filtro de aire")
else:    
    print("✅ El filtro de aire está bien.")

# Bujias
print("\n--- Sección: Bujías ---")
km_bujias = int(input("¿Hace cuántos km se cambiaron las bujías?: "))
if km_bujias >= 40000:
    costo = precios_base["bujias"]
    print(f"⚠️ Recomendable cambio de bujías. Costo: ${costo:,}")
    inversion_total += costo
    fallas_detectadas.append("Juego de bujías")
else:    
    print("✅ Bujías en buen estado.")

# Pastillas de freno
print("\n--- Sección: Frenos ---")
tipo_caja = input("¿El vehiculo es automático o manual? (a/m): ").strip().lower()
km_freno = int(input("¿Hace cuántos km se cambiaron las pastillas?: "))
limite_freno = 25000 if tipo_caja == "a" else 40000

if km_freno >= limite_freno:
    costo = precios_base["pastillas"]
    print(f"⚠️ Recomendable cambio de pastillas. Costo: ${costo:,}")
    inversion_total += costo
    fallas_detectadas.append(f"Pastillas de freno ({'Auto' if tipo_caja == 'a' else 'Manual'})")
else:
    print("✅ Los frenos están seguros.")

# Filtro de combustible
print("\n--- Sección: Filtro de Combustible ---")
tipo_combustible = input("¿El auto es Nafta o Diesel? (n/d): ").strip().lower()
km_filtro_comb = int(input("¿Cuántos km tiene el filtro de combustible?: "))

if tipo_combustible == "d":
    limite_comb = 15000
    costo_f_comb = precios_base["filtro_diesel"]
else:
    limite_comb = 25000
    costo_f_comb = precios_base["filtro_nafta"]

if km_filtro_comb >= limite_comb:
    print(f"⚠️ Filtro de combustible vencido. Costo: ${costo_f_comb:,}")
    inversion_total += costo_f_comb
    fallas_detectadas.append("Filtro de combustible")
else:
    print(f"✅ Filtro de combustible OK.")

# 4. DIAGNÓSTICO FINAL DE COMPRA
print("\n" + "="*45)
print("📊 INFORME FINAL DE VALUACIÓN")
print("="*45)
print(f"VEHÍCULO: {marca} {modelo}")
print(f"ESTADO GENERAL: {'⚠️ Mantenimiento Pendiente' if inversion_total > 0 else '✅ Al día'}")
print("-" * 45)

if fallas_detectadas:
    print("REPARACIONES NECESARIAS:")
    for falla in fallas_detectadas:
        print(f"  • {falla}")
    print("-" * 45)
    print(f"💰 TOTAL A INVERTIR: ${inversion_total:,}")
    print("\n💡 CONSEJO: Mostrale este presupuesto al vendedor")
    print("   para negociar el precio final del vehículo.")
else:
    print("✨ El vehículo no requiere inversión inmediata.")
    print("   ¡Parece una excelente oportunidad de compra!")
print("="*45)