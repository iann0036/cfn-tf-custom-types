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
    BandwidthPackageIds: Optional[str]
    Description: Optional[str]
    ForwardTableIds: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    Name: Optional[str]
    Period: Optional[float]
    SnatTableIds: Optional[str]
    Spec: Optional[str]
    Specification: Optional[str]
    VpcId: Optional[str]
    BandwidthPackages: Optional[Sequence["_BandwidthPackages"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BandwidthPackageIds=json_data.get("BandwidthPackageIds"),
            Description=json_data.get("Description"),
            ForwardTableIds=json_data.get("ForwardTableIds"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            SnatTableIds=json_data.get("SnatTableIds"),
            Spec=json_data.get("Spec"),
            Specification=json_data.get("Specification"),
            VpcId=json_data.get("VpcId"),
            BandwidthPackages=json_data.get("BandwidthPackages"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BandwidthPackages:
    Bandwidth: Optional[float]
    IpCount: Optional[float]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BandwidthPackages"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BandwidthPackages"]:
        if not json_data:
            return None
        return cls(
            Bandwidth=json_data.get("Bandwidth"),
            IpCount=json_data.get("IpCount"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BandwidthPackages = BandwidthPackages


