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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Yaml: Optional[str]
    PspSpec: Optional[Sequence["_PspSpecDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Yaml=json_data.get("Yaml"),
            PspSpec=deserialize_list(json_data.get("PspSpec"), PspSpecDefinition),
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
class PspSpecDefinition(BaseModel):
    AllowPrivilegeEscalation: Optional[bool]
    AllowedCsiDrivers: Optional[Sequence[str]]
    AllowedFlexVolumes: Optional[Sequence[str]]
    AllowedProcMounts: Optional[Sequence[str]]
    AllowedUnsafeSysctls: Optional[Sequence[str]]
    DefaultAllowPrivilegeEscalation: Optional[bool]
    ForbiddenSysctls: Optional[Sequence[str]]
    HostIpc: Optional[bool]
    HostNetwork: Optional[bool]
    HostPid: Optional[bool]
    HostPortRanges: Optional[str]
    NoAllowedCapabilities: Optional[bool]
    NoDefaultCapabilities: Optional[bool]
    NoDropCapabilities: Optional[bool]
    NoFsGroups: Optional[bool]
    NoRunAsGroup: Optional[bool]
    NoRunAsUser: Optional[bool]
    NoRuntimeClass: Optional[bool]
    NoSeLinuxOptions: Optional[bool]
    NoSupplementalGroups: Optional[bool]
    Privileged: Optional[bool]
    ReadOnlyRootFilesystem: Optional[bool]
    Volumes: Optional[Sequence[str]]
    AllowedCapabilities: Optional[Sequence["_AllowedCapabilitiesDefinition"]]
    AllowedHostPaths: Optional[Sequence["_AllowedHostPathsDefinition"]]
    DefaultCapabilities: Optional[Sequence["_DefaultCapabilitiesDefinition"]]
    DropCapabilities: Optional[Sequence["_DropCapabilitiesDefinition"]]
    FsGroupStrategyOptions: Optional[Sequence["_FsGroupStrategyOptionsDefinition"]]
    RunAsGroup: Optional[Sequence["_RunAsGroupDefinition"]]
    RunAsUser: Optional[Sequence["_RunAsUserDefinition"]]
    RuntimeClass: Optional[Sequence["_RuntimeClassDefinition"]]
    SeLinuxOptions: Optional[Sequence["_SeLinuxOptionsDefinition"]]
    SupplementalGroups: Optional[Sequence["_SupplementalGroupsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PspSpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PspSpecDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowPrivilegeEscalation=json_data.get("AllowPrivilegeEscalation"),
            AllowedCsiDrivers=json_data.get("AllowedCsiDrivers"),
            AllowedFlexVolumes=json_data.get("AllowedFlexVolumes"),
            AllowedProcMounts=json_data.get("AllowedProcMounts"),
            AllowedUnsafeSysctls=json_data.get("AllowedUnsafeSysctls"),
            DefaultAllowPrivilegeEscalation=json_data.get("DefaultAllowPrivilegeEscalation"),
            ForbiddenSysctls=json_data.get("ForbiddenSysctls"),
            HostIpc=json_data.get("HostIpc"),
            HostNetwork=json_data.get("HostNetwork"),
            HostPid=json_data.get("HostPid"),
            HostPortRanges=json_data.get("HostPortRanges"),
            NoAllowedCapabilities=json_data.get("NoAllowedCapabilities"),
            NoDefaultCapabilities=json_data.get("NoDefaultCapabilities"),
            NoDropCapabilities=json_data.get("NoDropCapabilities"),
            NoFsGroups=json_data.get("NoFsGroups"),
            NoRunAsGroup=json_data.get("NoRunAsGroup"),
            NoRunAsUser=json_data.get("NoRunAsUser"),
            NoRuntimeClass=json_data.get("NoRuntimeClass"),
            NoSeLinuxOptions=json_data.get("NoSeLinuxOptions"),
            NoSupplementalGroups=json_data.get("NoSupplementalGroups"),
            Privileged=json_data.get("Privileged"),
            ReadOnlyRootFilesystem=json_data.get("ReadOnlyRootFilesystem"),
            Volumes=json_data.get("Volumes"),
            AllowedCapabilities=deserialize_list(json_data.get("AllowedCapabilities"), AllowedCapabilitiesDefinition),
            AllowedHostPaths=deserialize_list(json_data.get("AllowedHostPaths"), AllowedHostPathsDefinition),
            DefaultCapabilities=deserialize_list(json_data.get("DefaultCapabilities"), DefaultCapabilitiesDefinition),
            DropCapabilities=deserialize_list(json_data.get("DropCapabilities"), DropCapabilitiesDefinition),
            FsGroupStrategyOptions=deserialize_list(json_data.get("FsGroupStrategyOptions"), FsGroupStrategyOptionsDefinition),
            RunAsGroup=deserialize_list(json_data.get("RunAsGroup"), RunAsGroupDefinition),
            RunAsUser=deserialize_list(json_data.get("RunAsUser"), RunAsUserDefinition),
            RuntimeClass=deserialize_list(json_data.get("RuntimeClass"), RuntimeClassDefinition),
            SeLinuxOptions=deserialize_list(json_data.get("SeLinuxOptions"), SeLinuxOptionsDefinition),
            SupplementalGroups=deserialize_list(json_data.get("SupplementalGroups"), SupplementalGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PspSpecDefinition = PspSpecDefinition


@dataclass
class AllowedCapabilitiesDefinition(BaseModel):
    Capabilities: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedCapabilitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedCapabilitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Capabilities=json_data.get("Capabilities"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedCapabilitiesDefinition = AllowedCapabilitiesDefinition


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
class DefaultCapabilitiesDefinition(BaseModel):
    Capabilities: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultCapabilitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultCapabilitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Capabilities=json_data.get("Capabilities"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultCapabilitiesDefinition = DefaultCapabilitiesDefinition


@dataclass
class DropCapabilitiesDefinition(BaseModel):
    Capabilities: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DropCapabilitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DropCapabilitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Capabilities=json_data.get("Capabilities"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DropCapabilitiesDefinition = DropCapabilitiesDefinition


@dataclass
class FsGroupStrategyOptionsDefinition(BaseModel):
    Rule: Optional[str]
    IdRanges: Optional[Sequence["_IdRangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FsGroupStrategyOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FsGroupStrategyOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            IdRanges=deserialize_list(json_data.get("IdRanges"), IdRangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FsGroupStrategyOptionsDefinition = FsGroupStrategyOptionsDefinition


@dataclass
class IdRangesDefinition(BaseModel):
    MaxId: Optional[float]
    MinId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IdRangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdRangesDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxId=json_data.get("MaxId"),
            MinId=json_data.get("MinId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdRangesDefinition = IdRangesDefinition


@dataclass
class RunAsGroupDefinition(BaseModel):
    Rule: Optional[str]
    IdRanges: Optional[Sequence["_IdRangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunAsGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunAsGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            IdRanges=deserialize_list(json_data.get("IdRanges"), IdRangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunAsGroupDefinition = RunAsGroupDefinition


@dataclass
class RunAsUserDefinition(BaseModel):
    Rule: Optional[str]
    IdRanges: Optional[Sequence["_IdRangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunAsUserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunAsUserDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            IdRanges=deserialize_list(json_data.get("IdRanges"), IdRangesDefinition),
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
class SeLinuxOptionsDefinition(BaseModel):
    Level: Optional[str]
    Role: Optional[str]
    Rule: Optional[str]
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
            Rule=json_data.get("Rule"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeLinuxOptionsDefinition = SeLinuxOptionsDefinition


@dataclass
class SupplementalGroupsDefinition(BaseModel):
    Rule: Optional[str]
    IdRanges: Optional[Sequence["_IdRangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SupplementalGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupplementalGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
            IdRanges=deserialize_list(json_data.get("IdRanges"), IdRangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupplementalGroupsDefinition = SupplementalGroupsDefinition


