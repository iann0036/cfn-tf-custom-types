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
    NetworkAclId: Optional[str]
    Egress: Optional[Sequence["_Egress"]]
    Ingress: Optional[Sequence["_Ingress"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            NetworkAclId=json_data.get("NetworkAclId"),
            Egress=json_data.get("Egress"),
            Ingress=json_data.get("Ingress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Egress:
    Description: Optional[str]
    DestinationCidrIp: Optional[str]
    EntryType: Optional[str]
    Name: Optional[str]
    Policy: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Egress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Egress"]:
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
_Egress = Egress


@dataclass
class Ingress:
    Description: Optional[str]
    EntryType: Optional[str]
    Name: Optional[str]
    Policy: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]
    SourceCidrIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ingress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ingress"]:
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
_Ingress = Ingress


