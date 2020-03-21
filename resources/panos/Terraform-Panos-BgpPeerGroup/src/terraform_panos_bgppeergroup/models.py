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
    AggregatedConfedAsPath: Optional[bool]
    Enable: Optional[bool]
    ExportNextHop: Optional[str]
    ImportNextHop: Optional[str]
    Name: Optional[str]
    RemovePrivateAs: Optional[bool]
    SoftResetWithStoredInfo: Optional[bool]
    Type: Optional[str]
    VirtualRouter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AggregatedConfedAsPath=json_data.get("AggregatedConfedAsPath"),
            Enable=json_data.get("Enable"),
            ExportNextHop=json_data.get("ExportNextHop"),
            ImportNextHop=json_data.get("ImportNextHop"),
            Name=json_data.get("Name"),
            RemovePrivateAs=json_data.get("RemovePrivateAs"),
            SoftResetWithStoredInfo=json_data.get("SoftResetWithStoredInfo"),
            Type=json_data.get("Type"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


