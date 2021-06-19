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
    AdditionalCodeRepositories: Optional[Sequence[str]]
    Arn: Optional[str]
    DefaultCodeRepository: Optional[str]
    DirectInternetAccess: Optional[str]
    Id: Optional[str]
    InstanceType: Optional[str]
    KmsKeyId: Optional[str]
    LifecycleConfigName: Optional[str]
    Name: Optional[str]
    NetworkInterfaceId: Optional[str]
    RoleArn: Optional[str]
    RootAccess: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Url: Optional[str]
    VolumeSize: Optional[float]

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
            AdditionalCodeRepositories=json_data.get("AdditionalCodeRepositories"),
            Arn=json_data.get("Arn"),
            DefaultCodeRepository=json_data.get("DefaultCodeRepository"),
            DirectInternetAccess=json_data.get("DirectInternetAccess"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LifecycleConfigName=json_data.get("LifecycleConfigName"),
            Name=json_data.get("Name"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            RoleArn=json_data.get("RoleArn"),
            RootAccess=json_data.get("RootAccess"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Url=json_data.get("Url"),
            VolumeSize=json_data.get("VolumeSize"),
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


