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
    DefaultNetworkAclId: Optional[str]
    Id: Optional[str]
    OwnerId: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcId: Optional[str]
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
            Arn=json_data.get("Arn"),
            DefaultNetworkAclId=json_data.get("DefaultNetworkAclId"),
            Id=json_data.get("Id"),
            OwnerId=json_data.get("OwnerId"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcId=json_data.get("VpcId"),
            Egress=deserialize_list(json_data.get("Egress"), EgressDefinition),
            Ingress=deserialize_list(json_data.get("Ingress"), IngressDefinition),
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
class EgressDefinition(BaseModel):
    Action: Optional[str]
    CidrBlock: Optional[str]
    FromPort: Optional[float]
    IcmpCode: Optional[float]
    IcmpType: Optional[float]
    Ipv6CidrBlock: Optional[str]
    Protocol: Optional[str]
    RuleNo: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EgressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CidrBlock=json_data.get("CidrBlock"),
            FromPort=json_data.get("FromPort"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            Protocol=json_data.get("Protocol"),
            RuleNo=json_data.get("RuleNo"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressDefinition = EgressDefinition


@dataclass
class IngressDefinition(BaseModel):
    Action: Optional[str]
    CidrBlock: Optional[str]
    FromPort: Optional[float]
    IcmpCode: Optional[float]
    IcmpType: Optional[float]
    Ipv6CidrBlock: Optional[str]
    Protocol: Optional[str]
    RuleNo: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IngressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CidrBlock=json_data.get("CidrBlock"),
            FromPort=json_data.get("FromPort"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            Protocol=json_data.get("Protocol"),
            RuleNo=json_data.get("RuleNo"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressDefinition = IngressDefinition


