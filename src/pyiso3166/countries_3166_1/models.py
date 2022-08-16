from typing import (
    List,
    Optional,
)

from core.models import (
    BaseDataClass,
    Database,
)


class Country(BaseDataClass):
    name: str
    alpha_2: str
    alpha_3: str
    flag: str
    numeric: str
    official_name: Optional[str]
    common_name: Optional[str]

    @staticmethod
    def get_searchable_fields() -> List[str]:
        return ["name", "official_name", "common_name"]


class Countries(Database):
    database: List[Country]
    dataclass = Country

    def get(self, **kwargs) -> Optional[Country]:
        return super(Countries, self).get(**kwargs)
