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
    AllowAnyHostAuth: Optional[bool]
    BlackedOut: Optional[bool]
    BlockMismatchingMimeTypes: Optional[bool]
    BowerRegistryUrl: Optional[str]
    BypassHeadRequests: Optional[bool]
    ClientTlsCertificate: Optional[str]
    Description: Optional[str]
    DownloadContextPath: Optional[str]
    EnableCookieManagement: Optional[bool]
    EnableTokenAuthentication: Optional[bool]
    ExcludesPattern: Optional[str]
    FeedContextPath: Optional[str]
    FetchJarsEagerly: Optional[bool]
    FetchSourcesEagerly: Optional[bool]
    ForceNugetAuthentication: Optional[bool]
    HandleReleases: Optional[bool]
    HandleSnapshots: Optional[bool]
    HardFail: Optional[bool]
    Id: Optional[str]
    IncludesPattern: Optional[str]
    Key: Optional[str]
    LocalAddress: Optional[str]
    MaxUniqueSnapshots: Optional[float]
    MissedCachePeriodSeconds: Optional[float]
    Notes: Optional[str]
    Offline: Optional[bool]
    PackageType: Optional[str]
    Password: Optional[str]
    PropagateQueryParams: Optional[bool]
    PropertySets: Optional[Sequence[str]]
    Proxy: Optional[str]
    PypiRegistryUrl: Optional[str]
    RemoteRepoChecksumPolicyType: Optional[str]
    RepoLayoutRef: Optional[str]
    RetrievalCachePeriodSeconds: Optional[float]
    ShareConfiguration: Optional[bool]
    SocketTimeoutMillis: Optional[float]
    StoreArtifactsLocally: Optional[bool]
    SuppressPomConsistencyChecks: Optional[bool]
    SynchronizeProperties: Optional[bool]
    UnusedArtifactsCleanupPeriodHours: Optional[float]
    Url: Optional[str]
    Username: Optional[str]
    V3FeedUrl: Optional[str]
    VcsGitDownloadUrl: Optional[str]
    VcsGitProvider: Optional[str]
    VcsType: Optional[str]
    XrayIndex: Optional[bool]
    ContentSynchronisation: Optional[Sequence["_ContentSynchronisationDefinition"]]
    Nuget: Optional[Sequence["_NugetDefinition"]]

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
            AllowAnyHostAuth=json_data.get("AllowAnyHostAuth"),
            BlackedOut=json_data.get("BlackedOut"),
            BlockMismatchingMimeTypes=json_data.get("BlockMismatchingMimeTypes"),
            BowerRegistryUrl=json_data.get("BowerRegistryUrl"),
            BypassHeadRequests=json_data.get("BypassHeadRequests"),
            ClientTlsCertificate=json_data.get("ClientTlsCertificate"),
            Description=json_data.get("Description"),
            DownloadContextPath=json_data.get("DownloadContextPath"),
            EnableCookieManagement=json_data.get("EnableCookieManagement"),
            EnableTokenAuthentication=json_data.get("EnableTokenAuthentication"),
            ExcludesPattern=json_data.get("ExcludesPattern"),
            FeedContextPath=json_data.get("FeedContextPath"),
            FetchJarsEagerly=json_data.get("FetchJarsEagerly"),
            FetchSourcesEagerly=json_data.get("FetchSourcesEagerly"),
            ForceNugetAuthentication=json_data.get("ForceNugetAuthentication"),
            HandleReleases=json_data.get("HandleReleases"),
            HandleSnapshots=json_data.get("HandleSnapshots"),
            HardFail=json_data.get("HardFail"),
            Id=json_data.get("Id"),
            IncludesPattern=json_data.get("IncludesPattern"),
            Key=json_data.get("Key"),
            LocalAddress=json_data.get("LocalAddress"),
            MaxUniqueSnapshots=json_data.get("MaxUniqueSnapshots"),
            MissedCachePeriodSeconds=json_data.get("MissedCachePeriodSeconds"),
            Notes=json_data.get("Notes"),
            Offline=json_data.get("Offline"),
            PackageType=json_data.get("PackageType"),
            Password=json_data.get("Password"),
            PropagateQueryParams=json_data.get("PropagateQueryParams"),
            PropertySets=json_data.get("PropertySets"),
            Proxy=json_data.get("Proxy"),
            PypiRegistryUrl=json_data.get("PypiRegistryUrl"),
            RemoteRepoChecksumPolicyType=json_data.get("RemoteRepoChecksumPolicyType"),
            RepoLayoutRef=json_data.get("RepoLayoutRef"),
            RetrievalCachePeriodSeconds=json_data.get("RetrievalCachePeriodSeconds"),
            ShareConfiguration=json_data.get("ShareConfiguration"),
            SocketTimeoutMillis=json_data.get("SocketTimeoutMillis"),
            StoreArtifactsLocally=json_data.get("StoreArtifactsLocally"),
            SuppressPomConsistencyChecks=json_data.get("SuppressPomConsistencyChecks"),
            SynchronizeProperties=json_data.get("SynchronizeProperties"),
            UnusedArtifactsCleanupPeriodHours=json_data.get("UnusedArtifactsCleanupPeriodHours"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
            V3FeedUrl=json_data.get("V3FeedUrl"),
            VcsGitDownloadUrl=json_data.get("VcsGitDownloadUrl"),
            VcsGitProvider=json_data.get("VcsGitProvider"),
            VcsType=json_data.get("VcsType"),
            XrayIndex=json_data.get("XrayIndex"),
            ContentSynchronisation=deserialize_list(json_data.get("ContentSynchronisation"), ContentSynchronisationDefinition),
            Nuget=deserialize_list(json_data.get("Nuget"), NugetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContentSynchronisationDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ContentSynchronisationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentSynchronisationDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentSynchronisationDefinition = ContentSynchronisationDefinition


@dataclass
class NugetDefinition(BaseModel):
    DownloadContextPath: Optional[str]
    FeedContextPath: Optional[str]
    V3FeedUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NugetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NugetDefinition"]:
        if not json_data:
            return None
        return cls(
            DownloadContextPath=json_data.get("DownloadContextPath"),
            FeedContextPath=json_data.get("FeedContextPath"),
            V3FeedUrl=json_data.get("V3FeedUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NugetDefinition = NugetDefinition


