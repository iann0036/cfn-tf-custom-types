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
    Domain: Optional[str]
    HttpsExt: Optional[str]
    Id: Optional[str]
    InstanceIds: Optional[Sequence[str]]
    RealServers: Optional[Sequence[str]]
    RsType: Optional[float]
    ProxyTypes: Optional[Sequence["_ProxyTypesDefinition"]]

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
            Domain=json_data.get("Domain"),
            HttpsExt=json_data.get("HttpsExt"),
            Id=json_data.get("Id"),
            InstanceIds=json_data.get("InstanceIds"),
            RealServers=json_data.get("RealServers"),
            RsType=json_data.get("RsType"),
            ProxyTypes=deserialize_list(json_data.get("ProxyTypes"), ProxyTypesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ProxyTypesDefinition(BaseModel):
    ProxyPorts: Optional[Sequence[float]]
    ProxyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            ProxyPorts=json_data.get("ProxyPorts"),
            ProxyType=json_data.get("ProxyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyTypesDefinition = ProxyTypesDefinition


