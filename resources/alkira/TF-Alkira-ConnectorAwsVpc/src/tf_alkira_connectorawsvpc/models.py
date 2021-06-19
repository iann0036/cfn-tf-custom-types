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
    AwsAccountId: Optional[str]
    AwsRegion: Optional[str]
    BillingTags: Optional[Sequence[float]]
    CredentialId: Optional[str]
    Cxp: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Segment: Optional[str]
    Size: Optional[str]
    VpcCidr: Optional[Sequence[str]]
    VpcId: Optional[str]
    VpcRouteTable: Optional[Sequence["_VpcRouteTableDefinition"]]
    VpcSubnet: Optional[Sequence["_VpcSubnetDefinition"]]

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
            AwsAccountId=json_data.get("AwsAccountId"),
            AwsRegion=json_data.get("AwsRegion"),
            BillingTags=json_data.get("BillingTags"),
            CredentialId=json_data.get("CredentialId"),
            Cxp=json_data.get("Cxp"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Segment=json_data.get("Segment"),
            Size=json_data.get("Size"),
            VpcCidr=json_data.get("VpcCidr"),
            VpcId=json_data.get("VpcId"),
            VpcRouteTable=deserialize_list(json_data.get("VpcRouteTable"), VpcRouteTableDefinition),
            VpcSubnet=deserialize_list(json_data.get("VpcSubnet"), VpcSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VpcRouteTableDefinition(BaseModel):
    Id: Optional[str]
    Options: Optional[str]
    PrefixListIds: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcRouteTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcRouteTableDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Options=json_data.get("Options"),
            PrefixListIds=json_data.get("PrefixListIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcRouteTableDefinition = VpcRouteTableDefinition


@dataclass
class VpcSubnetDefinition(BaseModel):
    Cidr: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcSubnetDefinition = VpcSubnetDefinition


