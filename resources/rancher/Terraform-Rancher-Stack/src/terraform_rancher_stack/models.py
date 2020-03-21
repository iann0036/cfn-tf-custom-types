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
    CatalogId: Optional[str]
    Description: Optional[str]
    DockerCompose: Optional[str]
    Environment: Optional[Sequence["_Environment"]]
    EnvironmentId: Optional[str]
    FinishUpgrade: Optional[bool]
    Name: Optional[str]
    RancherCompose: Optional[str]
    RenderedDockerCompose: Optional[str]
    RenderedRancherCompose: Optional[str]
    Scope: Optional[str]
    StartOnCreate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CatalogId=json_data.get("CatalogId"),
            Description=json_data.get("Description"),
            DockerCompose=json_data.get("DockerCompose"),
            Environment=json_data.get("Environment"),
            EnvironmentId=json_data.get("EnvironmentId"),
            FinishUpgrade=json_data.get("FinishUpgrade"),
            Name=json_data.get("Name"),
            RancherCompose=json_data.get("RancherCompose"),
            RenderedDockerCompose=json_data.get("RenderedDockerCompose"),
            RenderedRancherCompose=json_data.get("RenderedRancherCompose"),
            Scope=json_data.get("Scope"),
            StartOnCreate=json_data.get("StartOnCreate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Environment:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


