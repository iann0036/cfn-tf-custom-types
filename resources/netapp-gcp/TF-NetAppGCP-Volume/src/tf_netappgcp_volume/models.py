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
    DeleteOnCreationError: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    ProtocolTypes: Optional[Sequence[str]]
    Region: Optional[str]
    RegionalHa: Optional[bool]
    ServiceLevel: Optional[str]
    SharedVpcProjectNumber: Optional[str]
    Size: Optional[float]
    StorageClass: Optional[str]
    TypeDp: Optional[bool]
    VolumePath: Optional[str]
    Zone: Optional[str]
    ExportPolicy: Optional[Sequence["_ExportPolicyDefinition"]]
    MountPoints: Optional[Sequence["_MountPointsDefinition"]]
    SnapshotPolicy: Optional[Sequence["_SnapshotPolicyDefinition"]]

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
            DeleteOnCreationError=json_data.get("DeleteOnCreationError"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            ProtocolTypes=json_data.get("ProtocolTypes"),
            Region=json_data.get("Region"),
            RegionalHa=json_data.get("RegionalHa"),
            ServiceLevel=json_data.get("ServiceLevel"),
            SharedVpcProjectNumber=json_data.get("SharedVpcProjectNumber"),
            Size=json_data.get("Size"),
            StorageClass=json_data.get("StorageClass"),
            TypeDp=json_data.get("TypeDp"),
            VolumePath=json_data.get("VolumePath"),
            Zone=json_data.get("Zone"),
            ExportPolicy=deserialize_list(json_data.get("ExportPolicy"), ExportPolicyDefinition),
            MountPoints=deserialize_list(json_data.get("MountPoints"), MountPointsDefinition),
            SnapshotPolicy=deserialize_list(json_data.get("SnapshotPolicy"), SnapshotPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExportPolicyDefinition(BaseModel):
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExportPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportPolicyDefinition = ExportPolicyDefinition


@dataclass
class RuleDefinition(BaseModel):
    Access: Optional[str]
    AllowedClients: Optional[str]
    HasRootAccess: Optional[str]
    Kerberos5Readonly: Optional[bool]
    Kerberos5Readwrite: Optional[bool]
    Kerberos5iReadonly: Optional[bool]
    Kerberos5iReadwrite: Optional[bool]
    Kerberos5pReadonly: Optional[bool]
    Kerberos5pReadwrite: Optional[bool]
    Nfsv3: Optional[Sequence["_Nfsv3Definition"]]
    Nfsv4: Optional[Sequence["_Nfsv4Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            AllowedClients=json_data.get("AllowedClients"),
            HasRootAccess=json_data.get("HasRootAccess"),
            Kerberos5Readonly=json_data.get("Kerberos5Readonly"),
            Kerberos5Readwrite=json_data.get("Kerberos5Readwrite"),
            Kerberos5iReadonly=json_data.get("Kerberos5iReadonly"),
            Kerberos5iReadwrite=json_data.get("Kerberos5iReadwrite"),
            Kerberos5pReadonly=json_data.get("Kerberos5pReadonly"),
            Kerberos5pReadwrite=json_data.get("Kerberos5pReadwrite"),
            Nfsv3=deserialize_list(json_data.get("Nfsv3"), Nfsv3Definition),
            Nfsv4=deserialize_list(json_data.get("Nfsv4"), Nfsv4Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class Nfsv3Definition(BaseModel):
    Checked: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Nfsv3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nfsv3Definition"]:
        if not json_data:
            return None
        return cls(
            Checked=json_data.get("Checked"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nfsv3Definition = Nfsv3Definition


@dataclass
class Nfsv4Definition(BaseModel):
    Checked: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Nfsv4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nfsv4Definition"]:
        if not json_data:
            return None
        return cls(
            Checked=json_data.get("Checked"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nfsv4Definition = Nfsv4Definition


@dataclass
class MountPointsDefinition(BaseModel):
    Export: Optional[str]
    ProtocolType: Optional[str]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MountPointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountPointsDefinition"]:
        if not json_data:
            return None
        return cls(
            Export=json_data.get("Export"),
            ProtocolType=json_data.get("ProtocolType"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountPointsDefinition = MountPointsDefinition


@dataclass
class SnapshotPolicyDefinition(BaseModel):
    Enabled: Optional[bool]
    DailySchedule: Optional[Sequence["_DailyScheduleDefinition"]]
    HourlySchedule: Optional[Sequence["_HourlyScheduleDefinition"]]
    MonthlySchedule: Optional[Sequence["_MonthlyScheduleDefinition"]]
    WeeklySchedule: Optional[Sequence["_WeeklyScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            DailySchedule=deserialize_list(json_data.get("DailySchedule"), DailyScheduleDefinition),
            HourlySchedule=deserialize_list(json_data.get("HourlySchedule"), HourlyScheduleDefinition),
            MonthlySchedule=deserialize_list(json_data.get("MonthlySchedule"), MonthlyScheduleDefinition),
            WeeklySchedule=deserialize_list(json_data.get("WeeklySchedule"), WeeklyScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotPolicyDefinition = SnapshotPolicyDefinition


@dataclass
class DailyScheduleDefinition(BaseModel):
    Hour: Optional[float]
    Minute: Optional[float]
    SnapshotsToKeep: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DailyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Hour=json_data.get("Hour"),
            Minute=json_data.get("Minute"),
            SnapshotsToKeep=json_data.get("SnapshotsToKeep"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailyScheduleDefinition = DailyScheduleDefinition


@dataclass
class HourlyScheduleDefinition(BaseModel):
    Minute: Optional[float]
    SnapshotsToKeep: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HourlyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HourlyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Minute=json_data.get("Minute"),
            SnapshotsToKeep=json_data.get("SnapshotsToKeep"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HourlyScheduleDefinition = HourlyScheduleDefinition


@dataclass
class MonthlyScheduleDefinition(BaseModel):
    DaysOfMonth: Optional[str]
    Hour: Optional[float]
    Minute: Optional[float]
    SnapshotsToKeep: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MonthlyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonthlyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            DaysOfMonth=json_data.get("DaysOfMonth"),
            Hour=json_data.get("Hour"),
            Minute=json_data.get("Minute"),
            SnapshotsToKeep=json_data.get("SnapshotsToKeep"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonthlyScheduleDefinition = MonthlyScheduleDefinition


@dataclass
class WeeklyScheduleDefinition(BaseModel):
    Day: Optional[str]
    Hour: Optional[float]
    Minute: Optional[float]
    SnapshotsToKeep: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Hour=json_data.get("Hour"),
            Minute=json_data.get("Minute"),
            SnapshotsToKeep=json_data.get("SnapshotsToKeep"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklyScheduleDefinition = WeeklyScheduleDefinition


