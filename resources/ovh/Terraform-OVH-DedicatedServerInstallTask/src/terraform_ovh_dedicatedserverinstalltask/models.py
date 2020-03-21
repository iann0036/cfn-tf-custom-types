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
    BootidOnDestroy: Optional[float]
    Comment: Optional[str]
    DoneDate: Optional[str]
    Function: Optional[str]
    LastUpdate: Optional[str]
    PartitionSchemeName: Optional[str]
    ServiceName: Optional[str]
    StartDate: Optional[str]
    Status: Optional[str]
    TemplateName: Optional[str]
    Details: Optional[Sequence["_Details"]]
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
            BootidOnDestroy=json_data.get("BootidOnDestroy"),
            Comment=json_data.get("Comment"),
            DoneDate=json_data.get("DoneDate"),
            Function=json_data.get("Function"),
            LastUpdate=json_data.get("LastUpdate"),
            PartitionSchemeName=json_data.get("PartitionSchemeName"),
            ServiceName=json_data.get("ServiceName"),
            StartDate=json_data.get("StartDate"),
            Status=json_data.get("Status"),
            TemplateName=json_data.get("TemplateName"),
            Details=json_data.get("Details"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Details:
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
        cls: Type["_Details"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Details"]:
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
_Details = Details


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


