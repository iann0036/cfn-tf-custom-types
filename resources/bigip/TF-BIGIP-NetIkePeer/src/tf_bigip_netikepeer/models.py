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
    AppService: Optional[str]
    CaCertFile: Optional[str]
    CrlFile: Optional[str]
    Description: Optional[str]
    DpdDelay: Optional[float]
    GeneratePolicy: Optional[str]
    Id: Optional[str]
    Lifetime: Optional[float]
    Mode: Optional[str]
    MyCertFile: Optional[str]
    MyCertKeyFile: Optional[str]
    MyCertKeyPassphrase: Optional[str]
    MyIdType: Optional[str]
    MyIdValue: Optional[str]
    Name: Optional[str]
    NatTraversal: Optional[str]
    Passive: Optional[str]
    PeersCertFile: Optional[str]
    PeersCertType: Optional[str]
    PeersIdType: Optional[str]
    PeersIdValue: Optional[str]
    Phase1AuthMethod: Optional[str]
    Phase1EncryptAlgorithm: Optional[str]
    Phase1HashAlgorithm: Optional[str]
    Phase1PerfectForwardSecrecy: Optional[str]
    PresharedKey: Optional[str]
    PresharedKeyEncrypted: Optional[str]
    Prf: Optional[str]
    ProxySupport: Optional[str]
    RemoteAddress: Optional[str]
    ReplayWindowSize: Optional[float]
    State: Optional[str]
    TrafficSelector: Optional[Sequence[str]]
    VerifyCert: Optional[str]
    Version: Optional[Sequence[str]]

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
            AppService=json_data.get("AppService"),
            CaCertFile=json_data.get("CaCertFile"),
            CrlFile=json_data.get("CrlFile"),
            Description=json_data.get("Description"),
            DpdDelay=json_data.get("DpdDelay"),
            GeneratePolicy=json_data.get("GeneratePolicy"),
            Id=json_data.get("Id"),
            Lifetime=json_data.get("Lifetime"),
            Mode=json_data.get("Mode"),
            MyCertFile=json_data.get("MyCertFile"),
            MyCertKeyFile=json_data.get("MyCertKeyFile"),
            MyCertKeyPassphrase=json_data.get("MyCertKeyPassphrase"),
            MyIdType=json_data.get("MyIdType"),
            MyIdValue=json_data.get("MyIdValue"),
            Name=json_data.get("Name"),
            NatTraversal=json_data.get("NatTraversal"),
            Passive=json_data.get("Passive"),
            PeersCertFile=json_data.get("PeersCertFile"),
            PeersCertType=json_data.get("PeersCertType"),
            PeersIdType=json_data.get("PeersIdType"),
            PeersIdValue=json_data.get("PeersIdValue"),
            Phase1AuthMethod=json_data.get("Phase1AuthMethod"),
            Phase1EncryptAlgorithm=json_data.get("Phase1EncryptAlgorithm"),
            Phase1HashAlgorithm=json_data.get("Phase1HashAlgorithm"),
            Phase1PerfectForwardSecrecy=json_data.get("Phase1PerfectForwardSecrecy"),
            PresharedKey=json_data.get("PresharedKey"),
            PresharedKeyEncrypted=json_data.get("PresharedKeyEncrypted"),
            Prf=json_data.get("Prf"),
            ProxySupport=json_data.get("ProxySupport"),
            RemoteAddress=json_data.get("RemoteAddress"),
            ReplayWindowSize=json_data.get("ReplayWindowSize"),
            State=json_data.get("State"),
            TrafficSelector=json_data.get("TrafficSelector"),
            VerifyCert=json_data.get("VerifyCert"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


