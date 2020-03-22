# Terraform::Panos::Licensing

This resource manages the licenses installed on the PAN-OS firewall.

Installing the standard auth code for the standard PAN-OS license key for the
firewall causes the firewall to reboot.  Thus it is recommended that you use
this resource in a separate step of your overall firewall provisioning, as
using this resource will cause the firewall to be temporarily inaccessible.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::Licensing",
    "Properties" : {
        "<a href="#authcodes" title="AuthCodes">AuthCodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#delicense" title="Delicense">Delicense</a>" : <i>Boolean</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::Licensing
Properties:
    <a href="#authcodes" title="AuthCodes">AuthCodes</a>: <i>
      - String</i>
    <a href="#delicense" title="Delicense">Delicense</a>: <i>Boolean</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
</pre>

## Properties

#### AuthCodes

The list of auth codes to install.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delicense

Leave as `true` if you want to delicense
the firewall when this resource is removed, otherwise set to `false` to
prevent firewall delicensing.  Delicensing requires that the licensing
API key has been installed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

For `delicense` of `true`, the type of delicensing to
perform.  Right now, only `auto` is supported (no manual delicensing).

_Required_: No

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

#### Licenses

Returns the <code>Licenses</code> value.

