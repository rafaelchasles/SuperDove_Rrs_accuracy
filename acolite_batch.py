import sys, os, time
user_home = os.path.expanduser("~")
sys.path.append(user_home+"/home/chasles/acolite")
import acolite as ac

import os

# Diretório raiz onde as pastas com as imagens estão localizadas
diretorio_raiz = "/media/chasles/Seagate Basic/rasters/TOA"

# Diretório de saída
diretorio_saida = "/media/chasles/Seagate Basic/rasters/DSF_glint3"

# Loop para percorrer todas as pastas dentro do diretório raiz
for pasta in os.listdir(diretorio_raiz):
    pasta_caminho = os.path.join(diretorio_raiz, pasta)

    # Verifica se o item no diretório raiz é uma pasta
    if os.path.isdir(pasta_caminho):
        # Cria o nome da pasta de saída
        nome_pasta_saida = pasta 

        # Cria o caminho completo para a pasta de saída
        pasta_saida_caminho = os.path.join(diretorio_saida, nome_pasta_saida)

        # Cria a pasta de saída, se ainda não existir
        if not os.path.exists(pasta_saida_caminho):
            os.makedirs(pasta_saida_caminho)

        # Altera o nome do "inputfile" e "output" no dicionário de configurações
        settings = {
            "inputfile": pasta_caminho,
            "output": pasta_saida_caminho,
            "polygon": "/media/chasles/OS/mestrado/dissertacao/dados/vetores/BILL.geojson",
            "l2r_export_geotiff":True,
            "rgb_rhos":False,
            "rgb_rhot":False,
            "l2w_mask":False,
            "luts": "ACOLITE-LUT-202110-MOD1",
            "dsf_residual_glint_correction":True,
            "dsf_residual_glint_correction_method": "alternative",
            "dsf_residual_glint_wave_range": [800,900],
            "glint_mask_rhos_threshold": 0.15,
            "l1r_delete_netcdf":True,
            "l2t_delete_netcdf":True,
            "l2r_delete_netcdf":True,
            "l2r_pans_delete_netcdf":True,
            "l2w_delete_netcdf":True
        }

        # Executa o script com as configurações atualizadas
        ac.acolite.acolite_run(settings=settings)

