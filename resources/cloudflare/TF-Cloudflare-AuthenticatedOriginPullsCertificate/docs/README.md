# TF::Cloudflare::AuthenticatedOriginPullsCertificate

Provides a Cloudflare Authenticated Origin Pulls certificate resource. An uploaded client certificate is required to use Per-Zone or Per-Hostname Authenticated Origin Pulls.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::AuthenticatedOriginPullsCertificate",
    "Properties" : {
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::AuthenticatedOriginPullsCertificate
Properties:
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Certificate

The public client certificate.
- `private_key` - (Required) The private key of the client certificate.
- `type` - (Required) The form of Authenticated Origin Pulls to upload the certificate to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

The private key of the client certificate.
- `type` - (Required) The form of Authenticated Origin Pulls to upload the certificate to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The form of Authenticated Origin Pulls to upload the certificate to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The zone ID to upload the certificate to.
- `certificate` - (Required) The public client certificate.
- `private_key` - (Required) The private key of the client certificate.
- `type` - (Required) The form of Authenticated Origin Pulls to upload the certificate to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ExpiresOn

Returns the <code>ExpiresOn</code> value.

#### Id

Returns the <code>Id</code> value.

#### Issuer

Returns the <code>Issuer</code> value.

#### SerialNumber

Returns the <code>SerialNumber</code> value.

#### Signature

Returns the <code>Signature</code> value.

#### Status

Returns the <code>Status</code> value.

#### UploadedOn

Returns the <code>UploadedOn</code> value.

