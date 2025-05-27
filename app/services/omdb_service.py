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
    async def search_movie(cls, title: str):
        """Busca filme por título"""
        params = {
            's': title,
            'apikey': cls._api_key
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(cls._base_url, params=params)
        return response.json()

    @classmethod
    async def get_movie_details(cls, imdb_id: str):
        """Busca detalhes do filme por IMDb ID"""
        params = {
            'i': imdb_id,
            'apikey': cls._api_key
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(cls._base_url, params=params)
        return response.json()
