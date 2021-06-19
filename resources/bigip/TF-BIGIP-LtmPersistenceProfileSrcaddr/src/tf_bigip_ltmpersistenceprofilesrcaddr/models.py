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
    AppService: Optional[str]
    DefaultsFrom: Optional[str]
    HashAlgorithm: Optional[str]
    Id: Optional[str]
    MapProxies: Optional[str]
    Mask: Optional[str]
    MatchAcrossPools: Optional[str]
    MatchAcrossServices: Optional[str]
    MatchAcrossVirtuals: Optional[str]
    Mirror: Optional[str]
    Name: Optional[str]
    OverrideConnLimit: Optional[str]
    Timeout: Optional[float]

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
            AppService=json_data.get("AppService"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            HashAlgorithm=json_data.get("HashAlgorithm"),
            Id=json_data.get("Id"),
            MapProxies=json_data.get("MapProxies"),
            Mask=json_data.get("Mask"),
            MatchAcrossPools=json_data.get("MatchAcrossPools"),
            MatchAcrossServices=json_data.get("MatchAcrossServices"),
            MatchAcrossVirtuals=json_data.get("MatchAcrossVirtuals"),
            Mirror=json_data.get("Mirror"),
            Name=json_data.get("Name"),
            OverrideConnLimit=json_data.get("OverrideConnLimit"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


