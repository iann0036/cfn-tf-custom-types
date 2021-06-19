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
    NetworkAclId: Optional[str]
    Egress: Optional[Sequence["_EgressDefinition"]]
    Ingress: Optional[Sequence["_IngressDefinition"]]

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
            NetworkAclId=json_data.get("NetworkAclId"),
            Egress=deserialize_list(json_data.get("Egress"), EgressDefinition),
            Ingress=deserialize_list(json_data.get("Ingress"), IngressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EgressDefinition(BaseModel):
    Description: Optional[str]
    DestinationCidrIp: Optional[str]
    EntryType: Optional[str]
    Name: Optional[str]
    Policy: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EgressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DestinationCidrIp=json_data.get("DestinationCidrIp"),
            EntryType=json_data.get("EntryType"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressDefinition = EgressDefinition


@dataclass
class IngressDefinition(BaseModel):
    Description: Optional[str]
    EntryType: Optional[str]
    Name: Optional[str]
    Policy: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]
    SourceCidrIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IngressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            EntryType=json_data.get("EntryType"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SourceCidrIp=json_data.get("SourceCidrIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressDefinition = IngressDefinition


