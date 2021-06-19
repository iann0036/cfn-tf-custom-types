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
    CertificateChain: Optional[str]
    Domains: Optional[Sequence[str]]
    Id: Optional[str]
    LeafCertificate: Optional[str]
    Name: Optional[str]
    NotAfter: Optional[str]
    PrivateKey: Optional[str]
    Sha1Fingerprint: Optional[str]
    State: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]

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
            CertificateChain=json_data.get("CertificateChain"),
            Domains=json_data.get("Domains"),
            Id=json_data.get("Id"),
            LeafCertificate=json_data.get("LeafCertificate"),
            Name=json_data.get("Name"),
            NotAfter=json_data.get("NotAfter"),
            PrivateKey=json_data.get("PrivateKey"),
            Sha1Fingerprint=json_data.get("Sha1Fingerprint"),
            State=json_data.get("State"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


