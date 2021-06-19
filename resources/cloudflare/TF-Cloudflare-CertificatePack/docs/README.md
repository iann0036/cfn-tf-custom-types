# TF::Cloudflare::CertificatePack

Provides a Cloudflare Certificate Pack resource that is used to provision
managed TLS certificates.

~> **Important:** Certificate packs are not able to be updated in place and if
you require a zero downtime rotation, you need to use Terraform's meta-arguments
for [`lifecycle`](https://www.terraform.io/docs/configuration/resources.html#lifecycle-lifecycle-customizations) blocks.
`create_before_destroy` should be suffice for most scenarios (exceptions are
things like missing entitlements, high ranking domain). To completely
de-risk rotations, use you can create multiple resources using a 2-phase change
where you have both resources live at once and you remove the old one once
you've confirmed the certificate is available.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::CertificatePack",
    "Properties" : {
        "<a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>" : <i>String</i>,
        "<a href="#cloudflarebranding" title="CloudflareBranding">CloudflareBranding</a>" : <i>Boolean</i>,
        "<a href="#hosts" title="Hosts">Hosts</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#validationmethod" title="ValidationMethod">ValidationMethod</a>" : <i>String</i>,
        "<a href="#validitydays" title="ValidityDays">ValidityDays</a>" : <i>Double</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::CertificatePack
Properties:
    <a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>: <i>String</i>
    <a href="#cloudflarebranding" title="CloudflareBranding">CloudflareBranding</a>: <i>Boolean</i>
    <a href="#hosts" title="Hosts">Hosts</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#validationmethod" title="ValidationMethod">ValidationMethod</a>: <i>String</i>
    <a href="#validitydays" title="ValidityDays">ValidityDays</a>: <i>Double</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### CertificateAuthority

Which certificate
authority to issue the certificate pack. Allowed values: `"digicert"`,
`"lets_encrypt"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudflareBranding

Whether or not to include
Cloudflare branding. This will add `sni.cloudflaressl.com` as the Common Name
if set to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hosts

List of hostnames to provision the certificate pack for.
Note: If using Let's Encrypt, you cannot use individual subdomains and only a
wildcard for subdomain is available.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Certificate pack configuration type.
Allowed values: `"custom"`, `"dedicated_custom"`, `"advanced"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidationMethod

Which validation method to
use in order to prove domain ownership. Allowed values: `"txt"`, `"http"`, `"email"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidityDays

How long the certificate is valid
for. Note: If using Let's Encrypt, this value can only be 90 days.
Allowed values: 14, 30, 90, 365.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone to which the certificate pack should be added.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

