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
    DateCreated: Optional[str]
    DateUpdated: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Distribution: Optional[Sequence["_DistributionDefinition"]]

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
            DateCreated=json_data.get("DateCreated"),
            DateUpdated=json_data.get("DateUpdated"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Distribution=deserialize_list(json_data.get("Distribution"), DistributionDefinition),
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
class DistributionDefinition(BaseModel):
    LicenseConfigurationArns: Optional[Sequence[str]]
    Region: Optional[str]
    AmiDistributionConfiguration: Optional[Sequence["_AmiDistributionConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DistributionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributionDefinition"]:
        if not json_data:
            return None
        return cls(
            LicenseConfigurationArns=json_data.get("LicenseConfigurationArns"),
            Region=json_data.get("Region"),
            AmiDistributionConfiguration=deserialize_list(json_data.get("AmiDistributionConfiguration"), AmiDistributionConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributionDefinition = DistributionDefinition


@dataclass
class AmiDistributionConfigurationDefinition(BaseModel):
    AmiTags: Optional[Sequence["_AmiTagsDefinition"]]
    Description: Optional[str]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    TargetAccountIds: Optional[Sequence[str]]
    LaunchPermission: Optional[Sequence["_LaunchPermissionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AmiDistributionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmiDistributionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AmiTags=deserialize_list(json_data.get("AmiTags"), AmiTagsDefinition),
            Description=json_data.get("Description"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            TargetAccountIds=json_data.get("TargetAccountIds"),
            LaunchPermission=deserialize_list(json_data.get("LaunchPermission"), LaunchPermissionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmiDistributionConfigurationDefinition = AmiDistributionConfigurationDefinition


@dataclass
class AmiTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmiTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmiTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmiTagsDefinition = AmiTagsDefinition


@dataclass
class LaunchPermissionDefinition(BaseModel):
    UserGroups: Optional[Sequence[str]]
    UserIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchPermissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchPermissionDefinition"]:
        if not json_data:
            return None
        return cls(
            UserGroups=json_data.get("UserGroups"),
            UserIds=json_data.get("UserIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchPermissionDefinition = LaunchPermissionDefinition


