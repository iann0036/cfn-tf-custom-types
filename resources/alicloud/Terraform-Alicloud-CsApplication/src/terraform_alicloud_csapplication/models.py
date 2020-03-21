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
    BlueGreen: Optional[bool]
    BlueGreenConfirm: Optional[bool]
    ClusterName: Optional[str]
    DefaultDomain: Optional[str]
    Description: Optional[str]
    Environment: Optional[Sequence["_Environment"]]
    LatestImage: Optional[bool]
    Name: Optional[str]
    Services: Optional[Sequence["_Services"]]
    Template: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BlueGreen=json_data.get("BlueGreen"),
            BlueGreenConfirm=json_data.get("BlueGreenConfirm"),
            ClusterName=json_data.get("ClusterName"),
            DefaultDomain=json_data.get("DefaultDomain"),
            Description=json_data.get("Description"),
            Environment=json_data.get("Environment"),
            LatestImage=json_data.get("LatestImage"),
            Name=json_data.get("Name"),
            Services=json_data.get("Services"),
            Template=json_data.get("Template"),
            Version=json_data.get("Version"),
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


@dataclass
class Services:
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Services"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Services"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Services = Services


