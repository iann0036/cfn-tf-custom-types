# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    ClientCidrBlock: Optional[str]
    Description: Optional[str]
    DnsName: Optional[str]
    DnsServers: Optional[Sequence[str]]
    Id: Optional[str]
    ServerCertificateArn: Optional[str]
    SplitTunnel: Optional[bool]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TransportProtocol: Optional[str]
    AuthenticationOptions: Optional[Sequence["_AuthenticationOptions"]]
    ConnectionLogOptions: Optional[Sequence["_ConnectionLogOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClientCidrBlock=json_data.get("ClientCidrBlock"),
            Description=json_data.get("Description"),
            DnsName=json_data.get("DnsName"),
            DnsServers=json_data.get("DnsServers"),
            Id=json_data.get("Id"),
            ServerCertificateArn=json_data.get("ServerCertificateArn"),
            SplitTunnel=json_data.get("SplitTunnel"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            TransportProtocol=json_data.get("TransportProtocol"),
            AuthenticationOptions=json_data.get("AuthenticationOptions"),
            ConnectionLogOptions=json_data.get("ConnectionLogOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class AuthenticationOptions:
    ActiveDirectoryId: Optional[str]
    RootCertificateChainArn: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationOptions"]:
        if not json_data:
            return None
        return cls(
            ActiveDirectoryId=json_data.get("ActiveDirectoryId"),
            RootCertificateChainArn=json_data.get("RootCertificateChainArn"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationOptions = AuthenticationOptions


@dataclass
class ConnectionLogOptions:
    CloudwatchLogGroup: Optional[str]
    CloudwatchLogStream: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionLogOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionLogOptions"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogGroup=json_data.get("CloudwatchLogGroup"),
            CloudwatchLogStream=json_data.get("CloudwatchLogStream"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionLogOptions = ConnectionLogOptions


