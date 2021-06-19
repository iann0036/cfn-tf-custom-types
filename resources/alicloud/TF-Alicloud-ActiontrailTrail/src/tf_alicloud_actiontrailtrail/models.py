# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    EventRw: Optional[str]
    Id: Optional[str]
    IsOrganizationTrail: Optional[bool]
    MnsTopicArn: Optional[str]
    Name: Optional[str]
    OssBucketName: Optional[str]
    OssKeyPrefix: Optional[str]
    OssWriteRoleArn: Optional[str]
    RoleName: Optional[str]
    SlsProjectArn: Optional[str]
    SlsWriteRoleArn: Optional[str]
    Status: Optional[str]
    TrailName: Optional[str]
    TrailRegion: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EventRw=json_data.get("EventRw"),
            Id=json_data.get("Id"),
            IsOrganizationTrail=json_data.get("IsOrganizationTrail"),
            MnsTopicArn=json_data.get("MnsTopicArn"),
            Name=json_data.get("Name"),
            OssBucketName=json_data.get("OssBucketName"),
            OssKeyPrefix=json_data.get("OssKeyPrefix"),
            OssWriteRoleArn=json_data.get("OssWriteRoleArn"),
            RoleName=json_data.get("RoleName"),
            SlsProjectArn=json_data.get("SlsProjectArn"),
            SlsWriteRoleArn=json_data.get("SlsWriteRoleArn"),
            Status=json_data.get("Status"),
            TrailName=json_data.get("TrailName"),
            TrailRegion=json_data.get("TrailRegion"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


