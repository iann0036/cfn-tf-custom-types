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
    Arn: Optional[str]
    ClientCidrBlock: Optional[str]
    Description: Optional[str]
    DnsName: Optional[str]
    DnsServers: Optional[Sequence[str]]
    Id: Optional[str]
    ServerCertificateArn: Optional[str]
    SplitTunnel: Optional[bool]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TransportProtocol: Optional[str]
    AuthenticationOptions: Optional[Sequence["_AuthenticationOptionsDefinition"]]
    ConnectionLogOptions: Optional[Sequence["_ConnectionLogOptionsDefinition"]]

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
            Arn=json_data.get("Arn"),
            ClientCidrBlock=json_data.get("ClientCidrBlock"),
            Description=json_data.get("Description"),
            DnsName=json_data.get("DnsName"),
            DnsServers=json_data.get("DnsServers"),
            Id=json_data.get("Id"),
            ServerCertificateArn=json_data.get("ServerCertificateArn"),
            SplitTunnel=json_data.get("SplitTunnel"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TransportProtocol=json_data.get("TransportProtocol"),
            AuthenticationOptions=deserialize_list(json_data.get("AuthenticationOptions"), AuthenticationOptionsDefinition),
            ConnectionLogOptions=deserialize_list(json_data.get("ConnectionLogOptions"), ConnectionLogOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class AuthenticationOptionsDefinition(BaseModel):
    ActiveDirectoryId: Optional[str]
    RootCertificateChainArn: Optional[str]
    SamlProviderArn: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveDirectoryId=json_data.get("ActiveDirectoryId"),
            RootCertificateChainArn=json_data.get("RootCertificateChainArn"),
            SamlProviderArn=json_data.get("SamlProviderArn"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationOptionsDefinition = AuthenticationOptionsDefinition


@dataclass
class ConnectionLogOptionsDefinition(BaseModel):
    CloudwatchLogGroup: Optional[str]
    CloudwatchLogStream: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionLogOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionLogOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogGroup=json_data.get("CloudwatchLogGroup"),
            CloudwatchLogStream=json_data.get("CloudwatchLogStream"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionLogOptionsDefinition = ConnectionLogOptionsDefinition


