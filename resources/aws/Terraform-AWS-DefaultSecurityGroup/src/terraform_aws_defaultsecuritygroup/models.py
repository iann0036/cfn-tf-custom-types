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
    Description: Optional[str]
    Egress: Optional[Sequence["_Egress"]]
    Ingress: Optional[Sequence["_Ingress"]]
    Name: Optional[str]
    OwnerId: Optional[str]
    RevokeRulesOnDelete: Optional[bool]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    Timeouts: Optional["_Timeouts"]

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
            Description=json_data.get("Description"),
            Egress=json_data.get("Egress"),
            Ingress=json_data.get("Ingress"),
            Name=json_data.get("Name"),
            OwnerId=json_data.get("OwnerId"),
            RevokeRulesOnDelete=json_data.get("RevokeRulesOnDelete"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Egress:
    CidrBlocks: Optional[Sequence[str]]
    Description: Optional[str]
    FromPort: Optional[float]
    Ipv6CidrBlocks: Optional[Sequence[str]]
    PrefixListIds: Optional[Sequence[str]]
    Protocol: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    Self: Optional[bool]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Egress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Egress"]:
        if not json_data:
            return None
        return cls(
            CidrBlocks=json_data.get("CidrBlocks"),
            Description=json_data.get("Description"),
            FromPort=json_data.get("FromPort"),
            Ipv6CidrBlocks=json_data.get("Ipv6CidrBlocks"),
            PrefixListIds=json_data.get("PrefixListIds"),
            Protocol=json_data.get("Protocol"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Self=json_data.get("Self"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Egress = Egress


@dataclass
class Ingress:
    CidrBlocks: Optional[Sequence[str]]
    Description: Optional[str]
    FromPort: Optional[float]
    Ipv6CidrBlocks: Optional[Sequence[str]]
    PrefixListIds: Optional[Sequence[str]]
    Protocol: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    Self: Optional[bool]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ingress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ingress"]:
        if not json_data:
            return None
        return cls(
            CidrBlocks=json_data.get("CidrBlocks"),
            Description=json_data.get("Description"),
            FromPort=json_data.get("FromPort"),
            Ipv6CidrBlocks=json_data.get("Ipv6CidrBlocks"),
            PrefixListIds=json_data.get("PrefixListIds"),
            Protocol=json_data.get("Protocol"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Self=json_data.get("Self"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ingress = Ingress


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
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


