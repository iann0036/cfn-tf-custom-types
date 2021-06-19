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
    ClientEmail: Optional[str]
    ClientId: Optional[str]
    ClientX509CertUrl: Optional[str]
    DomainName: Optional[str]
    GsuiteUser: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrganizationalUnitId: Optional[str]
    OrganizationalUnitName: Optional[str]
    OrganizationalUnitPath: Optional[str]
    PrivateKey: Optional[str]
    PrivateKeyId: Optional[str]
    ProjectId: Optional[str]
    Vendor: Optional[str]

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
            ClientEmail=json_data.get("ClientEmail"),
            ClientId=json_data.get("ClientId"),
            ClientX509CertUrl=json_data.get("ClientX509CertUrl"),
            DomainName=json_data.get("DomainName"),
            GsuiteUser=json_data.get("GsuiteUser"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrganizationalUnitId=json_data.get("OrganizationalUnitId"),
            OrganizationalUnitName=json_data.get("OrganizationalUnitName"),
            OrganizationalUnitPath=json_data.get("OrganizationalUnitPath"),
            PrivateKey=json_data.get("PrivateKey"),
            PrivateKeyId=json_data.get("PrivateKeyId"),
            ProjectId=json_data.get("ProjectId"),
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


