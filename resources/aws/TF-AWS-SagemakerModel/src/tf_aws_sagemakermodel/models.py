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
    EnableNetworkIsolation: Optional[bool]
    ExecutionRoleArn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    PrimaryContainer: Optional[Sequence["_PrimaryContainerDefinition"]]
    VpcConfig: Optional[Sequence["_VpcConfigDefinition"]]

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
            EnableNetworkIsolation=json_data.get("EnableNetworkIsolation"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            PrimaryContainer=deserialize_list(json_data.get("PrimaryContainer"), PrimaryContainerDefinition),
            VpcConfig=deserialize_list(json_data.get("VpcConfig"), VpcConfigDefinition),
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
class ContainerDefinition(BaseModel):
    ContainerHostname: Optional[str]
    Environment: Optional[Sequence["_EnvironmentDefinition"]]
    Image: Optional[str]
    Mode: Optional[str]
    ModelDataUrl: Optional[str]
    ImageConfig: Optional[Sequence["_ImageConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerHostname=json_data.get("ContainerHostname"),
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentDefinition),
            Image=json_data.get("Image"),
            Mode=json_data.get("Mode"),
            ModelDataUrl=json_data.get("ModelDataUrl"),
            ImageConfig=deserialize_list(json_data.get("ImageConfig"), ImageConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class EnvironmentDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentDefinition = EnvironmentDefinition


@dataclass
class ImageConfigDefinition(BaseModel):
    RepositoryAccessMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            RepositoryAccessMode=json_data.get("RepositoryAccessMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageConfigDefinition = ImageConfigDefinition


@dataclass
class PrimaryContainerDefinition(BaseModel):
    ContainerHostname: Optional[str]
    Environment: Optional[Sequence["_EnvironmentDefinition2"]]
    Image: Optional[str]
    Mode: Optional[str]
    ModelDataUrl: Optional[str]
    ImageConfig: Optional[Sequence["_ImageConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerHostname=json_data.get("ContainerHostname"),
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentDefinition2),
            Image=json_data.get("Image"),
            Mode=json_data.get("Mode"),
            ModelDataUrl=json_data.get("ModelDataUrl"),
            ImageConfig=deserialize_list(json_data.get("ImageConfig"), ImageConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimaryContainerDefinition = PrimaryContainerDefinition


@dataclass
class EnvironmentDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentDefinition2 = EnvironmentDefinition2


@dataclass
class VpcConfigDefinition(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfigDefinition = VpcConfigDefinition


