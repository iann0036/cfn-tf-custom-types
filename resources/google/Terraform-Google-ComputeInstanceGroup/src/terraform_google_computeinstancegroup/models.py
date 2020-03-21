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
    Description: Optional[str]
    Instances: Optional[Sequence[str]]
    Name: Optional[str]
    Network: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Size: Optional[float]
    Zone: Optional[str]
    NamedPort: Optional[Sequence["_NamedPort"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Instances=json_data.get("Instances"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Size=json_data.get("Size"),
            Zone=json_data.get("Zone"),
            NamedPort=json_data.get("NamedPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NamedPort:
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NamedPort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamedPort"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamedPort = NamedPort


