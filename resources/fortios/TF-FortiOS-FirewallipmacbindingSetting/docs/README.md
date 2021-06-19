# TF::FortiOS::FirewallipmacbindingSetting

Configure IP to MAC binding settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallipmacbindingSetting",
    "Properties" : {
        "<a href="#bindthroughfw" title="Bindthroughfw">Bindthroughfw</a>" : <i>String</i>,
        "<a href="#bindtofw" title="Bindtofw">Bindtofw</a>" : <i>String</i>,
        "<a href="#undefinedhost" title="Undefinedhost">Undefinedhost</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallipmacbindingSetting
Properties:
    <a href="#bindthroughfw" title="Bindthroughfw">Bindthroughfw</a>: <i>String</i>
    <a href="#bindtofw" title="Bindtofw">Bindtofw</a>: <i>String</i>
    <a href="#undefinedhost" title="Undefinedhost">Undefinedhost</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Bindthroughfw

Enable/disable use of IP/MAC binding to filter packets that would normally go through the firewall. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bindtofw

Enable/disable use of IP/MAC binding to filter packets that would normally go to the firewall. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Undefinedhost

Select action to take on packets with IP/MAC addresses not in the binding list (default = block). Valid values: `allow`, `block`.

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

