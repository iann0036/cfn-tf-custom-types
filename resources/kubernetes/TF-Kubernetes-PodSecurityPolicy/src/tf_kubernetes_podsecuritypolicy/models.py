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
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]

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
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


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
class SpecDefinition(BaseModel):
    AllowPrivilegeEscalation: Optional[bool]
    AllowedCapabilities: Optional[Sequence[str]]
    AllowedProcMountTypes: Optional[Sequence[str]]
    AllowedUnsafeSysctls: Optional[Sequence[str]]
    DefaultAddCapabilities: Optional[Sequence[str]]
    DefaultAllowPrivilegeEscalation: Optional[bool]
    ForbiddenSysctls: Optional[Sequence[str]]
    HostIpc: Optional[bool]
    HostNetwork: Optional[bool]
    HostPid: Optional[bool]
    Privileged: Optional[bool]
    ReadOnlyRootFilesystem: Optional[bool]
    RequiredDropCapabilities: Optional[Sequence[str]]
    Volumes: Optional[Sequence[str]]
    AllowedFlexVolumes: Optional[Sequence["_AllowedFlexVolumesDefinition"]]
    AllowedHostPaths: Optional[Sequence["_AllowedHostPathsDefinition"]]
    FsGroup: Optional[Sequence["_FsGroupDefinition"]]
    HostPorts: Optional[Sequence["_HostPortsDefinition"]]
    RunAsGroup: Optional[Sequence["_RunAsGroupDefinition"]]
    RunAsUser: Optional[Sequence["_RunAsUserDefinition"]]
    SeLinux: Optional[Sequence["_SeLinuxDefinition"]]
    SupplementalGroups: Optional[Sequence["_SupplementalGroupsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowPrivilegeEscalation=json_data.get("AllowPrivilegeEscalation"),
            AllowedCapabilities=json_data.get("AllowedCapabilities"),
            AllowedProcMountTypes=json_data.get("AllowedProcMountTypes"),
            AllowedUnsafeSysctls=json_data.get("AllowedUnsafeSysctls"),
            DefaultAddCapabilities=json_data.get("DefaultAddCapabilities"),
            DefaultAllowPrivilegeEscalation=json_data.get("DefaultAllowPrivilegeEscalation"),
            ForbiddenSysctls=json_data.get("ForbiddenSysctls"),
            HostIpc=json_data.get("HostIpc"),
            HostNetwork=json_data.get("HostNetwork"),
            HostPid=json_data.get("HostPid"),
            Privileged=json_data.get("Privileged"),
            ReadOnlyRootFilesystem=json_data.get("ReadOnlyRootFilesystem"),
            RequiredDropCapabilities=json_data.get("RequiredDropCapabilities"),
            Volumes=json_data.get("Volumes"),
            AllowedFlexVolumes=deserialize_list(json_data.get("AllowedFlexVolumes"), AllowedFlexVolumesDefinition),
            AllowedHostPaths=deserialize_list(json_data.get("AllowedHostPaths"), AllowedHostPathsDefinition),
            FsGroup=deserialize_list(json_data.get("FsGroup"), FsGroupDefinition),
            HostPorts=deserialize_list(json_data.get("HostPorts"), HostPortsDefinition),
            RunAsGroup=deserialize_list(json_data.get("RunAsGroup"), RunAsGroupDefinition),
            RunAsUser=deserialize_list(json_data.get("RunAsUser"), RunAsUserDefinition),
            SeLinux=deserialize_list(json_data.get("SeLinux"), SeLinuxDefinition),
            SupplementalGroups=deserialize_list(json_data.get("SupplementalGroups"), SupplementalGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class AllowedFlexVolumesDefinition(BaseModel):
    Driver: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedFlexVolumesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedFlexVolumesDefinition"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedFlexVolumesDefinition = AllowedFlexVolumesDefinition


@dataclass
class AllowedHostPathsDefinition(BaseModel):
    PathPrefix: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedHostPathsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedHostPathsDefinition"]:
        if not json_data:
            return None
        return cls(
            PathPrefix=json_data.get("PathPrefix"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedHostPathsDefinition = AllowedHostPathsDefinition


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
class HostPortsDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HostPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostPortsDefinition = HostPortsDefinition


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
class SeLinuxDefinition(BaseModel):
    Rule: Optional[str]
    SeLinuxOptions: Optional[Sequence["_SeLinuxOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeLinuxDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeLinuxDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            SeLinuxOptions=deserialize_list(json_data.get("SeLinuxOptions"), SeLinuxOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeLinuxDefinition = SeLinuxDefinition


@dataclass
class SeLinuxOptionsDefinition(BaseModel):
    Level: Optional[str]
    Role: Optional[str]
    Type: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeLinuxOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeLinuxOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            Role=json_data.get("Role"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeLinuxOptionsDefinition = SeLinuxOptionsDefinition


@dataclass
class SupplementalGroupsDefinition(BaseModel):
    Rule: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SupplementalGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupplementalGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupplementalGroupsDefinition = SupplementalGroupsDefinition


