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
    AffinityHostGroupName: Optional[str]
    AntiAffinityHostGroupName: Optional[str]
    ComputeClusterId: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Mandatory: Optional[bool]
    Name: Optional[str]
    VmGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AffinityHostGroupName=json_data.get("AffinityHostGroupName"),
            AntiAffinityHostGroupName=json_data.get("AntiAffinityHostGroupName"),
            ComputeClusterId=json_data.get("ComputeClusterId"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Mandatory=json_data.get("Mandatory"),
            Name=json_data.get("Name"),
            VmGroupName=json_data.get("VmGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


