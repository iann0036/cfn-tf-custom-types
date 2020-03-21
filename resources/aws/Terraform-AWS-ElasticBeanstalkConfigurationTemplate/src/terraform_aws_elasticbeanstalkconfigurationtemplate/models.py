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
    Application: Optional[str]
    Description: Optional[str]
    EnvironmentId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SolutionStackName: Optional[str]
    Setting: Optional[Sequence["_Setting"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Application=json_data.get("Application"),
            Description=json_data.get("Description"),
            EnvironmentId=json_data.get("EnvironmentId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SolutionStackName=json_data.get("SolutionStackName"),
            Setting=json_data.get("Setting"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Setting:
    Name: Optional[str]
    Namespace: Optional[str]
    Resource: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Setting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Setting"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Resource=json_data.get("Resource"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Setting = Setting


