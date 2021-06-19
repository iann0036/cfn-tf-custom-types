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
    DownloadCustomLink: Optional[str]
    DownloadLocation: Optional[str]
    ForticlientAvdbUpdateInterval: Optional[float]
    ForticlientDeregUnsupportedClient: Optional[str]
    ForticlientDisconnectUnsupportedClient: Optional[str]
    ForticlientEmsRestApiCallTimeout: Optional[float]
    ForticlientKeepaliveInterval: Optional[float]
    ForticlientOfflineGrace: Optional[str]
    ForticlientOfflineGraceInterval: Optional[float]
    ForticlientRegKey: Optional[str]
    ForticlientRegKeyEnforce: Optional[str]
    ForticlientRegTimeout: Optional[float]
    ForticlientSysUpdateInterval: Optional[float]
    ForticlientUserAvatar: Optional[str]
    ForticlientWarningInterval: Optional[float]
    Id: Optional[str]
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
            DownloadCustomLink=json_data.get("DownloadCustomLink"),
            DownloadLocation=json_data.get("DownloadLocation"),
            ForticlientAvdbUpdateInterval=json_data.get("ForticlientAvdbUpdateInterval"),
            ForticlientDeregUnsupportedClient=json_data.get("ForticlientDeregUnsupportedClient"),
            ForticlientDisconnectUnsupportedClient=json_data.get("ForticlientDisconnectUnsupportedClient"),
            ForticlientEmsRestApiCallTimeout=json_data.get("ForticlientEmsRestApiCallTimeout"),
            ForticlientKeepaliveInterval=json_data.get("ForticlientKeepaliveInterval"),
            ForticlientOfflineGrace=json_data.get("ForticlientOfflineGrace"),
            ForticlientOfflineGraceInterval=json_data.get("ForticlientOfflineGraceInterval"),
            ForticlientRegKey=json_data.get("ForticlientRegKey"),
            ForticlientRegKeyEnforce=json_data.get("ForticlientRegKeyEnforce"),
            ForticlientRegTimeout=json_data.get("ForticlientRegTimeout"),
            ForticlientSysUpdateInterval=json_data.get("ForticlientSysUpdateInterval"),
            ForticlientUserAvatar=json_data.get("ForticlientUserAvatar"),
            ForticlientWarningInterval=json_data.get("ForticlientWarningInterval"),
            Id=json_data.get("Id"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


