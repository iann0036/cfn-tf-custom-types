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
    Annotation: Optional[str]
    BounceAgeIntvl: Optional[str]
    BounceTrig: Optional[str]
    Description: Optional[str]
    HoldIntvl: Optional[str]
    Id: Optional[str]
    LocalEpAgeIntvl: Optional[str]
    MoveFreq: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    RemoteEpAgeIntvl: Optional[str]
    TenantDn: Optional[str]

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
            Annotation=json_data.get("Annotation"),
            BounceAgeIntvl=json_data.get("BounceAgeIntvl"),
            BounceTrig=json_data.get("BounceTrig"),
            Description=json_data.get("Description"),
            HoldIntvl=json_data.get("HoldIntvl"),
            Id=json_data.get("Id"),
            LocalEpAgeIntvl=json_data.get("LocalEpAgeIntvl"),
            MoveFreq=json_data.get("MoveFreq"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            RemoteEpAgeIntvl=json_data.get("RemoteEpAgeIntvl"),
            TenantDn=json_data.get("TenantDn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


