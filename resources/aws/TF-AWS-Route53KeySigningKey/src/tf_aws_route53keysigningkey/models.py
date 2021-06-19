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
    DigestAlgorithmMnemonic: Optional[str]
    DigestAlgorithmType: Optional[float]
    DigestValue: Optional[str]
    DnskeyRecord: Optional[str]
    DsRecord: Optional[str]
    Flag: Optional[float]
    HostedZoneId: Optional[str]
    Id: Optional[str]
    KeyManagementServiceArn: Optional[str]
    KeyTag: Optional[float]
    Name: Optional[str]
    PublicKey: Optional[str]
    SigningAlgorithmMnemonic: Optional[str]
    SigningAlgorithmType: Optional[float]
    Status: Optional[str]

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
            DigestAlgorithmMnemonic=json_data.get("DigestAlgorithmMnemonic"),
            DigestAlgorithmType=json_data.get("DigestAlgorithmType"),
            DigestValue=json_data.get("DigestValue"),
            DnskeyRecord=json_data.get("DnskeyRecord"),
            DsRecord=json_data.get("DsRecord"),
            Flag=json_data.get("Flag"),
            HostedZoneId=json_data.get("HostedZoneId"),
            Id=json_data.get("Id"),
            KeyManagementServiceArn=json_data.get("KeyManagementServiceArn"),
            KeyTag=json_data.get("KeyTag"),
            Name=json_data.get("Name"),
            PublicKey=json_data.get("PublicKey"),
            SigningAlgorithmMnemonic=json_data.get("SigningAlgorithmMnemonic"),
            SigningAlgorithmType=json_data.get("SigningAlgorithmType"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


