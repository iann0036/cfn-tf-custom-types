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
    EspPort: Optional[str]
    FtpPort: Optional[str]
    HttpPort: Optional[str]
    IcmpPort: Optional[str]
    Id: Optional[str]
    Ikev2Port: Optional[str]
    Ikev2XxPort: Optional[str]
    Name: Optional[str]
    PptpVpnPort: Optional[str]
    SshPort: Optional[str]
    TlsPort: Optional[str]
    Vdomparam: Optional[str]
    VoipTcpPort: Optional[str]
    VoipUdpPort: Optional[str]

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
            EspPort=json_data.get("EspPort"),
            FtpPort=json_data.get("FtpPort"),
            HttpPort=json_data.get("HttpPort"),
            IcmpPort=json_data.get("IcmpPort"),
            Id=json_data.get("Id"),
            Ikev2Port=json_data.get("Ikev2Port"),
            Ikev2XxPort=json_data.get("Ikev2XxPort"),
            Name=json_data.get("Name"),
            PptpVpnPort=json_data.get("PptpVpnPort"),
            SshPort=json_data.get("SshPort"),
            TlsPort=json_data.get("TlsPort"),
            Vdomparam=json_data.get("Vdomparam"),
            VoipTcpPort=json_data.get("VoipTcpPort"),
            VoipUdpPort=json_data.get("VoipUdpPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


