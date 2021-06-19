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
    ArchiveBrowsingEnabled: Optional[bool]
    BlackedOut: Optional[bool]
    CalculateYumMetadata: Optional[bool]
    ChecksumPolicyType: Optional[str]
    DebianTrivialLayout: Optional[bool]
    Description: Optional[str]
    DockerApiVersion: Optional[str]
    EnableFileListsIndexing: Optional[bool]
    ExcludesPattern: Optional[str]
    ForceNugetAuthentication: Optional[bool]
    HandleReleases: Optional[bool]
    HandleSnapshots: Optional[bool]
    Id: Optional[str]
    IncludesPattern: Optional[str]
    Key: Optional[str]
    MaxUniqueSnapshots: Optional[float]
    MaxUniqueTags: Optional[float]
    Notes: Optional[str]
    PackageType: Optional[str]
    PropertySets: Optional[Sequence[str]]
    RepoLayoutRef: Optional[str]
    SnapshotVersionBehavior: Optional[str]
    SuppressPomConsistencyChecks: Optional[bool]
    XrayIndex: Optional[bool]
    YumRootDepth: Optional[float]

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
            ArchiveBrowsingEnabled=json_data.get("ArchiveBrowsingEnabled"),
            BlackedOut=json_data.get("BlackedOut"),
            CalculateYumMetadata=json_data.get("CalculateYumMetadata"),
            ChecksumPolicyType=json_data.get("ChecksumPolicyType"),
            DebianTrivialLayout=json_data.get("DebianTrivialLayout"),
            Description=json_data.get("Description"),
            DockerApiVersion=json_data.get("DockerApiVersion"),
            EnableFileListsIndexing=json_data.get("EnableFileListsIndexing"),
            ExcludesPattern=json_data.get("ExcludesPattern"),
            ForceNugetAuthentication=json_data.get("ForceNugetAuthentication"),
            HandleReleases=json_data.get("HandleReleases"),
            HandleSnapshots=json_data.get("HandleSnapshots"),
            Id=json_data.get("Id"),
            IncludesPattern=json_data.get("IncludesPattern"),
            Key=json_data.get("Key"),
            MaxUniqueSnapshots=json_data.get("MaxUniqueSnapshots"),
            MaxUniqueTags=json_data.get("MaxUniqueTags"),
            Notes=json_data.get("Notes"),
            PackageType=json_data.get("PackageType"),
            PropertySets=json_data.get("PropertySets"),
            RepoLayoutRef=json_data.get("RepoLayoutRef"),
            SnapshotVersionBehavior=json_data.get("SnapshotVersionBehavior"),
            SuppressPomConsistencyChecks=json_data.get("SuppressPomConsistencyChecks"),
            XrayIndex=json_data.get("XrayIndex"),
            YumRootDepth=json_data.get("YumRootDepth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


