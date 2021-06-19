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
    CertnameDsa1024: Optional[str]
    CertnameDsa2048: Optional[str]
    CertnameEcdsa256: Optional[str]
    CertnameEcdsa384: Optional[str]
    CertnameEcdsa521: Optional[str]
    CertnameEd25519: Optional[str]
    CertnameEd448: Optional[str]
    CertnameRsa1024: Optional[str]
    CertnameRsa2048: Optional[str]
    CertnameRsa4096: Optional[str]
    CheckCaCert: Optional[str]
    CheckCaChain: Optional[str]
    CmpKeyUsageChecking: Optional[str]
    CmpSaveExtraCerts: Optional[str]
    CnMatch: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    OcspDefaultServer: Optional[str]
    OcspOption: Optional[str]
    OcspStatus: Optional[str]
    SslMinProtoVersion: Optional[str]
    SslOcspSourceIp: Optional[str]
    StrictCrlCheck: Optional[str]
    StrictOcspCheck: Optional[str]
    SubjectMatch: Optional[str]
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
            CertnameDsa1024=json_data.get("CertnameDsa1024"),
            CertnameDsa2048=json_data.get("CertnameDsa2048"),
            CertnameEcdsa256=json_data.get("CertnameEcdsa256"),
            CertnameEcdsa384=json_data.get("CertnameEcdsa384"),
            CertnameEcdsa521=json_data.get("CertnameEcdsa521"),
            CertnameEd25519=json_data.get("CertnameEd25519"),
            CertnameEd448=json_data.get("CertnameEd448"),
            CertnameRsa1024=json_data.get("CertnameRsa1024"),
            CertnameRsa2048=json_data.get("CertnameRsa2048"),
            CertnameRsa4096=json_data.get("CertnameRsa4096"),
            CheckCaCert=json_data.get("CheckCaCert"),
            CheckCaChain=json_data.get("CheckCaChain"),
            CmpKeyUsageChecking=json_data.get("CmpKeyUsageChecking"),
            CmpSaveExtraCerts=json_data.get("CmpSaveExtraCerts"),
            CnMatch=json_data.get("CnMatch"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            OcspDefaultServer=json_data.get("OcspDefaultServer"),
            OcspOption=json_data.get("OcspOption"),
            OcspStatus=json_data.get("OcspStatus"),
            SslMinProtoVersion=json_data.get("SslMinProtoVersion"),
            SslOcspSourceIp=json_data.get("SslOcspSourceIp"),
            StrictCrlCheck=json_data.get("StrictCrlCheck"),
            StrictOcspCheck=json_data.get("StrictOcspCheck"),
            SubjectMatch=json_data.get("SubjectMatch"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


