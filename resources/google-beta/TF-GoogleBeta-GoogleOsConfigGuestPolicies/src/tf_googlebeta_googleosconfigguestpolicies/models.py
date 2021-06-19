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
    CreateTime: Optional[str]
    Description: Optional[str]
    Etag: Optional[str]
    GuestPolicyId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    UpdateTime: Optional[str]
    Assignment: Optional[Sequence["_AssignmentDefinition"]]
    PackageRepositories: Optional[Sequence["_PackageRepositoriesDefinition"]]
    Packages: Optional[Sequence["_PackagesDefinition"]]
    Recipes: Optional[Sequence["_RecipesDefinition"]]
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
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Etag=json_data.get("Etag"),
            GuestPolicyId=json_data.get("GuestPolicyId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            UpdateTime=json_data.get("UpdateTime"),
            Assignment=deserialize_list(json_data.get("Assignment"), AssignmentDefinition),
            PackageRepositories=deserialize_list(json_data.get("PackageRepositories"), PackageRepositoriesDefinition),
            Packages=deserialize_list(json_data.get("Packages"), PackagesDefinition),
            Recipes=deserialize_list(json_data.get("Recipes"), RecipesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AssignmentDefinition(BaseModel):
    InstanceNamePrefixes: Optional[Sequence[str]]
    Instances: Optional[Sequence[str]]
    Zones: Optional[Sequence[str]]
    GroupLabels: Optional[Sequence["_GroupLabelsDefinition"]]
    OsTypes: Optional[Sequence["_OsTypesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AssignmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssignmentDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceNamePrefixes=json_data.get("InstanceNamePrefixes"),
            Instances=json_data.get("Instances"),
            Zones=json_data.get("Zones"),
            GroupLabels=deserialize_list(json_data.get("GroupLabels"), GroupLabelsDefinition),
            OsTypes=deserialize_list(json_data.get("OsTypes"), OsTypesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssignmentDefinition = AssignmentDefinition


@dataclass
class GroupLabelsDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupLabelsDefinition = GroupLabelsDefinition


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
class OsTypesDefinition(BaseModel):
    OsArchitecture: Optional[str]
    OsShortName: Optional[str]
    OsVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            OsArchitecture=json_data.get("OsArchitecture"),
            OsShortName=json_data.get("OsShortName"),
            OsVersion=json_data.get("OsVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsTypesDefinition = OsTypesDefinition


@dataclass
class PackageRepositoriesDefinition(BaseModel):
    Apt: Optional[Sequence["_AptDefinition"]]
    Goo: Optional[Sequence["_GooDefinition"]]
    Yum: Optional[Sequence["_YumDefinition"]]
    Zypper: Optional[Sequence["_ZypperDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PackageRepositoriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PackageRepositoriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Apt=deserialize_list(json_data.get("Apt"), AptDefinition),
            Goo=deserialize_list(json_data.get("Goo"), GooDefinition),
            Yum=deserialize_list(json_data.get("Yum"), YumDefinition),
            Zypper=deserialize_list(json_data.get("Zypper"), ZypperDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PackageRepositoriesDefinition = PackageRepositoriesDefinition


@dataclass
class AptDefinition(BaseModel):
    ArchiveType: Optional[str]
    Components: Optional[Sequence[str]]
    Distribution: Optional[str]
    GpgKey: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AptDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveType=json_data.get("ArchiveType"),
            Components=json_data.get("Components"),
            Distribution=json_data.get("Distribution"),
            GpgKey=json_data.get("GpgKey"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AptDefinition = AptDefinition


@dataclass
class GooDefinition(BaseModel):
    Name: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GooDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GooDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GooDefinition = GooDefinition


@dataclass
class YumDefinition(BaseModel):
    BaseUrl: Optional[str]
    DisplayName: Optional[str]
    GpgKeys: Optional[Sequence[str]]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_YumDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YumDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseUrl=json_data.get("BaseUrl"),
            DisplayName=json_data.get("DisplayName"),
            GpgKeys=json_data.get("GpgKeys"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_YumDefinition = YumDefinition


@dataclass
class ZypperDefinition(BaseModel):
    BaseUrl: Optional[str]
    DisplayName: Optional[str]
    GpgKeys: Optional[Sequence[str]]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZypperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZypperDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseUrl=json_data.get("BaseUrl"),
            DisplayName=json_data.get("DisplayName"),
            GpgKeys=json_data.get("GpgKeys"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZypperDefinition = ZypperDefinition


@dataclass
class PackagesDefinition(BaseModel):
    DesiredState: Optional[str]
    Manager: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PackagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PackagesDefinition"]:
        if not json_data:
            return None
        return cls(
            DesiredState=json_data.get("DesiredState"),
            Manager=json_data.get("Manager"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PackagesDefinition = PackagesDefinition


@dataclass
class RecipesDefinition(BaseModel):
    DesiredState: Optional[str]
    Name: Optional[str]
    Version: Optional[str]
    Artifacts: Optional[Sequence["_ArtifactsDefinition"]]
    InstallSteps: Optional[Sequence["_InstallStepsDefinition"]]
    UpdateSteps: Optional[Sequence["_UpdateStepsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecipesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecipesDefinition"]:
        if not json_data:
            return None
        return cls(
            DesiredState=json_data.get("DesiredState"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
            Artifacts=deserialize_list(json_data.get("Artifacts"), ArtifactsDefinition),
            InstallSteps=deserialize_list(json_data.get("InstallSteps"), InstallStepsDefinition),
            UpdateSteps=deserialize_list(json_data.get("UpdateSteps"), UpdateStepsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecipesDefinition = RecipesDefinition


@dataclass
class ArtifactsDefinition(BaseModel):
    AllowInsecure: Optional[bool]
    Id: Optional[str]
    Gcs: Optional[Sequence["_GcsDefinition"]]
    Remote: Optional[Sequence["_RemoteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ArtifactsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowInsecure=json_data.get("AllowInsecure"),
            Id=json_data.get("Id"),
            Gcs=deserialize_list(json_data.get("Gcs"), GcsDefinition),
            Remote=deserialize_list(json_data.get("Remote"), RemoteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArtifactsDefinition = ArtifactsDefinition


@dataclass
class GcsDefinition(BaseModel):
    Bucket: Optional[str]
    Generation: Optional[float]
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Generation=json_data.get("Generation"),
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsDefinition = GcsDefinition


@dataclass
class RemoteDefinition(BaseModel):
    CheckSum: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckSum=json_data.get("CheckSum"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteDefinition = RemoteDefinition


@dataclass
class InstallStepsDefinition(BaseModel):
    ArchiveExtraction: Optional[Sequence["_ArchiveExtractionDefinition"]]
    DpkgInstallation: Optional[Sequence["_DpkgInstallationDefinition"]]
    FileCopy: Optional[Sequence["_FileCopyDefinition"]]
    FileExec: Optional[Sequence["_FileExecDefinition"]]
    MsiInstallation: Optional[Sequence["_MsiInstallationDefinition"]]
    RpmInstallation: Optional[Sequence["_RpmInstallationDefinition"]]
    ScriptRun: Optional[Sequence["_ScriptRunDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstallStepsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstallStepsDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveExtraction=deserialize_list(json_data.get("ArchiveExtraction"), ArchiveExtractionDefinition),
            DpkgInstallation=deserialize_list(json_data.get("DpkgInstallation"), DpkgInstallationDefinition),
            FileCopy=deserialize_list(json_data.get("FileCopy"), FileCopyDefinition),
            FileExec=deserialize_list(json_data.get("FileExec"), FileExecDefinition),
            MsiInstallation=deserialize_list(json_data.get("MsiInstallation"), MsiInstallationDefinition),
            RpmInstallation=deserialize_list(json_data.get("RpmInstallation"), RpmInstallationDefinition),
            ScriptRun=deserialize_list(json_data.get("ScriptRun"), ScriptRunDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstallStepsDefinition = InstallStepsDefinition


@dataclass
class ArchiveExtractionDefinition(BaseModel):
    ArtifactId: Optional[str]
    Destination: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveExtractionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveExtractionDefinition"]:
        if not json_data:
            return None
        return cls(
            ArtifactId=json_data.get("ArtifactId"),
            Destination=json_data.get("Destination"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveExtractionDefinition = ArchiveExtractionDefinition


@dataclass
class DpkgInstallationDefinition(BaseModel):
    ArtifactId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DpkgInstallationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DpkgInstallationDefinition"]:
        if not json_data:
            return None
        return cls(
            ArtifactId=json_data.get("ArtifactId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DpkgInstallationDefinition = DpkgInstallationDefinition


@dataclass
class FileCopyDefinition(BaseModel):
    ArtifactId: Optional[str]
    Destination: Optional[str]
    Overwrite: Optional[bool]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileCopyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileCopyDefinition"]:
        if not json_data:
            return None
        return cls(
            ArtifactId=json_data.get("ArtifactId"),
            Destination=json_data.get("Destination"),
            Overwrite=json_data.get("Overwrite"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileCopyDefinition = FileCopyDefinition


@dataclass
class FileExecDefinition(BaseModel):
    AllowedExitCodes: Optional[Sequence[float]]
    Args: Optional[Sequence[str]]
    ArtifactId: Optional[str]
    LocalPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileExecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileExecDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedExitCodes=json_data.get("AllowedExitCodes"),
            Args=json_data.get("Args"),
            ArtifactId=json_data.get("ArtifactId"),
            LocalPath=json_data.get("LocalPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileExecDefinition = FileExecDefinition


@dataclass
class MsiInstallationDefinition(BaseModel):
    AllowedExitCodes: Optional[Sequence[float]]
    ArtifactId: Optional[str]
    Flags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MsiInstallationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MsiInstallationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedExitCodes=json_data.get("AllowedExitCodes"),
            ArtifactId=json_data.get("ArtifactId"),
            Flags=json_data.get("Flags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MsiInstallationDefinition = MsiInstallationDefinition


@dataclass
class RpmInstallationDefinition(BaseModel):
    ArtifactId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RpmInstallationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RpmInstallationDefinition"]:
        if not json_data:
            return None
        return cls(
            ArtifactId=json_data.get("ArtifactId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RpmInstallationDefinition = RpmInstallationDefinition


@dataclass
class ScriptRunDefinition(BaseModel):
    AllowedExitCodes: Optional[Sequence[float]]
    Interpreter: Optional[str]
    Script: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptRunDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptRunDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedExitCodes=json_data.get("AllowedExitCodes"),
            Interpreter=json_data.get("Interpreter"),
            Script=json_data.get("Script"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptRunDefinition = ScriptRunDefinition


@dataclass
class UpdateStepsDefinition(BaseModel):
    ArchiveExtraction: Optional[Sequence["_ArchiveExtractionDefinition"]]
    DpkgInstallation: Optional[Sequence["_DpkgInstallationDefinition"]]
    FileCopy: Optional[Sequence["_FileCopyDefinition"]]
    FileExec: Optional[Sequence["_FileExecDefinition"]]
    MsiInstallation: Optional[Sequence["_MsiInstallationDefinition"]]
    RpmInstallation: Optional[Sequence["_RpmInstallationDefinition"]]
    ScriptRun: Optional[Sequence["_ScriptRunDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpdateStepsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdateStepsDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveExtraction=deserialize_list(json_data.get("ArchiveExtraction"), ArchiveExtractionDefinition),
            DpkgInstallation=deserialize_list(json_data.get("DpkgInstallation"), DpkgInstallationDefinition),
            FileCopy=deserialize_list(json_data.get("FileCopy"), FileCopyDefinition),
            FileExec=deserialize_list(json_data.get("FileExec"), FileExecDefinition),
            MsiInstallation=deserialize_list(json_data.get("MsiInstallation"), MsiInstallationDefinition),
            RpmInstallation=deserialize_list(json_data.get("RpmInstallation"), RpmInstallationDefinition),
            ScriptRun=deserialize_list(json_data.get("ScriptRun"), ScriptRunDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdateStepsDefinition = UpdateStepsDefinition


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


