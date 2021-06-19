# TF::TencentCloud::SslPayCertificate

Provide a resource to create a payment SSL.

~> **NOTE:** Provides the creation of a paid certificate, including the submission of certificate information and order functions;
currently, it does not support re-issuing certificates, revoking certificates, and deleting certificates; the certificate remarks
and belonging items can be updated. The Destroy operation will only cancel the certificate order, and will not delete the
certificate and refund the fee. If you need a refund, you need to check the current certificate status in the console
as `Review Cancel`, and then you can click `Request a refund` to refund the fee.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::SslPayCertificate",
    "Properties" : {
        "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
        "<a href="#domainnum" title="DomainNum">DomainNum</a>" : <i>Double</i>,
        "<a href="#productid" title="ProductId">ProductId</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#timespan" title="TimeSpan">TimeSpan</a>" : <i>Double</i>,
        "<a href="#information" title="Information">Information</a>" : <i>[ <a href="informationdefinition.md">InformationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::SslPayCertificate
Properties:
    <a href="#alias" title="Alias">Alias</a>: <i>String</i>
    <a href="#domainnum" title="DomainNum">DomainNum</a>: <i>Double</i>
    <a href="#productid" title="ProductId">ProductId</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#timespan" title="TimeSpan">TimeSpan</a>: <i>Double</i>
    <a href="#information" title="Information">Information</a>: <i>
      - <a href="informationdefinition.md">InformationDefinition</a></i>
</pre>

## Properties

#### Alias

Remark name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainNum

Number of domain names included in the certificate.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductId

Certificate commodity ID. Valid value ranges: (3~42). `3` means SecureSite Enhanced Enterprise Edition (EV Pro), `4` means SecureSite Enhanced (EV), `5` means SecureSite Enterprise Professional Edition (OV Pro), `6` means SecureSite Enterprise (OV), `7` means SecureSite Enterprise Type (OV) wildcard, `8` means Geotrust enhanced (EV), `9` means Geotrust enterprise (OV), `10` means Geotrust enterprise (OV) wildcard, `11` means TrustAsia domain type multi-domain SSL certificate, `12` means TrustAsia domain type ( DV) wildcard, `13` means TrustAsia enterprise wildcard (OV) SSL certificate (D3), `14` means TrustAsia enterprise (OV) SSL certificate (D3), `15` means TrustAsia enterprise multi-domain (OV) SSL certificate (D3), `16` means TrustAsia Enhanced (EV) SSL Certificate (D3), `17` means TrustAsia Enhanced Multiple Domain (EV) SSL Certificate (D3), `18` means GlobalSign Enterprise (OV) SSL Certificate, `19` means GlobalSign Enterprise Wildcard (OV) SSL Certificate, `20` means GlobalSign Enhanced (EV) SSL Certificate, `21` means TrustAsia Enterprise Wildcard Multiple Domain (OV) SSL Certificate (D3), `22` means GlobalSign Enterprise Multiple Domain (OV) SSL Certificate, `23` means GlobalSign Enterprise Multiple Wildcard Domain name (OV) SSL certificate, `24` means GlobalSign enhanced multi-domain (EV) SSL certificate, `25` means Wotrus domain type certificate, `26` means Wotrus domain type multi-domain certificate, `27` means Wotrus domain type wildcard certificate, `28` means Wotrus enterprise type certificate, `29` means Wotrus enterprise multi-domain certificate, `30` means Wotrus enterprise wildcard certificate, `31` means Wotrus enhanced certificate, `32` means Wotrus enhanced multi-domain certificate, `33` means DNSPod national secret domain name certificate, `34` means DNSPod national secret domain name certificate Multi-domain certificate, `35` means DNSPod national secret domain name wildcard certificate, `37` means DNSPod national secret enterprise certificate, `38` means DNSPod national secret enterprise multi-domain certificate, `39` means DNSPod national secret enterprise wildcard certificate, `40` means DNSPod national secret increase Strong certificate, `41` means DNSPod national secret enhanced multi-domain certificate, `42` means TrustAsia domain-type wildcard multi-domain certificate.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The ID of project.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeSpan

Certificate period, currently only supports 1 year certificate purchase.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Information

_Required_: No

_Type_: List of <a href="informationdefinition.md">InformationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertificateId

Returns the <code>CertificateId</code> value.

#### Id

Returns the <code>Id</code> value.

#### OrderId

Returns the <code>OrderId</code> value.

#### Status

Returns the <code>Status</code> value.

