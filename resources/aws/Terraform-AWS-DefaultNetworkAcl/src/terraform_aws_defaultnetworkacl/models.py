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
    DefaultNetworkAclId: Optional[str]
    Id: Optional[str]
    OwnerId: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
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
            DefaultNetworkAclId=json_data.get("DefaultNetworkAclId"),
            Id=json_data.get("Id"),
            OwnerId=json_data.get("OwnerId"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            Egress=json_data.get("Egress"),
            Ingress=json_data.get("Ingress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Egress:
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
        cls: Type["_Egress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Egress"]:
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
_Egress = Egress


@dataclass
class Ingress:
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
        cls: Type["_Ingress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ingress"]:
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
_Ingress = Ingress


