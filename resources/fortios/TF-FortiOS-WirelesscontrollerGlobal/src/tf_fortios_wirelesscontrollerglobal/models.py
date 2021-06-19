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
    ApLogServer: Optional[str]
    ApLogServerIp: Optional[str]
    ApLogServerPort: Optional[float]
    ControlMessageOffload: Optional[str]
    DataEthernetIi: Optional[str]
    DiscoveryMcAddr: Optional[str]
    FiappEthType: Optional[float]
    Id: Optional[str]
    ImageDownload: Optional[str]
    IpsecBaseIp: Optional[str]
    LinkAggregation: Optional[str]
    Location: Optional[str]
    MaxClients: Optional[float]
    MaxRetransmit: Optional[float]
    MeshEthType: Optional[float]
    Name: Optional[str]
    RogueScanMacAdjacency: Optional[float]
    Vdomparam: Optional[str]
    WtpShare: Optional[str]

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
            ApLogServer=json_data.get("ApLogServer"),
            ApLogServerIp=json_data.get("ApLogServerIp"),
            ApLogServerPort=json_data.get("ApLogServerPort"),
            ControlMessageOffload=json_data.get("ControlMessageOffload"),
            DataEthernetIi=json_data.get("DataEthernetIi"),
            DiscoveryMcAddr=json_data.get("DiscoveryMcAddr"),
            FiappEthType=json_data.get("FiappEthType"),
            Id=json_data.get("Id"),
            ImageDownload=json_data.get("ImageDownload"),
            IpsecBaseIp=json_data.get("IpsecBaseIp"),
            LinkAggregation=json_data.get("LinkAggregation"),
            Location=json_data.get("Location"),
            MaxClients=json_data.get("MaxClients"),
            MaxRetransmit=json_data.get("MaxRetransmit"),
            MeshEthType=json_data.get("MeshEthType"),
            Name=json_data.get("Name"),
            RogueScanMacAdjacency=json_data.get("RogueScanMacAdjacency"),
            Vdomparam=json_data.get("Vdomparam"),
            WtpShare=json_data.get("WtpShare"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


