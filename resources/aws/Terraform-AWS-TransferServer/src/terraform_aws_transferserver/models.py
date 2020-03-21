# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    Endpoint: Optional[str]
    EndpointType: Optional[str]
    ForceDestroy: Optional[bool]
    HostKey: Optional[str]
    HostKeyFingerprint: Optional[str]
    IdentityProviderType: Optional[str]
    InvocationRole: Optional[str]
    LoggingRole: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Url: Optional[str]
    EndpointDetails: Optional[Sequence["_EndpointDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Endpoint=json_data.get("Endpoint"),
            EndpointType=json_data.get("EndpointType"),
            ForceDestroy=json_data.get("ForceDestroy"),
            HostKey=json_data.get("HostKey"),
            HostKeyFingerprint=json_data.get("HostKeyFingerprint"),
            IdentityProviderType=json_data.get("IdentityProviderType"),
            InvocationRole=json_data.get("InvocationRole"),
            LoggingRole=json_data.get("LoggingRole"),
            Tags=json_data.get("Tags"),
            Url=json_data.get("Url"),
            EndpointDetails=json_data.get("EndpointDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class EndpointDetails:
    VpcEndpointId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDetails"]:
        if not json_data:
            return None
        return cls(
            VpcEndpointId=json_data.get("VpcEndpointId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDetails = EndpointDetails


