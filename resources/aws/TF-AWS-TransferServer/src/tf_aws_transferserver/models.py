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
    Arn: Optional[str]
    Certificate: Optional[str]
    Domain: Optional[str]
    Endpoint: Optional[str]
    EndpointType: Optional[str]
    ForceDestroy: Optional[bool]
    HostKey: Optional[str]
    HostKeyFingerprint: Optional[str]
    Id: Optional[str]
    IdentityProviderType: Optional[str]
    InvocationRole: Optional[str]
    LoggingRole: Optional[str]
    Protocols: Optional[Sequence[str]]
    SecurityPolicyName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Url: Optional[str]
    EndpointDetails: Optional[Sequence["_EndpointDetailsDefinition"]]

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
            Arn=json_data.get("Arn"),
            Certificate=json_data.get("Certificate"),
            Domain=json_data.get("Domain"),
            Endpoint=json_data.get("Endpoint"),
            EndpointType=json_data.get("EndpointType"),
            ForceDestroy=json_data.get("ForceDestroy"),
            HostKey=json_data.get("HostKey"),
            HostKeyFingerprint=json_data.get("HostKeyFingerprint"),
            Id=json_data.get("Id"),
            IdentityProviderType=json_data.get("IdentityProviderType"),
            InvocationRole=json_data.get("InvocationRole"),
            LoggingRole=json_data.get("LoggingRole"),
            Protocols=json_data.get("Protocols"),
            SecurityPolicyName=json_data.get("SecurityPolicyName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Url=json_data.get("Url"),
            EndpointDetails=deserialize_list(json_data.get("EndpointDetails"), EndpointDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class EndpointDetailsDefinition(BaseModel):
    AddressAllocationIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    VpcEndpointId: Optional[str]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressAllocationIds=json_data.get("AddressAllocationIds"),
            SubnetIds=json_data.get("SubnetIds"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDetailsDefinition = EndpointDetailsDefinition


