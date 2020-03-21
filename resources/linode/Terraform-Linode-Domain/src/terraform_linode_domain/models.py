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
    AxfrIps: Optional[Sequence[str]]
    Description: Optional[str]
    Domain: Optional[str]
    ExpireSec: Optional[float]
    Group: Optional[str]
    MasterIps: Optional[Sequence[str]]
    RefreshSec: Optional[float]
    RetrySec: Optional[float]
    SoaEmail: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    TtlSec: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AxfrIps=json_data.get("AxfrIps"),
            Description=json_data.get("Description"),
            Domain=json_data.get("Domain"),
            ExpireSec=json_data.get("ExpireSec"),
            Group=json_data.get("Group"),
            MasterIps=json_data.get("MasterIps"),
            RefreshSec=json_data.get("RefreshSec"),
            RetrySec=json_data.get("RetrySec"),
            SoaEmail=json_data.get("SoaEmail"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            TtlSec=json_data.get("TtlSec"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


