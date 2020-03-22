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
    Disks: Optional[Sequence[str]]
    Id: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    SchemeName: Optional[str]
    Step: Optional[float]
    TemplateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Disks=json_data.get("Disks"),
            Id=json_data.get("Id"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            SchemeName=json_data.get("SchemeName"),
            Step=json_data.get("Step"),
            TemplateName=json_data.get("TemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


