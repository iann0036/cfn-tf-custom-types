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
    CheckIntervalSec: Optional[float]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    HealthyThreshold: Optional[float]
    Host: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    Project: Optional[str]
    RequestPath: Optional[str]
    SelfLink: Optional[str]
    TimeoutSec: Optional[float]
    UnhealthyThreshold: Optional[float]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CheckIntervalSec=json_data.get("CheckIntervalSec"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Host=json_data.get("Host"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Project=json_data.get("Project"),
            RequestPath=json_data.get("RequestPath"),
            SelfLink=json_data.get("SelfLink"),
            TimeoutSec=json_data.get("TimeoutSec"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


