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
    AuthAlgorithm: Optional[str]
    Description: Optional[str]
    EncryptAlgorithm: Optional[str]
    Id: Optional[str]
    Ipcomp: Optional[str]
    KbLifetime: Optional[float]
    Lifetime: Optional[float]
    Mode: Optional[str]
    Name: Optional[str]
    PerfectForwardSecrecy: Optional[str]
    Protocol: Optional[str]
    TunnelLocalAddress: Optional[str]
    TunnelRemoteAddress: Optional[str]

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
            AuthAlgorithm=json_data.get("AuthAlgorithm"),
            Description=json_data.get("Description"),
            EncryptAlgorithm=json_data.get("EncryptAlgorithm"),
            Id=json_data.get("Id"),
            Ipcomp=json_data.get("Ipcomp"),
            KbLifetime=json_data.get("KbLifetime"),
            Lifetime=json_data.get("Lifetime"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            PerfectForwardSecrecy=json_data.get("PerfectForwardSecrecy"),
            Protocol=json_data.get("Protocol"),
            TunnelLocalAddress=json_data.get("TunnelLocalAddress"),
            TunnelRemoteAddress=json_data.get("TunnelRemoteAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


