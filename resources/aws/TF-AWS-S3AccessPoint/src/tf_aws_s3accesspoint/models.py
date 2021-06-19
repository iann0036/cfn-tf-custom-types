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
    Arn: Optional[str]
    Bucket: Optional[str]
    DomainName: Optional[str]
    HasPublicAccessPolicy: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    NetworkOrigin: Optional[str]
    Policy: Optional[str]
    PublicAccessBlockConfiguration: Optional[Sequence["_PublicAccessBlockConfigurationDefinition"]]
    VpcConfiguration: Optional[Sequence["_VpcConfigurationDefinition"]]

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
            Arn=json_data.get("Arn"),
            Bucket=json_data.get("Bucket"),
            DomainName=json_data.get("DomainName"),
            HasPublicAccessPolicy=json_data.get("HasPublicAccessPolicy"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NetworkOrigin=json_data.get("NetworkOrigin"),
            Policy=json_data.get("Policy"),
            PublicAccessBlockConfiguration=deserialize_list(json_data.get("PublicAccessBlockConfiguration"), PublicAccessBlockConfigurationDefinition),
            VpcConfiguration=deserialize_list(json_data.get("VpcConfiguration"), VpcConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PublicAccessBlockConfigurationDefinition(BaseModel):
    BlockPublicAcls: Optional[bool]
    BlockPublicPolicy: Optional[bool]
    IgnorePublicAcls: Optional[bool]
    RestrictPublicBuckets: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessBlockConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessBlockConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockPublicAcls=json_data.get("BlockPublicAcls"),
            BlockPublicPolicy=json_data.get("BlockPublicPolicy"),
            IgnorePublicAcls=json_data.get("IgnorePublicAcls"),
            RestrictPublicBuckets=json_data.get("RestrictPublicBuckets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccessBlockConfigurationDefinition = PublicAccessBlockConfigurationDefinition


@dataclass
class VpcConfigurationDefinition(BaseModel):
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfigurationDefinition = VpcConfigurationDefinition


