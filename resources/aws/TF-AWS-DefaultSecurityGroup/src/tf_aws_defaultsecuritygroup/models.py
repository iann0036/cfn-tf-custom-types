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
    Description: Optional[str]
    Egress: Optional[Sequence["_EgressDefinition"]]
    Id: Optional[str]
    Ingress: Optional[Sequence["_IngressDefinition"]]
    Name: Optional[str]
    OwnerId: Optional[str]
    RevokeRulesOnDelete: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcId: Optional[str]

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
            Description=json_data.get("Description"),
            Egress=deserialize_list(json_data.get("Egress"), EgressDefinition),
            Id=json_data.get("Id"),
            Ingress=deserialize_list(json_data.get("Ingress"), IngressDefinition),
            Name=json_data.get("Name"),
            OwnerId=json_data.get("OwnerId"),
            RevokeRulesOnDelete=json_data.get("RevokeRulesOnDelete"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EgressDefinition(BaseModel):
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
        cls: Type["_EgressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressDefinition"]:
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
_EgressDefinition = EgressDefinition


@dataclass
class IngressDefinition(BaseModel):
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
        cls: Type["_IngressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressDefinition"]:
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
_IngressDefinition = IngressDefinition


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

