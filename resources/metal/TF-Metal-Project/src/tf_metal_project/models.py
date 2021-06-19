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
    BackendTransfer: Optional[bool]
    Created: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrganizationId: Optional[str]
    PaymentMethodId: Optional[str]
    Updated: Optional[str]
    BgpConfig: Optional[Sequence["_BgpConfigDefinition"]]

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
            BackendTransfer=json_data.get("BackendTransfer"),
            Created=json_data.get("Created"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            PaymentMethodId=json_data.get("PaymentMethodId"),
            Updated=json_data.get("Updated"),
            BgpConfig=deserialize_list(json_data.get("BgpConfig"), BgpConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BgpConfigDefinition(BaseModel):
    Asn: Optional[float]
    DeploymentType: Optional[str]
    Md5: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn=json_data.get("Asn"),
            DeploymentType=json_data.get("DeploymentType"),
            Md5=json_data.get("Md5"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpConfigDefinition = BgpConfigDefinition


