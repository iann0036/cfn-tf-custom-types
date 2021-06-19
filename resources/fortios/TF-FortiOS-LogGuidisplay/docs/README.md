# TF::FortiOS::LogGuidisplay

Configure how log messages are displayed on the GUI.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::LogGuidisplay",
    "Properties" : {
        "<a href="#fortiviewunscannedapps" title="FortiviewUnscannedApps">FortiviewUnscannedApps</a>" : <i>String</i>,
        "<a href="#resolveapps" title="ResolveApps">ResolveApps</a>" : <i>String</i>,
        "<a href="#resolvehosts" title="ResolveHosts">ResolveHosts</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::LogGuidisplay
Properties:
    <a href="#fortiviewunscannedapps" title="FortiviewUnscannedApps">FortiviewUnscannedApps</a>: <i>String</i>
    <a href="#resolveapps" title="ResolveApps">ResolveApps</a>: <i>String</i>
    <a href="#resolvehosts" title="ResolveHosts">ResolveHosts</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### FortiviewUnscannedApps

Enable/disable showing unscanned traffic in FortiView application charts. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveApps

Resolve unknown applications on the GUI using Fortinet's remote application database. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveHosts

Enable/disable resolving IP addresses to hostname in log messages on the GUI using reverse DNS lookup Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

