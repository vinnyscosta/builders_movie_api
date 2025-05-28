import httpx


class OMDBService:
    """Classe para interação assíncrona com a API do OMDB"""
    _base_url = "https://www.omdbapi.com/"
    _api_key = None

    @classmethod
    def configure(cls, api_key: str):
        """Método para configuração da classe"""
        cls._api_key = api_key

    @classmethod
    async def search(
        cls,
        prod_type: str,
        title: str,
        year: int = None,
        page: int = 1
    ):
        """Busca produção por título"""
        params = {
            's': title,
            'apikey': cls._api_key
        }

        # Adiciona outros filtros se necessário
        if prod_type and prod_type != "all_types":
            params["type"] = prod_type
        if year:
            params["y"] = year
        if page != 1:
            params["page"] = page

        # Requisição para a API OMDb
        async with httpx.AsyncClient() as client:
            response = await client.get(cls._base_url, params=params)

        return response.json()

    @classmethod
    async def get_details(cls, imdb_id: str):
        """Busca detalhes da produção por IMDb ID"""
        params = {
            'i': imdb_id,
            'apikey': cls._api_key
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(cls._base_url, params=params)
        return response.json()
