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
    Location: Optional[str]
    Name: Optional[str]
    OutboundPublicIpAddresses: Optional[Sequence[str]]
    RequiredNetworkTrafficRules: Optional[Sequence["_RequiredNetworkTrafficRulesDefinition"]]
    ResourceGroupName: Optional[str]
    SkuName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ConfigServerGitSetting: Optional[Sequence["_ConfigServerGitSettingDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Trace: Optional[Sequence["_TraceDefinition"]]

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
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            OutboundPublicIpAddresses=json_data.get("OutboundPublicIpAddresses"),
            RequiredNetworkTrafficRules=deserialize_list(json_data.get("RequiredNetworkTrafficRules"), RequiredNetworkTrafficRulesDefinition),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SkuName=json_data.get("SkuName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ConfigServerGitSetting=deserialize_list(json_data.get("ConfigServerGitSetting"), ConfigServerGitSettingDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Trace=deserialize_list(json_data.get("Trace"), TraceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequiredNetworkTrafficRulesDefinition(BaseModel):
    Direction: Optional[str]
    Fqdns: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredNetworkTrafficRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredNetworkTrafficRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Direction=json_data.get("Direction"),
            Fqdns=json_data.get("Fqdns"),
            IpAddresses=json_data.get("IpAddresses"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredNetworkTrafficRulesDefinition = RequiredNetworkTrafficRulesDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class ConfigServerGitSettingDefinition(BaseModel):
    Label: Optional[str]
    SearchPaths: Optional[Sequence[str]]
    Uri: Optional[str]
    HttpBasicAuth: Optional[Sequence["_HttpBasicAuthDefinition"]]
    Repository: Optional[Sequence["_RepositoryDefinition"]]
    SshAuth: Optional[Sequence["_SshAuthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigServerGitSettingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigServerGitSettingDefinition"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            SearchPaths=json_data.get("SearchPaths"),
            Uri=json_data.get("Uri"),
            HttpBasicAuth=deserialize_list(json_data.get("HttpBasicAuth"), HttpBasicAuthDefinition),
            Repository=deserialize_list(json_data.get("Repository"), RepositoryDefinition),
            SshAuth=deserialize_list(json_data.get("SshAuth"), SshAuthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigServerGitSettingDefinition = ConfigServerGitSettingDefinition


@dataclass
class HttpBasicAuthDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpBasicAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpBasicAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpBasicAuthDefinition = HttpBasicAuthDefinition


@dataclass
class RepositoryDefinition(BaseModel):
    Label: Optional[str]
    Name: Optional[str]
    Pattern: Optional[Sequence[str]]
    SearchPaths: Optional[Sequence[str]]
    Uri: Optional[str]
    HttpBasicAuth: Optional[Sequence["_HttpBasicAuthDefinition"]]
    SshAuth: Optional[Sequence["_SshAuthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RepositoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepositoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            Pattern=json_data.get("Pattern"),
            SearchPaths=json_data.get("SearchPaths"),
            Uri=json_data.get("Uri"),
            HttpBasicAuth=deserialize_list(json_data.get("HttpBasicAuth"), HttpBasicAuthDefinition),
            SshAuth=deserialize_list(json_data.get("SshAuth"), SshAuthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepositoryDefinition = RepositoryDefinition


@dataclass
class SshAuthDefinition(BaseModel):
    HostKey: Optional[str]
    HostKeyAlgorithm: Optional[str]
    PrivateKey: Optional[str]
    StrictHostKeyCheckingEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SshAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            HostKey=json_data.get("HostKey"),
            HostKeyAlgorithm=json_data.get("HostKeyAlgorithm"),
            PrivateKey=json_data.get("PrivateKey"),
            StrictHostKeyCheckingEnabled=json_data.get("StrictHostKeyCheckingEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshAuthDefinition = SshAuthDefinition


@dataclass
class NetworkDefinition(BaseModel):
    AppNetworkResourceGroup: Optional[str]
    AppSubnetId: Optional[str]
    CidrRanges: Optional[Sequence[str]]
    ServiceRuntimeNetworkResourceGroup: Optional[str]
    ServiceRuntimeSubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            AppNetworkResourceGroup=json_data.get("AppNetworkResourceGroup"),
            AppSubnetId=json_data.get("AppSubnetId"),
            CidrRanges=json_data.get("CidrRanges"),
            ServiceRuntimeNetworkResourceGroup=json_data.get("ServiceRuntimeNetworkResourceGroup"),
            ServiceRuntimeSubnetId=json_data.get("ServiceRuntimeSubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class TraceDefinition(BaseModel):
    InstrumentationKey: Optional[str]
    SampleRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TraceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TraceDefinition"]:
        if not json_data:
            return None
        return cls(
            InstrumentationKey=json_data.get("InstrumentationKey"),
            SampleRate=json_data.get("SampleRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TraceDefinition = TraceDefinition


