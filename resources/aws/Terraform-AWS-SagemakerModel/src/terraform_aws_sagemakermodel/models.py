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
    Arn: Optional[str]
    EnableNetworkIsolation: Optional[bool]
    ExecutionRoleArn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Container: Optional[Sequence["_Container"]]
    PrimaryContainer: Optional[Sequence["_PrimaryContainer"]]
    VpcConfig: Optional[Sequence["_VpcConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            EnableNetworkIsolation=json_data.get("EnableNetworkIsolation"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Container=json_data.get("Container"),
            PrimaryContainer=json_data.get("PrimaryContainer"),
            VpcConfig=json_data.get("VpcConfig"),
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
class Container:
    ContainerHostname: Optional[str]
    Environment: Optional[Sequence["_Environment"]]
    Image: Optional[str]
    ModelDataUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Container"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Container"]:
        if not json_data:
            return None
        return cls(
            ContainerHostname=json_data.get("ContainerHostname"),
            Environment=json_data.get("Environment"),
            Image=json_data.get("Image"),
            ModelDataUrl=json_data.get("ModelDataUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Container = Container


@dataclass
class Environment:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


@dataclass
class PrimaryContainer:
    ContainerHostname: Optional[str]
    Environment: Optional[Sequence["_Environment2"]]
    Image: Optional[str]
    ModelDataUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryContainer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryContainer"]:
        if not json_data:
            return None
        return cls(
            ContainerHostname=json_data.get("ContainerHostname"),
            Environment=json_data.get("Environment"),
            Image=json_data.get("Image"),
            ModelDataUrl=json_data.get("ModelDataUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimaryContainer = PrimaryContainer


@dataclass
class Environment2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment2 = Environment2


@dataclass
class VpcConfig:
    SecurityGroupIds: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


