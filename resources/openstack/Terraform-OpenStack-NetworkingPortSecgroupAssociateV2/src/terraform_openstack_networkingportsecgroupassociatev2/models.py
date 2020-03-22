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
    AllSecurityGroupIds: Optional[Sequence[str]]
    Enforce: Optional[bool]
    Id: Optional[str]
    PortId: Optional[str]
    Region: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllSecurityGroupIds=json_data.get("AllSecurityGroupIds"),
            Enforce=json_data.get("Enforce"),
            Id=json_data.get("Id"),
            PortId=json_data.get("PortId"),
            Region=json_data.get("Region"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


