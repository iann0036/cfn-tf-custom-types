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
    CustomTags: Optional[Sequence["_CustomTagsDefinition"]]
    EnableElasticDisk: Optional[bool]
    Id: Optional[str]
    IdleInstanceAutoterminationMinutes: Optional[float]
    InstancePoolId: Optional[str]
    InstancePoolName: Optional[str]
    MaxCapacity: Optional[float]
    MinIdleInstances: Optional[float]
    NodeTypeId: Optional[str]
    PreloadedSparkVersions: Optional[Sequence[str]]
    AwsAttributes: Optional[Sequence["_AwsAttributesDefinition"]]
    AzureAttributes: Optional[Sequence["_AzureAttributesDefinition"]]
    DiskSpec: Optional[Sequence["_DiskSpecDefinition"]]
    PreloadedDockerImage: Optional[Sequence["_PreloadedDockerImageDefinition"]]

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
            CustomTags=deserialize_list(json_data.get("CustomTags"), CustomTagsDefinition),
            EnableElasticDisk=json_data.get("EnableElasticDisk"),
            Id=json_data.get("Id"),
            IdleInstanceAutoterminationMinutes=json_data.get("IdleInstanceAutoterminationMinutes"),
            InstancePoolId=json_data.get("InstancePoolId"),
            InstancePoolName=json_data.get("InstancePoolName"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MinIdleInstances=json_data.get("MinIdleInstances"),
            NodeTypeId=json_data.get("NodeTypeId"),
            PreloadedSparkVersions=json_data.get("PreloadedSparkVersions"),
            AwsAttributes=deserialize_list(json_data.get("AwsAttributes"), AwsAttributesDefinition),
            AzureAttributes=deserialize_list(json_data.get("AzureAttributes"), AzureAttributesDefinition),
            DiskSpec=deserialize_list(json_data.get("DiskSpec"), DiskSpecDefinition),
            PreloadedDockerImage=deserialize_list(json_data.get("PreloadedDockerImage"), PreloadedDockerImageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomTagsDefinition = CustomTagsDefinition


@dataclass
class AwsAttributesDefinition(BaseModel):
    Availability: Optional[str]
    SpotBidPricePercent: Optional[float]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Availability=json_data.get("Availability"),
            SpotBidPricePercent=json_data.get("SpotBidPricePercent"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAttributesDefinition = AwsAttributesDefinition


@dataclass
class AzureAttributesDefinition(BaseModel):
    Availability: Optional[str]
    SpotBidMaxPrice: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AzureAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Availability=json_data.get("Availability"),
            SpotBidMaxPrice=json_data.get("SpotBidMaxPrice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureAttributesDefinition = AzureAttributesDefinition


@dataclass
class DiskSpecDefinition(BaseModel):
    DiskCount: Optional[float]
    DiskSize: Optional[float]
    DiskType: Optional[Sequence["_DiskTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiskSpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskSpecDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskCount=json_data.get("DiskCount"),
            DiskSize=json_data.get("DiskSize"),
            DiskType=deserialize_list(json_data.get("DiskType"), DiskTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskSpecDefinition = DiskSpecDefinition


@dataclass
class DiskTypeDefinition(BaseModel):
    AzureDiskVolumeType: Optional[str]
    EbsVolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            AzureDiskVolumeType=json_data.get("AzureDiskVolumeType"),
            EbsVolumeType=json_data.get("EbsVolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskTypeDefinition = DiskTypeDefinition


@dataclass
class PreloadedDockerImageDefinition(BaseModel):
    Url: Optional[str]
    BasicAuth: Optional[Sequence["_BasicAuthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreloadedDockerImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreloadedDockerImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
            BasicAuth=deserialize_list(json_data.get("BasicAuth"), BasicAuthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreloadedDockerImageDefinition = PreloadedDockerImageDefinition


@dataclass
class BasicAuthDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAuthDefinition = BasicAuthDefinition


