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
    ApplicationList: Optional[str]
    AvProfile: Optional[str]
    CifsProfile: Optional[str]
    DlpSensor: Optional[str]
    DnsfilterProfile: Optional[str]
    EmailfilterProfile: Optional[str]
    FileFilterProfile: Optional[str]
    IcapProfile: Optional[str]
    Id: Optional[str]
    IpsSensor: Optional[str]
    Name: Optional[str]
    ProfileProtocolOptions: Optional[str]
    SpamfilterProfile: Optional[str]
    SshFilterProfile: Optional[str]
    SslSshProfile: Optional[str]
    Vdomparam: Optional[str]
    VoipProfile: Optional[str]
    WafProfile: Optional[str]
    WebfilterProfile: Optional[str]

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
            ApplicationList=json_data.get("ApplicationList"),
            AvProfile=json_data.get("AvProfile"),
            CifsProfile=json_data.get("CifsProfile"),
            DlpSensor=json_data.get("DlpSensor"),
            DnsfilterProfile=json_data.get("DnsfilterProfile"),
            EmailfilterProfile=json_data.get("EmailfilterProfile"),
            FileFilterProfile=json_data.get("FileFilterProfile"),
            IcapProfile=json_data.get("IcapProfile"),
            Id=json_data.get("Id"),
            IpsSensor=json_data.get("IpsSensor"),
            Name=json_data.get("Name"),
            ProfileProtocolOptions=json_data.get("ProfileProtocolOptions"),
            SpamfilterProfile=json_data.get("SpamfilterProfile"),
            SshFilterProfile=json_data.get("SshFilterProfile"),
            SslSshProfile=json_data.get("SslSshProfile"),
            Vdomparam=json_data.get("Vdomparam"),
            VoipProfile=json_data.get("VoipProfile"),
            WafProfile=json_data.get("WafProfile"),
            WebfilterProfile=json_data.get("WebfilterProfile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


