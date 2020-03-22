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
    DefaultVsys: Optional[str]
    Description: Optional[str]
    Devices: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Templates: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultVsys=json_data.get("DefaultVsys"),
            Description=json_data.get("Description"),
            Devices=json_data.get("Devices"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Templates=json_data.get("Templates"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


