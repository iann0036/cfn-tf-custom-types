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
    Authentication: Optional[str]
    Authkey: Optional[str]
    Enckey: Optional[str]
    Encryption: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    LocalGw: Optional[str]
    Localspi: Optional[str]
    Name: Optional[str]
    RemoteGw: Optional[str]
    Remotespi: Optional[str]
    Vdomparam: Optional[str]

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
            Authentication=json_data.get("Authentication"),
            Authkey=json_data.get("Authkey"),
            Enckey=json_data.get("Enckey"),
            Encryption=json_data.get("Encryption"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            LocalGw=json_data.get("LocalGw"),
            Localspi=json_data.get("Localspi"),
            Name=json_data.get("Name"),
            RemoteGw=json_data.get("RemoteGw"),
            Remotespi=json_data.get("Remotespi"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


