# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Accprofile: Optional[str]
    Comments: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Trusthost1: Optional[str]
    Trusthost10: Optional[str]
    Trusthost2: Optional[str]
    Trusthost3: Optional[str]
    Trusthost4: Optional[str]
    Trusthost5: Optional[str]
    Trusthost6: Optional[str]
    Trusthost7: Optional[str]
    Trusthost8: Optional[str]
    Trusthost9: Optional[str]
    Vdom: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Accprofile=json_data.get("Accprofile"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Trusthost1=json_data.get("Trusthost1"),
            Trusthost10=json_data.get("Trusthost10"),
            Trusthost2=json_data.get("Trusthost2"),
            Trusthost3=json_data.get("Trusthost3"),
            Trusthost4=json_data.get("Trusthost4"),
            Trusthost5=json_data.get("Trusthost5"),
            Trusthost6=json_data.get("Trusthost6"),
            Trusthost7=json_data.get("Trusthost7"),
            Trusthost8=json_data.get("Trusthost8"),
            Trusthost9=json_data.get("Trusthost9"),
            Vdom=json_data.get("Vdom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


