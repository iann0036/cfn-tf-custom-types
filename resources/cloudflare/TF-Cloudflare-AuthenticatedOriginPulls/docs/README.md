# TF::Cloudflare::AuthenticatedOriginPulls

Provides a Cloudflare Authenticated Origin Pulls resource. An `cloudflare_authenticated_origin_pulls` resource is required to use Per-Zone or Per-Hostname Authenticated Origin Pulls.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::AuthenticatedOriginPulls",
    "Properties" : {
        "<a href="#authenticatedoriginpullscertificate" title="AuthenticatedOriginPullsCertificate">AuthenticatedOriginPullsCertificate</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::AuthenticatedOriginPulls
Properties:
    <a href="#authenticatedoriginpullscertificate" title="AuthenticatedOriginPullsCertificate">AuthenticatedOriginPullsCertificate</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### AuthenticatedOriginPullsCertificate

The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
- `hostname` - (Optional) Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
- `enabled` - (Required) Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
- `enabled` - (Required) Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The zone ID to upload the certificate to.
- `authenticated_origin_pulls_certificate` - (Optional) The id of an uploaded Authenticated Origin Pulls certificate. If no hostname is provided, this certificate will be used zone wide as Per-Zone Authenticated Origin Pulls.
- `hostname` - (Optional) Specify a hostname to enable Per-Hostname Authenticated Origin Pulls on, using the provided certificate.
- `enabled` - (Required) Whether or not to enable Authenticated Origin Pulls on the given zone or hostname.

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

