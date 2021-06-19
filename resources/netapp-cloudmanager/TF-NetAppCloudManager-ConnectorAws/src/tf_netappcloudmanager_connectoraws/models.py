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
    AccountId: Optional[str]
    Ami: Optional[str]
    AssociatePublicIpAddress: Optional[bool]
    ClientId: Optional[str]
    Company: Optional[str]
    EnableTerminationProtection: Optional[bool]
    IamInstanceProfileName: Optional[str]
    Id: Optional[str]
    InstanceType: Optional[str]
    KeyName: Optional[str]
    Name: Optional[str]
    ProxyCertificates: Optional[Sequence[str]]
    ProxyPassword: Optional[str]
    ProxyUrl: Optional[str]
    ProxyUserName: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    SubnetId: Optional[str]
    AwsTag: Optional[Sequence["_AwsTagDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            Ami=json_data.get("Ami"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            ClientId=json_data.get("ClientId"),
            Company=json_data.get("Company"),
            EnableTerminationProtection=json_data.get("EnableTerminationProtection"),
            IamInstanceProfileName=json_data.get("IamInstanceProfileName"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            KeyName=json_data.get("KeyName"),
            Name=json_data.get("Name"),
            ProxyCertificates=json_data.get("ProxyCertificates"),
            ProxyPassword=json_data.get("ProxyPassword"),
            ProxyUrl=json_data.get("ProxyUrl"),
            ProxyUserName=json_data.get("ProxyUserName"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SubnetId=json_data.get("SubnetId"),
            AwsTag=deserialize_list(json_data.get("AwsTag"), AwsTagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AwsTagDefinition(BaseModel):
    TagKey: Optional[str]
    TagValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTagDefinition"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            TagValue=json_data.get("TagValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTagDefinition = AwsTagDefinition


