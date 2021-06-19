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
    Advertising: Optional[str]
    BeaconInterval: Optional[float]
    BleScanning: Optional[str]
    Comment: Optional[str]
    EddystoneInstance: Optional[str]
    EddystoneNamespace: Optional[str]
    EddystoneUrl: Optional[str]
    EddystoneUrlEncodeHex: Optional[str]
    IbeaconUuid: Optional[str]
    Id: Optional[str]
    MajorId: Optional[float]
    MinorId: Optional[float]
    Name: Optional[str]
    Txpower: Optional[str]
    Vdomparam: Optional[str]

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
            Advertising=json_data.get("Advertising"),
            BeaconInterval=json_data.get("BeaconInterval"),
            BleScanning=json_data.get("BleScanning"),
            Comment=json_data.get("Comment"),
            EddystoneInstance=json_data.get("EddystoneInstance"),
            EddystoneNamespace=json_data.get("EddystoneNamespace"),
            EddystoneUrl=json_data.get("EddystoneUrl"),
            EddystoneUrlEncodeHex=json_data.get("EddystoneUrlEncodeHex"),
            IbeaconUuid=json_data.get("IbeaconUuid"),
            Id=json_data.get("Id"),
            MajorId=json_data.get("MajorId"),
            MinorId=json_data.get("MinorId"),
            Name=json_data.get("Name"),
            Txpower=json_data.get("Txpower"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


