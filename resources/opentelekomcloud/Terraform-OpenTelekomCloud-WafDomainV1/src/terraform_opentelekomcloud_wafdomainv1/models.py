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
    AccessCode: Optional[str]
    AccessStatus: Optional[float]
    CertificateId: Optional[str]
    Cname: Optional[str]
    Hostname: Optional[str]
    PolicyId: Optional[str]
    ProtectStatus: Optional[float]
    Protocol: Optional[str]
    Proxy: Optional[bool]
    SipHeaderList: Optional[Sequence[str]]
    SipHeaderName: Optional[str]
    SubDomain: Optional[str]
    TxtCode: Optional[str]
    Server: Optional[Sequence["_Server"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessCode=json_data.get("AccessCode"),
            AccessStatus=json_data.get("AccessStatus"),
            CertificateId=json_data.get("CertificateId"),
            Cname=json_data.get("Cname"),
            Hostname=json_data.get("Hostname"),
            PolicyId=json_data.get("PolicyId"),
            ProtectStatus=json_data.get("ProtectStatus"),
            Protocol=json_data.get("Protocol"),
            Proxy=json_data.get("Proxy"),
            SipHeaderList=json_data.get("SipHeaderList"),
            SipHeaderName=json_data.get("SipHeaderName"),
            SubDomain=json_data.get("SubDomain"),
            TxtCode=json_data.get("TxtCode"),
            Server=json_data.get("Server"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Server:
    Address: Optional[str]
    BackProtocol: Optional[str]
    FrontProtocol: Optional[str]
    Port: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Server"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Server"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            BackProtocol=json_data.get("BackProtocol"),
            FrontProtocol=json_data.get("FrontProtocol"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Server = Server


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


