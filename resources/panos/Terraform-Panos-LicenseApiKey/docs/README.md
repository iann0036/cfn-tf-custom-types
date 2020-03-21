# Terraform::Panos::LicenseApiKey

This resource manages the licensing API key, which is necessary to delicense
the PAN-OS firewall.

This resource's `retain_key` param is a Terraform side configuration only.  In
order for the firewall to delicense itself, the licensing API key must be
present.  This means that either the `panos_licensing` resource must use
`depends_on` and depend on this resource, or you must set the `retain_key`
param to `true`.  As there is no harm in leaving the licensing API key on the
PAN-OS firewall, it is recommended that `retain_key` be set to `true`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::LicenseApiKey",
    "Properties" : {
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#retainkey" title="RetainKey">RetainKey</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::LicenseApiKey
Properties:
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#retainkey" title="RetainKey">RetainKey</a>: <i>Boolean</i>
</pre>

## Properties

#### Key

The licensing API key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainKey

Set to `true` to retain the licensing API key
even after the deletion of this resource (recommended).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

