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
    BootidOnDestroy: Optional[float]
    Comment: Optional[str]
    DoneDate: Optional[str]
    Function: Optional[str]
    Id: Optional[str]
    LastUpdate: Optional[str]
    PartitionSchemeName: Optional[str]
    ServiceName: Optional[str]
    StartDate: Optional[str]
    Status: Optional[str]
    TemplateName: Optional[str]
    Details: Optional[Sequence["_DetailsDefinition"]]
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
            BootidOnDestroy=json_data.get("BootidOnDestroy"),
            Comment=json_data.get("Comment"),
            DoneDate=json_data.get("DoneDate"),
            Function=json_data.get("Function"),
            Id=json_data.get("Id"),
            LastUpdate=json_data.get("LastUpdate"),
            PartitionSchemeName=json_data.get("PartitionSchemeName"),
            ServiceName=json_data.get("ServiceName"),
            StartDate=json_data.get("StartDate"),
            Status=json_data.get("Status"),
            TemplateName=json_data.get("TemplateName"),
            Details=deserialize_list(json_data.get("Details"), DetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DetailsDefinition(BaseModel):
    ChangeLog: Optional[str]
    CustomHostname: Optional[str]
    DiskGroupId: Optional[float]
    InstallRtm: Optional[bool]
    InstallSqlServer: Optional[bool]
    Language: Optional[str]
    NoRaid: Optional[bool]
    PostInstallationScriptLink: Optional[str]
    PostInstallationScriptReturn: Optional[str]
    ResetHwRaid: Optional[bool]
    SoftRaidDevices: Optional[float]
    SshKeyName: Optional[str]
    UseDistribKernel: Optional[bool]
    UseSpla: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            ChangeLog=json_data.get("ChangeLog"),
            CustomHostname=json_data.get("CustomHostname"),
            DiskGroupId=json_data.get("DiskGroupId"),
            InstallRtm=json_data.get("InstallRtm"),
            InstallSqlServer=json_data.get("InstallSqlServer"),
            Language=json_data.get("Language"),
            NoRaid=json_data.get("NoRaid"),
            PostInstallationScriptLink=json_data.get("PostInstallationScriptLink"),
            PostInstallationScriptReturn=json_data.get("PostInstallationScriptReturn"),
            ResetHwRaid=json_data.get("ResetHwRaid"),
            SoftRaidDevices=json_data.get("SoftRaidDevices"),
            SshKeyName=json_data.get("SshKeyName"),
            UseDistribKernel=json_data.get("UseDistribKernel"),
            UseSpla=json_data.get("UseSpla"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetailsDefinition = DetailsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


