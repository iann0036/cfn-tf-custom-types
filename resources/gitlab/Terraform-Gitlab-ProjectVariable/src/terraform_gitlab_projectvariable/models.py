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
    EnvironmentScope: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    Masked: Optional[bool]
    Project: Optional[str]
    Protected: Optional[bool]
    Value: Optional[str]
    VariableType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EnvironmentScope=json_data.get("EnvironmentScope"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            Masked=json_data.get("Masked"),
            Project=json_data.get("Project"),
            Protected=json_data.get("Protected"),
            Value=json_data.get("Value"),
            VariableType=json_data.get("VariableType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


