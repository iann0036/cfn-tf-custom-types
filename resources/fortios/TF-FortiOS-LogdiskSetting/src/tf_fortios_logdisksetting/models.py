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
    Diskfull: Optional[str]
    DlpArchiveQuota: Optional[float]
    FullFinalWarningThreshold: Optional[float]
    FullFirstWarningThreshold: Optional[float]
    FullSecondWarningThreshold: Optional[float]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    IpsArchive: Optional[str]
    LogQuota: Optional[float]
    MaxLogFileSize: Optional[float]
    MaxPolicyPacketCaptureSize: Optional[float]
    MaximumLogAge: Optional[float]
    ReportQuota: Optional[float]
    RollDay: Optional[str]
    RollSchedule: Optional[str]
    RollTime: Optional[str]
    SourceIp: Optional[str]
    Status: Optional[str]
    Upload: Optional[str]
    UploadDeleteFiles: Optional[str]
    UploadDestination: Optional[str]
    UploadSslConn: Optional[str]
    Uploaddir: Optional[str]
    Uploadip: Optional[str]
    Uploadpass: Optional[str]
    Uploadport: Optional[float]
    Uploadsched: Optional[str]
    Uploadtime: Optional[str]
    Uploadtype: Optional[str]
    Uploaduser: Optional[str]
    Vdomparam: Optional[str]

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
            Diskfull=json_data.get("Diskfull"),
            DlpArchiveQuota=json_data.get("DlpArchiveQuota"),
            FullFinalWarningThreshold=json_data.get("FullFinalWarningThreshold"),
            FullFirstWarningThreshold=json_data.get("FullFirstWarningThreshold"),
            FullSecondWarningThreshold=json_data.get("FullSecondWarningThreshold"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            IpsArchive=json_data.get("IpsArchive"),
            LogQuota=json_data.get("LogQuota"),
            MaxLogFileSize=json_data.get("MaxLogFileSize"),
            MaxPolicyPacketCaptureSize=json_data.get("MaxPolicyPacketCaptureSize"),
            MaximumLogAge=json_data.get("MaximumLogAge"),
            ReportQuota=json_data.get("ReportQuota"),
            RollDay=json_data.get("RollDay"),
            RollSchedule=json_data.get("RollSchedule"),
            RollTime=json_data.get("RollTime"),
            SourceIp=json_data.get("SourceIp"),
            Status=json_data.get("Status"),
            Upload=json_data.get("Upload"),
            UploadDeleteFiles=json_data.get("UploadDeleteFiles"),
            UploadDestination=json_data.get("UploadDestination"),
            UploadSslConn=json_data.get("UploadSslConn"),
            Uploaddir=json_data.get("Uploaddir"),
            Uploadip=json_data.get("Uploadip"),
            Uploadpass=json_data.get("Uploadpass"),
            Uploadport=json_data.get("Uploadport"),
            Uploadsched=json_data.get("Uploadsched"),
            Uploadtime=json_data.get("Uploadtime"),
            Uploadtype=json_data.get("Uploadtype"),
            Uploaduser=json_data.get("Uploaduser"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


