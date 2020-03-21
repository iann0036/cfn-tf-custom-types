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
    Arguments: Optional[str]
    ClusterId: Optional[str]
    HiveScriptPath: Optional[str]
    Input: Optional[str]
    IsProtected: Optional[bool]
    IsPublic: Optional[bool]
    JarPath: Optional[str]
    JobLog: Optional[str]
    JobName: Optional[str]
    JobState: Optional[str]
    JobType: Optional[float]
    Output: Optional[str]
    Region: Optional[str]
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
            Arguments=json_data.get("Arguments"),
            ClusterId=json_data.get("ClusterId"),
            HiveScriptPath=json_data.get("HiveScriptPath"),
            Input=json_data.get("Input"),
            IsProtected=json_data.get("IsProtected"),
            IsPublic=json_data.get("IsPublic"),
            JarPath=json_data.get("JarPath"),
            JobLog=json_data.get("JobLog"),
            JobName=json_data.get("JobName"),
            JobState=json_data.get("JobState"),
            JobType=json_data.get("JobType"),
            Output=json_data.get("Output"),
            Region=json_data.get("Region"),
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


