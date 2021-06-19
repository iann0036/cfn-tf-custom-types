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
    Id: Optional[str]
    VpcPeeringConnectionId: Optional[str]
    Accepter: Optional[Sequence["_AccepterDefinition"]]
    Requester: Optional[Sequence["_RequesterDefinition"]]

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
            Id=json_data.get("Id"),
            VpcPeeringConnectionId=json_data.get("VpcPeeringConnectionId"),
            Accepter=deserialize_list(json_data.get("Accepter"), AccepterDefinition),
            Requester=deserialize_list(json_data.get("Requester"), RequesterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccepterDefinition(BaseModel):
    AllowClassicLinkToRemoteVpc: Optional[bool]
    AllowRemoteVpcDnsResolution: Optional[bool]
    AllowVpcToRemoteClassicLink: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccepterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccepterDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowClassicLinkToRemoteVpc=json_data.get("AllowClassicLinkToRemoteVpc"),
            AllowRemoteVpcDnsResolution=json_data.get("AllowRemoteVpcDnsResolution"),
            AllowVpcToRemoteClassicLink=json_data.get("AllowVpcToRemoteClassicLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccepterDefinition = AccepterDefinition


@dataclass
class RequesterDefinition(BaseModel):
    AllowClassicLinkToRemoteVpc: Optional[bool]
    AllowRemoteVpcDnsResolution: Optional[bool]
    AllowVpcToRemoteClassicLink: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RequesterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequesterDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowClassicLinkToRemoteVpc=json_data.get("AllowClassicLinkToRemoteVpc"),
            AllowRemoteVpcDnsResolution=json_data.get("AllowRemoteVpcDnsResolution"),
            AllowVpcToRemoteClassicLink=json_data.get("AllowVpcToRemoteClassicLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequesterDefinition = RequesterDefinition


