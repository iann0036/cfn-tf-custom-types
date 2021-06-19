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
    AllowPrivilegeEscalation: Optional[bool]
    AllowedCapabilities: Optional[Sequence[str]]
    AllowedProcMountTypes: Optional[Sequence[str]]
    AllowedUnsafeSysctls: Optional[Sequence[str]]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    DefaultAddCapabilities: Optional[Sequence[str]]
    DefaultAllowPrivilegeEscalation: Optional[bool]
    Description: Optional[str]
    ForbiddenSysctls: Optional[Sequence[str]]
    HostIpc: Optional[bool]
    HostNetwork: Optional[bool]
    HostPid: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Privileged: Optional[bool]
    ReadOnlyRootFilesystem: Optional[bool]
    RequiredDropCapabilities: Optional[Sequence[str]]
    Volumes: Optional[Sequence[str]]
    AllowedCsiDriver: Optional[Sequence["_AllowedCsiDriverDefinition"]]
    AllowedFlexVolume: Optional[Sequence["_AllowedFlexVolumeDefinition"]]
    AllowedHostPath: Optional[Sequence["_AllowedHostPathDefinition"]]
    FsGroup: Optional[Sequence["_FsGroupDefinition"]]
    HostPort: Optional[Sequence["_HostPortDefinition"]]
    RunAsGroup: Optional[Sequence["_RunAsGroupDefinition"]]
    RunAsUser: Optional[Sequence["_RunAsUserDefinition"]]
    RuntimeClass: Optional[Sequence["_RuntimeClassDefinition"]]
    SeLinux: Optional[Sequence["_SeLinuxDefinition"]]
    SupplementalGroup: Optional[Sequence["_SupplementalGroupDefinition"]]
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
            AllowPrivilegeEscalation=json_data.get("AllowPrivilegeEscalation"),
            AllowedCapabilities=json_data.get("AllowedCapabilities"),
            AllowedProcMountTypes=json_data.get("AllowedProcMountTypes"),
            AllowedUnsafeSysctls=json_data.get("AllowedUnsafeSysctls"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            DefaultAddCapabilities=json_data.get("DefaultAddCapabilities"),
            DefaultAllowPrivilegeEscalation=json_data.get("DefaultAllowPrivilegeEscalation"),
            Description=json_data.get("Description"),
            ForbiddenSysctls=json_data.get("ForbiddenSysctls"),
            HostIpc=json_data.get("HostIpc"),
            HostNetwork=json_data.get("HostNetwork"),
            HostPid=json_data.get("HostPid"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Privileged=json_data.get("Privileged"),
            ReadOnlyRootFilesystem=json_data.get("ReadOnlyRootFilesystem"),
            RequiredDropCapabilities=json_data.get("RequiredDropCapabilities"),
            Volumes=json_data.get("Volumes"),
            AllowedCsiDriver=deserialize_list(json_data.get("AllowedCsiDriver"), AllowedCsiDriverDefinition),
            AllowedFlexVolume=deserialize_list(json_data.get("AllowedFlexVolume"), AllowedFlexVolumeDefinition),
            AllowedHostPath=deserialize_list(json_data.get("AllowedHostPath"), AllowedHostPathDefinition),
            FsGroup=deserialize_list(json_data.get("FsGroup"), FsGroupDefinition),
            HostPort=deserialize_list(json_data.get("HostPort"), HostPortDefinition),
            RunAsGroup=deserialize_list(json_data.get("RunAsGroup"), RunAsGroupDefinition),
            RunAsUser=deserialize_list(json_data.get("RunAsUser"), RunAsUserDefinition),
            RuntimeClass=deserialize_list(json_data.get("RuntimeClass"), RuntimeClassDefinition),
            SeLinux=deserialize_list(json_data.get("SeLinux"), SeLinuxDefinition),
            SupplementalGroup=deserialize_list(json_data.get("SupplementalGroup"), SupplementalGroupDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class AllowedCsiDriverDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedCsiDriverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedCsiDriverDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedCsiDriverDefinition = AllowedCsiDriverDefinition


@dataclass
class AllowedFlexVolumeDefinition(BaseModel):
    Driver: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedFlexVolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedFlexVolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedFlexVolumeDefinition = AllowedFlexVolumeDefinition


@dataclass
class AllowedHostPathDefinition(BaseModel):
    PathPrefix: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedHostPathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedHostPathDefinition"]:
        if not json_data:
            return None
        return cls(
            PathPrefix=json_data.get("PathPrefix"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedHostPathDefinition = AllowedHostPathDefinition


@dataclass
class FsGroupDefinition(BaseModel):
    Rule: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FsGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FsGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FsGroupDefinition = FsGroupDefinition


@dataclass
class RangeDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeDefinition = RangeDefinition


@dataclass
class HostPortDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HostPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostPortDefinition = HostPortDefinition


@dataclass
class RunAsGroupDefinition(BaseModel):
    Rule: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunAsGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunAsGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunAsGroupDefinition = RunAsGroupDefinition


@dataclass
class RunAsUserDefinition(BaseModel):
    Rule: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunAsUserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunAsUserDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunAsUserDefinition = RunAsUserDefinition


@dataclass
class RuntimeClassDefinition(BaseModel):
    AllowedRuntimeClassNames: Optional[Sequence[str]]
    DefaultRuntimeClassName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeClassDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeClassDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedRuntimeClassNames=json_data.get("AllowedRuntimeClassNames"),
            DefaultRuntimeClassName=json_data.get("DefaultRuntimeClassName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeClassDefinition = RuntimeClassDefinition


@dataclass
class SeLinuxDefinition(BaseModel):
    Rule: Optional[str]
    SeLinuxOption: Optional[Sequence["_SeLinuxOptionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeLinuxDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeLinuxDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            SeLinuxOption=deserialize_list(json_data.get("SeLinuxOption"), SeLinuxOptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeLinuxDefinition = SeLinuxDefinition


@dataclass
class SeLinuxOptionDefinition(BaseModel):
    Level: Optional[str]
    Role: Optional[str]
    Type: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeLinuxOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeLinuxOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            Role=json_data.get("Role"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeLinuxOptionDefinition = SeLinuxOptionDefinition


@dataclass
class SupplementalGroupDefinition(BaseModel):
    Rule: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SupplementalGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupplementalGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupplementalGroupDefinition = SupplementalGroupDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


